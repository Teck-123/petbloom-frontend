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