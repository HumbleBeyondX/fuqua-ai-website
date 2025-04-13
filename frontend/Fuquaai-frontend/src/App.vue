<script setup lang="ts">
import { Location, Message, Link } from '@element-plus/icons-vue'
import { ElConfigProvider } from 'element-plus'
import TheHeader from './components/TheHeader.vue'
import SubNavigation from './components/SubNavigation.vue'
import HeroSection from '@/components/HeroSection.vue'
import NewsEventsSection from '@/components/NewsEventsSection.vue'
import TheFooter from './components/TheFooter.vue'
import BackToTop from './components/BackToTop.vue'
import { RouterView, useRoute } from 'vue-router'
import { computed } from 'vue'

// Determine if current route is home page
const route = useRoute()
const isHomePage = computed(() => route.path === '/' || route.path === '/home')
</script>

<template>
  <div class="app-wrapper">
    <TheHeader />
    <SubNavigation v-if="isHomePage" />
    <main class="main-content" :class="{ 'no-subnav': !isHomePage }">
      <RouterView />
    </main>
    <TheFooter />
    <BackToTop />
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
  padding-top: 70px; /* Space for main nav */
}

.main-content.no-subnav {
  padding-top: 70px; /* Just space for main nav when no subnav is present */
}

/* Add scroll padding to account for fixed headers */
html {
  scroll-padding-top: 120px; /* Main nav + sub nav height */
}
</style>
