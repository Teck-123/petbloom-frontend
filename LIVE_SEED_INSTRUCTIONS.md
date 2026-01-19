# 🚀 Seed Live Database - Complete Instructions

## ✅ Your Setup

- **Frontend:** https://petbloom-frontend-five.vercel.app (Live on Vercel)
- **Database:** Railway PostgreSQL (Live)
- **Backend:** Needs to be deployed to live URL

---

## 3-Step Process to Seed Live Database

### Step 1: Deploy Backend to Live

You can use **Railway** (same as your database) or **Render**:

#### Option A: Deploy to Railway (Recommended - Same service as DB)

1. Go to [Railway Dashboard](https://railway.app)
2. Create new service → Select GitHub repo
3. Connect your GitHub account
4. Select `petbloom-frontend` repository
5. Railway auto-detects `Dockerfile`
6. Set environment variables:
   ```
   DATABASE_URL = [auto-populated by Railway]
   JWT_SECRET = your-secret-key
   FRONTEND_URL = https://petbloom-frontend-five.vercel.app
   ```
7. Deploy! Railway generates your backend URL: `https://petbloom-backend-xxx.railway.app`

#### Option B: Deploy to Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. New → Web Service
3. Connect GitHub → select this repo
4. Settings:
   - Name: `petbloom-backend`
   - Runtime: `Python 3.8`
   - Build: `pip install -r requirements.txt`
   - Start: `python -m uvicorn app.main:app --host 0.0.0.0 --port 8000`
5. Set environment variables (same as above)
6. Deploy! You get URL: `https://petbloom-backend.onrender.com`

---

### Step 2: Update Frontend Config

Once backend is live, update frontend to use live API:

**File:** `src/services/api.js`

```javascript
// Before (localhost):
const API_URL = "http://localhost:8000";

// After (production):
const API_URL = "https://petbloom-backend-xxx.railway.app";
// OR
const API_URL = "https://petbloom-backend.onrender.com";
```

Then:
```bash
git add src/services/api.js
git commit -m "Update API URL to production backend"
git push origin main
```

Vercel auto-deploys and your frontend now talks to live backend.

---

### Step 3: Seed Live Database

Once backend is live, call the seed endpoint:

#### Method A: Using curl
```bash
curl -X POST https://petbloom-backend-xxx.railway.app/seed/init
# OR
curl -X POST https://petbloom-backend.onrender.com/seed/init
```

#### Method B: Using Python
```python
import requests

backend_url = "https://petbloom-backend-xxx.railway.app"  # Your live URL
response = requests.post(f"{backend_url}/seed/init")
print(response.json())

# Output:
# {
#   "message": "✅ Database seeded successfully!",
#   "pets": 10,
#   "products": 17,
#   "currency": "Kenyan Shillings (KES)"
# }
```

#### Method C: Visit in Browser
```
https://petbloom-backend-xxx.railway.app/docs
```
Then click "Try it out" on `/seed/init` endpoint.

---

## ✅ Verification

After seeding, check live website:

```bash
# Check pets on live site
curl https://petbloom-backend-xxx.railway.app/pets | jq 'length'
# Should return: 10

# Check products
curl https://petbloom-backend-xxx.railway.app/products | jq 'length'
# Should return: 17

# Visit live website
open https://petbloom-frontend-five.vercel.app
```

You should now see:
- ✅ 10 pets with images, prices in KES
- ✅ 17 products with descriptions
- ✅ Cart, wishlist, checkout all working
- ✅ Fully functional live website!

---

## 📊 What Gets Added

### Pets (10 total)
- 5 dogs: Max, Buddy, Rocky, Charlie, Duke
- 5 cats: Whiskers, Luna, Shadow, Mittens, Tiger

### Products (17 total)
- 3 Dog Foods
- 2 Cat Foods
- 3 Dog Toys
- 2 Cat Toys
- 2 Habitats
- 2 Accessories
- 2 Grooming items

All in **Kenyan Shillings (KES)** with realistic pricing!

---

## 🔧 Advanced Options

### Clear Database (if needed)
```bash
curl -X POST https://petbloom-backend-xxx.railway.app/seed/clear
```

### Check Seed Status (view logs)
```bash
# Railway: View logs in dashboard
# Render: View logs in Service page
```

---

## 🎯 After Everything is Live

1. ✅ Backend deployed and running
2. ✅ Frontend updated to use live backend API
3. ✅ Database seeded with data
4. ✅ Visit https://petbloom-frontend-five.vercel.app
5. ✅ Browse pets and products
6. ✅ Test full functionality (register, add cart, checkout)
7. ✅ Enjoy your live app! 🎉

---

## 📝 Troubleshooting

| Problem | Solution |
|---------|----------|
| 404 on seed endpoint | Backend not deployed yet - follow Step 1 |
| "Connection refused" | Check DATABASE_URL env var on backend |
| Empty pets/products | Seed endpoint was successful, check database |
| Images not loading | Unsplash URLs need internet (check CORS if needed) |
| Frontend still localhost | Update src/services/api.js with live backend URL |

---

## 💡 Quick Checklist

- [ ] Backend deployed to Railway or Render
- [ ] Get backend live URL
- [ ] Update `src/services/api.js` with live backend URL
- [ ] Push to GitHub (Vercel auto-deploys)
- [ ] Call `POST /seed/init` on live backend
- [ ] Verify on https://petbloom-frontend-five.vercel.app
- [ ] Test add to cart, wishlist, checkout

---

*Your live website will be fully functional with data in minutes!*
