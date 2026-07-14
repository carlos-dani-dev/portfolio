<script setup>
import MarkdownText from '@/components/MarkdownText.vue'

import thumbVueTemplate from '@/assets/images/thumb-vue-template.png'
import previewVueTemplate from '@/assets/videos/preview-vue-template.mp4'
import thumbTanamesaPipeline from '@/assets/images/thumb-tanamesa-pipe.png'
import previewTanamesaPipeline from '@/assets/videos/preview-tanamesa-pipe.mp4'
import thumbPortfolio from '@/assets/images/thumb-portfolio.png'
import previewPortfolio from '@/assets/videos/preview-portfolio.mp4'
import thumbInferenceApi from '@/assets/images/thumb-inference-api.png'
import previewInferenceApi from '@/assets/videos/preview-inference-api.mp4'

import RightArrow from '@/assets/icons/right-arrow.svg'
import LeftArrow from '@/assets/icons/left-arrow.svg'

import { useI18n } from 'vue-i18n';
import { ref } from 'vue';

const { t } = useI18n()
const carouselRef = ref(null)

function scrollCarousel(direction) {
  const carousel = carouselRef.value
  if (!carousel) return
  const cardWidth = carousel.querySelector('.carousel-item')?.offsetWidth || 0
  carousel.scrollBy({ left: direction * cardWidth, behavior: 'smooth' })
}

const projects = [
  {
    key: 'inference_api',
    titleKey: 'projects_locale.items.inference_api.title',
    descriptionKey: 'projects_locale.items.inference_api.description',
    thumb: thumbInferenceApi,
    video: previewInferenceApi,
    tags: ['Ollama', 'FastAPI', 'Vue.js'],
    projectLink: "https://github.com/carlos-dani-dev/inference-api",
    videoElement: null
  },  
  {
    key: 'vue_chatbot',
    titleKey: 'projects_locale.items.vue_chatbot.title',
    descriptionKey: 'projects_locale.items.vue_chatbot.description',
    thumb: thumbVueTemplate,
    video: previewVueTemplate,
    tags: ['Vue.js', 'FastAPI', 'PostgreSQL'],
    projectLink: "https://github.com/carlos-dani-dev/vue-chatbot-template",
    videoElement: null
  },
  {
    key: 'tanamesa_pipeline',
    titleKey: 'projects_locale.items.tanamesa_pipeline.title',
    descriptionKey: 'projects_locale.items.tanamesa_pipeline.description',
    thumb: thumbTanamesaPipeline,
    video: previewTanamesaPipeline,
    tags: ['SQL', 'PostgreSQL', 'FastAPI'],
    projectLink: "https://github.com/carlos-dani-dev/tanamesa-data-pipeline",
    videoElement: null
  },
  {
    key: 'portfolio',
    titleKey: 'projects_locale.items.portfolio.title',
    descriptionKey: 'projects_locale.items.portfolio.description',
    thumb: thumbPortfolio,
    video: previewPortfolio,
    tags: ['Vue', 'Tailwind', 'Javascript'],
    projectLink: "https://github.com/carlos-dani-dev/portfolio",
    videoElement: null
  }
]

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

const activeProject = ref(null)

function openModal(project) {
  activeProject.value = project
}
function closeModal() {
  activeProject.value = null
}
</script>

<template>
  <section id="projects-section" class="py-12 max-w-10xl mx-auto px-4 md:px-8">
    
    <div class="text-center mb-16">
      <h2 class="colored-text text-4xl md:text-5xl font-bold tracking-tight mb-4">{{ t('projects_locale.title') }}</h2>
      <p class="text-lg opacity-80 max-w-1xl">
        <MarkdownText :content="t('projects_locale.section_description')" />
      </p>
    </div>

    <div class="carousel-wrapper">
      <button class="carousel-btn carousel-btn--left" @click="scrollCarousel(-1)" aria-label="Previous project">
        <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>

      <ul ref="carouselRef" class="carousel">
        <li
          v-for="project in projects" :key="project.key"
          class="project-card carousel-item overflow-hidden border flex flex-col max-w-[1000px] mx-auto w-full rounded-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">
          
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
              
              <div class="flex flex-row justify-center items-center gap-3">
                <a href="#"
                  @click.prevent="openModal(project)"
                  class="project-btn inline-flex items-center gap-2 px-5 py-2 font-semibold transition-all duration-300"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <polygon points="6 3 20 12 6 21 6 3"></polygon>
                  </svg>
                  {{ t('projects_locale.full_preview_btn') }}
                </a>

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
        </li>
      </ul>
      
      <div v-if="activeProject" class="modal-overlay" @click.self="closeModal">
        <div class="modal-content">
          <button class="modal-close" @click="closeModal" aria-label="Fechar">✕</button>
          <video :src="activeProject.video" controls autoplay class="modal-video"></video>
        </div>
      </div>

      <button class="carousel-btn carousel-btn--right" @click="scrollCarousel(1)" aria-label="Next project">
        <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>
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

.carousel-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.carousel-btn {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid var(--project-card-border-color);
  background: var(--project-card-bg-color);
  color: var(--title-text-color);
  cursor: pointer;
  transition: all 0.25s ease;
  opacity: 0.7;
}

.carousel-btn:hover {
  opacity: 1;
  border-color: var(--title-text-color);
  background: var(--title-text-color);
  color: var(--color-bg);
  transform: scale(1.08);
}

.carousel {
  display: flex;
  gap: 1rem;
  list-style: none;
  padding: 8px;
  margin: 0;
  
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  
  scroll-marker-group: after;
}

.carousel::-webkit-scrollbar {
  display: none;
}

.carousel-item {
  flex: 0 0 100%;
  min-height: 250px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  
  scroll-snap-align: center;
}

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  position: relative;
  width: 90%;
  max-width: 900px;
}

.modal-video {
  width: 100%;
  border-radius: 8px;
  display: block;
}

.modal-close {
  position: absolute;
  top: -40px;
  right: 0;
  background: transparent;
  border: none;
  color: #fff;
  font-size: 1.5rem;
  cursor: pointer;
}
</style>