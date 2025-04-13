<script setup lang="ts">
import { ref } from 'vue';

// Example data for news items
const newsItems = ref([
  {
    title: 'OpenAI and Duke Launch New MetaScience Initiative',
    content: 'Professor Ronnie Chatterji Appointed First Chief Economist of OpenAI.',
    date: 'June 2023'
  },
  {
    title: 'Duke University Launches Society-Centered AI Initiative',
    content: 'Including Fuqua Faculty and Amazon Scholar Alex Belloni.',
    date: 'May 2023'
  },
  {
    title: 'Jiaming Xu Research on Deep Learning',
    content: 'Jiaming Xu researches and teaches deep learning and its business applications, supported by an NSF Career Award.',
    date: 'April 2023'
  },
  {
    title: 'Net-Zero Analytics',
    content: 'David Brown shares how Net-Zero Analytics can accelerate the climate transition.',
    date: 'March 2023'
  }
]);

// Research areas
const researchAreas = ref([
  {
    title: 'Decision-Making & Business Optimization',
    description: 'Fuqua researchers are using AI to improve how businesses make decisions, forecast outcomes, and optimize performance across complex systems.'
  },
  {
    title: 'Entrepreneurship & Innovation',
    description: 'AI is transforming how entrepreneurs build, fund, and scale new ventures. Fuqua AI Entrepreneurship course prepares students to lead in this space.'
  },
  {
    title: 'Organizations & Human-AI Interaction',
    description: 'Fuqua faculty investigate how AI is reshaping workplace behavior, collaboration, and perceptions of fairness.'
  },
  {
    title: 'Market & Consumer Insights',
    description: 'Researchers at Fuqua are using AI to decode consumer behavior, personalize engagement, and inform marketing strategy.'
  },
  {
    title: 'Policy & the Societal Impact of AI',
    description: 'Fuqua faculty are exploring the broader societal implications of AI adoption—including its effects on privacy, fairness, regulation, and user experience.'
  },
  {
    title: 'Analytics and Quantitative Methods',
    description: 'AI is being woven into foundational analytics instruction across Fuqua programs, especially within Decision Sciences.'
  }
]);

// AI Approach Categories
const aiApproachCategories = ref([
  {
    title: 'AI + Foundations',
    items: [
      'AI for Managers',
      'Transforming Tech Analytics with Machine Intelligence',
      'Foundations of Business Analytics',
      'Data Science for Business',
      'Modern Analytics & Deep Learning'
    ]
  },
  {
    title: 'AI + Applications',
    items: [
      'Finance and Accounting',
      'Operations',
      'Strategy and Markets',
      'Marketing',
      'Core Strategy'
    ]
  },
  {
    title: 'AI + Society',
    items: [
      'Navigating Organizations',
      'Ethics in Management',
      'Leadership, Ethics, and Organizations'
    ]
  }
]);

// Faculty experts
const facultyExperts = ref([
  { 
    name: 'Alessandro Arlotto', 
    expertise: 'Election Analytics, Machine Learning',
    image: '/src/assets/images/faculty/alessandro-arlotto.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/alessandro-arlotto'
  },
  { 
    name: 'Alex Belloni', 
    expertise: 'Predictive Models, Causal Inference',
    image: '/src/assets/images/faculty/alex-belloni.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/alexandre-belloni'
  },
  { 
    name: 'David Brown', 
    expertise: 'AI in Energy and Climate',
    image: '/src/assets/images/faculty/david-brown.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/david-brown'
  },
  { 
    name: 'Ali Makhdoumi', 
    expertise: 'Data Markets, Privacy, AI Policy',
    image: '/src/assets/images/faculty/ali-makhdoumi.jpeg',
    url: 'https://www.fuqua.duke.edu/faculty/ali-makhdoumi'
  },
  { 
    name: 'Saša Pekeč', 
    expertise: 'Market Design, Algorithmic Decision-Making, Platform Economics',
    image: '/src/assets/images/faculty/sasa-pekec.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/aleksandar-pekec'
  },
  { 
    name: 'Anqi Zhao', 
    expertise: 'Causal Inference, Machine Learning',
    image: '/src/assets/images/faculty/anqi-zhao.png',
    url: 'https://www.fuqua.duke.edu/faculty/anqi-zhao'
  },
  { 
    name: 'Jiaming Xu', 
    expertise: 'Machine Learning, Networks',
    image: '/src/assets/images/faculty/jiaming-xu.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/jiaming-xu'
  },
  { 
    name: 'Yehua Wei', 
    expertise: 'E-Commerce Optimization, Machine Learning',
    image: '/src/assets/images/faculty/yehua-wei.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/yehua-wei'
  },
  {
    name:'Tong Guo',
    expertise: 'Misinformation,Beliefs',
    image: '/src/assets/images/faculty/tong-guo.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/tong-guo'
  },
  {
    name:'Carl Mela',
    expertise: 'Marketing Technology',
    image: '/src/assets/images/faculty/carl-mela.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/carl-mela'
  },
  {
    name:'Bora Keskin',
    expertise: 'AI in Value Chain Management',
    image: '/src/assets/images/faculty/bora-keskin.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/bora-keskin'
  },
  {
    name:'Fernando Bernstein',
    expertise: 'Customer Preference, Forecasting',
    image: '/src/assets/images/faculty/fernando-bernstein.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/fernando-bernstein'
  },

  {
    name:'Jeannette Song',
    expertise: 'E-commerce logistics, staffing optimization, inventory/pricing',
    image: '/src/assets/images/faculty/jeannette-song.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/jeannette-song'
  },
  {
    name:'Kevin Shang',
    expertise: 'Inventory Management with AI',
    image: '/src/assets/images/faculty/kevin-shang.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/kevin-shang'
  },
  {
    name:'Sharique Hasan',
    expertise: 'Innovation and Deep Tech Commercialization',
    image: '/src/assets/images/faculty/sharique-hasan.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/sharique-hasan'
  },
  {
    name:'Wesley Cohen',
    expertise: 'Innovation and Deep Tech Commercialization',
    image: '/src/assets/images/faculty/wesley-cohen.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/wesley-cohen'
  },
  {
    name:'Ronnie Chatterji',
    expertise: 'Chief Economist at OpenAI',
    image: '/src/assets/images/faculty/aaron-chatterji.jpeg',
    url: 'https://www.fuqua.duke.edu/faculty/aaron-chatterji'
  },
  {
    name:'Jack Soll',
    expertise: 'Human AI Collaboration',
    image: '/src/assets/images/faculty/jack-soll.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/jack-soll'
  },
  {
    name:'Richard Larrick',
    expertise: 'Human AI Collaboration',
    image: '/src/assets/images/faculty/richard-larrick.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/richard-larrick'
  },
  {
    name:'Ashleigh Rosette',
    expertise: 'Bias and Fairness in AI',
    image: '/src/assets/images/faculty/ashleigh-rosette.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/ashleigh-rosette'
  },
  {
    name:'Srinivas Tunuguntla',
    expertise: 'Marketing Analytics and Digital Advertising',
    image: '/src/assets/images/faculty/srinivas-tunuguntla.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/srinivas-tunuguntla'
  },
  {
    name:'Manuel Adelino',
    expertise: 'Finance and Venture Capital',
    image: '/src/assets/images/faculty/manuel-adelino.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/manuel-adelino'
  },
  {
    name:'Jamie Jones',
    expertise: 'Innovation & Entrepreneurship',
    image: '/src/assets/images/faculty/jamie-jones.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/jamie-jones'
  },
  {
    name:'Kimberly Wade-Benzoni',
    expertise: 'AI and Legacy',
    image: '/src/assets/images/faculty/kimberly-wade-benzoni.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/kimberly-wade-benzoni'
  },
  {
    name:'Peng Sun',
    expertise: 'AI and Mechanism Design',
    image: '/src/assets/images/faculty/peng-sun.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/peng-sun'
  },
  {
    name:'Campbell Harvey',
    expertise: 'AI in Decentralized Finance, Asset Allocation',
    image: '/src/assets/images/faculty/campbell-harvey.jpg',
    url: 'https://www.fuqua.duke.edu/faculty/campbell-harvey'
  }

]);


// Function to scroll to a section
const scrollToSection = (sectionId: string) => {
  const element = document.getElementById(sectionId);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
};

// Function to handle image loading errors
const handleImageError = (event: Event) => {
  const img = event.target as HTMLImageElement;
  // Hide the image by setting opacity to 0
  img.style.opacity = "0";
};

// Function to get initials from faculty name
const getInitials = (name: string) => {
  const parts = name.split(' ');
  return parts.map(part => part.charAt(0)).join('');
};
</script>

<template>
  <div class="home-container">
    <!-- Hero Section with full-width background image -->
    <section class="hero-section">
      <div class="hero-content">
        <h1 class="hero-title">AI@Fuqua</h1>
        <p class="hero-subtitle">Preparing the next generation of leaders with the skills, insights, and frameworks to create value for business and society in an AI-driven world.</p>
        <el-button type="primary" size="large" class="learn-more-btn" @click="scrollToSection('about')">Learn More</el-button>
      </div>
    </section>

    <!-- Main content section with light background -->
    <section class="main-content" id="about">
      <div class="section-container">
        <h2 class="section-title">Advancing Business Through AI Research & Learning</h2>
        <p class="section-description">AI is transforming business, and Duke University's Fuqua School of Business is leading the way. Discover how AI is integrated into research and learning across all areas of business education.</p>
        
        <!-- News cards grid -->
        <div class="news-grid">
          <el-row :gutter="30">
            <el-col :span="24" :xs="24" :sm="12" :md="12" :lg="6" v-for="(item, index) in newsItems" :key="index">
              <el-card class="news-card" shadow="hover">
                <div class="news-card-content">
                  <h3 class="news-title">{{ item.title }}</h3>
                  <p class="news-content">{{ item.content }}</p>
                  <div class="news-footer">
                    <span class="news-date">{{ item.date }}</span>
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </div>
      </div>
    </section>

    <!-- Research Areas section with alternating background -->
    <section class="research-areas" id="research-areas">
      <div class="section-container">
        <h2 class="section-title">Fuqua Researchers are Driving Applications of AI to all Areas of Business</h2>
        
        <el-row :gutter="30" class="research-grid">
          <el-col :span="24" :xs="24" :sm="24" :md="12" :lg="8" v-for="(area, index) in researchAreas" :key="index" class="research-col">
            <div class="research-area-card">
              <h3 class="research-area-title">{{ area.title }}</h3>
              <p class="research-area-content">{{ area.description }}</p>
            </div>
          </el-col>
        </el-row>
      </div>
    </section>

    <!-- Featured Courses section -->
    <section class="featured-courses" id="featured-courses">
      <div class="section-container">
        <h2 class="section-title">The Duke Fuqua Approach to AI</h2>
        <p class="section-description">At Fuqua, AI is not confined to a single course or specialization. It is woven throughout the curriculum, integrated into the way we teach analytics, decision-making, strategy, operations, finance, accounting, marketing, and leadership.</p>
        
        <div class="ai-approach-grid">
          <el-row :gutter="30">
            <el-col :span="24" :xs="24" :sm="24" :md="8" v-for="(category, index) in aiApproachCategories" :key="index" class="approach-col">
              <div class="ai-approach-card">
                <h3 class="ai-approach-title">{{ category.title }}</h3>
                <ul class="ai-approach-list">
                  <li v-for="(item, idx) in category.items" :key="idx">{{ item }}</li>
                </ul>
              </div>
            </el-col>
          </el-row>
        </div>
      </div>
    </section>

    <!-- Faculty Experts section -->
    <section class="faculty-experts" id="faculty-experts">
      <div class="section-container">
        <h2 class="section-title">AI@Fuqua Faculty AI Experts</h2>
        
        <div class="faculty-grid">
          <el-row :gutter="30">
            <el-col :span="24" :xs="24" :sm="12" :md="8" :lg="6" v-for="(faculty, index) in facultyExperts" :key="index" class="faculty-col">
              <a :href="faculty.url" target="_blank" rel="noopener noreferrer" class="faculty-card-link">
                <div class="faculty-card">
                  <div class="faculty-image-container">
                    <img 
                      :src="faculty.image" 
                      :alt="faculty.name" 
                      class="faculty-image"
                      @error="handleImageError($event)"
                    >
                    <div class="faculty-image-overlay">
                      <div class="faculty-initials">
                        {{ getInitials(faculty.name) }}
                      </div>
                    </div>
                  </div>
                  <div class="faculty-info">
                    <h3 class="faculty-name">{{ faculty.name }}</h3>
                    <p class="faculty-expertise">{{ faculty.expertise }}</p>
                  </div>
                </div>
              </a>
            </el-col>
          </el-row>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped lang="scss">
.home-container {
  width: 100%;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0;
  padding: 0;
}

/* Hero section styles */
.hero-section {
  position: relative;
  height: 100vh;
  min-height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: #fff;
  overflow: hidden;
  /* Fallback background in case ::after doesn't work in some browsers */
  background-image: url('/src/assets/images/FuquaCoverPage.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  width: 100%;
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: rgba(0, 26, 87, 0.6); /* Duke blue with opacity */
    z-index: 1;
  }
  
  /* Advanced background handling */
  &::after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-image: url('/src/assets/images/FuquaCoverPage.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    z-index: 0;
    transform: scale(1.01); /* Slight scale to avoid white edges during transitions */
    transition: transform 0.5s ease-out;
  }
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 800px;
  padding: 0 20px;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  line-height: 1.2;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #ffffff;
}

.hero-subtitle {
  font-size: 1rem;
  margin-bottom: 2.5rem;
  line-height: 1.5;
  font-weight: 400;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.learn-more-btn {
  padding: 10px 30px;
  font-size: 1.1rem;
  font-weight: 600;
  background-color: #0736A4; /* Duke blue */
  border-color: #0736A4;
  
  &:hover {
    background-color: #012169; /* Darker Duke blue */
    border-color: #012169;
  }
}

/* Main content section styles */
.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 80px 20px;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 2rem;
  color: #012169; /* Duke blue */
  text-align: center;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.section-description {
  font-size: 1.2rem;
  line-height: 1.7;
  margin-bottom: 3rem;
  text-align: center;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
  color: #333;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.main-content {
  background-color: #f8f9fa;
}

/* News cards styles */
.news-grid {
  margin-top: 3rem;
}

.el-row {
  margin-bottom: 20px !important;
}

.el-col {
  margin-bottom: 30px;
}

.news-card {
  height: 100%;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  border: none;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  }
}

.news-card-content {
  padding: 15px;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.news-title {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  color: #012169; /* Duke blue */
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.news-content {
  font-size: 0.95rem;
  color: #555;
  line-height: 1.5;
  margin-bottom: 1rem;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  flex-grow: 1;
}

.news-footer {
  display: flex;
  justify-content: flex-end;
  margin-top: auto;
}

.news-date {
  font-size: 0.85rem;
  color: #888;
}

/* Research areas styles */
.research-areas {
  background-color: #fff;
}

.research-grid {
  margin-top: 3rem;
}

.research-col {
  margin-bottom: 30px;
}

.research-area-card {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 25px;
  height: 100%;
  transition: all 0.3s ease;
  border-left: 4px solid #012169; /* Duke blue */
  margin-bottom: 20px;
  
  &:hover {
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    transform: translateY(-5px);
  }
}

.research-area-title {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #012169; /* Duke blue */
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.research-area-content {
  font-size: 1rem;
  line-height: 1.6;
  color: #444;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

/* Featured courses styles */
.featured-courses {
  background-color: #f1f5f9;
}

.ai-approach-grid {
  margin-top: 3rem;
}

.approach-col {
  margin-bottom: 30px;
}

.ai-approach-card {
  background-color: #fff;
  border-radius: 8px;
  padding: 25px;
  height: 100%;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  }
}

.ai-approach-title {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  color: #012169; /* Duke blue */
  text-align: center;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.ai-approach-list {
  padding-left: 20px;
  
  li {
    margin-bottom: 10px;
    font-size: 1rem;
    line-height: 1.5;
    font-family: 'Helvetica Neue', Arial, sans-serif;
  }
}

/* Faculty experts styles */
.faculty-experts {
  background-color: #fff;
}

.faculty-grid {
  margin-top: 3rem;
}

.faculty-col {
  margin-bottom: 30px;
}

.faculty-card-link {
  display: block;
  text-decoration: none;
  height: 100%;
  color: inherit;
  cursor: pointer;
  
  &:hover, &:focus {
    text-decoration: none;
    color: inherit;
    outline: none;
    background-color: transparent !important;
  }
  
  &:hover .faculty-card {
    transform: translateY(-5px);
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
    background-color: #f8f9fa; /* Keep the same background color on hover */
  }
  
  &:hover .faculty-image {
    transform: scale(1.05);
  }
  
  &:active {
    transform: translateY(1px);
  }
}

.faculty-card {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 0;
  height: 100%;
  transition: all 0.3s ease;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.faculty-image-container {
  width: 100%;
  height: 0;
  padding-bottom: 100%; /* Creates a square aspect ratio */
  position: relative;
  overflow: hidden;
  background-color: #e9effb;
}

.faculty-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
  transition: transform 0.5s ease;
  z-index: 1;
}

.faculty-image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #012169; /* Duke blue */
  z-index: 0; /* Behind the image */
}

.faculty-initials {
  font-size: 3rem;
  font-weight: 700;
  color: #fff;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.faculty-info {
  padding: 15px;
  position: relative;
}

.faculty-info::after {
  content: '';
  position: absolute;
  right: 10px;
  top: 18px; /* Align with the professor's name */
  width: 8px;
  height: 8px;
  border-top: 2px solid #012169;
  border-right: 2px solid #012169;
  transform: rotate(45deg);
  opacity: 0.6;
  transition: all 0.3s ease;
}

.faculty-card-link:hover .faculty-info::after {
  opacity: 1;
  right: 8px; /* Adjust this if needed */
}

.faculty-name {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #012169; /* Duke blue */
  font-family: 'Helvetica Neue', Arial, sans-serif;
  padding-right: 15px; /* Make space for the arrow */
}

.faculty-expertise {
  font-size: 0.9rem;
  color: #555;
  line-height: 1.5;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

/* Responsive styles */
@media (max-width: 1200px) {
  .hero-section::after {
    background-position: center center;
  }
}

@media (max-width: 768px) {
  .hero-section {
    min-height: 500px;
  }
  
  .hero-section::after {
    background-position: center center;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1.2rem;
    margin-bottom: 2rem;
  }
}

@media (max-width: 480px) {
  .hero-section {
    min-height: 450px;
  }
  
  .hero-title {
    font-size: 2rem;
  }
  
  .hero-subtitle {
    font-size: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .learn-more-btn {
    padding: 10px 20px;
    font-size: 1rem;
  }
}

/* For extra-wide screens */
@media (min-width: 2000px) {
  .hero-section::after {
    background-size: 100% auto;
    background-position: center top;
  }
}

/* For portrait orientation on mobile devices */
@media (max-width: 768px) and (orientation: portrait) {
  .hero-section::after {
    background-size: cover;
    background-position: center center;
  }
}

/* For landscape orientation on mobile devices */
@media (max-width: 900px) and (orientation: landscape) {
  .hero-section {
    min-height: 450px;
  }
  
  .hero-section::after {
    background-size: cover;
    background-position: center center;
  }
}

/* General responsive styling for content sections */
@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }
  
  .section-container {
    padding: 60px 20px;
  }
}
</style>
