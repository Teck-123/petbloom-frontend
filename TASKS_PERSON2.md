# Tasks for Person 2 - Services Documentation & README

## Your Job: Document services and improve project documentation

### Step 1: Setup (Copy-paste these commands)
```bash
git clone https://github.com/Vanessa-Faith/petbloom-frontend.git
cd petbloom-frontend
npm install
git checkout dev
git pull origin dev
git checkout -b feature/services-documentation
```

### Step 2: Do These Tasks (Each is 1 commit)

#### Task A: Document API service with detailed JSDoc
Open `src/services/api.js`

Add this at the **very top** (before the imports):
```javascript
/**
 * API Service Module
 * 
 * Axios instance configured with:
 * - Base URL pointing to backend API
 * - Request interceptor for JWT token authentication
 * - Response interceptor for handling 401 errors
 * 
 * All API calls should use this instance to ensure
 * authentication headers are automatically included
 * 
 * @module api
 */
```

Then run:
```bash
git add src/services/api.js
git commit -m "Add comprehensive documentation to API service module"
```

#### Task B: Document Firebase service
Open `src/services/firebase.js`

Add this at the **very top** (before the imports):
```javascript
/**
 * Firebase Service Module
 * 
 * Initializes Firebase app with configuration from environment variables
 * Exports initialized instances of:
 * - auth: Firebase Authentication
 * - db: Firestore Database
 * - storage: Firebase Storage
 * 
 * Configuration is loaded from .env file (VITE_FIREBASE_* variables)
 * 
 * @module firebase
 */
```

Then run:
```bash
git add src/services/firebase.js
git commit -m "Add detailed documentation to Firebase service module"
```

#### Task C: Create comprehensive project README
Replace entire `README.md` content with:
```markdown
# 🐾 PetBloom Frontend

A modern React-based frontend for the PetBloom pet marketplace application.

## 📋 Features

- 🔐 **User Authentication** - Firebase authentication with email/password and Google sign-in
- 🐕 **Pet Marketplace** - Browse, search, and view detailed information about available pets
- 🛍️ **Product Catalog** - Shop for pet supplies, food, toys, and accessories
- 🛒 **Shopping Cart** - Add items to cart and proceed to checkout
- ❤️ **Wishlist** - Save favorite pets and products for later
- 📦 **Order Management** - Track order history and status
- 👤 **User Profile** - Manage account information and preferences
- 📱 **Responsive Design** - Optimized for desktop, tablet, and mobile devices

## 🛠️ Tech Stack

- **React 18** - Modern React with hooks
- **Vite** - Fast build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router v6** - Client-side routing
- **Firebase** - Authentication and user management
- **Axios** - HTTP client for API requests
- **React Hook Form** - Form validation and handling
- **Lucide React** - Beautiful icon library

## 🚀 Getting Started

### Prerequisites
- Node.js 16+ and npm
- Firebase account (for authentication)
- Backend API running (optional for development)

### Installation

1. **Clone the repository**
\`\`\`bash
git clone https://github.com/Vanessa-Faith/petbloom-frontend.git
cd petbloom-frontend
\`\`\`

2. **Install dependencies**
\`\`\`bash
npm install
\`\`\`

3. **Set up environment variables**
\`\`\`bash
cp .env.example .env
\`\`\`

Edit `.env` and add your Firebase configuration:
\`\`\`env
VITE_FIREBASE_API_KEY=your-api-key
VITE_FIREBASE_AUTH_DOMAIN=your-auth-domain
VITE_FIREBASE_PROJECT_ID=your-project-id
VITE_FIREBASE_STORAGE_BUCKET=your-storage-bucket
VITE_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
VITE_FIREBASE_APP_ID=your-app-id
VITE_FIREBASE_MEASUREMENT_ID=your-measurement-id
VITE_API_URL=http://localhost:8000/api/v1
\`\`\`

4. **Run the development server**
\`\`\`bash
npm run dev
\`\`\`

5. **Open your browser**
Navigate to [http://localhost:3000](http://localhost:3000)

## 📁 Project Structure

\`\`\`
src/
├── components/       # Reusable UI components
│   ├── Header.jsx
│   ├── Footer.jsx
│   └── ProtectedRoute.jsx
├── contexts/         # React Context providers
│   └── AuthContext.jsx
├── pages/            # Page components
│   ├── Home.jsx
│   ├── Login.jsx
│   ├── Register.jsx
│   ├── Pets.jsx
│   ├── Products.jsx
│   ├── Cart.jsx
│   └── ...
├── services/         # API and external services
│   ├── api.js
│   └── firebase.js
├── App.jsx           # Main app component with routing
├── main.jsx          # Application entry point
└── index.css         # Global styles
\`\`\`

## 🧪 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## 👥 Team

Built by the PetBloom development team.

## 📄 License

This project is part of a group academic assignment.
```

Then run:
```bash
git add README.md
git commit -m "Create comprehensive project README with setup and documentation"
```

#### Task D: Create SERVICES_README.md
Create new file `src/services/README.md` with:
```markdown
# Services Documentation

## Overview
This directory contains service modules for external integrations and API communication.

## Services

### api.js
Configured Axios instance for backend API communication.

**Features:**
- Automatic JWT token inclusion in requests
- Base URL configuration
- 401 error handling with automatic redirect to login

**Usage:**
\`\`\`javascript
import api from '../services/api'

// GET request
const response = await api.get('/pets')

// POST request
const response = await api.post('/auth/login', { email, password })
\`\`\`

### firebase.js
Firebase initialization and configuration.

**Exports:**
- `auth` - Firebase Authentication instance
- `db` - Firestore Database instance
- `storage` - Firebase Storage instance
- `app` - Main Firebase app instance

**Usage:**
\`\`\`javascript
import { auth } from '../services/firebase'
import { signInWithEmailAndPassword } from 'firebase/auth'

await signInWithEmailAndPassword(auth, email, password)
\`\`\`

## Environment Variables

All services use environment variables from `.env`:
- Firebase: `VITE_FIREBASE_*`
- API: `VITE_API_URL`
```

Then run:
```bash
git add src/services/README.md
git commit -m "Add services documentation with usage examples"
```

### Step 3: Push to GitHub
```bash
git push origin feature/services-documentation
```

### Step 4: Create Pull Request
1. Go to https://github.com/Vanessa-Faith/petbloom-frontend
2. Click "Pull Requests" → "New Pull Request"
3. Set **base: dev** ← **compare: feature/services-documentation**
4. Title: "Add comprehensive documentation for services and project"
5. Description: "Added JSDoc to services, created detailed README, and documented project structure"
6. Click "Create Pull Request"

✅ DONE! You now have 4 meaningful commits!
