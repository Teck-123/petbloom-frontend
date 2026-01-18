#!/bin/bash

# PostgreSQL Setup for PetBloom

echo "Setting up PostgreSQL database..."

# Create PostgreSQL user and database
# Run these commands manually:

echo "1. Create PostgreSQL user:"
echo "   sudo -u postgres createuser -s thecla"
echo ""
echo "2. Create database:"
echo "   createdb petbloom"
echo ""
echo "3. Then run prisma db push:"
echo "   cd /home/thecla/petbloom-frontend"
echo "   bash -c \"export PATH=\$PWD/back-end/venv/bin:\$PATH && cd back-end && prisma db push\""
