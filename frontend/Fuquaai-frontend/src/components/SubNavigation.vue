<template>
  <nav class="sub-nav" :class="{ 'visible': showSubNav }">
    <div class="sub-nav-container">
      <ul class="sub-nav-list">
        <li class="sub-nav-item">
          <a href="#news" class="sub-nav-link" :class="{ 'active': activeSection === 'news' }">News</a>
        </li>
        <li class="sub-nav-item">
          <a href="#research-areas" class="sub-nav-link" :class="{ 'active': activeSection === 'research-areas' }">Research Areas</a>
        </li>
        <li class="sub-nav-item">
          <a href="#featured-courses" class="sub-nav-link" :class="{ 'active': activeSection === 'featured-courses' }">AI Approach</a>
        </li>
        <li class="sub-nav-item">
          <a href="#faculty-experts" class="sub-nav-link" :class="{ 'active': activeSection === 'faculty-experts' }">Faculty Experts</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

const showSubNav = ref(false);
const activeSection = ref('');
const mainNavHeight = 70; // Height of the main navigation in pixels
const scrollThreshold = 400; // When to show the sub navigation

// Check scroll position to show/hide sub nav and highlight active section
const handleScroll = () => {
  // Show sub nav after scrolling past the threshold
  showSubNav.value = window.scrollY > scrollThreshold;
  
  // Determine active section based on scroll position
  const sections = [
    { id: 'research-areas', element: document.getElementById('research-areas') },
    { id: 'featured-courses', element: document.getElementById('featured-courses') },
    { id: 'faculty-experts', element: document.getElementById('faculty-experts') }
  ];
  
  // Find the current section in view
  for (const section of sections) {
    if (section.element) {
      const rect = section.element.getBoundingClientRect();
      // Check if the section is in the viewport (accounting for the header)
      if (rect.top <= mainNavHeight + 100 && rect.bottom > mainNavHeight) {
        activeSection.value = section.id;
        break;
      }
    }
  }
};

// Smooth scroll to the section when clicking a link
const scrollToSection = (e: Event, sectionId: string) => {
  e.preventDefault();
  const section = document.getElementById(sectionId);
  if (section) {
    // Offset for the fixed headers
    const yOffset = -1 * (mainNavHeight + 50); 
    const y = section.getBoundingClientRect().top + window.pageYOffset + yOffset;
    
    window.scrollTo({
      top: y,
      behavior: 'smooth'
    });
  }
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
  handleScroll(); // Initial check
  
  // Add event listeners to links
  const links = document.querySelectorAll('.sub-nav-link');
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        scrollToSection(e, href.substring(1));
      }
    });
  });
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
  
  // Remove event listeners from links
  const links = document.querySelectorAll('.sub-nav-link');
  links.forEach(link => {
    link.removeEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        scrollToSection(e, href.substring(1));
      }
    });
  });
});
</script>

<style scoped lang="scss">
.sub-nav {
  position: fixed;
  top: 70px; /* Position it below the main nav */
  left: 0;
  right: 0;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.95);
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.05);
  z-index: 99;
  transform: translateY(-100%);
  opacity: 0;
  transition: all 0.3s ease;
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
  
  &.visible {
    transform: translateY(0);
    opacity: 1;
  }
}

.sub-nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.sub-nav-list {
  display: flex;
  list-style-type: none;
  padding: 0;
  margin: 0;
  justify-content: center;
}

.sub-nav-item {
  margin: 0 0.5rem;
  display: flex;
  align-items: center;
}

.sub-nav-link {
  color: #333;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  padding: 0.5rem 0.8rem;
  transition: all 0.25s ease;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  border-radius: 4px;
  position: relative;
  
  &:hover {
    color: #012169; /* Duke blue */
    background-color: rgba(120, 120, 120, 0.1);
  }
  
  &.active {
    color: #012169; /* Duke blue */
    font-weight: 600;
    
    &::after {
      content: '';
      position: absolute;
      bottom: 0.1rem;
      left: 0.6rem;
      right: 0.6rem;
      height: 2px;
      background-color: #012169; /* Duke blue */
      border-radius: 1px;
    }
  }
}

@media (max-width: 768px) {
  .sub-nav {
    top: 110px; /* Adjust based on your mobile header height */
  }
  
  .sub-nav-container {
    padding: 0 1rem;
  }
  
  .sub-nav-list {
    flex-wrap: wrap;
  }
  
  .sub-nav-item {
    margin: 0.2rem;
  }
  
  .sub-nav-link {
    padding: 0.4rem 0.6rem;
    font-size: 0.9rem;
  }
}
</style> 