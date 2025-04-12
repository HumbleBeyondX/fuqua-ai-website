<script setup lang="ts">
import { Location, Message, Link } from '@element-plus/icons-vue'
import { ElConfigProvider } from 'element-plus'
import TheHeader from '@/components/TheHeader.vue'
import HeroSection from '@/components/HeroSection.vue'
import NewsEventsSection from '@/components/NewsEventsSection.vue'
import TheFooter from './components/TheFooter.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <TheHeader />
  <RouterView />
  <TheFooter />
</template>

<style>
html, body {
  margin: 0;
  padding: 0;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}
</style>
