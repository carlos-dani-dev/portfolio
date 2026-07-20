<script setup>
import MarkdownText from '@/components/MarkdownText.vue'

import { useI18n } from 'vue-i18n';

import { useLangStore } from '@/stores/langStore';
import { useThemeStore } from '@/stores/themeStore';

const { t } = useI18n()
const langStore = useLangStore()
const themeStore = useThemeStore()

themeStore.initTheme()
langStore.initLang()

function download_resume() {
  const topbar = document.querySelector('.topbar')
  if (topbar) topbar.style.display = 'none'

  window.print()

  if (topbar) topbar.style.display = ''
}

const projects = [
  {
    key: 'cashback_multiagent',
    titleKey: 'projects_locale.items.cashback_multiagent.title',
    descriptionKey: 'projects_locale.items.cashback_multiagent.description',
    tags: ['Python', 'Pandas', 'Claude'],
    projectLink: "",
    videoElement: null
  },
  {
    key: 'inference_api',
    titleKey: 'projects_locale.items.inference_api.title',
    descriptionKey: 'projects_locale.items.inference_api.description',
    tags: ['Ollama', 'FastAPI', 'Vue.js'],
    projectLink: "https://github.com/carlos-dani-dev/inference-api",
    videoElement: null
  },
  {
    key: 'vue_chatbot',
    titleKey: 'projects_locale.items.vue_chatbot.title',
    descriptionKey: 'projects_locale.items.vue_chatbot.description',
    tags: ['Vue.js', 'FastAPI', 'PostgreSQL'],
    projectLink: "https://github.com/carlos-dani-dev/vue-chatbot-template",
    videoElement: null
  },
  {
    key: 'tanamesa_pipeline',
    titleKey: 'projects_locale.items.tanamesa_pipeline.title',
    descriptionKey: 'projects_locale.items.tanamesa_pipeline.description',
    tags: ['SQL', 'PostgreSQL', 'FastAPI'],
    projectLink: "https://github.com/carlos-dani-dev/tanamesa-data-pipeline",
    videoElement: null
  },
  {
    key: 'portfolio',
    titleKey: 'projects_locale.items.portfolio.title',
    descriptionKey: 'projects_locale.items.portfolio.description',
    tags: ['Vue', 'Tailwind', 'Javascript'],
    projectLink: "https://github.com/carlos-dani-dev/portfolio",
    videoElement: null
  }
]

const experiences = [
  {
    key: 'exp_1',
    roleKey: 'resume.exp_1_role',
    companyKey: 'resume.exp_1_company',
    periodKey: 'resume.exp_1_period',
    bulletKeys: [
      'resume.exp_1_bullet_1',
      'resume.exp_1_bullet_2',
      'resume.exp_1_bullet_3'
    ]
  },
  {
    key: 'exp_2',
    roleKey: 'resume.exp_2_role',
    companyKey: 'resume.exp_2_company',
    periodKey: 'resume.exp_2_period',
    bulletKeys: [
      'resume.exp_2_bullet_1',
      'resume.exp_2_bullet_2',
      'resume.exp_2_bullet_3',
      'resume.exp_2_bullet_4'
    ]
  },
  {
    key: 'exp_3',
    roleKey: 'resume.exp_3_role',
    companyKey: 'resume.exp_3_company',
    periodKey: 'resume.exp_3_period',
    bulletKeys: [
      'resume.exp_3_bullet_1',
      'resume.exp_3_bullet_2',
      'resume.exp_3_bullet_3',
      'resume.exp_3_bullet_4'
    ]
  }
]

</script>

<template>
<div class="resume-page">

  <div class="topbar">
    <nav class="breadcrumb">
      <router-link to="/" class="breadcrumb__link">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 3l9 8h-3v9h-5v-6H11v6H6v-9H3l9-8z"/></svg>
        {{ t('nav.home') }}
      </router-link>
      <span class="breadcrumb__sep">/</span>
      <span class="breadcrumb__current">{{ t('nav.resume') }}</span>
    </nav>

    <div class="topbar__controls">
      <div>
        <select class="font-bold" :value="langStore.currentLang" @change="langStore.setLang($event.target.value)">
          <option value="pt-br">pt-BR</option>
          <option value="en-usa">en-USA</option>
        </select>
      </div>

      <div>
        <input :checked="themeStore.isDark" v-on:change="themeStore.changeTheme()" id="checkboxInput" type="checkbox" />
        <label class="toggleSwitch" for="checkboxInput">
          <div class="icon icon--moon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="26" height="26">
              <path fill-rule="evenodd" d="M9.528 1.718a.75.75 0 01.162.819A8.97 8.97 0 009 6a9 9 0 009 9 8.97 8.97 0 003.463-.69.75.75 0 01.981.98 10.503 10.503 0 01-9.694 6.46c-5.799 0-10.5-4.701-10.5-10.5 0-4.368 2.667-8.112 6.46-9.694a.75.75 0 01.818.162z" clip-rule="evenodd"></path>
            </svg>
          </div>
          <div class="icon icon--sun">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="26" height="26">
              <path d="M12 2.25a.75.75 0 01.75.75v2.25a.75.75 0 01-1.5 0V3a.75.75 0 01.75-.75zM7.5 12a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM18.894 6.166a.75.75 0 00-1.06-1.06l-1.591 1.59a.75.75 0 101.06 1.061l1.591-1.59zM21.75 12a.75.75 0 01-.75.75h-2.25a.75.75 0 010-1.5H21a.75.75 0 01.75.75zM17.834 18.894a.75.75 0 001.06-1.06l-1.59-1.591a.75.75 0 10-1.061 1.06l1.59 1.591zM12 18a.75.75 0 01.75.75V21a.75.75 0 01-1.5 0v-2.25A.75.75 0 0112 18zM7.758 17.303a.75.75 0 00-1.061-1.06l-1.591 1.59a.75.75 0 001.06 1.061l1.591-1.59zM6 12a.75.75 0 01-.75.75H3a.75.75 0 010-1.5h2.25A.75.75 0 016 12zM6.697 7.757a.75.75 0 001.06-1.06l-1.59-1.591a.75.75 0 00-1.061 1.06l1.59 1.591z"></path>
            </svg>
          </div>
        </label>
      </div>

      <a class="download-a" v-on:click="download_resume()" download>
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 3v10.586l3.293-3.293 1.414 1.414L12 17.414l-4.707-4.707 1.414-1.414L12 13.586V3h0zM5 19h14v2H5v-2z"/></svg>
        {{ t('resume.download_btn') }}
      </a>
    </div>
  </div>

  <section id="resume" class="resume">
    <header class="resume__header">
      <h1 class="resume__name">{{ t('resume.name') }}</h1>
      <p class="resume__role">{{ t('resume.role') }}</p>

      <div class="resume__contact">
        <a class="resume__contact-item" href="mailto:carlos.rocha@ufpi.edu.br">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M2 4h20v16H2V4zm2 2.4V18h16V6.4l-8 6.4-8-6.4zm.8-.4L12 11.5 19.2 6H4.8z"/></svg>
          carlos.rocha@ufpi.edu.br
        </a>
        <a class="resume__contact-item" href="#" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M19 3a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h14zM8.34 18v-8.4H5.67V18h2.67zM7 8.4a1.55 1.55 0 100-3.1 1.55 1.55 0 000 3.1zM18.34 18v-4.62c0-2.48-1.32-3.63-3.08-3.63a2.66 2.66 0 00-2.4 1.32V9.6h-2.67c.03.7 0 8.4 0 8.4h2.67v-4.69c0-.25.02-.5.1-.68a1.5 1.5 0 011.4-1c1 0 1.4.75 1.4 1.86V18h2.58z"/></svg>
          carlos-daniel-portela
        </a>
        <a class="resume__contact-item" href="https://github.com/carlos-dani-dev" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M12 2a10 10 0 00-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.46-1.16-1.11-1.47-1.11-1.47-.9-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.9 1.52 2.34 1.08 2.91.83.09-.65.35-1.08.63-1.33-2.22-.25-4.56-1.11-4.56-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.65 0 0 .84-.27 2.75 1.02a9.4 9.4 0 015 0c1.9-1.3 2.75-1.02 2.75-1.02.55 1.38.2 2.4.1 2.65.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.85v2.75c0 .26.18.58.69.48A10 10 0 0012 2z"/></svg>
          @carlos-dani-dev
        </a>
        <a class="resume__contact-item" href="https://carlos-dani-dev.github.io/portfolio/home" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
          Web Portfolio
        </a>
      </div>
    </header>

    <section class="resume__section">
      <h2 class="resume__title">{{ t('resume.summary_title') }}</h2>
      <MarkdownText class="resume__summary" :content="t('resume.summary_text')" />
    </section>

    <!-- experiência profissional -->
    <section class="resume__section">
      <h2 class="resume__title">{{ t('resume.experience_title') }}</h2>

      <article
        v-for="exp in experiences" :key="exp.key"
        class="resume__entry">
        <div class="resume__entry-head">
          <div>
            <h3 class="resume__entry-role">{{ t(exp.roleKey) }}</h3>
            <p class="resume__entry-company">{{ t(exp.companyKey) }}</p>
          </div>
          <span class="resume__entry-period">{{ t(exp.periodKey) }}</span>
        </div>
        <ul class="resume__bullets">
          <li v-for="bulletKey in exp.bulletKeys" :key="bulletKey">{{ t(bulletKey) }}</li>
        </ul>
      </article>
    </section>

    <section class="resume__section">
      <h2 class="resume__title">{{ t('projects_locale.title') }}</h2>

      <a
        v-for="project in projects" :key="project.key"
        class="resume__entry resume__entry--link"
        :href="project.projectLink"
        target="_blank"
        rel="noopener">
        <div class="resume__entry-head">
          <h3 class="resume__entry-role"><MarkdownText :content="t(project.titleKey)" /></h3>
        </div>
        <ul class="resume__bullets">
          <li><MarkdownText :content="t(project.descriptionKey)" /></li>
        </ul>
      </a>
    </section>

    <section class="resume__section">
      <h2 class="resume__title">{{ t('resume.education_title') }}</h2>
      <div class="resume__entry-head">
        <div>
          <h3 class="resume__entry-role">{{ t('resume.education_degree') }}</h3>
          <p class="resume__entry-company">{{ t('resume.education_school') }}</p>
        </div>
        <span class="resume__entry-period">{{ t('resume.education_period') }}</span>
      </div>
    </section>

    <section class="resume__section">
      <h2 class="resume__title">{{ t('resume.languages_title') }}</h2>
      <ul class="resume__bullets">
        <li>{{ t('resume.language_1') }}</li>
        <li>{{ t('resume.language_2') }}</li>
      </ul>
    </section>
  </section>

</div>
</template>

<style scoped>
.resume-page {
  background-color: var(--color-bg);
  min-height: 100vh;
  padding: 5.5rem 1.25rem 4rem;
}

.topbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 40;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.75rem;
  padding: 0.85rem 1.5rem;
  background-color: var(--color-bg);
  border-bottom: 1px solid var(--resume-section-border-color);
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
}

.breadcrumb__link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  text-decoration: none;
  color: var(--resume-muted-text-color);
}

.breadcrumb__link:hover { color: var(--nav-a-text-color-hover); }
.breadcrumb__sep { color: var(--resume-muted-text-color); }
.breadcrumb__current { font-weight: 700; }

.topbar__controls {
  display: flex;
  align-items: center;
  gap: 1.1rem;
}

.download-a {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.85rem;
  font-weight: 700;
  text-decoration: none;
  color: inherit;
  border: 1px solid var(--resume-card-border-color);
  border-radius: 8px;
  padding: 0.4rem 0.75rem;
  transition: border-color 0.2s ease, color 0.2s ease;
}

.download-a:hover {
  color: var(--nav-a-text-color-hover);
  border-color: var(--nav-a-text-color-hover);
}

select option {
  background-color: var(--resume-option-bg-color);
  color: var(--resume-option-text-color);
}

/* theme toggle — mesmo mecanismo do Nav.vue */
.toggleSwitch {
  width: 40px;
  height: 40px;
  display: grid;
  border-radius: 50%;
  position: relative;
  place-items: center;
  cursor: pointer;
  line-height: 1;
  overflow: hidden;
}

#checkboxInput { display: none; }

.icon {
  grid-column: 1 / 1;
  grid-row: 1 / 1;
  width: 70%;
  height: 70%;
  display: grid;
  place-items: center;
  z-index: 2;
  transform-origin: center center;
  transition: transform 500ms ease, opacity 300ms ease;
  opacity: 0;
  pointer-events: none;
  color: var(--nav-theme-btn-icon-color);
}

.icon--moon,
.icon--sun {
  transform: rotate(0deg) scale(0);
  opacity: 0;
}

#checkboxInput:not(:checked) + .toggleSwitch .icon--moon {
  transform: rotate(360deg) scale(1);
  opacity: 1;
}

#checkboxInput:not(:checked) + .toggleSwitch .icon--sun {
  transform: rotate(0deg) scale(0);
  opacity: 0;
}

#checkboxInput:checked + .toggleSwitch .icon--sun {
  transform: rotate(360deg) scale(1);
  opacity: 1;
}

#checkboxInput:checked + .toggleSwitch .icon--moon {
  transform: rotate(0deg) scale(0);
  opacity: 0;
}

#checkboxInput:active + .toggleSwitch { transform: scale(0.94); }
.icon svg { fill: currentColor !important; }

/* ---------- resume card ---------- */
.resume {
  max-width: 820px;
  margin: 0 auto;
  background: var(--resume-card-bg-color);
  border: 1px solid var(--resume-card-border-color);
  border-radius: 14px;
  padding: 2.5rem 2.25rem;
}

.resume__header { margin-bottom: 1.5rem; }

.resume__name {
  font-size: 2rem;
  font-weight: 700;
  margin: 0 0 0.25rem;
}

.resume__role {
  color: var(--resume-accent-color);
  font-weight: 600;
  font-size: 1.05rem;
  margin: 0 0 1rem;
}

.resume__contact {
  display: flex;
  flex-wrap: wrap;
  gap: 1.1rem;
}

.resume__contact-item {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.85rem;
  color: var(--resume-muted-text-color);
  text-decoration: none;
}

.resume__contact-item:hover { color: var(--nav-a-text-color-hover); }

.resume__section {
  padding: 1.35rem 0;
  border-top: 1px solid var(--resume-section-border-color);
}

.resume__title {
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--resume-muted-text-color);
  margin: 0 0 1rem;
}

.resume__summary {
  display: block;
  line-height: 1.65;
  font-size: 0.95rem;
}

.resume__summary :deep(strong) {
  color: var(--resume-accent-color);
  font-weight: 600;
}

.resume__entry { margin-bottom: 1.4rem; }
.resume__entry:last-child { margin-bottom: 0; }

.resume__entry--link {
  display: block;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
  transition: color 0.2s ease;
}

.resume__entry--link:hover,
.resume__entry--link:focus-visible {
  color: var(--resume-accent-color);
}

.resume__entry--link:hover .resume__entry-role,
.resume__entry--link:focus-visible .resume__entry-role {
  color: var(--resume-accent-color);
}

.resume__entry-head {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: baseline;
  gap: 0.4rem 1rem;
  margin-bottom: 0.5rem;
}

.resume__entry-role {
  font-weight: 700;
  font-size: 1rem;
  margin: 0;
}

.resume__entry-company {
  color: var(--resume-accent-color);
  font-size: 0.88rem;
  margin: 0.15rem 0 0;
}

.resume__entry-period {
  font-size: 0.82rem;
  color: var(--resume-muted-text-color);
  white-space: nowrap;
}

.resume__bullets {
  margin: 0;
  padding-left: 1.15rem;
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--resume-muted-text-color);
}

.resume__bullets li { margin-bottom: 0.35rem; }
.resume__bullets li::marker { color: var(--resume-bullet-marker-color); }

.resume__bullets--projects li { list-style: disc; color: inherit; }
.resume__project-stack {
  display: block;
  color: var(--resume-muted-text-color);
  font-size: 0.85rem;
  margin-top: 0.15rem;
}

@media (max-width: 640px) {
  .resume { padding: 1.75rem 1.4rem; }
  .resume__name { font-size: 1.6rem; }
  .topbar { padding: 0.75rem 1rem; }
  .topbar__controls { gap: 0.7rem; }
}

@media print {
  * {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    color-adjust: exact !important;
  }

  @page {
    margin: 0;
    size: A4;
  }

  .topbar {
    display: none !important;
  }

  .resume-page {
    padding: 0 !important;
    min-height: 0 !important;
    background-color: var(--color-bg) !important;
  }

  .resume {
    border: none !important;
    border-radius: 0 !important;
    box-shadow: none !important;
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 0.6in 0.55in !important;
    background-color: var(--color-bg) !important;
  }

  html, body {
    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    background-color: var(--color-bg) !important;
    color: var(--color-text) !important;
  }

  .resume__entry {
    break-inside: avoid;
  }

  .resume__header {
    break-inside: avoid;
  }

  .resume__title {
    break-after: avoid;
  }
}

</style>