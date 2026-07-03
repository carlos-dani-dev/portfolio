<script setup>
import { useI18n } from 'vue-i18n';

import { ref } from 'vue';

const {t} = useI18n()

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

<section id="projects-section" class="py-12 max-w-10xl mx-auto px-8">
  <div class="text-center mb-16">
    <h2 class="colored-text text-4xl md:text-5xl font-bold tracking-tight mb-4">{{ t('projects.title') }}</h2>
    <p class="text-lg opacity-80 max-w-1xl"><MarkdownText :content="t('projects.section_description')" /></p>
  </div>

  <div class="project-card overflow-hidden border flex flex-col max-w-[1000px] mx-auto w-full rounded-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">
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

    <div class="flex flex-col gap-4 p-3">

      <p class="colored-text text-3xl font-semibold"><MarkdownText :content="t('projects.project1_title')" /></p>

      <div class="flex flex-wrap gap-3">
        <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-sm">
          Vue.js
        </span>
        <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-sm">
          FastAPI
        </span>
        <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-sm">
          PostgreSQL
        </span>
      </div>

      <p class="">
        <MarkdownText :content="t('projects.project1_description')" />
      </p>

    </div>
  </div>

</section>

</template>

<style scoped>
.project-card {
  background-color: var(--project-card-bg-color);
  border-color: var(--project-card-border-color);
}

.project-card:hover {
  border-color: var(--project-card-border-color-hover);
}

.card-media {
  position: relative;
  overflow: hidden;
  height: 300px;
  width: 100%;
  aspect-ratio: 16/9;
}

.thumb, .preview-video {
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

.colored-text{
  color: var(--title-text-color);
}

.skill-tag{
    border-color: var(--tag-skill-border-color);
    background-color: var(--tag-skill-bg-color);
}
</style>