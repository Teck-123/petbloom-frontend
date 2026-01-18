# Database Setup Instructions

## Current Status
 Prisma client generated with new field names
 Database needs credentials update

## To Complete Setup:

### Option 1: Update Database Credentials
Edit `/home/thecla/petbloom-frontend/back-end/.env`:
```
DATABASE_URL="postgresql://YOUR_USER:YOUR_PASSWORD@localhost:5432/petbloom"
```

Then run:
```bash
cd /home/thecla/petbloom-frontend
bash -c "export PATH=$PWD/back-end/venv/bin:$PATH && cd back-end && prisma db push"
```

### Option 2: Use Existing Database
If you already have a working database, just start the server:
```bash
cd /home/thecla/petbloom-frontend
bash -c "export PATH=$PWD/back-end/venv/bin:$PATH && cd back-end && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
```

## What's Fixed:
- Field names: email, available, firebaseUid
- Pagination endpoints
- Species/breeds/categories/brands list endpoints
- Cart/wishlist endpoints
- Prisma client regenerated

## Start Backend:
```bash
cd /home/thecla/petbloom-frontend
bash -c "export PATH=$PWD/back-end/venv/bin:$PATH && cd back-end && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
```
