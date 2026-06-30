<script setup>
    import { onMounted } from 'vue';
    
    import { useLangStore } from '@/stores/langStore';
    import { useThemeStore } from '@/stores/themeStore';
    
    const langStore = useLangStore();
    const themeStore = useThemeStore();
    onMounted(() => {
        themeStore.initTheme()
    })

</script>

<template>

<nav class="w-full">

    <div :page-theme="themeStore.currentTheme" class="flex justify-between items-center">

        <h1 class="text-x1 font-bold">Carlos Portela</h1>

        <div class="">
            <ul class="flex flex-wrap gap-3">
                <li><a>Sobre mim</a></li>
                <li><a>Projetos</a></li>
                <li><a>Experiências</a></li>
                <li><a>Contato</a></li>
            </ul>
        </div>

        <div class="flex gap-3">
            <div>
                <select :value="langStore.currentLang" @change="langStore.setLang($event.target.value)">
                    <option value="pt-br">pt-BR</option>
                    <option value="en-usa">en-USA</option>
                </select>
            </div>
            <div>
                <a @click="themeStore.changeTheme()">
                    <span>Language switch button</span>
                </a>
            </div>
        </div>
    </div>

</nav>

</template>

<style scoped>
nav {
    background-color: var(--color-bg);
    color: var(--color-text);
    transition: background-color 0.3s ease, color 0.3s ease;
    padding: 1rem;
}
</style>