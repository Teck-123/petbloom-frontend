# Firebase Setup Guide

## Step 1: Go to Firebase Console
Visit: https://console.firebase.google.com

## Step 2: Create a New Project
1. Click "Add project"
2. Enter project name: "petbloom" (or any name)
3. Click Continue
4. Disable Google Analytics (optional)
5. Click "Create project"

## Step 3: Add Web App
1. Click the Web icon (</>) on the project homepage
2. Register app name: "PetBloom Frontend"
3. Click "Register app"
4. You'll see your Firebase config - COPY IT

## Step 4: Enable Authentication
1. In left sidebar, click "Authentication"
2. Click "Get started"
3. Click "Email/Password" under Sign-in method
4. Enable it and click "Save"

## Step 5: Copy Your Config
You'll see something like:
```javascript
const firebaseConfig = {
  apiKey: "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  authDomain: "petbloom-xxxxx.firebaseapp.com",
  projectId: "petbloom-xxxxx",
  storageBucket: "petbloom-xxxxx.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:xxxxxxxxxxxxx"
};
```

## Step 6: Update .env File
Edit `/home/thecla/petbloom-frontend/.env`:

```bash
VITE_API_URL=http://localhost:8000/api/v1
VITE_FIREBASE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
VITE_FIREBASE_AUTH_DOMAIN=petbloom-xxxxx.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=petbloom-xxxxx
VITE_FIREBASE_STORAGE_BUCKET=petbloom-xxxxx.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=123456789012
VITE_FIREBASE_APP_ID=1:123456789012:web:xxxxxxxxxxxxx
```

## Step 7: Restart Frontend
```bash
cd /home/thecla/petbloom-frontend
npm run dev
```

## Done!
Your frontend will now work with Firebase authentication.

---

## Quick Alternative: Test Without Firebase
If you want to test without Firebase, you can temporarily disable auth:

1. Comment out Firebase imports in `src/services/firebase.js`
2. Modify `src/contexts/AuthContext.jsx` to return mock user
3. This is NOT recommended for production
