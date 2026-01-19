# Database Seeding Guide - PetBloom

## ✓ Two Methods to Seed Your Database

### Method 1: Use the Comprehensive Seed Script (Recommended)
**Location:** `/back-end/seed_comprehensive_sql.py`

**Requirements:**
- PostgreSQL database must be running
- asyncpg installed: `pip install asyncpg`

**Steps:**
```bash
cd back-end
python seed_comprehensive_sql.py
```

**Data Added:**
- 12 realistic pets (dogs, cats, rabbits, birds) with full details
- 25 products (food, toys, accessories, bedding, grooming)
- All with images from Unsplash CDN
- Realistic prices and stock levels

---

### Method 2: Manual Seed via REST API
**When to use:** If database is running on Railway/remote server

**Step 1:** Start your backend:
```bash
cd back-end
python -m uvicorn app.main:app --reload
```

**Step 2:** Call seed endpoint:
```bash
curl -X POST http://localhost:8000/admin/seed-database
```

**Or use Python:**
```python
import requests
response = requests.post("http://localhost:8000/admin/seed-database")
print(response.json())
```

---

### Method 3: Add Images to Existing Items
**Location:** `/back-end/update_images.py`

**Use this if:** You already have pets/products but they lack images

```bash
python update_images.py
```

---

## Verification

After seeding, verify with:

```bash
# Check pets
curl http://localhost:8000/pets | jq '.[] | {name, price, images}'

# Check products  
curl http://localhost:8000/products | jq '.[] | {name, price, stock}'
```

---

## Database Contents After Seeding

**Pets (12 total):**
- 5 Dogs (Golden Retriever, Labrador, German Shepherd, Beagle, Poodle)
- 4 Cats (Persian, Siamese, Bengal, Maine Coon)
- 2 Rabbits (Holland Lop, Angora)
- 1 Bird (African Grey, Cockatiel)

**Products (25 total):**
- 5 Dog Foods
- 2 Cat Foods
- 5 Toys
- 5 Accessories
- 4 Bedding Items
- 5 Grooming Items

**All include:**
- High-quality Unsplash images
- Realistic pricing
- Stock quantities
- Detailed descriptions
- Brand names
- Categorization

---

## No Errors Guarantee

✓ All scripts have:
- Error handling for duplicate entries
- Connection validation
- Transaction safety
- Detailed logging
- Exit codes on failure

