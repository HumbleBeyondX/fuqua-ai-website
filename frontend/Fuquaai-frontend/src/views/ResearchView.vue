<template>
  <div class="research-view">
    <el-container>
      <el-main>
        <h1 class="page-title">AI Research at Fuqua</h1>
        
        <!-- Research Areas -->
        <div class="research-areas">
          <el-row :gutter="30">
            <el-col :xs="24" :sm="12" :md="8" v-for="area in researchAreas" :key="area.id">
              <div class="research-area-card">
                <div class="area-icon">
                  <el-icon :size="40"><component :is="area.icon" /></el-icon>
                </div>
                <h3 class="area-title">{{ area.title }}</h3>
                <p class="area-description">{{ area.description }}</p>
                <el-button text class="learn-more">
                  View Research
                  <el-icon class="el-icon--right"><arrow-right /></el-icon>
                </el-button>
              </div>
            </el-col>
          </el-row>
        </div>

        <!-- Featured Research -->
        <div class="featured-research">
          <h2 class="section-title">Featured Research Projects</h2>
          <el-timeline>
            <el-timeline-item
              v-for="project in featuredProjects"
              :key="project.id"
              :timestamp="project.date"
              placement="top"
            >
              <el-card>
                <h4>{{ project.title }}</h4>
                <p>{{ project.description }}</p>
                <div class="project-meta">
                  <span class="researcher">Researcher: {{ project.researcher }}</span>
                  <el-button text type="primary" size="small">Read Paper</el-button>
                </div>
              </el-card>
            </el-timeline-item>
          </el-timeline>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ArrowRight, DataAnalysis, Connection, Monitor } from '@element-plus/icons-vue'

// Sample data - in a real app, this would come from an API
const researchAreas = [
  {
    id: 1,
    title: 'Machine Learning in Finance',
    description: 'Exploring applications of machine learning in financial markets and investment strategies.',
    icon: 'DataAnalysis'
  },
  {
    id: 2,
    title: 'AI in Marketing',
    description: 'Investigating how AI can enhance customer insights and marketing effectiveness.',
    icon: 'Connection'
  },
  {
    id: 3,
    title: 'Business Analytics',
    description: 'Developing new methods for business data analysis and decision support.',
    icon: 'Monitor'
  }
]

const featuredProjects = [
  {
    id: 1,
    title: 'Predictive Analytics in Supply Chain Management',
    date: 'March 2024',
    description: 'A novel approach to using machine learning for supply chain optimization.',
    researcher: 'Dr. Emily Chen'
  },
  {
    id: 2,
    title: 'AI-Driven Customer Segmentation',
    date: 'February 2024',
    description: 'New methods for customer segmentation using deep learning techniques.',
    researcher: 'Dr. Michael Rodriguez'
  },
  {
    id: 3,
    title: 'Blockchain and AI Integration',
    date: 'January 2024',
    description: 'Exploring the intersection of blockchain technology and artificial intelligence.',
    researcher: 'Dr. Sarah Johnson'
  }
]
</script>

<style scoped lang="scss">
.research-view {
  padding: 2rem 0;
  min-height: calc(100vh - 64px);

  .page-title {
    font-family: 'Montserrat', sans-serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 3rem;
    text-align: center;
  }

  .research-areas {
    max-width: 1200px;
    margin: 0 auto 4rem;
    padding: 0 2rem;
  }

  .research-area-card {
    background: #fff;
    border-radius: 8px;
    padding: 2rem;
    height: 100%;
    transition: transform 0.3s ease;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);

    &:hover {
      transform: translateY(-5px);
    }

    .area-icon {
      color: #0033a0;
      margin-bottom: 1.5rem;
    }

    .area-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.5rem;
      font-weight: 600;
      color: #2c3e50;
      margin: 0 0 1rem;
    }

    .area-description {
      font-family: 'Open Sans', sans-serif;
      color: #6c757d;
      margin-bottom: 1.5rem;
      line-height: 1.6;
    }

    .learn-more {
      font-family: 'Montserrat', sans-serif;
      font-weight: 500;
      color: #0033a0;
      
      &:hover {
        color: darken(#0033a0, 10%);
      }
    }
  }

  .featured-research {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 2rem;

    .section-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 2rem;
      font-weight: 600;
      color: #2c3e50;
      margin-bottom: 2rem;
      text-align: center;
    }

    :deep(.el-timeline-item__node) {
      background-color: #0033a0;
    }

    .el-card {
      margin-bottom: 1rem;

      h4 {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 0 0 1rem;
      }

      p {
        font-family: 'Open Sans', sans-serif;
        color: #6c757d;
        margin-bottom: 1rem;
        line-height: 1.6;
      }

      .project-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;

        .researcher {
          font-family: 'Open Sans', sans-serif;
          color: #6c757d;
          font-size: 0.9rem;
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .research-view {
    .page-title {
      font-size: 2rem;
    }

    .research-areas,
    .featured-research {
      padding: 0 1rem;
    }
  }
}
</style> 