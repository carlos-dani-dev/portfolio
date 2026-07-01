<script setup>
import { ref } from 'vue';

const videoRef = ref(null);

const thumb = new URL('../assets/images/thumb-vue-template.png', import.meta.url).href;
const previewVideo = new URL('../assets/videos/preview-vue-template.mp4', import.meta.url).href;

function playPreview() {
  if (videoRef.value) {
    videoRef.value.currentTime = 0;
    videoRef.value.play();
  }
}

function stopPreview() {
  if (videoRef.value) {
    videoRef.value.pause();
    videoRef.value.currentTime = 0;
  }
}
</script>

<template>

<section id="projects-section">


  <div
    class="card-media"
    @mouseenter="playPreview"
    @mouseleave="stopPreview"
  >
    <img :src="thumb" class="thumb" alt="Preview" />

    <video
      ref="videoRef"
      :src="previewVideo"
      class="preview-video"
      muted
      loop
      playsinline
      preload="metadata"
    ></video>
  </div>

</section>

</template>

<style scoped>
.card-media {
  position: relative;
  overflow: hidden;
  width: 100%;
  max-width: 900px;
  aspect-ratio: 16/9;
}

.thumb,
.preview-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  inset: 0;
  transition: opacity 0.3s ease;
}

.preview-video {
  opacity: 0;
  pointer-events: none;
}

.card-media:hover .preview-video {
  opacity: 1;
}

.card-media:hover .thumb {
  opacity: 0;
}
</style>