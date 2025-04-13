<template>
  <div class="contact-view">
    <el-container>
      <el-main>
        <h1 class="page-title">Contact Us</h1>
        
        <div class="contact-content">
          <el-row :gutter="40">
            <!-- Contact Form -->
            <el-col :xs="24" :md="12">
              <el-card class="contact-form-card">
                <h2>Send Us a Message</h2>
                <el-form
                  ref="contactForm"
                  :model="form"
                  :rules="rules"
                  label-position="top"
                >
                  <el-form-item label="Name" prop="name">
                    <el-input v-model="form.name" placeholder="Your name" />
                  </el-form-item>
                  
                  <el-form-item label="Email" prop="email">
                    <el-input v-model="form.email" placeholder="Your email" />
                  </el-form-item>
                  
                  <el-form-item label="Subject" prop="subject">
                    <el-input v-model="form.subject" placeholder="Subject" />
                  </el-form-item>
                  
                  <el-form-item label="Message" prop="message">
                    <el-input
                      v-model="form.message"
                      type="textarea"
                      :rows="6"
                      placeholder="Your message"
                    />
                  </el-form-item>
                  
                  <el-form-item>
                    <el-button type="primary" @click="submitForm" :loading="submitting">
                      Send Message
                    </el-button>
                  </el-form-item>
                </el-form>
              </el-card>
            </el-col>
            
            <!-- Contact Information -->
            <el-col :xs="24" :md="12">
              <div class="contact-info">
                <h2>Get in Touch</h2>
                
                <div class="info-item">
                  <el-icon><location /></el-icon>
                  <div>
                    <h3>Address</h3>
                    <p>Fuqua School of Business<br>
                      100 Fuqua Drive<br>
                      27708 Durham, NC</p>
                  </div>
                </div>
                
                <div class="info-item">
                  <el-icon><phone /></el-icon>
                  <div>
                    <h3>Phone</h3>
                    <p>+1 (919) 660-7700</p>
                  </div>
                </div>
                
                <div class="info-item">
                  <el-icon><message /></el-icon>
                  <div>
                    <h3>Email</h3>
                    <p>ai@fuqua.duke.edu</p>
                  </div>
                </div>
                
                <div class="social-links">
                  <h3>Follow Us</h3>
                  <div class="links">
                    <a href="#" class="social-link">
                      <el-icon><linkedin /></el-icon>
                    </a>
                    <a href="#" class="social-link">
                      <el-icon><twitter /></el-icon>
                    </a>
                    <a href="#" class="social-link">
                      <el-icon><youtube /></el-icon>
                    </a>
                  </div>
                </div>
              </div>
            </el-col>
          </el-row>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Location, Phone, Message} from '@element-plus/icons-vue'
import type { FormInstance, FormRules } from 'element-plus'

const contactForm = ref<FormInstance>()
const submitting = ref(false)

const form = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const rules: FormRules = {
  name: [
    { required: true, message: 'Please enter your name', trigger: 'blur' },
    { min: 2, message: 'Name must be at least 2 characters', trigger: 'blur' }
  ],
  email: [
    { required: true, message: 'Please enter your email', trigger: 'blur' },
    { type: 'email', message: 'Please enter a valid email', trigger: 'blur' }
  ],
  subject: [
    { required: true, message: 'Please enter a subject', trigger: 'blur' }
  ],
  message: [
    { required: true, message: 'Please enter your message', trigger: 'blur' },
    { min: 10, message: 'Message must be at least 10 characters', trigger: 'blur' }
  ]
}

const submitForm = async () => {
  if (!contactForm.value) return
  
  try {
    await contactForm.value.validate()
    submitting.value = true
    
    // Here you would typically send the form data to your backend
    // For now, we'll just simulate a delay
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    ElMessage.success('Message sent successfully!')
    form.value = {
      name: '',
      email: '',
      subject: '',
      message: ''
    }
  } catch (error) {
    console.error('Form validation failed:', error)
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped lang="scss">
.contact-view {
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

  .contact-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
  }

  .contact-form-card {
    h2 {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.75rem;
      font-weight: 600;
      color: #2c3e50;
      margin-bottom: 2rem;
    }

    :deep(.el-form-item__label) {
      font-family: 'Montserrat', sans-serif;
      font-weight: 500;
    }

    .el-button {
      font-family: 'Montserrat', sans-serif;
      font-weight: 500;
      padding: 12px 30px;
    }
  }

  .contact-info {
    h2 {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.75rem;
      font-weight: 600;
      color: #2c3e50;
      margin-bottom: 2rem;
    }

    .info-item {
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 2rem;

      .el-icon {
        font-size: 24px;
        color: #0033a0;
        margin-top: 0.25rem;
      }

      h3 {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 0 0 0.5rem;
      }

      p {
        font-family: 'Open Sans', sans-serif;
        color: #6c757d;
        line-height: 1.6;
        margin: 0;
      }
    }

    .social-links {
      margin-top: 3rem;

      h3 {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
      }

      .links {
        display: flex;
        gap: 1rem;

        .social-link {
          display: flex;
          align-items: center;
          justify-content: center;
          width: 40px;
          height: 40px;
          border-radius: 50%;
          background: #f5f7fa;
          color: #0033a0;
          transition: all 0.3s ease;

          &:hover {
            background: #0033a0;
            color: #fff;
            transform: translateY(-3px);
          }

          .el-icon {
            font-size: 20px;
          }
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .contact-view {
    .page-title {
      font-size: 2rem;
    }

    .contact-content {
      padding: 0 1rem;
    }

    .el-col {
      margin-bottom: 2rem;
    }
  }
}
</style> 