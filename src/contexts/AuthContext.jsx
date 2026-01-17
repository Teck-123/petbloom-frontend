import React, { createContext, useContext, useState, useEffect } from 'react'
import { auth } from '../services/firebase'
import { 
  signInWithEmailAndPassword, 
  createUserWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  GoogleAuthProvider,
  signInWithPopup
} from 'firebase/auth'
import api from '../services/api'
import toast from 'react-hot-toast'

const AuthContext = createContext()

export function useAuth() {
  return useContext(AuthContext)
}

export function AuthProvider({ children }) {
  const [currentUser, setCurrentUser] = useState(null)
  const [loading, setLoading] = useState(true)
  const [token, setToken] = useState(null)

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      if (user) {
        try {
          const idToken = await user.getIdToken()
          setToken(idToken)
          
          // Login to backend with Firebase token
          const response = await api.post('/auth/login', { token: idToken })
          setCurrentUser(response.data)
        } catch (error) {
          console.error('Auth error:', error)
          setCurrentUser(null)
          setToken(null)
        }
      } else {
        setCurrentUser(null)
        setToken(null)
      }
      setLoading(false)
    })

    return unsubscribe
  }, [])

  const login = async (email, password) => {
    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password)
      const idToken = await userCredential.user.getIdToken()
      
      const response = await api.post('/auth/login', { token: idToken })
      setCurrentUser(response.data)
      setToken(response.data.access_token)
      
      // Set authorization header
      api.defaults.headers.common['Authorization'] = `Bearer ${response.data.access_token}`
      
      toast.success('Login successful!')
      return response.data
    } catch (error) {
      toast.error(error.response?.data?.detail || 'Login failed')
      throw error
    }
  }

  const register = async (email, password, fullName, phone) => {
    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password)
      const idToken = await userCredential.user.getIdToken()
      
      // Update user profile
      await userCredential.user.updateProfile({
        displayName: fullName
      })
      
      const response = await api.post('/auth/login', { token: idToken })
      setCurrentUser(response.data)
      setToken(response.data.access_token)
      
      // Set authorization header
      api.defaults.headers.common['Authorization'] = `Bearer ${response.data.access_token}`
      
      toast.success('Registration successful!')
      return response.data
    } catch (error) {
      toast.error(error.response?.data?.detail || 'Registration failed')
      throw error
    }
  }

  const loginWithGoogle = async () => {
    try {
      const provider = new GoogleAuthProvider()
      const userCredential = await signInWithPopup(auth, provider)
      const idToken = await userCredential.user.getIdToken()
      
      const response = await api.post('/auth/login', { token: idToken })
      setCurrentUser(response.data)
      setToken(response.data.access_token)
      
      // Set authorization header
      api.defaults.headers.common['Authorization'] = `Bearer ${response.data.access_token}`
      
      toast.success('Google login successful!')
      return response.data
    } catch (error) {
      toast.error(error.response?.data?.detail || 'Google login failed')
      throw error
    }
  }

  const logout = async () => {
    try {
      await signOut(auth)
      setCurrentUser(null)
      setToken(null)
      delete api.defaults.headers.common['Authorization']
      toast.success('Logged out successfully!')
    } catch (error) {
      toast.error('Logout failed')
      throw error
    }
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
      {!loading && children}
    </AuthContext.Provider>
  )
}
