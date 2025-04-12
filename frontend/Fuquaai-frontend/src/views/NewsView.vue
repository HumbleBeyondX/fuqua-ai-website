<template>
  <div class="news-view">
    <el-container>
      <el-main>
        <h1 class="page-title">News & Events</h1>
        
        <!-- News Filter -->
        <div class="filter-section">
          <el-input
            v-model="searchQuery"
            placeholder="Search news and events..."
            class="search-input"
            clearable
          >
            <template #prefix>
              <el-icon><search /></el-icon>
            </template>
          </el-input>
          
          <el-select v-model="filterCategory" placeholder="Category" clearable>
            <el-option label="Events" value="events" />
            <el-option label="News" value="news" />
            <el-option label="Research" value="research" />
          </el-select>
        </div>

        <!-- News Grid -->
        <el-row :gutter="20">
          <el-col :xs="24" :sm="12" :md="8" v-for="item in filteredItems" :key="item.id">
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

        <!-- Pagination -->
        <div class="pagination-container">
          <el-pagination
            v-model:current-page="currentPage"
            v-model:page-size="pageSize"
            :page-sizes="[9, 18, 36, 72]"
            :total="totalItems"
            layout="total, sizes, prev, pager, next, jumper"
          />
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { Search, ArrowRight } from '@element-plus/icons-vue'

// Sample data - in a real app, this would come from an API
const newsItems = [
  {
    id: 1,
    title: 'AI in Business: The Future of Decision Making',
    date: 'March 15, 2024',
    excerpt: 'Join us for an exciting symposium on how AI is transforming business decision-making processes.',
    image: '/src/assets/images/news-1.jpg',
    category: 'events'
  },
  {
    id: 2,
    title: 'New AI Research Center Opening',
    date: 'March 10, 2024',
    excerpt: 'Fuqua School of Business announces the opening of a new AI research center focused on business applications.',
    image: '/src/assets/images/news-2.jpg',
    category: 'news'
  },
  // Add more sample items as needed
]

const searchQuery = ref('')
const filterCategory = ref('')
const currentPage = ref(1)
const pageSize = ref(9)

const filteredItems = computed(() => {
  let filtered = [...newsItems]
  
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(item => 
      item.title.toLowerCase().includes(query) ||
      item.excerpt.toLowerCase().includes(query)
    )
  }
  
  if (filterCategory.value) {
    filtered = filtered.filter(item => item.category === filterCategory.value)
  }
  
  return filtered
})

const totalItems = computed(() => filteredItems.value.length)
</script>

<style scoped lang="scss">
.news-view {
  padding: 2rem 0;
  min-height: calc(100vh - 64px);

  .page-title {
    font-family: 'Montserrat', sans-serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 2rem;
    text-align: center;
  }

  .filter-section {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;

    .search-input {
      flex: 1;
      min-width: 200px;
    }

    .el-select {
      width: 200px;
    }
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

  .pagination-container {
    margin-top: 2rem;
    display: flex;
    justify-content: center;
  }
}

@media (max-width: 768px) {
  .news-view {
    .page-title {
      font-size: 2rem;
    }

    .filter-section {
      flex-direction: column;
      
      .search-input,
      .el-select {
        width: 100%;
      }
    }
  }
}
</style> 