<template>
  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-info">
        <div class="university-info">
          <h3 class="footer-heading">Duke University</h3>
          <h3 class="footer-heading">Fuqua School of Business</h3>
          <p class="address">100 Fuqua Drive, Durham, NC 27708</p>
        </div>
        <div class="social-links">
          <a href="#" aria-label="Facebook">
            <el-icon><Message /></el-icon>
          </a>
          <a href="#" aria-label="Twitter">
            <el-icon><ChatRound /></el-icon>
          </a>
          <a href="#" aria-label="LinkedIn">
            <el-icon><Connection /></el-icon>
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { Message, ChatRound, Connection } from '@element-plus/icons-vue';
</script>

<style scoped lang="scss">
.site-footer {
  background-color: #012169; /* Duke blue */
  color: #fff;
  padding: 40px 0;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.footer-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  
  @media (max-width: 768px) {
    flex-direction: column;
    text-align: center;
  }
}

.university-info {
  @media (max-width: 768px) {
    margin-bottom: 20px;
  }
}

.footer-heading {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 1.2rem;
  font-weight: 600;
  margin: 0 0 8px 0;
}

.address {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 0.9rem;
  margin: 10px 0 0 0;
  font-weight: 400;
}

.social-links {
  display: flex;
  gap: 15px;
  
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
    
    .el-icon {
      font-size: 20px;
      color: #fff;
    }
  }
}
</style> 