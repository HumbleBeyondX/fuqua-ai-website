<template>
  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-content">
        <div class="footer-logo-column">
          <img src="/src/assets/images/Fuqualogo.png" alt="Fuqua School of Business" class="fuqua-logo">
        </div>
        <div class="spacer-column"></div>
        <div class="footer-info-column">
          <div class="footer-text">
            <p class="footer-line">Duke University</p>
            <p class="footer-line">Fuqua School of Business</p>
            <p class="footer-line">100 Fuqua Drive, Durham, NC 27708</p>
          </div>
          <div class="social-links">
            <a href="https://www.facebook.com/Duke.Fuqua/" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
              <span class="icon facebook-icon"></span>
            </a>
            <a href="https://www.instagram.com/dukefuqua/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
              <span class="icon instagram-icon"></span>
            </a>
            <a href="https://www.linkedin.com/school/fuqua-school-of-business/posts/?feedView=all" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
              <span class="icon linkedin-icon"></span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
// No additional imports needed
</script>

<style scoped lang="scss">
.site-footer {
  background-color: #012169; /* Duke blue */
  color: #fff;
  padding: 15px 0;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.footer-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  
  @media (max-width: 768px) {
    flex-direction: column;
    text-align: center;
  }
}

.footer-logo-column {
  flex: 0 0 auto;
  
  @media (max-width: 768px) {
    margin-bottom: 20px;
  }
}

.spacer-column {
  flex: 1;
  min-width: 60px;
  
  @media (max-width: 768px) {
    display: none;
  }
}

.fuqua-logo {
  height: 120px;
  width: auto;
  
  @media (max-width: 768px) {
    height: 100px;
  }
}

.footer-info-column {
  flex: 0 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.footer-text {
  margin-bottom: 15px;
  margin-top: 15px;
}

.footer-line {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 1rem;
  font-weight: 300;
  margin: 0 0 8px 0;
  color: #ffffff;
  line-height: 1.4;
}

.social-links {
  display: flex;
  gap: 15px;
  margin-top: 10px;
  
  @media (max-width: 768px) {
    justify-content: center;
  }
  
  a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.1);
    transition: background-color 0.3s ease;
    
    &:hover {
      background-color: rgba(255, 255, 255, 0.2);
    }
  }
}

.icon {
  display: inline-block;
  width: 20px;
  height: 20px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  filter: invert(100%);
}

.facebook-icon {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512'%3E%3Cpath d='M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z'/%3E%3C/svg%3E");
}

.instagram-icon {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 448 512'%3E%3Cpath d='M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z'/%3E%3C/svg%3E");
}

.linkedin-icon {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 448 512'%3E%3Cpath d='M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z'/%3E%3C/svg%3E");
}
</style> 