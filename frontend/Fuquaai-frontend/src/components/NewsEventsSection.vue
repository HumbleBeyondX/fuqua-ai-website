<template>
  <section class="news-events">
    <el-container>
      <div class="section-content">
        <h2 class="section-title">Latest News & Events</h2>
        <el-row :gutter="30">
          <el-col :xs="24" :sm="12" :md="8" v-for="item in newsItems" :key="item.id">
            <el-card class="news-card" :body-style="{ padding: '0px' }">
              <img :src="item.image" class="news-image" />
              <div class="news-content">
                <span class="news-date">{{ item.date }}</span>
                <h3 class="news-title">{{ item.title }}</h3>
                <p class="news-excerpt">{{ item.excerpt }}</p>
                <el-button text class="read-more">
                  Read More
                  <el-icon class="el-icon--right"><arrow-right /></el-icon>
                </el-button>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <div class="view-all">
          <el-button type="primary" plain>View All News & Events</el-button>
        </div>
      </div>
    </el-container>
  </section>
</template>

<script setup lang="ts">
import { ArrowRight } from '@element-plus/icons-vue'

// Sample data - in a real app, this would come from an API
const newsItems = [
  {
    id: 1,
    title: 'AI in Business: The Future of Decision Making',
    date: 'March 15, 2024',
    excerpt: 'Join us for an exciting symposium on how AI is transforming business decision-making processes.',
    image: '/src/assets/news-1.jpg'
  },
  {
    id: 2,
    title: 'New AI Research Center Opening',
    date: 'March 10, 2024',
    excerpt: 'Fuqua School of Business announces the opening of a new AI research center focused on business applications.',
    image: '/src/assets/news-2.jpg'
  },
  {
    id: 3,
    title: 'AI Ethics Workshop Series',
    date: 'March 5, 2024',
    excerpt: 'A new workshop series exploring ethical considerations in AI business applications.',
    image: '/src/assets/news-3.jpg'
  }
]
</script>

<style scoped lang="scss">
.news-events {
  padding: 5rem 0;
  background-color: #f8f9fa;

  .section-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
  }

  .section-title {
    font-family: 'Montserrat', sans-serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 3rem;
  }

  .news-card {
    margin-bottom: 2rem;
    transition: transform 0.3s ease;
    cursor: pointer;

    &:hover {
      transform: translateY(-5px);
    }

    .news-image {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }

    .news-content {
      padding: 1.5rem;
    }

    .news-date {
      font-family: 'Open Sans', sans-serif;
      color: #6c757d;
      font-size: 0.9rem;
    }

    .news-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.25rem;
      font-weight: 600;
      margin: 0.5rem 0;
      color: #2c3e50;
      line-height: 1.4;
    }

    .news-excerpt {
      font-family: 'Open Sans', sans-serif;
      color: #6c757d;
      margin-bottom: 1rem;
      line-height: 1.6;
    }

    .read-more {
      font-family: 'Montserrat', sans-serif;
      font-weight: 500;
      color: #0033a0;
      
      &:hover {
        color: darken(#0033a0, 10%);
      }
    }
  }

  .view-all {
    text-align: center;
    margin-top: 3rem;

    .el-button {
      font-family: 'Montserrat', sans-serif;
      font-weight: 500;
      padding: 12px 30px;
    }
  }
}
</style> 