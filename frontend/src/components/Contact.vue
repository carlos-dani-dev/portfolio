<script setup>
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';

import GithubIcon from "@/assets/icons/icons8-github.svg";
import LinkedinIcon from "@/assets/icons/icons8-linkedin.svg";


const { t } = useI18n();
const recipientEmail = 'seuemail@provedor.com.br';

const name = ref('');
const email = ref('');
const message = ref('');

function send_email() {
  const subject = `Contato pelo portfólio - ${name.value}`;
  const body = [
    `Nome: ${name.value}`,
    `Email: ${email.value}`,
    '',
    message.value,
  ].join('\n');

  const mailto = `mailto:${recipientEmail}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;

  window.location.href = mailto;
}
</script>

<template>
<section id="contact-section" class="py-24 max-w-[800px] mx-auto px-8">
  <div class="flex flex-col items-center text-center mb-16">
    <h2 class="colored-text text-4xl md:text-5xl font-bold tracking-tight mb-4">{{t('contact.title')}}</h2>
    <p class="text-lg opacity-80 max-w-1xl">
      <MarkdownText :content="t('contact.section_description')" />
    </p>
  </div>

  <div class="flex gap-3 mb-6 justify-center">
    <a class="skill-tag w-20 h-20 flex items-center justify-center">
        <GithubIcon class="social-icon"></GithubIcon>
    </a>
    <a class="skill-tag w-20 h-20 flex items-center justify-center">
        <LinkedinIcon class="social-icon"></LinkedinIcon>
    </a>
  </div>

  <div class="contact-card p-8 md:p-10 rounded-2xl flex flex-col gap-6">
    <form class="flex flex-col gap-6" @submit.prevent="send_email">
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="flex flex-col gap-2">
          <label for="name" class="font-medium opacity-90 text-sm">{{ t('contact.name_label') }}</label>
          <input 
            type="text" 
            id="name" 
            :placeholder="t('contact.name_ph')"
            class="input-field px-4 py-3 rounded-lg outline-none transition-all duration-300"
            v-model="name"
            required
          />
        </div>
        
        <div class="flex flex-col gap-2">
          <label for="email" class="font-medium opacity-90 text-sm">{{t('contact.email_label')}}</label>
          <input 
            type="email" 
            id="email" 
            :placeholder="t('contact.email_ph')"
            class="input-field px-4 py-3 rounded-lg outline-none transition-all duration-300"
            v-model="email"
            required
          />
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <label for="message" class="font-medium opacity-90 text-sm">{{t('contact.message_label')}}</label>
        <textarea 
          id="message" 
          rows="5" 
          :placeholder="t('contact.message_ph')"
          class="input-field px-4 py-3 rounded-lg outline-none transition-all duration-300 resize-y"
          v-model="message"
          required
        ></textarea>
      </div>

      <button 
        type="submit"
        class="submit-btn font-bold py-3 px-6 rounded-lg transition-all duration-300 mt-2 self-center md:self-end"
      >
        {{t('contact.send_btn')}}
      </button>

    </form>
  </div>
</section>
</template>

<style scoped>
.contact-card {
  background-color: var(--project-card-bg-color, rgba(128, 128, 128, 0.05));
  border: 1px solid rgba(128, 128, 128, 0.15);
}

.input-field {
  background-color: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(128, 128, 128, 0.2);
  color: inherit;
}

.input-field:focus {
  border-color: var(--me-text-color, #8b5cf6);
  background-color: rgba(0, 0, 0, 0.3);
}

.colored-text {
  color: var(--me-text-color);
}

.submit-btn {
  background-color: transparent;
  color: var(--me-text-color);
  border: 1px solid var(--me-text-color);
  cursor: pointer;
}

.submit-btn:hover {
  background-color: var(--me-tag-skill-bg-color, rgba(139, 92, 246, 0.1));
  transform: translateY(-2px);
}

.skill-tag{
    border-color: var(--me-tag-skill-border-color);
    background-color: var(--me-tag-skill-bg-color);
}
.social-icon :deep(path) {
  fill: var(--me-social-icon-color);
}
</style>
