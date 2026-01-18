#!/bin/bash
# PetBloom Quick Commands Reference

# ============================================================
# BACKEND COMMANDS
# ============================================================

# Start test server (for development/testing)
cd back-end && python test_server.py

# Test backend endpoints
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/products
curl http://localhost:8000/api/v1/pets

# Check backend logs
tail -f back-end/server.log

# Stop backend
pkill -f "python test_server.py"

# ============================================================
# FRONTEND COMMANDS
# ============================================================

# Install dependencies
npm install

# Start development server
npm run dev
# Opens at http://localhost:5173

# Build for production
npm run build
# Output in dist/ folder

# Preview production build
npm run preview

# ============================================================
# TESTING COMMANDS
# ============================================================

# Test API health
curl -s http://localhost:8000/health | jq .

# Test products endpoint
curl -s http://localhost:8000/api/v1/products | jq .

# Test with headers (CORS test)
curl -X GET http://localhost:8000/api/v1/health \
  -H "Origin: http://localhost:5173" \
  -H "Access-Control-Request-Method: GET" \
  -v

# Check environment variables
grep VITE_ .env
grep VITE_ .env.production

# Verify Firebase config loaded
curl -s http://localhost:8000/api/v1/health | jq .

# ============================================================
# GIT COMMANDS
# ============================================================

# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your message here"

# Push to GitHub (triggers Vercel auto-deploy)
git push

# View recent commits
git log --oneline -5

# ============================================================
# VERCEL COMMANDS
# ============================================================

# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy to production
vercel --prod --team=G7pAfOmi7diMewBtcWrdXuNx

# Deploy to preview
vercel --team=G7pAfOmi7diMewBtcWrdXuNx

# ============================================================
# DEBUGGING COMMANDS
# ============================================================

# Check Node version
node --version

# Check npm version
npm --version

# Check Python version
python --version

# List running Node processes
ps aux | grep node

# List running Python processes
ps aux | grep python

# Clear npm cache
npm cache clean --force

# Clear Vite cache
rm -rf node_modules/.vite

# Reinstall dependencies
rm package-lock.json
npm install

# ============================================================
# ENVIRONMENT VARIABLES
# ============================================================

# View local development environment
echo "=== Local Development (.env) ==="
cat .env

# View production environment  
echo "=== Production (.env.production) ==="
cat .env.production

# View local alternative environment
echo "=== Local Alternative (.env.local) ==="
cat .env.local

# ============================================================
# DIRECTORY STRUCTURE
# ============================================================

# View project structure
tree -L 2 -I 'node_modules'

# List important files
ls -la *.json *.md .env* vercel.json

# Check dist folder size
du -sh dist/

# ============================================================
# FIREBASE COMMANDS
# ============================================================

# View Firebase config in code
grep -r "apiKey\|projectId" src/services/firebase.js

# Check Firebase env variables
grep VITE_FIREBASE .env
grep VITE_FIREBASE .env.production

# ============================================================
# USEFUL ALIASES
# ============================================================

# Add to your ~/.bashrc or ~/.zshrc:

# alias petbloom-dev="cd /home/alex/My_Projects/petbloom-frontend && npm run dev"
# alias petbloom-build="cd /home/alex/My_Projects/petbloom-frontend && npm run build"
# alias petbloom-backend="cd /home/alex/My_Projects/petbloom-frontend/back-end && python test_server.py"
# alias petbloom-test="curl -s http://localhost:8000/health | jq ."
# alias petbloom-status="echo 'Backend:' && curl -s http://localhost:8000/health && echo && echo 'Frontend:' && curl -s http://localhost:5173/"

# ============================================================
# HEALTH CHECKS
# ============================================================

# Complete health check script
echo "🔍 PetBloom Health Check"
echo "========================"
echo ""
echo "Backend Status:"
curl -s http://localhost:8000/health | jq . || echo "❌ Backend not running"
echo ""
echo "Frontend Build:"
[ -d "dist" ] && echo "✅ Production build exists" || echo "❌ No production build"
echo ""
echo "Environment Files:"
[ -f ".env" ] && echo "✅ .env found" || echo "❌ .env missing"
[ -f ".env.production" ] && echo "✅ .env.production found" || echo "❌ .env.production missing"
echo ""
echo "Dependencies:"
npm list firebase 2>/dev/null | head -2 && echo "✅ Firebase installed" || echo "❌ Firebase missing"
echo ""

# ============================================================
# QUICK DEPLOYMENT
# ============================================================

# One-line deployment
git add . && git commit -m "Deploy" && git push && echo "✅ Pushed to GitHub - Vercel deploying..."

# Check Vercel deployment status
vercel --team=G7pAfOmi7diMewBtcWrdXuNx --list

# View Vercel logs
vercel logs petbloom-frontend --team=G7pAfOmi7diMewBtcWrdXuNx --follow

# ============================================================
# DATABASE / BACKEND
# ============================================================

# Check Railway backend status
curl -s https://YOUR_RAILWAY_BACKEND_URL/health | jq .

# View Railway logs
# Visit: https://railway.app/dashboard

# ============================================================
# USEFUL CURL COMMANDS
# ============================================================

# Test CORS
curl -i -X OPTIONS \
  -H "Origin: https://petbloom-frontend-five.vercel.app" \
  -H "Access-Control-Request-Method: GET" \
  http://localhost:8000/api/v1/health

# Send JSON
curl -X POST http://localhost:8000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com"}'

# With auth token
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/v1/users/profile

# ============================================================
# NOTE
# ============================================================

# This is a reference document. Copy individual commands to terminal.
# Do not run this entire file as a script.

# For more information, see:
# - DEPLOYMENT_CHECKLIST.md
# - TEST_REPORT.md
# - FIREBASE_RAILWAY_SETUP.md

echo "✅ Commands reference loaded!"
