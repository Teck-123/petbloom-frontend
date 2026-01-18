# PetBloom Deployment Guide

## Deployment Options

### Option 1: Render.com (Recommended - Free Tier Available)

#### Prerequisites
- GitHub account
- Render.com account
- Firebase project setup

#### Steps

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

2. **Deploy on Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New" → "Blueprint"
   - Connect your GitHub repository
   - Select `render.yaml`
   - Add environment variables:
     - `FBASE_CREDENTIALS`: Your Firebase service account JSON (as string)
     - `VITE_FIREBASE_API_KEY`: From Firebase console
     - `VITE_FIREBASE_AUTH_DOMAIN`: From Firebase console
     - `VITE_FIREBASE_PROJECT_ID`: From Firebase console
     - `VITE_FIREBASE_STORAGE_BUCKET`: From Firebase console
     - `VITE_FIREBASE_MESSAGING_SENDER_ID`: From Firebase console
     - `VITE_FIREBASE_APP_ID`: From Firebase console

3. **Update Firebase Authorized Domains**
   - Go to Firebase Console → Authentication → Settings
   - Add your Render frontend URL to authorized domains

---

### Option 2: Vercel (Frontend) + Railway (Backend)

#### Frontend on Vercel

1. **Deploy Frontend**
   ```bash
   npm install -g vercel
   vercel login
   vercel
   ```

2. **Add Environment Variables in Vercel Dashboard**
   - `VITE_API_URL`: Your Railway backend URL
   - All Firebase config variables

#### Backend on Railway

1. **Deploy Backend**
   - Go to [Railway](https://railway.app)
   - New Project → Deploy from GitHub
   - Select `back-end` directory
   - Add PostgreSQL database
   - Add environment variables:
     - `DATABASE_URL`: Auto-populated by Railway
     - `FBASE_CREDENTIALS`: Firebase service account JSON
     - `JWT_SECRET`: Generate a secure secret
     - `FRONTEND_URL`: Your Vercel URL

2. **Build Command**: `pip install -r requirements.txt && prisma generate && prisma db push`
3. **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

---

### Option 3: Docker Deployment (VPS/Cloud)

#### Prerequisites
- Docker and Docker Compose installed
- VPS (DigitalOcean, AWS EC2, etc.)

#### Steps

1. **Clone Repository on Server**
   ```bash
   git clone https://github.com/Teck-123/petbloom-frontend.git
   cd petbloom-frontend
   ```

2. **Create .env File**
   ```bash
   cat > .env << EOF
   DB_PASSWORD=your_secure_password
   JWT_SECRET=your_jwt_secret
   FBASE_CREDENTIALS=/path/to/firebase-credentials.json
   EOF
   ```

3. **Add Firebase Credentials**
   ```bash
   # Copy your Firebase service account JSON to the server
   scp firebase-credentials.json user@server:/path/to/petbloom-frontend/back-end/
   ```

4. **Update Frontend Environment**
   Create `.env` in root:
   ```
   VITE_API_URL=http://your-server-ip:8000/api/v1
   VITE_FIREBASE_API_KEY=your-api-key
   VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
   VITE_FIREBASE_PROJECT_ID=your-project-id
   VITE_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
   VITE_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
   VITE_FIREBASE_APP_ID=your-app-id
   ```

5. **Deploy with Docker Compose**
   ```bash
   docker-compose up -d
   ```

6. **Run Database Migrations**
   ```bash
   docker-compose exec backend prisma db push
   docker-compose exec backend python seed.py
   ```

7. **Access Application**
   - Frontend: http://your-server-ip:3000
   - Backend: http://your-server-ip:8000
   - API Docs: http://your-server-ip:8000/docs

---

### Option 4: AWS Deployment

#### Frontend on S3 + CloudFront

1. **Build Frontend**
   ```bash
   npm run build
   ```

2. **Deploy to S3**
   ```bash
   aws s3 sync dist/ s3://your-bucket-name --delete
   aws s3 website s3://your-bucket-name --index-document index.html
   ```

3. **Setup CloudFront** for HTTPS and CDN

#### Backend on AWS Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize and Deploy**
   ```bash
   cd back-end
   eb init -p python-3.12 petbloom-backend
   eb create petbloom-backend-env
   eb setenv DATABASE_URL=your_db_url FBASE_CREDENTIALS=your_credentials
   eb deploy
   ```

---

## Post-Deployment Checklist

- [ ] Update CORS origins in backend to include production URLs
- [ ] Add production URLs to Firebase authorized domains
- [ ] Set up SSL/HTTPS certificates
- [ ] Configure custom domain (optional)
- [ ] Set up monitoring and logging
- [ ] Enable database backups
- [ ] Test all features in production
- [ ] Set up CI/CD pipeline (GitHub Actions)

---

## Environment Variables Reference

### Backend
- `DATABASE_URL`: PostgreSQL connection string
- `FBASE_CREDENTIALS`: Firebase service account JSON
- `JWT_SECRET`: Secret key for JWT tokens
- `JWT_ALGORITHM`: HS256
- `FRONTEND_URL`: Frontend URL for CORS

### Frontend
- `VITE_API_URL`: Backend API URL
- `VITE_FIREBASE_API_KEY`: Firebase API key
- `VITE_FIREBASE_AUTH_DOMAIN`: Firebase auth domain
- `VITE_FIREBASE_PROJECT_ID`: Firebase project ID
- `VITE_FIREBASE_STORAGE_BUCKET`: Firebase storage bucket
- `VITE_FIREBASE_MESSAGING_SENDER_ID`: Firebase messaging sender ID
- `VITE_FIREBASE_APP_ID`: Firebase app ID

---

## Troubleshooting

### Database Connection Issues
```bash
# Check database connectivity
docker-compose exec backend python -c "from prisma import Prisma; import asyncio; asyncio.run(Prisma().connect())"
```

### CORS Errors
- Ensure `FRONTEND_URL` is set correctly in backend
- Check backend CORS middleware configuration

### Build Failures
- Verify all environment variables are set
- Check Node.js and Python versions match requirements
- Review build logs for specific errors

---

## Monitoring

### Health Checks
- Backend: `https://your-backend-url/health`
- Database: Check connection in backend logs

### Logs
```bash
# Docker
docker-compose logs -f backend
docker-compose logs -f frontend

# Render
View logs in Render dashboard
```

---

## Scaling Considerations

- Use managed PostgreSQL (AWS RDS, Render PostgreSQL)
- Enable CDN for static assets
- Implement Redis for caching
- Use load balancers for high traffic
- Set up auto-scaling for backend instances

---

## Support

For issues, check:
- [GitHub Issues](https://github.com/Teck-123/petbloom-frontend/issues)
- Backend logs
- Frontend console errors
