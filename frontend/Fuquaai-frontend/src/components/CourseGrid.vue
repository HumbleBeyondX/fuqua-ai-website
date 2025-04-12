<template>
  <el-row :gutter="20">
    <el-col :xs="24" :sm="12" :md="8" v-for="course in courses" :key="course.id">
      <el-card class="course-card" shadow="hover">
        <div class="course-header">
          <h3 class="course-code">{{ course.code }}</h3>
          <el-tag size="small" :type="getCategoryTagType(course.category)">
            {{ formatCategory(course.category) }}
          </el-tag>
        </div>
        <h2 class="course-title">{{ course.title }}</h2>
        <p class="course-description">{{ course.description }}</p>
        <div class="course-meta">
          <div class="meta-item">
            <el-icon><user /></el-icon>
            <span>{{ course.instructor }}</span>
          </div>
          <div class="meta-item">
            <el-icon><calendar /></el-icon>
            <span>{{ course.term }}</span>
          </div>
        </div>
        <div class="course-actions">
          <el-button type="primary" plain>Learn More</el-button>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
import { User, Calendar } from '@element-plus/icons-vue'

defineProps<{
  courses: Array<{
    id: number
    title: string
    code: string
    description: string
    category: string
    instructor: string
    term: string
  }>
}>()

const getCategoryTagType = (category: string) => {
  const types: Record<string, string> = {
    mba: 'success',
    executive: 'warning',
    phd: 'danger'
  }
  return types[category] || 'info'
}

const formatCategory = (category: string) => {
  const formats: Record<string, string> = {
    mba: 'MBA',
    executive: 'Executive',
    phd: 'PhD'
  }
  return formats[category] || category
}
</script>

<style scoped lang="scss">
.course-card {
  height: 100%;
  margin-bottom: 2rem;
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-5px);
  }

  .course-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;

    .course-code {
      font-family: 'Montserrat', sans-serif;
      font-weight: 600;
      color: #0033a0;
      margin: 0;
    }
  }

  .course-title {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.25rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 0 0 1rem;
    line-height: 1.4;
  }

  .course-description {
    font-family: 'Open Sans', sans-serif;
    color: #6c757d;
    margin-bottom: 1.5rem;
    line-height: 1.6;
  }

  .course-meta {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 1.5rem;

    .meta-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: #6c757d;
      font-size: 0.9rem;

      .el-icon {
        font-size: 1rem;
      }
    }
  }

  .course-actions {
    .el-button {
      width: 100%;
      font-family: 'Montserrat', sans-serif;
      font-weight: 500;
    }
  }
}
</style> 