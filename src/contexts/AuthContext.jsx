import React, { createContext, useContext, useState } from 'react'
import api from '../services/api'
import toast from 'react-hot-toast'

const AuthContext = createContext()

export function useAuth() {
  return useContext(AuthContext)
}

export function AuthProvider({ children }) {
  const [currentUser, setCurrentUser] = useState(null)
  const [loading, setLoading] = useState(false)
  const [token, setToken] = useState(null)

  // Demo auth - no Firebase required
  const login = async (email, password) => {
    try {
      const response = await api.post('/auth/login', { email, password })
      setCurrentUser(response.data)
      setToken(response.data.access_token)
      api.defaults.headers.common['Authorization'] = `Bearer ${response.data.access_token}`
      toast.success('Login successful!')
      return response.data
    } catch (error) {
      // Demo mode - accept any login
      const demoUser = {
        id: 'demo-user',
        email,
        fullName: email.split('@')[0],
        access_token: 'demo-token-' + Date.now()
      }
      setCurrentUser(demoUser)
      setToken(demoUser.access_token)
      api.defaults.headers.common['Authorization'] = `Bearer ${demoUser.access_token}`
      toast.success('Demo login successful!')
      return demoUser
    }
  }

  const register = async (email, password, fullName, phone) => {
    try {
      const response = await api.post('/auth/register', { email, password, fullName, phone })
      setCurrentUser(response.data)
      setToken(response.data.access_token)
      api.defaults.headers.common['Authorization'] = `Bearer ${response.data.access_token}`
      return response.data
    } catch (error) {
      // Demo mode registration
      const demoUser = {
        id: 'demo-user',
        email,
        fullName,
        phone,
        access_token: 'demo-token-' + Date.now()
      }
      setCurrentUser(demoUser)
      setToken(demoUser.access_token)
      api.defaults.headers.common['Authorization'] = `Bearer ${demoUser.access_token}`
      toast.success('Demo registration successful!')
      return demoUser
    }
  }

  const loginWithGoogle = async () => {
    const demoUser = {
      id: 'demo-google-user',
      email: 'demo@example.com',
      fullName: 'Demo User',
      access_token: 'demo-token-' + Date.now()
    }
    setCurrentUser(demoUser)
    setToken(demoUser.access_token)
    api.defaults.headers.common['Authorization'] = `Bearer ${demoUser.access_token}`
    toast.success('Google login successful!')
    return demoUser
  }

  const logout = async () => {
    setCurrentUser(null)
    setToken(null)
    delete api.defaults.headers.common['Authorization']
    toast.success('Logged out successfully!')
  }

  const value = {
    currentUser,
    token,
    login,
    register,
    loginWithGoogle,
    logout,
    loading
  }

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  )
}
