<template>
  <header class="site-header">
    <div class="header-container">
      <div class="logo-container">
        <router-link to="/">
          <img src="/src/assets/images/icon.png" alt="Fuqua AI" class="site-logo">
          <span class="site-title">AI@Fuqua</span>
        </router-link>
      </div>
      <nav class="main-nav">
        <ul class="nav-list">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/research" class="nav-link">Research</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/courses" class="nav-link">Courses</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/about" class="nav-link">About</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/contact" class="nav-link">Contact</router-link>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup lang="ts">
// Component logic here if needed
</script>

<style scoped lang="scss">
.site-header {
  position: fixed;
  top: 0;
  z-index: 100;
  background-color: rgba(255, 255, 255, 0.98);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  width: 100%;
  left: 0;
  right: 0;
  transition: transform 0.3s ease;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0.5rem 1.5rem;
  box-sizing: border-box;
}

.logo-container {
  margin-right: 1rem;
  
  a {
    display: flex;
    align-items: center;
    text-decoration: none;
    color: #012169; /* Duke blue */
    padding: 0.6rem 1rem;
    border-radius: 4px;
    transition: all 0.25s ease;
    
    &:hover {
      background-color: rgba(120, 120, 120, 0.1); /* Same as nav items */
    }
  }
}

.site-logo {
  height: 38px;
  margin-right: 10px;
}

.site-title {
  font-size: 1.5rem;
  font-weight: 700;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.main-nav {
  display: flex;
  align-items: center;
}

.nav-list {
  display: flex;
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  margin-left: 0.8rem;
  display: flex;
  align-items: center;
  font-weight: 800;
}

.nav-link {
  color: #333;
  text-decoration: none;
  font-weight: 500;
  font-size: 1rem;
  padding: 0.6rem 1rem;
  transition: all 0.25s ease;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  border-radius: 4px;
  position: relative;
  
  &:hover {
    color: #012169; /* Duke blue */
    background-color: rgba(120, 120, 120, 0.1); 
  }
  
  &.router-link-active {
    color: #012169; /* Duke blue */
    // background-color: rgba(120, 120, 120, 0.3); 
    font-weight: 600;
    
    &::after {
      content: '';
      position: absolute;
      bottom: 0.2rem;
      left: 0.8rem;
      right: 0.8rem;
      height: 2px;
      background-color: #012169; /* Duke blue */
      border-radius: 1px;
    }
  }
}

@media (max-width: 768px) {
  .header-container {
    flex-direction: column;
    padding: 1rem;
    width: 100%;
  }
  
  .logo-container {
    margin-bottom: 1rem;
    margin-right: 0;
    display: flex;
    justify-content: center;
    width: 100%;
    
    a {
      padding: 0.5rem 1rem;
    }
  }
  
  .nav-list {
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
  }
  
  .nav-item {
    margin: 0.3rem;
  }
  
  .nav-link {
    padding: 0.5rem 0.8rem;
    
    &.router-link-active::after {
      bottom: 0.1rem;
      left: 0.6rem;
      right: 0.6rem;
    }
  }
}
</style> 