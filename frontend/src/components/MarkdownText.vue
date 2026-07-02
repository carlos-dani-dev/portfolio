<script setup>
import MarkdownIt from 'markdown-it';
import { computed } from 'vue';

const props = defineProps({
  content: {
    type: String,
    required: true,
  },
});

const markdown = new MarkdownIt({
  html: false,
  linkify: true,
  breaks: true,
});

const renderedContent = computed(() => markdown.renderInline(props.content));
</script>

<template>
  <span v-html="renderedContent"></span>
</template>