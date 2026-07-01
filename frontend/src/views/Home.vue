<script setup>
import AboutMe from '@/components/AboutMe.vue';
import Me from '@/components/Me.vue';
import Header from '@/components/Header.vue';
import Stacks from '@/components/Stacks.vue';
import Projects from '@/components/Projects.vue';

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
<Me></Me>
<AboutMe></AboutMe>
<Stacks></Stacks>
<Projects></Projects>
</template>

<style scoped>
</style>