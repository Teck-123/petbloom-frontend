# Firebase & Backend Communication Troubleshooting Guide

## Summary of Changes Made ✅
1. Created `.env.production` - Ensures Firebase config is available during Vercel builds
2. Created `.env.local` - Local development configuration
3. Fixed `.env` - Removed incorrect API endpoint
4. Updated `vercel.json` - Removed hardcoded env vars (use Project Settings instead)
5. Cleaned up `.env.example` - Removed duplicates

---

## Step 1: Set Environment Variables in Vercel Dashboard

Firebase and API configuration must be set in **Vercel Project Settings**, not in `vercel.json`.

### Go to Vercel Dashboard:
1. Visit: https://vercel.com/teams/G7pAfOmi7diMewBtcWrdXuNx/petbloom-frontend
2. Click **Settings** → **Environment Variables**
3. Add these variables for **Production**:

#### Firebase Configuration (copy exactly):
```
VITE_FIREBASE_API_KEY = AIzaSyD8hxlXo7mjuM1e7Yg_DCCRLrIyrhW7TRA
VITE_FIREBASE_AUTH_DOMAIN = petbloom-71bbc.firebaseapp.com
VITE_FIREBASE_PROJECT_ID = petbloom-71bbc
VITE_FIREBASE_STORAGE_BUCKET = petbloom-71bbc.firebasestorage.app
VITE_FIREBASE_MESSAGING_SENDER_ID = 918044598228
VITE_FIREBASE_APP_ID = 1:918044598228:web:5a85cb15270f08fed64041
VITE_FIREBASE_MEASUREMENT_ID = G-2311X47GF1
```

#### API Configuration:
```
VITE_API_URL = https://YOUR_RAILWAY_BACKEND_URL/api/v1
```
**⚠️ CRITICAL:** Replace `YOUR_RAILWAY_BACKEND_URL` with your actual Railway backend URL!
- Example: `https://petbloom-backend-prod-abc123.railway.app`
- Do NOT use the frontend URL

---

## Step 2: Get Your Railway Backend URL

### Method A: From Railway Dashboard
1. Go to https://railway.app/dashboard
2. Select your **petbloom-backend** service
3. Click **Settings** → **Domains**
4. Copy the **Public URL** (should look like: `https://petbloom-backend-xxxxx.railway.app`)

### Method B: From Railway Service
1. In Railway, select petbloom-backend
2. Click **Deployments** → Latest deployment
3. Click the public URL in the top right

### Find your backend URL and paste it here:
```
YOUR_RAILWAY_BACKEND_URL = ___________________________________
```

---

## Step 3: Configure Backend CORS (Railway)

Your backend needs to accept requests from Vercel frontend.

1. Go to Railway Dashboard → petbloom-backend
2. Click **Variables**
3. Update or add these environment variables:

```
FRONTEND_URL = https://YOUR_VERCEL_FRONTEND_URL
ENVIRONMENT = production
```

Get your Vercel frontend URL:
- It should be something like: `https://petbloom-frontend-xxxxx.vercel.app`
- Or your custom domain if configured

---

## Step 4: Test Firebase Configuration

After deploying, open your Vercel app and check the browser console:

### Open DevTools (F12) → Console tab

**Expected:** No Firebase initialization errors

**If you see errors like:**
- `"Firebase configuration is incomplete"`
- `"Cannot read property 'apiKey' of undefined"`

**Then:**
1. Verify all Firebase variables are in Vercel Project Settings
2. Redeploy: Click **Deployments** → Latest → Click the three dots → **Redeploy**
3. Wait 2-3 minutes for the build to complete
4. Refresh the page in an incognito/private window

---

## Step 5: Test Backend Communication

### Test the API connection:

1. In your Vercel app, try logging in
2. Open DevTools → **Network** tab
3. Look for API requests (should start with your Railway URL)

**Expected:** Successful response from your backend

**If API calls fail:**

### Check 1: Verify correct API URL
```javascript
// Open DevTools Console and run:
console.log(import.meta.env.VITE_API_URL)
```
Should output your Railway URL, not the frontend URL.

### Check 2: Test backend directly
```bash
curl https://YOUR_RAILWAY_BACKEND_URL/health
```
Should return a 200 response.

### Check 3: Check Railway backend logs
1. Go to Railway Dashboard → petbloom-backend
2. Click **Logs** tab
3. Look for CORS errors or connection issues
4. If you see CORS errors, verify FRONTEND_URL is set correctly

---

## Step 6: Verify Firebase in Code

The Firebase initialization is already configured in [src/services/firebase.js](src/services/firebase.js).

It will:
- Read config from environment variables (now set in Vercel)
- Validate that required fields exist
- Initialize Firebase if valid
- Log warnings if incomplete

No code changes needed—just ensure variables are set!

---

## Complete Checklist

- [ ] Created `.env.production` file
- [ ] Created `.env.local` file
- [ ] Set all Firebase variables in Vercel Project Settings
- [ ] Found your Railway backend URL
- [ ] Set VITE_API_URL in Vercel to correct Railway URL
- [ ] Updated FRONTEND_URL in Railway backend
- [ ] Redeployed Vercel frontend
- [ ] Tested Firebase (check console)
- [ ] Tested API calls (check Network tab)
- [ ] Verified `curl` to `/health` endpoint works
- [ ] Backend and frontend communicating successfully

---

## Quick Reference

| Configuration | Location | Value |
|---|---|---|
| Firebase Keys | Vercel Project Settings | VITE_FIREBASE_* |
| API URL | Vercel Project Settings | VITE_API_URL = Railway URL |
| Frontend URL | Railway backend Variables | FRONTEND_URL = Vercel URL |
| Development API | `.env` or `.env.local` | http://localhost:8000/api/v1 |

---

## If Still Having Issues

### For Firebase problems:
- Check browser console for specific error
- Verify each Firebase variable in Vercel Settings (no typos!)
- Ensure project ID matches: `petbloom-71bbc`

### For backend communication:
- Verify API URL doesn't include `/api/v1` twice
- Check that Railway backend is actually running
- Look at Railway backend logs for CORS errors
- Ensure FRONTEND_URL in Railway exactly matches Vercel domain

### Need to redeploy?
```bash
# From your local project
git add .
git commit -m "Update Firebase and API configuration"
git push
# Vercel will auto-deploy on push
```

Or redeploy manually from Vercel Dashboard if variables changed.
