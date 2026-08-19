import os

# O keras_facenet carrega pesos pré-treinados em formato HDF5 legado (Keras 2).
# A partir do TensorFlow 2.16, o Keras 3 passa a ser o backend padrão e seu
# carregador de HDF5 legado é incompatível com esse formato antigo, causando
# "ValueError: object __array__ method not producing an array". Forçar o uso
# do tf_keras (Keras 2) resolve o carregamento. Precisa ser definido ANTES de
# importar tensorflow/keras/keras_facenet.
os.environ.setdefault("TF_USE_LEGACY_KERAS", "1")

import argparse
from pathlib import Path
from functools import wraps

import cv2 as cv
import torch
from tqdm import tqdm
from PIL import Image

import pandas as pd

from facenet_pytorch import MTCNN
from keras_facenet import FaceNet

from concurrent.futures import ThreadPoolExecutor

from face_detection import capture_output, redim_face, crop_face

_DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
MTCNN_MODEL = MTCNN(keep_all=True, device=_DEVICE)


def get_total_images(dataset_path, valid_extensions=[".jpg", ".jpeg", ".png"]):
    
    if valid_extensions is not None:
        valid_extensions = [ext.lower() for ext in valid_extensions]
    total=0
    for path in Path(dataset_path).rglob("*"):
        if not path.is_file():
            continue

        if valid_extensions:
            if path.suffix.lower() not in valid_extensions:
                continue
        total+=1
    return total


@capture_output
def get_embeddings(facenet, resized_image_array_batch):

    embedding = facenet.embeddings(resized_image_array_batch)
    return embedding

import os
from pathlib import Path


def load_faces_generator(dataset_path,batch_size=10, valid_extensions=[".jpg", ".jpeg", ".png"]):

    if valid_extensions is not None:
        valid_extensions = [ext.lower() for ext in valid_extensions]

    batch_files = []

    for path in Path(dataset_path).rglob("*"):

        if not path.is_file():
            continue

        if valid_extensions:
            if path.suffix.lower() not in valid_extensions:
                continue
        filepath = str(path)

        batch_files.append(filepath)

        if len(batch_files) == batch_size:
            yield batch_files
            batch_files = []

    if batch_files:
        yield batch_files


def load_single_image(filename):
    img = cv.imread(filename)
    
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    #img_resized = cv.resize(img_rgb, (720, 720))
    
    return Image.fromarray(img_rgb)


def load_face_embeddings(path: Path):
    facenet = FaceNet()

    chaves = ["filename", "face_embedding"]

    df_dict = {chave: [] for chave in chaves}

    total_imgs = get_total_images(path)

    pbar = tqdm(total=total_imgs, desc="Processamento de imagens em lotes", ncols=100)
    with ThreadPoolExecutor(max_workers=18) as executor:
        for image_filenames_batch in load_faces_generator(path):
            resized_image_array_batch = []
            valid_index = []

            #original_images_batch = list(executor.map(load_single_image, image_filenames_batch))
            original_images_batch = [load_single_image(img) for img in image_filenames_batch]
            
            boxes_batch, probs_batch = MTCNN_MODEL.detect(original_images_batch)

            for i in range(len(original_images_batch)):
                img_boxes = boxes_batch[i] if boxes_batch is not None else None
                img_probs = probs_batch[i] if probs_batch is not None else None

                cropped_image_array = crop_face(original_images_batch[i], img_boxes, img_probs)
                if cropped_image_array is None: continue
                
                resized_image_array = redim_face(cropped_image_array)
                resized_image_array_batch.append(resized_image_array)
                valid_index.append(i)
            
            if not resized_image_array_batch:
                pbar.update(len(image_filenames_batch))
                continue
                
            image_embeddings_batch=get_embeddings(facenet, resized_image_array_batch)

            for idx, i in enumerate(valid_index):
                df_dict["filename"].append(image_filenames_batch[i])
                df_dict["face_embedding"].append(image_embeddings_batch[idx])

            pbar.update(len(image_filenames_batch))

    pbar.close()

    df = pd.DataFrame(df_dict)
    df.to_pickle("./embeddings.pkl")

            
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_path", type=str)
    args = parser.parse_args()

    dataset_path = args.dataset_path

    try:
        path = Path(dataset_path)
    except:
        print("Error")

    load_face_embeddings(path)