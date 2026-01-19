#!/bin/bash

# Seed Live Database Script
# Usage: chmod +x seed_live.sh && ./seed_live.sh

BACKEND_URL="https://petbloom-backend-production.up.railway.app"
ENDPOINT="/seed/init"

echo "🌐 Seeding Live Database"
echo "========================"
echo "Backend URL: $BACKEND_URL"
echo ""

# Check if backend is up
echo "⏳ Checking if backend is online..."
if ! curl -s -I "$BACKEND_URL" > /dev/null 2>&1; then
    echo "❌ Backend is not responding!"
    echo ""
    echo "Possible solutions:"
    echo "1. Check Railway dashboard - backend service might be crashing"
    echo "2. Wait a few minutes - Railway might be redeploying"
    echo "3. Check env variables - DATABASE_URL might be wrong"
    echo "4. View logs: https://railway.app/project/PROJECT_ID"
    exit 1
fi

echo "✅ Backend is online!"
echo ""

# Call seed endpoint
echo "🌱 Seeding database... this may take a minute..."
RESPONSE=$(curl -X POST "$BACKEND_URL$ENDPOINT" \
    -H "Content-Type: application/json" \
    -s)

# Parse response
if echo "$RESPONSE" | grep -q "successfully"; then
    echo "✅ SUCCESS!"
    echo ""
    echo "Response:"
    echo "$RESPONSE" | python3 -m json.tool
    echo ""
    echo "🎉 Database seeded! Your live website now has:"
    echo "  • 10 pets with images"
    echo "  • 17 products"
    echo "  • All in Kenyan Shillings (KES)"
    echo ""
    echo "Visit: https://petbloom-frontend-production.up.railway.app"
else
    echo "❌ Seeding failed!"
    echo ""
    echo "Response:"
    echo "$RESPONSE" | python3 -m json.tool
    echo ""
    echo "Troubleshooting:"
    echo "• Check that database is connected"
    echo "• View backend logs in Railway"
    echo "• Try again in a few minutes"
fi
