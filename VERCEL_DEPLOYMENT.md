# PetBloom Vercel Deployment Checklist

## Step 1: Connect Repository to Vercel
1. Go to https://vercel.com/new
2. Click "Import Git Repository"
3. Select your GitHub repo: `AlexMureti/petbloom-frontend`
4. Click "Import"

## Step 2: Configure Build Settings
- **Framework Preset**: Select "Vite"
- **Build Command**: `npm run build` (should auto-detect)
- **Output Directory**: `dist` (should auto-detect)
- **Install Command**: `npm install` (default)

## Step 3: Set Environment Variables
In the "Environment Variables" section, add:
```
VITE_API_URL = https://petbloom-frontend-production.up.railway.app/api/v1
```

Or use the `vercel.json` which already has this configured.

## Step 4: Deploy
Click "Deploy" - Vercel will:
1. Clone your repository
2. Install dependencies
3. Build the project
4. Deploy to https://pet-bloom.vercel.app/

## Step 5: Verify
Once deployed, test:
1. Visit https://pet-bloom.vercel.app
2. You should see products loading
3. Check browser console (F12) for any errors
4. Verify API calls are going to the Railway backend

## Current Status
- ✅ Backend deployed on Railway
- ✅ Backend API working (tested with curl)
- ✅ CORS configured for Vercel origin
- ✅ Frontend code ready with Vercel config
- ⏳ Awaiting frontend deployment to Vercel

## If Still Getting Errors:
1. Hard refresh browser (Ctrl+Shift+R)
2. Clear browser cache
3. Check browser DevTools Console (F12)
4. Look for Network tab errors
5. Verify VITE_API_URL is set correctly in build
