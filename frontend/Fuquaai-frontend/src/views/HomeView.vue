<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue';

// Example data for news items
const newsItems = ref([
  {
    title: 'OpenAI and Duke Launch New MetaScience Initiative',
    content: 'Professor Ronnie Chatterji Appointed First Chief Economist of OpenAI.',
    date: 'June 2023',
    url: 'https://www.nytimes.com/2024/10/22/technology/openai-chief-economist.html',
    source: 'The New York Times',
    summary: 'OpenAI hires former White House official Aaron "Ronnie" Chatterji, a Duke University professor, as its chief economist. His role will involve economic strategies for AI infrastructure and investment.',
    mediaType: 'image',
    mediaSrc: 'https://static01.nyt.com/images/2024/10/21/multimedia/OPENAI-ECONOMIST-1-hzfg/OPENAI-ECONOMIST-1-hzfg-superJumbo.jpg?quality=75&auto=webp',
    mediaAlt: 'Aaron "Ronnie" Chatterji, Duke University professor appointed as OpenAI chief economist'
  },
  {
    title: 'Duke University Launches Society-Centered AI Initiative',
    content: 'Including Fuqua Faculty and Amazon Scholar Alex Belloni.',
    date: 'May 2023',
    url: 'https://scai.duke.edu/',
    source: 'Duke University',
    summary: 'The Society-Centered AI Initiative (SCAI) at Duke brings together scholars to explore the co-evolution of AI and human behavior, addressing critical questions about the societal impacts of AI.',
    mediaType: 'image',
    mediaSrc: 'https://scai.duke.edu/sites/scai.duke.edu/files/styles/4_1_landscape_100_width_1140x285/public/images/011719b_brodhead071.jpg?h=07813f53&itok=7O4A4klC', 
    mediaAlt: 'Society-Centered AI Initiative at Duke University logo'
  },
  {
    title: 'Jiaming Xu Research on Deep Learning',
    content: 'Jiaming Xu researches and teaches deep learning and its business applications, supported by an NSF Career Award.',
    date: 'April 2023',
    url: 'https://www.nsf.gov/awardsearch/showAward?AWD_ID=2144593&HistoricalAwards=false',
    source: 'Duke Scholars',
    summary: 'Jiaming Xu, Associate Professor in Decision Sciences at Fuqua, focuses on machine learning and networks, developing methodologies for data inference to enable decision-making at scale.',
    mediaType: 'image',
    mediaSrc: '',
    mediaAlt: 'Duke Scholars logo'
  },
  {
    title: 'Net-Zero Analytics',
    content: 'David Brown shares how Net-Zero Analytics can accelerate the climate transition.',
    date: 'March 2023',
    url: 'https://www.youtube.com/watch?v=_dic12lrygg',
    source: 'YouTube',
    summary: 'A video presentation on how AI and advanced analytics can support climate initiatives and help businesses transition to sustainable practices through data-driven insights.',
    mediaType: 'video',
    mediaSrc: 'https://www.youtube.com/embed/_dic12lrygg',
    mediaAlt: 'David Brown discussing Net-Zero Analytics'
  },
  {
    title: 'Fuqua AI Platform Launch',
    content: 'Fuqua Researchers Launch Scientifiq.AI AI-Driven Platform to Accelerate the Translation of Science.',
    date: 'March 2023',
    url: 'https://scientifiq.ai/',
    source: 'Fuqua AI Research',
    summary: 'Fuqua AI Research',
    mediaType: 'image',
    mediaSrc: 'https://fuqua.ai/wp-content/uploads/2025/03/screenshot-2025-03-29-at-10.26.44e280afam.png',
    mediaAlt: 'Fuqua AI Research logo'
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

// For news carousel
const visibleNewsIndex = ref(0);
const newsPerView = 2;
let newsRotationTimer: number | null = null;

// Start news rotation
const startNewsRotation = () => {
  // Clear any existing timer
  if (newsRotationTimer !== null) {
    clearInterval(newsRotationTimer);
  }
  
  // Set interval to rotate news
  newsRotationTimer = setInterval(() => {
    // Calculate next index, wrapping back to 0 at the end
    visibleNewsIndex.value = (visibleNewsIndex.value + newsPerView) % newsItems.value.length;
    
    // Handle case where we don't have complete pairs at the end
    if (visibleNewsIndex.value + newsPerView > newsItems.value.length) {
      visibleNewsIndex.value = 0;
    }
  }, 5000) as unknown as number;
};

// Get visible news items
const visibleNews = computed(() => {
  const start = visibleNewsIndex.value;
  const end = Math.min(start + newsPerView, newsItems.value.length);
  return newsItems.value.slice(start, end);
});

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

// Typing animation for subtitle
const subtitleText = "Preparing the next generation of leaders with the skills, insights, and frameworks to create value for business and society in an AI-driven world.";
const displayedSubtitle = ref('');
const isTyping = ref(true);

onMounted(() => {
  startTypingAnimation();
  startNewsRotation();
});

const startTypingAnimation = () => {
  let currentIndex = 0;
  displayedSubtitle.value = '';
  isTyping.value = true;
  
  const typeNextChar = () => {
    if (currentIndex < subtitleText.length) {
      displayedSubtitle.value += subtitleText.charAt(currentIndex);
      currentIndex++;
      setTimeout(typeNextChar, 50); // Speed of typing
    } else {
      isTyping.value = false;
      setTimeout(() => {
        // Pause before restarting animation
        setTimeout(() => {
          startTypingAnimation();
        }, 3000); // Wait 3 seconds before restarting
      }, 1000);
    }
  };
  
  typeNextChar();
};

// Function to handle image loading errors for news items
const handleNewsMediaError = (event: Event) => {
  const media = event.target as HTMLImageElement;
  // Replace with fallback image
  media.src = '/src/assets/images/dukeicon.jpg';
  media.classList.add('fallback-media');
};

// Clean up on unmount
onUnmounted(() => {
  if (newsRotationTimer !== null) {
    clearInterval(newsRotationTimer);
  }
});
</script>

<template>
  <div class="home-container">
    <!-- Hero Section with full-width background image -->
    <section class="hero-section">
      <div class="hero-content">
        <h1 class="hero-title">AI@Fuqua</h1>
        <p class="hero-subtitle">{{ displayedSubtitle }}</p>
        <el-button type="primary" size="large" class="learn-more-btn" @click="scrollToSection('about')">Learn More</el-button>
      </div>
    </section>

    <!-- Main content section with light background -->
    <section class="main-content" id="about">
      <div class="section-container">
        <h2 class="section-title">Advancing Business Through AI Research & Learning</h2>
        <p class="section-description">AI is transforming business, and Duke University's Fuqua School of Business is leading the way. Discover how AI is integrated into research and learning across all areas of business education.</p>
        
        <!-- News cards grid with media embeds -->
        <div class="news-grid" id="news">
          <div class="news-carousel-container">
            <div class="news-dots">
              <span 
                v-for="(_, i) in Math.ceil(newsItems.length / newsPerView)" 
                :key="i" 
                :class="{ 'active-dot': Math.floor(visibleNewsIndex / newsPerView) === i }"
                @click="visibleNewsIndex = i * newsPerView; scrollToSection('news')"
                class="news-dot">
              </span>
            </div>
            
            <el-row :gutter="30">
              <transition-group name="news-fade">
                <el-col :span="24" :xs="24" :sm="24" :md="12" :lg="12" v-for="item in visibleNews" :key="item.title + item.date">
                  <div class="news-card-container">
                    <el-card class="news-card" shadow="hover">
                      <div class="news-card-content">
                        <h3 class="news-title">{{ item.title }}</h3>
                        <p class="news-content">{{ item.content }}</p>
                        
                        <!-- Media embed based on type -->
                        <div class="news-media-container">
                          <!-- Image preview with error handling -->
                          <img v-if="item.mediaType === 'image'" 
                               :src="item.mediaSrc || '/src/assets/images/dukeicon.jpg'" 
                               :alt="item.mediaAlt" 
                               class="news-media-image" 
                               loading="lazy"
                               @error="handleNewsMediaError($event)">
                          
                          <!-- Video embed with fallback -->
                          <iframe v-else-if="item.mediaType === 'video'"
                                  :src="item.mediaSrc"
                                  class="news-media-video"
                                  frameborder="0"
                                  allowfullscreen
                                  loading="lazy"
                                  :title="item.title"
                                  @error="handleNewsMediaError($event)">
                          </iframe>
                          <!-- Fallback for empty sources or error loading iframe -->
                          <img v-if="!item.mediaSrc || item.mediaType === 'video'" 
                               src="/src/assets/images/dukeicon.jpg" 
                               :alt="item.mediaAlt" 
                               class="fallback-media-image" 
                               loading="lazy"
                               :style="{ display: !item.mediaSrc ? 'block' : 'none' }">
                        </div>
                        
                        <div class="news-source-info">
                          <span class="news-source">{{ item.source }}</span>
                          <span class="news-date">{{ item.date }}</span>
                        </div>
                      </div>
                      
                      <div class="news-footer">
                        <a :href="item.url" target="_blank" class="news-link-button">
                          Read More <span class="arrow-icon">→</span>
                        </a>
                      </div>
              </el-card>
                  </div>
                </el-col>
              </transition-group>
            </el-row>
          </div>
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
  min-height: 100vh; /* Ensure it takes at least full viewport height */
  box-sizing: border-box;
}

/* Hero section styles */
.hero-section {
  position: relative;
  height: 100vh;
  width: 100%; 
  max-width: 100%;
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
  left: 0;
  right: 0;
  
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
  width: 90%; /* Responsive width */
  padding: 0 20px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.hero-title {
  font-size: clamp(2rem, 5vw, 3rem); /* Responsive font size */
  font-weight: 700;
  margin-bottom: 1.5rem;
  line-height: 1.2;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #ffffff;
  width: 100%;
}

.hero-subtitle {
  font-size: clamp(0.9rem, 2vw, 1.1rem); /* Responsive font size */
  margin-bottom: 2.5rem;
  line-height: 1.6;
  font-weight: 400;
  font-family: 'Montserrat', 'Roboto', 'Open Sans', sans-serif;
  letter-spacing: 0.3px;
  min-height: 80px; /* Reserve space for text to prevent layout shift */
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 100%;
  text-align: center;
}

.learn-more-btn {
  padding: 10px 30px;
  font-size: clamp(0.9rem, 2vw, 1.1rem); /* Responsive font size */
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
  width: 100%;
  max-width: 1200px; /* Match the header container max-width */
  margin: 0 auto;
  padding: clamp(40px, 6vw, 80px) 1.5rem; /* Use consistent 1.5rem padding to match header */
  box-sizing: border-box;
}

.section-title {
  font-size: clamp(1.8rem, 4vw, 2.5rem); /* Responsive font size */
  font-weight: 700;
  margin-bottom: 2rem;
  color: #012169; /* Duke blue */
  text-align: center;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  width: 100%;
}

.section-description {
  font-size: clamp(1rem, 2vw, 1.2rem); /* Responsive font size */
  line-height: 1.7;
  margin-bottom: 3rem;
    text-align: center;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
  color: #333;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  width: 100%;
}

.main-content, .research-areas, .featured-courses, .faculty-experts {
  width: 100%;
  display: flex;
  justify-content: center;
  box-sizing: border-box;
}

.main-content {
  background-color: #f8f9fa;
}

/* News cards with media embeds styles */
.news-grid {
  margin-top: 3rem;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.el-row {
  margin-bottom: 20px !important;
  width: 100%;
}

.el-col {
  margin-bottom: 30px;
}

.news-card-container {
  height: 100%;
}

.news-card {
  height: 100%;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  border: none;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 20px rgba(0, 0, 0, 0.15);
  }
}

.news-card-content {
  padding: 20px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.news-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  color: #012169; /* Duke blue */
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.news-content {
  font-size: 0.95rem;
  color: #333;
  line-height: 1.5;
  margin-bottom: 1.25rem;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.news-media-container {
  width: 100%;
  margin-bottom: 1.25rem;
  border-radius: 6px;
  overflow: hidden;
  background-color: #f1f1f1;
  aspect-ratio: 16 / 9;
  position: relative;
}

.news-media-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

.news-media-video {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.news-source-info {
  display: flex;
  justify-content: space-between;
      margin-bottom: 1rem;
  font-size: 0.85rem;
}

.news-source {
  font-weight: 600;
  color: #0736A4;
}

.news-date {
  color: #666;
}

.news-footer {
  padding: 15px 20px;
  border-top: 1px solid #eee;
  margin-top: auto;
  display: flex;
  justify-content: flex-end;
}

.news-link-button {
  display: inline-block;
  color: #0736A4;
  font-weight: 500;
  text-decoration: none;
  padding: 8px 0;
  font-size: 0.95rem;
  transition: all 0.2s ease;
  
  .arrow-icon {
    display: inline-block;
    margin-left: 4px;
    transition: transform 0.2s ease;
  }
  
  &:hover {
    color: #012169;
    
    .arrow-icon {
      transform: translateX(3px);
    }
  }
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
  
  .section-container {
    width: 100%;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
  }
}

@media (max-width: 992px) {
  .el-col {
    margin-bottom: 20px;
  }
  
  .news-card-container {
    max-width: 100%;
  }
  
  .research-area-card,
  .ai-approach-card,
  .faculty-card {
    max-width: 100%;
  }
}

@media (max-width: 768px) {
  .hero-section {
    min-height: 500px;
    height: 90vh;
  }
  
  .hero-section::after {
    background-position: center center;
  }
  
  .section-container {
    padding-top: 40px;
    padding-bottom: 40px;
    padding-left: 1rem;
    padding-right: 1rem;
  }
  
  .news-card-content {
    padding: 15px;
  }
  
  .news-media-container {
    aspect-ratio: 16 / 10; /* Adjusted for mobile */
  }
  
  .news-footer {
    padding: 12px 15px;
  }
  
  .research-grid,
  .ai-approach-grid,
  .faculty-grid {
    margin-top: 2rem;
  }
  
  .news-carousel-container {
    padding-bottom: 60px;
  }
}

@media (max-width: 576px) {
  .hero-section {
    min-height: 450px;
  }
  
  .section-container {
    padding-left: 1rem;
    padding-right: 1rem;
  }
  
  .news-dot {
    width: 10px;
    height: 10px;
    margin: 0 4px;
  }
  
  .faculty-col {
    width: 100%;
    padding-left: 12px;
    padding-right: 12px;
  }
  
  .faculty-name {
    font-size: 1rem;
  }
  
  .faculty-expertise {
    font-size: 0.85rem;
  }
}

/* For extra-small screens */
@media (max-width: 380px) {
  .hero-title {
    margin-top: 50px;
  }
  
  .hero-subtitle {
    min-height: 100px;
  }
  
  .news-title {
      font-size: 1.1rem;
  }
  
  .news-content {
    font-size: 0.85rem;
  }
  
  .research-area-title {
    font-size: 1.2rem;
  }
  
  .research-area-content {
    font-size: 0.9rem;
  }
}

/* For landscape mode on small devices */
@media (max-height: 500px) and (orientation: landscape) {
  .hero-section {
    min-height: 400px;
    height: auto;
    padding: 60px 0;
  }
  
  .hero-title {
    margin-bottom: 10px;
  }
  
  .hero-subtitle {
    min-height: 60px;
    margin-bottom: 20px;
  }
}

/* Fix for Safari and iOS devices */
@supports (-webkit-touch-callout: none) {
  .hero-section {
    height: -webkit-fill-available;
  }
}

/* Fix for notched phones */
@supports (padding: max(0px)) {
  .hero-section {
    padding-left: max(20px, env(safe-area-inset-left));
    padding-right: max(20px, env(safe-area-inset-right));
  }
}

/* Eliminate any potential scroll issues on all browsers */
html, body {
  overflow-x: hidden;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}

*, *:before, *:after {
  box-sizing: inherit;
}

.fallback-media {
  object-fit: contain !important;
  padding: 15px;
  background-color: #f8f9fa;
}

.fallback-media-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  padding: 15px;
  background-color: #f8f9fa;
  z-index: 0;
}

/* News cards rotation styles */
.news-carousel-container {
  position: relative;
  padding-bottom: 40px;
  width: 100%;
}

.news-dots {
  display: flex;
  justify-content: center;
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  margin-top: 20px;
}

.news-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: #e0e0e0;
  margin: 0 5px;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &.active-dot {
    background-color: #0736A4;
    transform: scale(1.2);
  }
  
  &:hover {
    background-color: #bdbdbd;
  }
}

.news-fade-enter-active,
.news-fade-leave-active {
  transition: all 0.5s ease;
}

.news-fade-enter-from {
  opacity: 0;
  transform: translateX(30px);
}

.news-fade-leave-to {
  opacity: 0;
  transform: translateX(-30px);
  position: absolute;
}

/* Make cards larger since we're only showing 2 at a time */
.news-card {
      margin-bottom: 30px;
    }

@media (max-width: 768px) {
  .news-carousel-container {
    padding-bottom: 60px;
  }
}

/* Fix for container centering */
@media (min-width: 1201px) {
  .section-container {
    padding-left: 1.5rem;
    padding-right: 1.5rem;
  }
}
</style>
