<script setup>
    import { useI18n } from "vue-i18n";

    import GithubIcon from "@/assets/icons/icons8-github.svg";
    import LinkedinIcon from "@/assets/icons/icons8-linkedin.svg";
    import meImage from "@/assets/images/me.png";

    const {t} = useI18n()
</script>

<template>

<section class="p-12 max-w-6xl mx-auto flex flex-col-reverse lg:grid lg:grid-cols-[1fr_auto] gap-12 lg:gap-24 items-center justify-between">
  <div>
    <div class="flex gap-2">
        <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-sm mb-6">
        {{t('me.fs_skill_tag')}}
        </span>
        <span class="colored-text skill-tag inline-flex border rounded-full px-3.5 py-1.5 text-sm mb-6">
        {{t('me.ml_researcher_skill_tag')}}
        </span>
    </div>
    <p class="text-xl mb-2"><MarkdownText :content="t('me.hello')" /></p>
    <h1 class="colored-text lg:text-7xl font-bold mb-6 tracking-tight">Carlos Portela</h1>
    <p class="leading-relaxed text-xl opacity-80  mb-8">
        <MarkdownText :content="t('me.intro')" />
    </p>
    <div class="flex gap-3 mb-6">
        <a href="https://github.com/carlos-dani-dev" class="social-tag w-10 h-10 rounded-full border flex items-center justify-center">
            <GithubIcon class="social-icon"></GithubIcon>
        </a>
        <a href="https://www.linkedin.com/in/carlos-daniel-5794a3311" class="social-tag w-10 h-10 rounded-full border flex items-center justify-center">
            <LinkedinIcon class="social-icon"></LinkedinIcon>
        </a>
    </div>
    <div class="flex gap-3">
    </div>
  </div>
  <div class="img-mockup lg:w-[430px] lg:h-[430px] rounded-full overflow-hidden mx-auto">
        <img :src="meImage" alt="Carlos Portela" class="w-full h-full object-cover" />
  </div>
</section>

</template>

<style scoped>
.img-mockup{
    background-color: var(--me-img-mockup-bg-color);
    box-shadow: 0 0 100px -20px var(--me-img-mockup-bg-color);
}

.skill-tag{
    border: 1px solid var(--me-tag-skill-border-color);
    background-color: var(--me-tag-skill-bg-color);
}

.colored-text{
    color: var(--me-text-color);
}

.social-tag{
    border: 1px solid rgba(128, 128, 128, 0.15);
    background-color: var(--me-tag-skill-bg-color);
}
.social-icon:deep(path) {
  fill: var(--me-social-icon-color);
}

.social-tag:hover {
  background-color: var(--me-tag-skill-border-color);
}


</style>