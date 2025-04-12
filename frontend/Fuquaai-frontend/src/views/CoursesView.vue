<template>
  <div class="courses-view">
    <el-container>
      <el-main>
        <h1 class="page-title">AI Courses at Fuqua</h1>
        
        <!-- Course Categories -->
        <div class="categories">
          <el-tabs v-model="activeCategory" class="category-tabs">
            <el-tab-pane label="All Courses" name="all">
              <course-grid :courses="filteredCourses" />
            </el-tab-pane>
            <el-tab-pane label="MBA Courses" name="mba">
              <course-grid :courses="filteredCourses" />
            </el-tab-pane>
            <el-tab-pane label="Executive Education" name="executive">
              <course-grid :courses="filteredCourses" />
            </el-tab-pane>
            <el-tab-pane label="PhD Courses" name="phd">
              <course-grid :courses="filteredCourses" />
            </el-tab-pane>
          </el-tabs>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import CourseGrid from '@/components/CourseGrid.vue'

// Sample data - in a real app, this would come from an API
const courses = [
  {
    id: 1,
    title: 'AI for Business Strategy',
    code: 'MBA 123',
    description: 'Learn how AI is transforming business strategy and decision-making processes.',
    category: 'mba',
    instructor: 'Dr. John Smith',
    term: 'Spring 2024'
  },
  {
    id: 2,
    title: 'Machine Learning for Business',
    code: 'MBA 456',
    description: 'Practical applications of machine learning in business contexts.',
    category: 'mba',
    instructor: 'Dr. Sarah Johnson',
    term: 'Fall 2024'
  },
  {
    id: 3,
    title: 'AI Leadership Program',
    code: 'EXEC 789',
    description: 'Executive education program focused on AI leadership and strategy.',
    category: 'executive',
    instructor: 'Dr. Michael Brown',
    term: 'Summer 2024'
  }
]

const activeCategory = ref('all')

const filteredCourses = computed(() => {
  if (activeCategory.value === 'all') {
    return courses
  }
  return courses.filter(course => course.category === activeCategory.value)
})
</script>

<style scoped lang="scss">
.courses-view {
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

  .categories {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;

    :deep(.el-tabs__nav-wrap) {
      margin-bottom: 2rem;
    }

    :deep(.el-tabs__item) {
      font-family: 'Montserrat', sans-serif;
      font-weight: 500;
      font-size: 1.1rem;
    }
  }
}

@media (max-width: 768px) {
  .courses-view {
    .page-title {
      font-size: 2rem;
    }

    .categories {
      padding: 0 1rem;
    }
  }
}
</style> 