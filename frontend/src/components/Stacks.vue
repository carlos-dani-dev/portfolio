<script setup>
import { useI18n } from 'vue-i18n';

const {t} = useI18n()

const stacks = [
    { name: 'JavaScript', usage: 'Frontend', icon: new URL('../assets/icons/js.svg', import.meta.url).href },
    { name: 'Python', usage: 'APIs & Backend', icon: new URL('../assets/icons/py.svg', import.meta.url).href },
    { name: 'AWS', usage: 'APIs & Backend', icon: new URL('../assets/icons/aws.svg', import.meta.url).href },
    { name: 'Docker', usage: 'DevOps', icon: new URL('../assets/icons/docker.png', import.meta.url).href },
    { name: 'Linux OS', usage: 'DevOps', icon: new URL('../assets/icons/linux.png', import.meta.url).href },
    { name: 'Vue.js', usage: 'Frontend', icon: new URL('../assets/icons/vue.svg', import.meta.url).href },
    { name: 'Git', usage: 'Code versioning', icon: new URL('../assets/icons/git.svg', import.meta.url).href },
    { name: 'PostgreSQL', usage: 'Backend', icon: new URL('../assets/icons/postgre.png', import.meta.url).href },
    { name: 'FastAPI', usage: 'APIs & Backend', icon: new URL('../assets/icons/fastapi.svg', import.meta.url).href},
    { name: 'Tailwind', usage: 'Frontend', icon: new URL('../assets/icons/tailwind.svg', import.meta.url).href}
];
</script>

<template>

<section id="stacks-section" class="py-12 max-w-6xl mx-auto px-8">
    <div class="text-center mb-16">
        <h2 class="colored-text text-4xl md:text-5xl font-bold mb-4 tracking-tight">{{t('stacks.title')}}</h2>
        <p class="max-w-2xl mx-auto text-lg opacity-80 max-w-1xl">
            <MarkdownText :content="t('stacks.description')" />
        </p>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6">
        <div 
            v-for="stack in stacks" 
            :key="stack.name"
            class="stack-card flex flex-col items-center justify-center p-6 rounded-2xl border transition-all duration-300 hover:-translate-y-1 cursor-pointer"
        >
            <div class="w-14 h-14 mb-4 flex items-center justify-center">
                <img :src="stack.icon" :alt="stack.name" class="stack-icon" />
            </div>
            <span class="text-sm font-bold">{{ stack.name }}</span>
            <span class="text-xs font-semibold">{{ stack.usage }}</span>
        </div>
    </div>
</section>

</template>

<style scoped>
.stack-card {
    background-color: rgba(128, 128, 128, 0.05);
    border-color: rgba(128, 128, 128, 0.15);
}

.stack-card:hover {
    background-color: rgba(128, 128, 128, 0.1);
    border-color: var(--me-tag-skill-border-color, rgba(128, 128, 128, 0.3));
}

.stack-icon {
    width: 100%;
    height: 100%;
    object-fit: contain;
}

.colored-text{
    color: var(--me-text-color);
}
</style>