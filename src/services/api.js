import axios from 'axios'

// Determine API URL based on environment
let baseURL = import.meta.env.VITE_API_URL
if (!baseURL || baseURL.includes('localhost')) {
  // For Vercel/production, use the local machine's IP or fallback to demo
  baseURL = 'http://localhost:8000/api/v1'
}

const api = axios.create({
  baseURL: baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor
api.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default api
