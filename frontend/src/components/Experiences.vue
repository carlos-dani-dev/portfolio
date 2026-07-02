<script setup>
import { useI18n } from 'vue-i18n';

const {t} = useI18n()

</script>

<template>
<section id="experiences-section" class="py-12 max-w-[1000px] mx-auto px-8">
  
  <div class="flex flex-col items-center mb-16">
    <h2 class="colored-text text-4xl md:text-5xl font-bold tracking-tight mb-4">{{t('experiences.title')}}</h2>
    <p class="text-lg opacity-80 max-w-1xl">
      <MarkdownText :content="t('experiences.section_description')" />
    </p>
  </div>

  <div class="relative border-l-2 border-gray-700/50 ml-3 md:ml-4 space-y-12 pb-8">
    
    <div class="relative pl-8 md:pl-12">
      <span class="timeline-dot absolute -left-[9px] top-8 w-4 h-4 rounded-full"></span>
      
      <div class="experience-card flex flex-col p-6 md:p-8 rounded-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">
        
        <div class="flex flex-col md:flex-row md:justify-between md:items-start mb-4 gap-2">
          <div>
            <h3 class="text-2xl font-bold">{{t('experiences.xp_1_title')}}</h3>
            <div class="flex items-center gap-3 mt-1">
              <span class="colored-text font-semibold text-lg tracking-wider">LabVip, UFPI</span>
            </div>
          </div>
          <span class="text-sm font-medium opacity-60 md:text-right whitespace-nowrap pt-1">
            {{t('experiences.xp_1_date')}}
          </span>
        </div>
        
        <p class="text-base opacity-80 mb-6 leading-relaxed">
          <MarkdownText :content="t('experiences.xp_1_description')" />
        </p>
        
        <div class="flex flex-wrap gap-3 mt-auto">
          <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-xs font-medium">Python</span>
          <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-xs font-medium">Tensorflow</span>
          <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-xs font-medium">Numpy</span>
          <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-xs font-medium">Pandas</span>
        </div>
        
      </div>
    </div>

    <div class="relative pl-8 md:pl-12">
      <span class="timeline-dot absolute -left-[9px] top-8 w-4 h-4 rounded-full"></span>
      
      <div class="experience-card flex flex-col p-6 md:p-8 rounded-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">

        <div class="flex flex-col md:flex-row md:justify-between md:items-start mb-4 gap-2">
          <div>
            <h3 class="text-2xl font-bold">{{ t('experiences.xp_2_title') }}</h3>
            <div class="flex items-center gap-3 mt-1">
              <span class="colored-text font-semibold text-lg tracking-wider">IGDS - Instituto de Gestão e Desenvolvimento Sustentável</span>
            </div>
          </div>
          <span class="text-sm font-medium opacity-60 md:text-right whitespace-nowrap pt-1">
            {{t('experiences.xp_2_date')}}
          </span>
        </div>
        
        <p class="text-base opacity-80 mb-6 leading-relaxed">
          <MarkdownText :content="t('experiences.xp_2_description')" />
        </p>
        
        <div class="flex flex-wrap gap-3 mt-auto">
          <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-xs font-medium">Python</span>
          <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-xs font-medium">FastAPI</span>
          <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-xs font-medium">PostgreSQL</span>
          <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-xs font-medium">Metabase</span>
        </div>
        
      </div>
    </div>

  </div>

</section>
</template>

<style scoped>
.experience-card {
  background-color: var(--project-card-bg-color, rgba(128, 128, 128, 0.05));
  border: 1px solid rgba(128, 128, 128, 0.15);
}

.experience-card:hover {
  border-color: var(--me-tag-skill-border-color, rgba(128, 128, 128, 0.3));
}

.colored-text {
  color: var(--me-text-color);
}

.timeline-dot {
  background-color: var(--me-text-color);
  box-shadow: 0 0 0 4px var(--app-bg-color, #0f172a);
}

.badge-bg {
  background-color: var(--me-tag-skill-bg-color);
}

.skill-tag {
  border-color: var(--me-tag-skill-border-color);
  background-color: var(--me-tag-skill-bg-color);
}

h3, p {
  color: var(--text-primary, inherit);
}
</style>
