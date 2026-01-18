# Backend-Frontend Integration Checklist

## COMPLETED

### Backend
- [x] All route files created and fixed
- [x] Prisma schema with all models
- [x] Database connected and migrated
- [x] CORS configured
- [x] Added species/breeds list endpoints
- [x] Added categories/brands list endpoints
- [x] Fixed cart/wishlist POST endpoints

### Frontend
- [x] All pages created
- [x] API service configured
- [x] React Query setup
- [x] Authentication context
- [x] Routing configured

## STILL NEEDED

### 1. Field Name Alignment
**Backend needs to change:**
- `eml` → `email` (in User model and all routes)
- `avlble` → `available` (in Pet model)
- `fbaseUid` → `firebaseUid` (in User model)

**OR Frontend needs to change to match backend**

### 2. Authentication Integration
- [ ] Backend: Implement proper Firebase token validation in routes
- [ ] Backend: Add authentication middleware
- [ ] Frontend: Get user ID from Firebase auth instead of hardcoding

### 3. Missing Backend Features
- [ ] Pagination metadata (return `{data: [], total: count}`)
- [ ] Search functionality in pets/products endpoints
- [ ] User registration endpoint needs to match frontend expectations
- [ ] File upload handling for pet/product images

### 4. Frontend Fixes Needed
- [ ] Update API calls to use correct field names
- [ ] Handle authentication properly (get userId from context)
- [ ] Fix cart/wishlist calls to not require userId in URL

### 5. Environment Variables
**Backend (.env):**
```
DATABASE_URL=postgresql://user:password@localhost:5432/petbloom
FBASE_CREDENTIALS=path/to/firebase-credentials.json
FRONTEND_URL=http://localhost:5173
```

**Frontend (.env):**
```
VITE_API_URL=http://localhost:8000/api/v1
VITE_FIREBASE_API_KEY=your-key
VITE_FIREBASE_AUTH_DOMAIN=your-domain
VITE_FIREBASE_PROJECT_ID=your-project-id
```

### 6. Testing Checklist
- [ ] User registration/login
- [ ] Browse pets with filters
- [ ] Browse products with filters
- [ ] Add to cart
- [ ] Add to wishlist
- [ ] Checkout process
- [ ] View orders
- [ ] Update profile

## Quick Fixes Priority

1. **HIGH**: Fix field names (eml, avlble, fbaseUid)
2. **HIGH**: Add authentication middleware
3. **MEDIUM**: Add pagination metadata
4. **MEDIUM**: Implement search functionality
5. **LOW**: Add image upload handling

## Estimated Time to Full Integration
- Field name fixes: 30 minutes
- Authentication: 2 hours
- Pagination/Search: 1 hour
- Testing: 2 hours

**Total: ~5-6 hours of work remaining**
