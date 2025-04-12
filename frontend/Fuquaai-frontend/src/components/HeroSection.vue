<template>
  <section class="hero">
    <el-container>
      <div class="hero-content">
        <h1 class="hero-title">
          Artificial Intelligence at
          <span class="highlight">Fuqua School of Business</span>
        </h1>
        <p class="hero-description">
          Exploring the intersection of AI and business innovation through cutting-edge research,
          comprehensive education, and industry collaboration.
        </p>
        <div class="hero-actions">
          <el-button type="primary" size="large" class="learn-more-btn">
            Explore Our Programs
          </el-button>
        </div>
      </div>
    </el-container>
  </section>
</template>

<script setup lang="ts">
// Component logic here if needed
</script>

<style scoped lang="scss">
.hero {
  min-height: 80vh;
  display: flex;
  align-items: center;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  padding: 6rem 0;
  margin-top: 64px; // Account for fixed header

  .hero-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
    padding: 0 2rem;
  }

  .hero-title {
    font-family: 'Montserrat', sans-serif;
    font-size: 3.5rem;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 1.5rem;
    color: #2c3e50;

    .highlight {
      color: #0033a0;
      display: block;
      margin-top: 0.5rem;
    }
  }

  .hero-description {
    font-family: 'Open Sans', sans-serif;
    font-size: 1.25rem;
    line-height: 1.6;
    color: #6c757d;
    margin-bottom: 2.5rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }

  .hero-actions {
    .learn-more-btn {
      font-family: 'Montserrat', sans-serif;
      font-weight: 600;
      padding: 1rem 2rem;
      font-size: 1.1rem;
      background-color: #0033a0;
      border-color: #0033a0;

      &:hover {
        background-color: darken(#0033a0, 10%);
        border-color: darken(#0033a0, 10%);
      }
    }
  }
}

@media (max-width: 768px) {
  .hero {
    .hero-title {
      font-size: 2.5rem;
    }

    .hero-description {
      font-size: 1.1rem;
    }
  }
}
</style> 