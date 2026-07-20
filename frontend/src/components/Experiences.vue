<script setup>
import MarkdownText from '@/components/MarkdownText.vue'
import { useI18n } from 'vue-i18n';

const { t } = useI18n()

const experiences = [
  {
    key: 'xp_1',
    titleKey: 'experiences.xp_1_title',
    descriptionKey: 'experiences.xp_1_description',
    dateKey: 'experiences.xp_1_date',
    company: 'LabVip, UFPI',
    tags: ['Python', 'Tensorflow', 'Numpy', 'Pandas']
  },
  {
    key: 'xp_2',
    titleKey: 'experiences.xp_2_title',
    descriptionKey: 'experiences.xp_2_description',
    dateKey: 'experiences.xp_2_date',
    company: 'IGDS - Instituto de Gestão e Desenvolvimento Sustentável',
    tags: ['Python', 'FastAPI', 'PostgreSQL', 'Metabase']
  }
]
</script>

<template>
  <section id="experiences-section" class="min-h-dvh snap-start flex flex-col justify-center py-12 max-w-[1000px] mx-auto px-8">

    <div class="flex flex-col items-center mb-16">
      <h2 class="colored-text text-4xl md:text-5xl font-bold tracking-tight mb-4">{{ t('experiences.title') }}</h2>
      <p class="text-lg opacity-80 max-w-1xl">
        <MarkdownText :content="t('experiences.section_description')" />
      </p>
    </div>

    <div class="relative border-l-2 border-gray-700/50 ml-3 md:ml-4 space-y-12 pb-8">

      <div
        v-for="experience in experiences" :key="experience.key"
        class="relative pl-8 md:pl-12"
      >
        <span class="timeline-dot absolute -left-[9px] top-8 w-4 h-4 rounded-full"></span>

        <div class="experience-card flex flex-col p-6 md:p-8 rounded-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">

          <div class="flex flex-col md:flex-row md:justify-between md:items-start mb-4 gap-2">
            <div>
              <h3 class="text-2xl font-bold">{{ t(experience.titleKey) }}</h3>
              <div class="flex items-center gap-3 mt-1">
                <span class="colored-text font-semibold text-lg tracking-wider">{{ experience.company }}</span>
              </div>
            </div>
            <span class="text-sm font-medium opacity-60 md:text-right whitespace-nowrap pt-1">
              {{ t(experience.dateKey) }}
            </span>
          </div>

          <p class="text-base opacity-80 mb-6 leading-relaxed">
            <MarkdownText :content="t(experience.descriptionKey)" />
          </p>

          <div class="flex flex-wrap gap-3 mt-auto">
            <span
              v-for="tag in experience.tags" :key="tag"
              class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-xs font-medium"
            >{{ tag }}</span>
          </div>

        </div>
      </div>

    </div>

  </section>
</template>

<style scoped>
.experience-card {
  background-color: var(--experience-card-bg-color);
  border: 1px solid var(--experience-card-border-color);
}

.experience-card:hover {
  border-color: var(--experience-card-border-color-hover, rgba(128, 128, 128, 0.3));
}

.colored-text {
  color: var(--title-text-color);
}

.timeline-dot {
  background-color: var(--title-text-color);
}

.skill-tag {
  border-color: var(--tag-skill-border-color);
  background-color: var(--tag-skill-bg-color);
}

h3, p {
  color: var(--text-primary, inherit);
}
</style>
