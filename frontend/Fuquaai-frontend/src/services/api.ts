import axios from 'axios'

// Create an axios instance with default config
const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json'
  }
})

// News API
export const getNews = () => api.get('/news/')
export const getNewsById = (id: string) => api.get(`/news/${id}/`)
export const getNewsByCategory = (category: string) => api.get(`/news/?category=${category}`)

// Courses API
export const getCourses = () => api.get('/courses/')
export const getCourseById = (id: string) => api.get(`/courses/${id}/`)
export const getCoursesByCategory = (category: string) => api.get(`/courses/?category=${category}`)

// Research API
export const getResearch = () => api.get('/research/')
export const getResearchById = (id: string) => api.get(`/research/${id}/`)
export const getResearchByCategory = (category: string) => api.get(`/research/?category=${category}`)

export default api 