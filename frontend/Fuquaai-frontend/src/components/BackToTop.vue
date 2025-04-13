<template>
  <div class="back-to-top" :class="{ 'visible': showButton }" @click="scrollToTop">
    <el-icon><ArrowUp /></el-icon>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { ArrowUp } from '@element-plus/icons-vue';

const showButton = ref(false);
const scrollThreshold = 300; // Show button after scrolling this many pixels

const checkScroll = () => {
  showButton.value = window.scrollY > scrollThreshold;
};

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
};

onMounted(() => {
  window.addEventListener('scroll', checkScroll);
  checkScroll(); // Initial check
});

onUnmounted(() => {
  window.removeEventListener('scroll', checkScroll);
});
</script>

<style scoped lang="scss">
.back-to-top {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: #012169; /* Duke blue */
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  opacity: 0;
  visibility: hidden;
  transform: translateY(20px);
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  z-index: 99;
  
  &:hover {
    background-color: #0736A4;
    transform: translateY(0) scale(1.05);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  }
  
  &.visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
  
  .el-icon {
    font-size: 24px;
  }
}

@media (max-width: 768px) {
  .back-to-top {
    bottom: 20px;
    right: 20px;
    width: 45px;
    height: 45px;
  }
}
</style> 