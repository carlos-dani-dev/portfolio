<script setup>
    import { useI18n } from "vue-i18n";

    import GithubIcon from "@/assets/icons/icons8-github.svg";
    import LinkedinIcon from "@/assets/icons/icons8-linkedin.svg";

    const {t} = useI18n()
</script>

<template>

<section class="p-12 max-w-6xl mx-auto grid grid-cols-[1fr_320px] gap-8 items-center">
  <div>
    <div class="flex gap-2">
        <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-sm mb-6">
        {{t('me.fs_skill_tag')}}
        </span>
        <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-sm mb-6">
        {{t('me.ml_researcher_skill_tag')}}
        </span>
    </div>
    <p class="text-xl mb-1">{{ t('me.hello') }}</p>
    <h1 class="colored-text text-4xl font-bold mb-4">Carlos Portela</h1>
    <p class="leading-relaxed max-w-md mb-6">
        {{ t('me.intro') }}
    </p>
    <div class="flex gap-3 mb-6">
        <a class="skill-tag w-10 h-10 rounded-full border flex items-center justify-center">
            <GithubIcon class="social-icon"></GithubIcon>
        </a>
        <a class="skill-tag w-10 h-10 rounded-full border flex items-center justify-center">
            <LinkedinIcon class="social-icon"></LinkedinIcon>
        </a>
    </div>
    <div class="flex gap-3">
    </div>
  </div>
  <div class="img-mockup w-[300px] h-[300px] rounded-full overflow-hidden mx-auto">
    <img src="../assets/images/me.png" class="w-full h-full object-cover" />
  </div>
</section>

</template>

<style scoped>
.img-mockup{
    background-color: var(--me-img-mockup-bg-color);
}

.skill-tag{
    border-color: var(--me-tag-skill-border-color);
    background-color: var(--me-tag-skill-bg-color);
}

.colored-text{
    color: var(--me-text-color);
}

.social-icon :deep(path) {
  fill: var(--me-social-icon-color);
}

</style>