import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'

import tailwindcss from '@tailwindcss/vite'
import svgLoader from 'vite-svg-loader'

import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    tailwindcss(),
    svgLoader(),
    vue(),
    vueDevTools(),
  ],
  base: '/portfolio/',
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
