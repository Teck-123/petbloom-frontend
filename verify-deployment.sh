#!/bin/bash

# PetBloom Firebase & Backend Communication Verification Script
# Run this script to verify your setup is correct

echo "🔍 PetBloom Deployment Verification"
echo "===================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check local environment files
echo "📁 Checking local environment files..."
if [ -f ".env.production" ]; then
    echo -e "${GREEN}✓ .env.production exists${NC}"
else
    echo -e "${RED}✗ .env.production missing${NC}"
fi

if [ -f ".env.local" ]; then
    echo -e "${GREEN}✓ .env.local exists${NC}"
else
    echo -e "${RED}✗ .env.local missing${NC}"
fi

echo ""
echo "🔐 Checking Firebase Configuration..."
echo "Current VITE_FIREBASE_PROJECT_ID: $(grep VITE_FIREBASE_PROJECT_ID .env | cut -d'=' -f2)"
if grep -q "VITE_FIREBASE_API_KEY=AIzaSyD8hxlXo7mjuM1e7Yg_DCCRLrIyrhW7TRA" .env; then
    echo -e "${GREEN}✓ Firebase API Key configured${NC}"
else
    echo -e "${RED}✗ Firebase API Key incorrect${NC}"
fi

echo ""
echo "🔌 Checking API Configuration..."
API_URL=$(grep "^VITE_API_URL=" .env | cut -d'=' -f2)
echo "API URL: $API_URL"

if [[ "$API_URL" == *"petbloom-frontend-production"* ]]; then
    echo -e "${RED}✗ ERROR: API URL points to frontend, not backend!${NC}"
    echo "   Should be: https://YOUR_RAILWAY_BACKEND_URL/api/v1"
elif [[ "$API_URL" == "http://localhost:8000/api/v1" ]]; then
    echo -e "${GREEN}✓ Correct local API URL${NC}"
elif [[ "$API_URL" == *"railway.app"* ]]; then
    echo -e "${GREEN}✓ Production API URL set (Railway backend)${NC}"
fi

echo ""
echo "📋 Configuration Summary"
echo "======================="
echo ""
echo "Local Development (.env):"
echo "  VITE_API_URL = $(grep '^VITE_API_URL=' .env | cut -d'=' -f2)"
echo ""
echo "Production (.env.production):"
echo "  VITE_API_URL = $(grep '^VITE_API_URL=' .env.production | cut -d'=' -f2)"
echo ""

echo "⚠️  Next Steps:"
echo "1. Get your Railway backend URL from: https://railway.app/dashboard"
echo "2. Update VITE_API_URL in .env.production with the correct URL"
echo "3. Set environment variables in Vercel Project Settings:"
echo "   - All VITE_FIREBASE_* variables"
echo "   - VITE_API_URL (with correct Railway backend)"
echo "4. Deploy with: git push (or redeploy from Vercel dashboard)"
echo ""
echo "✅ Test after deployment:"
echo "   - Open browser DevTools (F12)"
echo "   - Check Console for Firebase errors"
echo "   - Check Network tab for API calls"
echo "   - Should see requests to your Railway backend"
