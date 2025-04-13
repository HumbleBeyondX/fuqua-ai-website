<script setup lang="ts">
import { Location, Message, Link } from '@element-plus/icons-vue'
import { ElConfigProvider } from 'element-plus'
import TheHeader from './components/TheHeader.vue'
import HeroSection from '@/components/HeroSection.vue'
import NewsEventsSection from '@/components/NewsEventsSection.vue'
import TheFooter from './components/TheFooter.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="app-wrapper">
    <TheHeader />
    <main class="main-content">
      <RouterView />
    </main>
    <TheFooter />
  </div>
</template>

<style>
html, body {
  margin: 0;
  padding: 0;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  width: 100%;
  overflow-x: hidden;
}

* {
  box-sizing: border-box;
}

.app-wrapper {
  display: flex;
  flex-direction: column;
  width: 100%;
  min-height: 100vh;
  margin: 0 auto;
  position: relative;
}

.main-content {
  flex: 1;
  width: 100%;
}
</style>
