#!/bin/bash

# Backend-Frontend Integration Fix Script

echo "Applying backend fixes..."

cd /home/thecla/petbloom-frontend

# Regenerate Prisma client
echo "Regenerating Prisma client..."
export PATH=$PWD/venv/bin:$PATH
cd back-end
prisma generate

# Push database changes
echo "Updating database schema..."
prisma db push

echo "All fixes applied!"
echo ""
echo "To start the backend server:"
echo "cd /home/thecla/petbloom-frontend"
echo "bash -c \"export PATH=\$PWD/venv/bin:\$PATH && cd back-end && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000\""
