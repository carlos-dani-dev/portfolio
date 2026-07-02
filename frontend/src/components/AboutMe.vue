<script setup>
    import { useI18n } from "vue-i18n";

    import MLIcon from "@/assets/icons/ml-icon.svg";
    import ResearchIcon from "@/assets/icons/research-icon.svg";
    import ServerIcon from "@/assets/icons/server-icon.svg";

    const {t} = useI18n()
</script>

<template>

<section id="aboutMe-section" class="flex flex-col items-center py-12">
    <div class="flex flex-col items-center py-10">
        <h2 class="colored-text lg:text-5xl font-bold tracking-tight mb-4">{{ t('aboutMe.title') }}</h2>
        <p>{{ t('aboutMe.section_description') }}</p>
    </div>
    
    <div class="flex flex-col gap-5">
        <p class="leading-relaxed text-lg max-w-6xl">
            {{ t('aboutMe.paragraph1') }}
        </p>
        
        <p class="leading-relaxed text-lg max-w-6xl">
            {{ t('aboutMe.paragraph2') }}
        </p>
    </div>

    <div class="flex justify-center items-center text-lg font-semibold py-10 gap-10">
        <div class="aboutMe-skill-card">
            <ServerIcon class="skill-card-icon"></ServerIcon>
            <p>{{ t('aboutMe.backend') }}</p>
        </div>
        <div class="aboutMe-skill-card">
            <MLIcon class="skill-card-icon"></MLIcon>
            <p>{{ t('aboutMe.ai') }}</p>
        </div>
        <div class="aboutMe-skill-card">
            <ResearchIcon class="skill-card-icon"></ResearchIcon>
            <p>{{ t('aboutMe.research') }}</p>
        </div>
    </div>
</section>

</template>

<style scoped>
.aboutMe-skill-card{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 300px;
    height: 140px;
    gap: 12px;
    border: 1px solid rgba(128, 128, 128, 0.15);
    border-radius: 14px;
    cursor: default;
    padding: 16px;
    background-color: var(--tags-bg-color);
    text-align: center;

    transition: transform 0.25s ease,
                    border-color 0.25s ease,
                    box-shadow 0.25s ease;
}

.aboutMe-skill-card:hover {
    transform: translateY(-6px);
    border-color: var(--me-tag-skill-border-color);
    background-color:  rgba(128, 128, 128, 0.2);
    box-shadow: 0 12px 30px -10px var(--aboutMe-skill-card-shade-color-hover);
}

.aboutMe-skill-card p{
    margin: 0;
    width: 100%;
}
.aboutMe-skill-card:hover p, .skill-card-icon {
    color: var(--aboutMe-skill-card-shade-color-hover);
    transform: scale(1.06);
}

.skill-card-icon{
    width: 40px;
    height: 40px;
    display: block;
}

.aboutMe-skill-card:hover .skill-card-icon :deep(path){
    fill: var(--aboutMe-skill-card-shade-color-hover);    
}

.skill-card-icon :deep(path){
    fill: var(--me-social-icon-color);
}

.colored-text{
    color: var(--me-text-color);
}
</style>