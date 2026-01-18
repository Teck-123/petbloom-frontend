import { initializeApp } from 'firebase/app'
import { getAuth } from 'firebase/auth'
import { getFirestore } from 'firebase/firestore'
import { getStorage } from 'firebase/storage'

const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY || '',
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN || '',
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID || '',
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET || '',
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID || '',
  appId: import.meta.env.VITE_FIREBASE_APP_ID || '',
  measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID || '',
}

// Check if Firebase config is valid
const isFirebaseConfigValid = () => {
  return firebaseConfig.apiKey && firebaseConfig.projectId && firebaseConfig.appId
}

if (!isFirebaseConfigValid()) {
  console.warn('Firebase configuration is incomplete. Firebase features will be disabled.')
}

let app, auth, db, storage

if (isFirebaseConfigValid()) {
  try {
    app = initializeApp(firebaseConfig)
    auth = getAuth(app)
    db = getFirestore(app)
    storage = getStorage(app)
  } catch (error) {
    console.error('Firebase initialization error:', error)
  }
} else {
  console.warn('Firebase will not be initialized due to missing configuration')
}

export { auth, db, storage }
export default app

