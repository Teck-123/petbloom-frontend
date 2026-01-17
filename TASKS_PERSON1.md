# Tasks for Person 1 - Component Documentation & Error Handling

## Your Job: Improve components with docs and error handling

### Step 1: Setup (Copy-paste these commands)
```bash
git clone https://github.com/Vanessa-Faith/petbloom-frontend.git
cd petbloom-frontend
npm install
git checkout dev
git pull origin dev
git checkout -b feature/component-improvements
```

### Step 2: Do These Tasks (Each is 1 commit)

#### Task A: Add comprehensive documentation to Header.jsx
Open `src/components/Header.jsx`

Add this at the **very top** (before the imports):
```javascript
/**
 * Header Component
 * 
 * Main navigation bar with responsive design
 * Features:
 * - Logo and brand name
 * - Navigation links (Home, Pets, Products, About, Contact)
 * - Search functionality
 * - User authentication menu (login/logout, cart, wishlist)
 * - Mobile responsive hamburger menu
 * 
 * @component
 */
```

Then run:
```bash
git add src/components/Header.jsx
git commit -m "Add comprehensive JSDoc documentation to Header component"
```

#### Task B: Add error boundary documentation to ProtectedRoute
Open `src/components/ProtectedRoute.jsx`

Add this at the **very top** (before the imports):
```javascript
/**
 * ProtectedRoute Component
 * 
 * Higher-order component that protects routes requiring authentication
 * - Redirects unauthenticated users to login page
 * - Shows loading spinner while checking auth status
 * - Renders children only for authenticated users
 * 
 * @component
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - Child components to protect
 */
```

Then run:
```bash
git add src/components/ProtectedRoute.jsx
git commit -m "Add JSDoc documentation to ProtectedRoute component"
```

#### Task C: Improve Footer with SEO meta description
Open `src/components/Footer.jsx`

Add this at the **very top** (before the imports):
```javascript
/**
 * Footer Component
 * 
 * Site-wide footer with company information and links
 * Features:
 * - Company description and social media links
 * - Quick navigation links
 * - Contact information (email, phone, address)
 * - Copyright and legal links (Privacy Policy, Terms)
 * 
 * @component
 */
```

Then run:
```bash
git add src/components/Footer.jsx
git commit -m "Add detailed JSDoc documentation to Footer component"
```

#### Task D: Create a COMPONENTS_README.md
Create new file `src/components/README.md` with this content:
```markdown
# Components Documentation

## Overview
This directory contains reusable React components used throughout the application.

## Components

### Header.jsx
Main navigation component with authentication menu and mobile responsiveness.

### Footer.jsx
Site-wide footer with company info, links, and contact details.

### ProtectedRoute.jsx
Authentication guard component for protected routes.

## Usage Example
\`\`\`javascript
import Header from './components/Header'
import Footer from './components/Footer'
import ProtectedRoute from './components/ProtectedRoute'

// Wrap protected pages
<ProtectedRoute>
  <ProfilePage />
</ProtectedRoute>
\`\`\`
```

Then run:
```bash
git add src/components/README.md
git commit -m "Add components documentation and usage guide"
```

### Step 3: Push to GitHub
```bash
git push origin feature/component-improvements
```

### Step 4: Create Pull Request
1. Go to https://github.com/Vanessa-Faith/petbloom-frontend
2. Click "Pull Requests" → "New Pull Request"
3. Set **base: dev** ← **compare: feature/component-improvements**
4. Title: "Add component documentation and improve code quality"
5. Description: "Added JSDoc documentation to all components and created components README"
6. Click "Create Pull Request"

✅ DONE! You now have 4 meaningful commits!
