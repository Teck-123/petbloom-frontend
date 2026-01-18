# Database Seeding Guide - PetBloom

## Quick Start - Seed the Database

### For Vercel/Railway Deployment
Make a POST request to your deployed backend:

```bash
curl -X POST https://petbloom-frontend-production.up.railway.app/api/v1/seed/init
```

Or using JavaScript/Axios in your frontend:
```javascript
import axios from 'axios';

async function seedDatabase() {
  try {
    const response = await axios.post(
      'https://petbloom-frontend-production.up.railway.app/api/v1/seed/init'
    );
    console.log('Database seeded:', response.data);
  } catch (error) {
    console.error('Seeding error:', error.response?.data || error.message);
  }
}
```

### For Local Development
Make a POST request to your local backend:

```bash
curl -X POST http://localhost:8000/api/v1/seed/init
```

## What Gets Seeded

The database will be populated with:

### 🐕 **10 Pets (5 Dogs + 5 Cats)**
All prices in **Kenyan Shillings (KES)**

**Dogs:**
- Max (Golden Retriever) - KES 95,000
- Buddy (Labrador Retriever) - KES 85,000
- Rocky (German Shepherd) - KES 110,000
- Charlie (Beagle) - KES 65,000
- Duke (Rottweiler) - KES 120,000

**Cats:**
- Whiskers (Persian) - KES 55,000
- Luna (Siamese) - KES 48,000
- Shadow (Black Domestic Shorthair) - KES 35,000
- Mittens (British Shorthair) - KES 52,000
- Tiger (Orange Tabby) - KES 40,000

### 📦 **16 Products (in KES)**

**Food (5 items):**
- Premium Adult Dog Food - KES 3,500
- Grain-Free Puppy Food - KES 4,200
- Senior Dog Food - KES 3,800
- Premium Cat Food - Salmon - KES 2,800
- Kitten Growth Formula - KES 3,200

**Toys (5 items):**
- Interactive Dog Toy Set - KES 2,200
- Durable Rope Tug Toy - KES 1,500
- Dog Puzzle Feeder - KES 2,800
- Feather Wand Cat Toy - KES 800
- Cat Laser Toy - KES 1,200

**Habitats (2 items):**
- Deluxe Cat Bed - KES 4,500
- Multi-Level Cat Tree - KES 12,000

**Accessories (2 items):**
- Premium Dog Collar with Leash - KES 2,500
- Cat Harness and Leash Set - KES 1,800

**Grooming (2 items):**
- Professional Dog Grooming Kit - KES 5,500
- Cat Grooming Brush - KES 1,500

### ⭐ **Reviews**
- 7+ product reviews with ratings and comments
- 7+ pet reviews with ratings and comments
- All reflecting Kenyan Shilling pricing

## Important Notes

1. **One-Time Seed**: The endpoint will NOT reseed if data already exists
2. **No Blank Details**: Every pet and product has:
   - Detailed description (not blank)
   - High-quality images (real URLs from Unsplash)
   - Comprehensive information
   - Customer reviews

3. **All Currencies in KES**: All prices are in Kenyan Shillings for real market pricing

4. **Test Data**: All data is properly formatted and linked (reviews → products/pets)

## Clear Database (Optional)

To clear all data and start fresh:

```bash
curl -X POST http://localhost:8000/api/v1/seed/clear
```

## Verify the Data

After seeding, you can check:

**Get all pets:**
```bash
curl http://localhost:8000/api/v1/pets
```

**Get all products:**
```bash
curl http://localhost:8000/api/v1/products
```

**Get reviews for a product:**
```bash
curl http://localhost:8000/api/v1/reviews?productId=<product_id>
```

## Frontend Integration

You can trigger the seed from your frontend admin panel or dashboard:

```javascript
async function setupDatabase() {
  try {
    const apiUrl = process.env.VITE_API_URL || 'http://localhost:8000/api/v1';
    const response = await fetch(`${apiUrl}/seed/init`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    });
    
    if (response.ok) {
      const data = await response.json();
      console.log('✅ Database seeded!');
      console.log(`📊 Created ${data.pets} pets and ${data.products} products`);
      // Redirect or refresh data
      window.location.reload();
    }
  } catch (error) {
    console.error('❌ Seeding failed:', error);
  }
}
```

## Database Structure

The seed creates:
- **Pets table**: Complete pet listings with breeder info and ratings
- **Products table**: Categorized products (food, toys, habitats, accessories, grooming)
- **Reviews table**: Linked to both pets and products
- **Messages table**: User communication samples
- **UserAddress table**: Sample shipping addresses

All with proper foreign key relationships and constraints.

---

**Last Updated**: January 19, 2026
**Status**: ✅ Ready for Production
