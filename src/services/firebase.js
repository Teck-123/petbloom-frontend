import { initializeApp } from 'firebase/app'
import { getAuth } from 'firebase/auth'
import { getFirestore } from 'firebase/firestore'
import { getStorage } from 'firebase/storage'

const requiredEnv = (key) => {
  const value = import.meta.env[key]
  if (!value) {
    console.warn(`[Firebase] Missing env var ${key}`)
    return null
  }
  return value
}

const firebaseConfig = {
  apiKey: requiredEnv('VITE_FIREBASE_API_KEY') || 'demo-key',
  authDomain: requiredEnv('VITE_FIREBASE_AUTH_DOMAIN') || 'demo.firebaseapp.com',
  projectId: requiredEnv('VITE_FIREBASE_PROJECT_ID') || 'demo-project',
  storageBucket: requiredEnv('VITE_FIREBASE_STORAGE_BUCKET') || 'demo.appspot.com',
  messagingSenderId: requiredEnv('VITE_FIREBASE_MESSAGING_SENDER_ID') || 'demo-sender',
  appId: requiredEnv('VITE_FIREBASE_APP_ID') || 'demo-app',
  measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID,
}

let app, auth, db, storage

try {
  app = initializeApp(firebaseConfig)
  auth = getAuth(app)
  db = getFirestore(app)
  storage = getStorage(app)
} catch (error) {
  console.warn('[Firebase] Using demo/fallback mode:', error.message)
  // Create mock objects for demo mode
  export const auth = null
  export const db = null
  export const storage = null
}

export { auth, db, storage }
export default app
