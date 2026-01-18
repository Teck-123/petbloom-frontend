# PetBloom

A full-stack pet adoption and pet supplies e-commerce platform.

## Features

- Browse pets from verified breeders and shelters
- Shop for pet supplies and accessories
- User authentication with Firebase
- Shopping cart and wishlist
- Order management and tracking
- Responsive design with Tailwind CSS

## Tech Stack

### Frontend
- React 18
- React Router v6
- TanStack Query (React Query)
- Tailwind CSS
- Firebase Authentication
- Axios

### Backend
- FastAPI (Python)
- Prisma ORM
- PostgreSQL
- Firebase Admin SDK
- Uvicorn

## Prerequisites

- Node.js 16+
- Python 3.12+
- PostgreSQL
- Firebase account

## Installation

### 1. Clone Repository

git clone https://github.com/Teck-123/petbloom-frontend.git
cd petbloom-frontend

### 2. Backend Setup

# Create PostgreSQL user and database
sudo -u postgres createuser -s thecla
createdb petbloom

# Install Python dependencies
cd back-end
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your database credentials

# Generate Prisma client and migrate database
export PATH=$PWD/venv/bin:$PATH
prisma generate
prisma db push

# Seed database with sample data (optional)
python seed.py

### 3. Frontend Setup

# Install dependencies
npm install

# Configure environment variables
cp .env.example .env
# Add your Firebase credentials to .env

### 4. Firebase Configuration

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Create a new project
3. Enable Authentication > Email/Password
4. Get your Firebase config from Project Settings
5. Add credentials to frontend `.env` file

## Running the Application

### Start Backend

cd back-end
export PATH=$PWD/venv/bin:$PATH
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Backend runs on: http://localhost:8000

### Start Frontend

npm run dev

Frontend runs on: http://localhost:5173

## API Documentation

Once backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

petbloom-frontend/
├── back-end/
│   ├── app/
│   │   ├── routes/          # API endpoints
│   │   ├── schemas/         # Pydantic models
│   │   ├── services/        # Business logic
│   │   ├── config.py        # Configuration
│   │   └── main.py          # FastAPI app
│   ├── prisma/
│   │   └── schema.prisma    # Database schema
│   └── seed.py              # Database seeder
├── src/
│   ├── components/          # React components
│   ├── contexts/            # React contexts
│   ├── pages/               # Page components
│   ├── services/            # API & Firebase
│   └── App.jsx              # Main app component
└── public/                  # Static assets

## Environment Variables

### Backend (.env)
DATABASE_URL=postgresql://user:password@localhost:5432/petbloom
FBASE_CREDENTIALS=path/to/firebase-credentials.json
JWT_SECRET=your-secret-key
FRONTEND_URL=http://localhost:5173

### Frontend (.env)
VITE_API_URL=http://localhost:8000/api/v1
VITE_FIREBASE_API_KEY=your-api-key
VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your-project-id
VITE_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
VITE_FIREBASE_APP_ID=your-app-id

## Available Scripts

### Frontend
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

### Backend
- `uvicorn app.main:app --reload` - Start development server
- `prisma generate` - Generate Prisma client
- `prisma db push` - Push schema to database
- `python seed.py` - Seed database

## Features Overview

### User Features
- User registration and login
- Browse pets by species, breed, and price
- Browse products by category and brand
- Add items to cart
- Add items to wishlist
- Place orders with delivery options
- Track order status

### Admin Features (Coming Soon)
- Add/edit/delete pets
- Add/edit/delete products
- Manage orders
- View analytics

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Contact

Project Link: https://github.com/Teck-123/petbloom-frontend
