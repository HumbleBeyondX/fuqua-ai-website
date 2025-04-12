<template>
  <div class="about-view">
    <el-container>
      <el-main>
        <h1 class="page-title">About AI@Fuqua</h1>
        
        <!-- Mission Section -->
        <section class="mission-section">
          <div class="mission-container">
            <div class="mission-overlay">
              <div class="mission-content">
                <h2 class="mission-title">Our Mission</h2>
                <p>
                  The Fuqua AI Initiative is dedicated to advancing artificial intelligence education and research
                  at Duke University's Fuqua School of Business. We bring together faculty, students, and industry
                  partners to explore the transformative potential of AI in business.
                </p>
                <p>
                  Our mission is to prepare future business leaders with the knowledge and skills needed to
                  leverage AI technologies effectively and ethically in their organizations.
                </p>
              </div>
            </div>
          </div>
        </section>

        <!-- Leadership Section -->
        <section class="leadership-section">
          <h2 class="section-title">Leadership Team</h2>
          <el-row :gutter="30">
            <el-col :xs="24" :sm="12" :md="8" v-for="leader in leadership" :key="leader.id">
              <el-card class="leader-card" shadow="hover">
                <div class="leader-image">
                  <img :src="leader.image" :alt="leader.name" />
                </div>
                <div class="leader-info">
                  <h3>{{ leader.name }}</h3>
                  <p class="title">{{ leader.title }}</p>
                  <p class="bio">{{ leader.bio }}</p>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </section>

        <!-- Partners Section -->
        <section class="partners-section">
          <h2 class="section-title">Our Partners</h2>
          <div class="partners-grid">
            <div v-for="partner in partners" :key="partner.id" class="partner-logo">
              <img :src="partner.logo" :alt="partner.name" />
            </div>
          </div>
        </section>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
// Sample data - in a real app, this would come from an API
const leadership = [
  {
    id: 1,
    name: 'Professor Jiaming Xu',
    title: 'Director, Fuqua AI Initiative',
    bio: 'Professor of Business Analytics with over 15 years of experience in AI research and education.',
    image: '@/assets/images/leadership/jiaming_xu.jpg'
  },
  {
    id: 2,
    name: 'Dr. Michael Chen',
    title: 'Associate Director',
    bio: 'Expert in machine learning applications for business strategy and decision-making.',
    image: '@/assets/images/leadership/michael-chen.jpg'
  },
  {
    id: 3,
    name: 'Dr. Emily Rodriguez',
    title: 'Research Director',
    bio: 'Specialist in AI ethics and responsible AI implementation in business contexts.',
    image: '@/assets/images/leadership/emily-rodriguez.jpg'
  }
]

const partners = [
  {
    id: 1,
    name: 'Microsoft',
    logo: '@/assets/images/partners/microsoft.png'
  },
  {
    id: 2,
    name: 'Google',
    logo: '@/assets/images/partners/google.png'
  },
  {
    id: 3,
    name: 'IBM',
    logo: '@/assets/images/partners/ibm.png'
  },
  {
    id: 4,
    name: 'Amazon',
    logo: '@/assets/images/partners/amazon.png'
  }
]
</script>

<style scoped lang="scss">
.about-view {
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

  section {
    max-width: 1200px;
    margin: 0 auto 4rem;
    padding: 0 2rem;
  }

  .mission-section {
    padding: 80px 20px;
    background-color: #f8f9fa;
  }

  .mission-container {
    position: relative;
    max-width: 1200px;
    margin: 0 auto;
    height: 500px;
    border-radius: 12px;
    overflow: hidden;
    background-image: url('@/assets/images/about-mission.png');
    background-size: cover;
    background-position: center;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
    transition: transform 0.5s ease-out;
    
    &:hover {
      transform: scale(1.01);
    }
  }

  .mission-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    // background: linear-gradient(rgba(1, 33, 105, 0.8), rgba(1, 33, 105, 0.7)); /* Duke blue gradient with transparency */
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 40px;
  }

  .mission-content {
    max-width: 800px;
    color: #fff;
    text-align: center;
    padding: 30px;
    backdrop-filter: blur(2px);
    border-radius: 10px;
    line-height: 1.3;
  }

  .mission-title {
    font-size: 2rem;
    margin-bottom: 2rem;
    color: #fff;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-weight: 700;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  }

  .mission-content p {
    font-size: 1rem;
    line-height: 1.5;
    margin-bottom: 1.5rem;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-weight: 400;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  }

  .leadership-section {
    .section-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 2rem;
      font-weight: 600;
      color: #2c3e50;
      margin-bottom: 2rem;
      text-align: center;
    }

    .leader-card {
      margin-bottom: 2rem;
      transition: transform 0.3s ease;

      &:hover {
        transform: translateY(-5px);
      }

      .leader-image {
        img {
          width: 100%;
          height: 300px;
          object-fit: cover;
          border-radius: 8px 8px 0 0;
        }
      }

      .leader-info {
        padding: 1.5rem;

        h3 {
          font-family: 'Montserrat', sans-serif;
          font-size: 1.25rem;
          font-weight: 600;
          color: #2c3e50;
          margin: 0 0 0.5rem;
        }

        .title {
          font-family: 'Open Sans', sans-serif;
          color: #0033a0;
          font-weight: 500;
          margin-bottom: 1rem;
        }

        .bio {
          font-family: 'Open Sans', sans-serif;
          color: #6c757d;
          line-height: 1.6;
        }
      }
    }
  }

  .partners-section {
    .section-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 2rem;
      font-weight: 600;
      color: #2c3e50;
      margin-bottom: 2rem;
      text-align: center;
    }

    .partners-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 2rem;
      align-items: center;
      justify-items: center;

      .partner-logo {
        padding: 1rem;
        background: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;

        &:hover {
          transform: translateY(-5px);
        }

        img {
          max-width: 100%;
          height: auto;
          filter: grayscale(100%);
          transition: filter 0.3s ease;

          &:hover {
            filter: grayscale(0%);
          }
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .about-view {
    .page-title {
      font-size: 2rem;
    }

    section {
      padding: 0 1rem;
    }

    .mission-container {
      height: auto;
      min-height: 400px;
    }
    
    .mission-title {
      font-size: 2rem;
      margin-bottom: 1.5rem;
    }
    
    .mission-content p {
      font-size: 1.1rem;
    }
  }
}
</style>
