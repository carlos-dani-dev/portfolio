<!--
  Uso:
  Importe e use o componente em qualquer view/component:
    import Script from '@/components/Script.vue'
    <Script />

  Para trocar quais arquivos ele exibe, edite o array `scripts` abaixo:
  cada item precisa de { filename, code }, onde `code` vem de um import
  `?raw` (Vite lê o arquivo como texto puro, sem precisar colar o conteúdo
  manualmente e sem risco de o código exibido divergir do arquivo real).
-->
<script setup>
import { ref } from 'vue'

import pyprojectGpu from '@/assets/scripts/pyproject-gpu.toml?raw'
import faceDetection from '@/assets/scripts/face_detection.py?raw'
import datasetVectorizer from '@/assets/scripts/dataset_vectorizer.py?raw'

const scripts = [
  { filename: 'pyproject-gpu.toml', code: pyprojectGpu },
  { filename: 'face_detection.py', code: faceDetection },
  { filename: 'dataset_vectorizer.py', code: datasetVectorizer }
]

const copiedIndex = ref(null)

async function copyCode(code, index) {
  await navigator.clipboard.writeText(code)
  copiedIndex.value = index
  setTimeout(() => { if (copiedIndex.value === index) copiedIndex.value = null }, 1800)
}
</script>

<template>
  <section class="flex flex-col gap-6 py-12 px-4 md:px-8 max-w-4xl mx-auto">
    <article
      v-for="(script, index) in scripts" :key="script.filename"
      class="script-card overflow-hidden rounded-2xl border"
    >
      <header class="script-header flex items-center justify-between px-4 py-2">
        <span class="font-mono text-sm font-semibold">{{ script.filename }}</span>
        <button
          class="copy-btn inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold transition-all duration-300"
          @click="copyCode(script.code, index)"
        >
          {{ copiedIndex === index ? 'Copiado!' : 'Copiar' }}
        </button>
      </header>
      <pre class="script-body overflow-x-auto px-4 py-4 text-xs leading-relaxed"><code>{{ script.code }}</code></pre>
    </article>
  </section>
</template>

<style scoped>
.script-card {
  background-color: var(--code-bg-color);
  border-color: var(--code-border-color);
}

.script-header {
  background-color: var(--code-header-bg-color);
  border-bottom: 1px solid var(--code-border-color);
  color: var(--title-text-color);
}

.script-body {
  color: var(--code-text-color);
}

.copy-btn {
  color: var(--title-text-color);
  border: 1px solid var(--code-border-color);
  background-color: var(--contact-social-tag-bg-color);
}

.copy-btn:hover {
  background-color: var(--title-text-color);
  color: black;
}
</style>
