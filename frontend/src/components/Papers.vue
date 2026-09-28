<script setup>
import MarkdownText from '@/components/MarkdownText.vue'

import thumbMicai2026 from '@/assets/images/thumb-micai2026.png'
import thumbSbpo2026 from '@/assets/images/thumb-sbpo2026.png'

import { useI18n } from 'vue-i18n';

const { t } = useI18n()

const papers = [
  {
    key: 'micai2026',
    titleKey: 'papers_locale.items.micai2026.title',
    descriptionKey: 'papers_locale.items.micai2026.description',
    thumb: thumbMicai2026,
    tags: ['Python', 'Tensorflow', 'Deep Learning'],
    paperLink: "https://micai.org/2026/authors/#guide_accepted",
  },
  {
    key: 'sbpo2026',
    titleKey: 'papers_locale.items.sbpo2026.title',
    descriptionKey: 'papers_locale.items.sbpo2026.description',
    thumb: thumbSbpo2026,
    tags: ['Otimização', 'Pesquisa Operacional', 'Python'],
    paperLink: "https://eventos.galoa.com.br/sbpo-2026/page/7035-inicio",
  }
]
</script>

<template>
  <section id="papers-section" class="min-h-dvh snap-start flex flex-col justify-center py-8 max-w-10xl mx-auto px-4 md:px-8">

    <div class="text-center mb-8">
      <h2 class="colored-text text-4xl md:text-5xl font-bold tracking-tight mb-4">{{ t('papers_locale.title') }}</h2>
      <p class="text-lg opacity-80 max-w-1xl">
        <MarkdownText :content="t('papers_locale.section_description')" />
      </p>
    </div>

    <ul class="papers-grid">
      <li
        v-for="paper in papers" :key="paper.key"
        class="paper-card overflow-hidden border flex flex-col w-full rounded-2xl transition-all duration-300 hover:-translate-y-1">

        <div class="card-media">
          <img :src="paper.thumb" class="thumb" alt="Paper poster" />
        </div>

        <div class="flex flex-col gap-3 p-3 sm:p-4">

          <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-2 min-w-0">
            <p class="colored-text text-lg sm:text-xl font-semibold break-words min-w-0"><MarkdownText :content="t(paper.titleKey)" /></p>

            <a
              :href="paper.paperLink"
              target="_blank"
              rel="noopener noreferrer"
              class="paper-btn inline-flex items-center gap-2 px-2.5 py-1 sm:px-4 sm:py-1.5 text-xs sm:text-sm font-semibold transition-all duration-300 whitespace-nowrap shrink-0"
            >
              {{ t('papers_locale.view_paper_btn') }}
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="7" y1="17" x2="17" y2="7"></line>
                <polyline points="7 7 17 7 17 17"></polyline>
              </svg>
            </a>
          </div>

          <div class="flex flex-wrap gap-2">
            <span
              v-for="tag in paper.tags" :key="tag"
              class="colored-text skill-tag inline-flex border rounded-full px-3 py-1 text-xs sm:text-sm"
              >{{ tag }}</span>
          </div>

          <p class="text-sm sm:text-base opacity-80">
            <MarkdownText :content="t(paper.descriptionKey)" />
          </p>
        </div>
      </li>
    </ul>

  </section>
</template>

<style scoped>
.paper-card {
  background-color: var(--project-card-bg-color);
  border-color: var(--project-card-border-color);
}

.paper-card:hover {
  border-color: var(--project-card-border-color-hover);
}

.card-media {
  position: relative;
  overflow: hidden;
  width: 100%;
  aspect-ratio: 16 / 9;
  background-color: var(--project-card-bg-color);
}

.thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  inset: 0;
}

.colored-text {
  color: var(--title-text-color);
}

.skill-tag {
  border-color: var(--tag-skill-border-color);
  background-color: var(--tag-skill-bg-color);
}

.paper-btn {
  color: var(--title-text-color);
  border: 1px solid var(--contact-social-tag-border-color);
  background-color: var(--contact-social-tag-bg-color);
  text-decoration: none;
}

.paper-btn:hover {
  background-color: var(--title-text-color);
  color: black;
  border-color: var(--title-text-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.paper-btn svg {
  transition: transform 0.3s ease;
}

.paper-btn:hover svg {
  transform: translate(2px, -2px);
}

.papers-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.5rem;
  list-style: none;
  margin: 0;
  padding: 8px;
  max-width: 1100px;
  width: 100%;
  margin-inline: auto;
}

@media (max-width: 768px) {
  .papers-grid {
    grid-template-columns: 1fr;
  }
}
</style>
