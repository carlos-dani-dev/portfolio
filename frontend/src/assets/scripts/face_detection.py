import sys
import io
from functools import wraps

import PIL as pil
import numpy as np


def capture_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        try:
            return func(*args, **kwargs)
        finally:
            sys.stdout = old_stdout

    return wrapper


@capture_output
def crop_face(original_image, boxes, probs):
    
    if boxes is not None and len(boxes) > 0:
        alpha=40
        best_idx = np.argmax(probs)
        x1, y1, x2, y2 = [int(coord) for coord in boxes[best_idx]]

        x1-=alpha
        y1-=alpha
        x2+=alpha
        y2+=alpha

        w, h = original_image.size
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w, x2), min(h, y2)

        cropped_face = original_image.crop((x1, y1, x2, y2))

        return np.asarray(cropped_face)
    else:
        return None


def redim_face(cropped_face_array, required_size=(160, 160)):
    
    cropped_face_image = pil.Image.fromarray(cropped_face_array)
    face_image = cropped_face_image.convert('RGB')
    resized_face_image = face_image.resize(required_size)
    
    return np.asarray(resized_face_image)