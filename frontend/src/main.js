import '@/assets/main.css';

import { createApp } from 'vue';
import {createPinia} from 'pinia';
import { createI18n } from 'vue-i18n';

import App from '@/App.vue';
import router from '@/router/router.js';

import ptBr from '@/locales/pt-br'
import enUsa from '@/locales/en-usa'


const app = createApp(App);
const pinia = createPinia();

const i18n = createI18n({
  legacy: false,
  locale: localStorage.getItem('lang') ?? 'pt-br',
  fallbackLocale: 'pt-br',
  messages: {
    'pt-br': ptBr,
    'en-usa': enUsa
  }
})

app.use(pinia);
app.use(router);
app.use(i18n);

app.mount('#app');