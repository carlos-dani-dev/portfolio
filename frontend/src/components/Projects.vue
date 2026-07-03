<script setup>
import MarkdownText from '@/components/MarkdownText.vue'

import thumbVueTemplate from '@/assets/images/thumb-vue-template.png'
import previewVueTemplate from '@/assets/videos/preview-vue-template.mp4'

import { useI18n } from 'vue-i18n';

const { t } = useI18n()

// 1. Removida a necessidade do `ref(null)` aninhado. 
// Usaremos apenas uma propriedade vazia para guardar o elemento HTML.
const projects = [
  {
    key: 'vue_chatbot',
    titleKey: 'projects_locale.items.vue_chatbot.title',
    descriptionKey: 'projects_locale.items.vue_chatbot.description',
    thumb: thumbVueTemplate,
    video: previewVueTemplate,
    tags: ['Vue.js', 'FastAPI', 'PostgreSQL'],
    projectLink: "https://github.com/carlos-dani-dev/vue-chatbot-template",
    videoElement: null // Alterado aqui
  }
]

// Apague o const videoRef = ref(null); global que estava aqui.

// 2. As funções agora recebem o projeto específico como parâmetro
function playPreview(project) {
  if (project.videoElement) {
    project.videoElement.currentTime = 0;
    project.videoElement.play();
  }
}

function stopPreview(project) {
  if (project.videoElement) {
    project.videoElement.pause();
    project.videoElement.currentTime = 0;
  }
}
</script>

<template>
  <section id="projects-section" class="py-12 max-w-10xl mx-auto px-8">
    
    <div class="text-center mb-16">
      <h2 class="colored-text text-4xl md:text-5xl font-bold tracking-tight mb-4">{{ t('projects_locale.title') }}</h2>
      <p class="text-lg opacity-80 max-w-1xl">
        <MarkdownText :content="t('projects_locale.section_description')" />
      </p>
    </div>

    <div
      v-for="project in projects" :key="project.key"
      class="project-card overflow-hidden border flex flex-col max-w-[1000px] mx-auto w-full rounded-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">
      
      <div
        class="card-media"
        @mouseenter="playPreview(project)"
        @mouseleave="stopPreview(project)"
      >
        <img :src="project.thumb" class="thumb" alt="Preview" />
        
        <video
          :ref="(el) => project.videoElement = el"
          :src="project.video"
          class="preview-video"
          muted
          loop
          playsinline
          preload="metadata"
        ></video>
      </div>

      <div class="flex flex-col gap-4 p-3">
        
        <div class="flex justify-between items-center">
          <p class="colored-text text-3xl font-semibold"><MarkdownText :content="t(project.titleKey)" /></p>
          
          <a 
            :href="project.projectLink" 
            target="_blank" 
            rel="noopener noreferrer"
            class="project-btn inline-flex items-center gap-2 px-5 py-2 font-semibold transition-all duration-300"
          >
            {{t('projects_locale.project_btn_label')}}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="7" y1="17" x2="17" y2="7"></line>
              <polyline points="7 7 17 7 17 17"></polyline>
            </svg>
          </a>
        </div>
        
        <div class="flex flex-wrap gap-3">
          <span
            v-for="tag in project.tags" :key="tag"
            class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-sm"
            >{{ tag }}</span>
        </div>

        <p class="">
          <MarkdownText :content="t(project.descriptionKey)" />
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

.project-btn {
  color: var(--title-text-color);
  border: 1px solid var(--contact-social-tag-border-color);
  background-color: var(--contact-social-tag-bg-color);
  text-decoration: none;
}

.project-btn:hover {
  background-color: var(--title-text-color);
  color: black;
  border-color: var(--title-text-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.project-btn svg {
  transition: transform 0.3s ease;
}

.project-btn:hover svg {
  transform: translate(2px, -2px);
}

</style>