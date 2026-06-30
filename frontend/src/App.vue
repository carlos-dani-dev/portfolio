<script setup>
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
    <router-view></router-view>
</template>

<style scoped>
</style>
