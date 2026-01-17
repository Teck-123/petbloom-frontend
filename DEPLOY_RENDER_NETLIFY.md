# Deploy: Backend (Render) + Frontend (Netlify)

## 1. Deploy Backend on Render

### Steps:
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New" → "Blueprint"
3. Connect GitHub repo: `Teck-123/petbloom-frontend`
4. Select branch: `main`
5. Render will detect `render.yaml`

### Environment Variables (Add in Render):
```
DATABASE_URL → Auto-populated by Render PostgreSQL
FBASE_CREDENTIALS → Paste your Firebase service account JSON
JWT_SECRET → Click "Generate" or use: openssl rand -hex 32
JWT_ALGORITHM → HS256
FRONTEND_URL → https://petbloom.netlify.app (update after Netlify deploy)
```

6. Click "Apply"
7. Wait for deployment (5-10 minutes)
8. Copy your backend URL: `https://petbloom-backend.onrender.com`

---

## 2. Deploy Frontend on Netlify

### Option A: Netlify CLI
```bash
npm install -g netlify-cli
netlify login
netlify deploy --prod
```

### Option B: Netlify Dashboard
1. Go to [Netlify](https://app.netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect GitHub: `Teck-123/petbloom-frontend`
4. Build settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
5. Add Environment Variables:
   ```
   VITE_API_URL=https://petbloom-backend.onrender.com/api/v1
   VITE_FIREBASE_API_KEY=your-firebase-api-key
   VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
   VITE_FIREBASE_PROJECT_ID=your-project-id
   VITE_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
   VITE_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
   VITE_FIREBASE_APP_ID=your-app-id
   ```
6. Click "Deploy"

---

## 3. Update Backend CORS

After getting Netlify URL, update Render backend:
1. Go to Render Dashboard → petbloom-backend
2. Environment → Edit `FRONTEND_URL`
3. Set to: `https://your-site.netlify.app`
4. Save (will auto-redeploy)

---

## 4. Update Firebase

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Authentication → Settings → Authorized domains
3. Add:
   - `your-site.netlify.app`
   - `petbloom-backend.onrender.com`

---

## 5. Test Deployment

- Frontend: `https://your-site.netlify.app`
- Backend API: `https://petbloom-backend.onrender.com/docs`
- Health Check: `https://petbloom-backend.onrender.com/health`

---

## Troubleshooting

### Backend won't start
- Check Render logs
- Verify `DATABASE_URL` is set
- Ensure `FBASE_CREDENTIALS` is valid JSON

### Frontend can't connect to backend
- Check `VITE_API_URL` in Netlify env vars
- Verify CORS settings in backend
- Check browser console for errors

### Database connection failed
- Render free tier: DB sleeps after inactivity
- First request may take 30-60 seconds

---

## Quick Commands

### Redeploy Frontend
```bash
git add .
git commit -m "Update"
git push origin main
```
Netlify auto-deploys on push.

### Redeploy Backend
Push to GitHub or use Render dashboard "Manual Deploy"

### View Logs
- Render: Dashboard → Service → Logs
- Netlify: Dashboard → Deploys → Deploy log
