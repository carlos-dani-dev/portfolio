<script setup>
import AboutMe from '@/components/AboutMe.vue';
import Me from '@/components/Me.vue';
import Header from '@/components/Header.vue';
import Stacks from '@/components/Stacks.vue';
import Projects from '@/components/Projects.vue';
import Experiences from '@/components/Experiences.vue';
import Contact from '@/components/Contact.vue';

import { onMounted } from 'vue';

import { useThemeStore } from '@/stores/themeStore';
import { useLangStore } from '@/stores/langStore'; 


const themeStore = useThemeStore()
const langStore = useLangStore()

onMounted(() => {
    themeStore.initTheme()
    langStore.initLang()
})

</script>

<template>
<Header></Header>
<main class="pt-24 h-dvh overflow-y-auto snap-y snap-proximity scroll-pt-24 scroll-smooth">
    <Me></Me>
    <AboutMe></AboutMe>
    <Stacks></Stacks>
    <Projects></Projects>
    <Experiences></Experiences>
    <Contact></Contact>
</main>
</template>

<style scoped>
</style>