<script setup>
import MarkdownText from '@/components/MarkdownText.vue'

import previewVueTemplate from '@/assets/videos/preview-vue-template.mp4'
import previewTanamesaPipeline from '@/assets/videos/preview-tanamesa-pipe.mp4'
import previewPortfolio from '@/assets/videos/preview-portfolio.mp4'
import previewInferenceApi from '@/assets/videos/preview-inference-api.mp4'
import previewCashbackMultiagent from '@/assets/videos/preview-cashback-multiagent-analysis.mp4'

import { useI18n } from 'vue-i18n';
import { ref } from 'vue';

const { t } = useI18n()

const projects = [
  {
    key: 'arnaldo_gym',
    titleKey: 'projects_locale.items.arnaldo_gym.title',
    descriptionKey: 'projects_locale.items.arnaldo_gym.description',
    video: null,
    tags: ['Gemini', 'FastAPI', 'PostgreSQL'],
    projectLink: "https://arnaldogymai.com",
  },
  {
    key: 'cashback_multiagent',
    titleKey: 'projects_locale.items.cashback_multiagent.title',
    descriptionKey: 'projects_locale.items.cashback_multiagent.description',
    video: previewCashbackMultiagent,
    tags: ['Claude', 'Python', 'Pandas'],
    projectLink: "",
  },
  {
    key: 'inference_api',
    titleKey: 'projects_locale.items.inference_api.title',
    descriptionKey: 'projects_locale.items.inference_api.description',
    video: previewInferenceApi,
    tags: ['Ollama', 'FastAPI', 'Vue.js'],
    projectLink: "https://github.com/carlos-dani-dev/inference-api",
  },
  {
    key: 'vue_chatbot',
    titleKey: 'projects_locale.items.vue_chatbot.title',
    descriptionKey: 'projects_locale.items.vue_chatbot.description',
    video: previewVueTemplate,
    tags: ['Vue.js', 'FastAPI', 'PostgreSQL'],
    projectLink: "https://github.com/carlos-dani-dev/vue-chatbot-template",
  },
  {
    key: 'tanamesa_pipeline',
    titleKey: 'projects_locale.items.tanamesa_pipeline.title',
    descriptionKey: 'projects_locale.items.tanamesa_pipeline.description',
    video: previewTanamesaPipeline,
    tags: ['SQL', 'PostgreSQL', 'FastAPI'],
    projectLink: "https://github.com/carlos-dani-dev/tanamesa-data-pipeline",
  },
  {
    key: 'portfolio',
    titleKey: 'projects_locale.items.portfolio.title',
    descriptionKey: 'projects_locale.items.portfolio.description',
    video: previewPortfolio,
    tags: ['Vue', 'Tailwind', 'Javascript'],
    projectLink: "https://github.com/carlos-dani-dev/portfolio",
  }
]

const activeProject = ref(null)

function openModal(project) {
  activeProject.value = project
}
function closeModal() {
  activeProject.value = null
}
</script>

<template>
  <section id="projects-section" class="min-h-dvh snap-start flex flex-col justify-center py-8 max-w-10xl mx-auto px-4 md:px-8">

    <div class="text-center mb-8">
      <h2 class="colored-text text-4xl md:text-5xl font-bold tracking-tight mb-4">{{ t('projects_locale.title') }}</h2>
      <p class="text-lg opacity-80 max-w-1xl">
        <MarkdownText :content="t('projects_locale.section_description')" />
      </p>
    </div>

    <div class="project-list-wrapper">
      <ul class="project-list">
        <li
          v-for="project in projects" :key="project.key"
          class="project-card flex flex-col gap-3 w-full border rounded-2xl p-4 transition-all duration-300 hover:-translate-y-0.5">

          <div class="flex flex-row items-center justify-between gap-3">
            <p class="colored-text text-lg md:text-xl font-semibold break-words min-w-0"><MarkdownText :content="t(project.titleKey)" /></p>

            <div class="flex flex-row items-center gap-2 sm:gap-3 shrink-0">
              <a href="#"
                v-if="project.video"
                @click.prevent="openModal(project)"
                class="project-btn inline-flex items-center gap-2 px-2.5 py-1 sm:px-4 sm:py-1.5 text-xs sm:text-sm font-semibold transition-all duration-300 whitespace-nowrap"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                  <polygon points="6 3 20 12 6 21 6 3"></polygon>
                </svg>
                {{ t('projects_locale.full_preview_btn') }}
              </a>

              <a
                :href="project.projectLink"
                target="_blank"
                rel="noopener noreferrer"
                class="project-btn inline-flex items-center gap-2 px-2.5 py-1 sm:px-4 sm:py-1.5 text-xs sm:text-sm font-semibold transition-all duration-300 whitespace-nowrap"
              >
                {{t('projects_locale.project_btn_label')}}
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="7" y1="17" x2="17" y2="7"></line>
                  <polyline points="7 7 17 7 17 17"></polyline>
                </svg>
              </a>
            </div>
          </div>

          <div class="flex flex-wrap gap-2">
            <span
              v-for="tag in project.tags" :key="tag"
              class="colored-text skill-tag inline-flex border rounded-full px-3 py-1 text-xs sm:text-sm"
              >{{ tag }}</span>
          </div>

          <p class="text-sm sm:text-base opacity-80">
            <MarkdownText :content="t(project.descriptionKey)" />
          </p>
        </li>
      </ul>

      <div class="scroll-fade" aria-hidden="true"></div>
    </div>

    <div v-if="activeProject" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <button class="modal-close" @click="closeModal" aria-label="Fechar">✕</button>
        <video :src="activeProject.video" controls autoplay class="modal-video"></video>
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

.project-list-wrapper {
  position: relative;
  max-width: 900px;
  width: 100%;
  margin: 0 auto;
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  list-style: none;
  margin: 0;
  padding: 4px 4px 4px 4px;

  max-height: 55vh;
  overflow-y: auto;
  scroll-behavior: smooth;
}

.project-list::-webkit-scrollbar {
  width: 6px;
}

.project-list::-webkit-scrollbar-thumb {
  background-color: var(--project-card-border-color);
  border-radius: 999px;
}

.scroll-fade {
  position: absolute;
  left: 0;
  right: 6px;
  bottom: 0;
  height: 48px;
  pointer-events: none;
  background: linear-gradient(to bottom, transparent, var(--color-bg));
  border-radius: 0 0 16px 16px;
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

@media (max-width: 640px) {
  .project-list {
    max-height: 60vh;
  }
}
</style>
