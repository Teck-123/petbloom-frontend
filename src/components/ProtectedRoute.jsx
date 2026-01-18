/**
 * ProtectedRoute Component
 * 
 * Higher-order component that protects routes requiring authentication
 * - Redirects unauthenticated users to login page
 * - Shows loading spinner while checking auth status
 * - Renders children only for authenticated users
 * 
 * @component
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - Child components to protect
 */
import React from 'react'
import { Navigate } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'

function ProtectedRoute({ children }) {
  const { currentUser, loading } = useAuth()

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500"></div>
      </div>
    )
  }

  return currentUser ? children : <Navigate to="/login" />
}

export default ProtectedRoute
