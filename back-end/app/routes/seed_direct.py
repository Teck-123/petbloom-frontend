"""
Simple SQL-based seed endpoint for Railway deployment
Add this to your routes and it will work even if Prisma has issues
"""

from fastapi import APIRouter, HTTPException
import os
import asyncpg

router = APIRouter(prefix="/seed-direct", tags=["seed"])

PETS_DATA = [
    ("Max", "dogs", "Golden Retriever", 2, 30.0, "Friendly and energetic golden retriever with beautiful cream coat. Perfect for active families. Fully vaccinated and dewormed.", ["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400", "https://images.unsplash.com/photo-1558788353-f76d92427f16?w=400"], ["friendly", "energetic", "loyal"], "Golden Dreams Kennel", 4.8, 95000.00, True),
    ("Buddy", "dogs", "Labrador Retriever", 3, 35.0, "Playful chocolate Labrador with excellent temperament. Great with children and other pets. Trained basic commands.", ["https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400", "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400"], ["playful", "loyal", "intelligent"], "Happy Paws", 4.7, 85000.00, True),
    ("Rocky", "dogs", "German Shepherd", 1, 28.0, "Strong and intelligent German Shepherd. Alert and protective family guardian. Excellent bloodline, trained for obedience.", ["https://images.unsplash.com/photo-1568572933382-74d440641117?w=400", "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400"], ["intelligent", "protective", "loyal"], "Shepherd Elite", 4.9, 110000.00, True),
    ("Charlie", "dogs", "Beagle", 2, 12.0, "Small but mighty Beagle with excellent hunting instincts. Friendly and curious personality. Great for apartment living.", ["https://images.unsplash.com/photo-1505628346881-b72b27e84530?w=400"], ["friendly", "curious", "energetic"], "Beagle House", 4.6, 65000.00, True),
    ("Duke", "dogs", "Rottweiler", 4, 50.0, "Magnificent Rottweiler with calm temperament. Despite reputation, very affectionate and family-oriented. Well-trained.", ["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400"], ["calm", "loyal", "protective"], "Noble Rotts", 4.8, 120000.00, True),
    ("Whiskers", "cats", "Persian", 1, 4.5, "Elegant and refined Persian cat with luxurious long coat. Calm and affectionate. Requires regular grooming.", ["https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?w=400", "https://images.unsplash.com/photo-1606214174585-fe31582dc1d7?w=400"], ["calm", "affectionate", "elegant"], "Purrfect Cats", 4.9, 55000.00, True),
    ("Luna", "cats", "Siamese", 2, 3.2, "Beautiful Siamese with striking blue eyes. Vocal and interactive. Loves attention and playtime.", ["https://images.unsplash.com/photo-1513360371669-4a8e1949883e?w=400", "https://images.unsplash.com/photo-1606214174585-fe31582dc1d7?w=400"], ["vocal", "playful", "affectionate"], "Siamese Dreams", 4.8, 48000.00, True),
    ("Shadow", "cats", "Black Domestic Shorthair", 3, 4.0, "Sleek black cat with golden eyes. Independent but loving. Perfect for quiet homes. Excellent mouser.", ["https://images.unsplash.com/photo-1570158108855-a920fb1b81d9?w=400"], ["independent", "loving", "intelligent"], "Shadow's Sanctuary", 4.7, 35000.00, True),
    ("Mittens", "cats", "British Shorthair", 2, 5.5, "Plump and cuddly British Shorthair with grey coat. Very calm and sociable. Great family pet.", ["https://images.unsplash.com/photo-1567517381829-ba595fac2ec0?w=400"], ["calm", "sociable", "cuddly"], "British Beauties", 4.9, 52000.00, True),
    ("Tiger", "cats", "Orange Tabby", 1, 3.8, "Energetic and playful orange tabby. Full of personality and mischief. Loves interactive toys.", ["https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400"], ["playful", "energetic", "mischievous"], "Tabby House", 4.6, 40000.00, True),
]

PRODUCTS_DATA = [
    ("Premium Adult Dog Food", "High-quality dry dog food with balanced nutrition. Rich in protein and essential vitamins. Suitable for all dog breeds.", "food", "dogs", "PetPro", 3500.00, ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"], 50, ["adult", "nutritious"]),
    ("Grain-Free Puppy Food", "Specially formulated for puppies. No grains, rich in DHA for brain development. Supports healthy growth.", "food", "dogs", "NutriPaws", 4200.00, ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"], 35, ["puppy", "grain-free"]),
    ("Senior Dog Food", "Low-calorie formula for senior dogs. Easy to digest with joint support ingredients.", "food", "dogs", "GoldenYears", 3800.00, ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"], 25, ["senior", "low-calorie"]),
    ("Premium Cat Food - Salmon", "Delicious salmon flavor cat food. Complete nutrition for adult cats. Promotes healthy coat.", "food", "cats", "FelineFresh", 2800.00, ["https://images.unsplash.com/photo-1537462715957-923ec97dd6f0?w=400"], 40, ["salmon", "adult"]),
    ("Kitten Growth Formula", "Specially designed for kittens aged 2-12 months. High protein for development.", "food", "cats", "KittyStart", 3200.00, ["https://images.unsplash.com/photo-1537462715957-923ec97dd6f0?w=400"], 30, ["kitten", "growth"]),
    ("Interactive Dog Toy Set", "Set of 5 interactive toys to keep dogs entertained. Includes balls, ropes, and chew toys.", "toys", "dogs", "PlayPets", 2200.00, ["https://images.unsplash.com/photo-1591769225440-811ad7d6eab3?w=400"], 45, ["interactive", "durable"]),
    ("Durable Rope Tug Toy", "Strong rope toy for aggressive chewers. Great for multi-dog families. Machine washable.", "toys", "dogs", "ChewMaster", 1500.00, ["https://images.unsplash.com/photo-1535241749838-299277b6305f?w=400"], 50, ["rope", "durable"]),
    ("Dog Puzzle Feeder", "Keep your dog mentally stimulated. Improves problem-solving skills during feeding time.", "toys", "dogs", "BrainPlay", 2800.00, ["https://images.unsplash.com/photo-1570158108855-a920fb1b81d9?w=400"], 20, ["puzzle", "mental-stimulation"]),
    ("Feather Wand Cat Toy", "Interactive feather wand toy. Stimulates hunting instincts. Great for exercise.", "toys", "cats", "CatPlay", 800.00, ["https://images.unsplash.com/photo-1559163499-64dd58e07650?w=400"], 60, ["interactive", "feather"]),
    ("Cat Laser Toy", "Safe laser toy for cats. Promotes exercise and play. Includes auto-timer feature.", "toys", "cats", "LaserFun", 1200.00, ["https://images.unsplash.com/photo-1559163499-64dd58e07650?w=400"], 30, ["laser", "interactive"]),
    ("Deluxe Cat Bed", "Soft and comfortable cat bed. Machine washable cover. Cozy cave design.", "habitats", "cats", "CatsLounge", 4500.00, ["https://images.unsplash.com/photo-1577023311546-cdc07a8454d9?w=400"], 25, ["comfortable", "cave"]),
    ("Multi-Level Cat Tree", "5-level cat tree with scratching posts. Provides climbing and resting areas. Sturdy construction.", "habitats", "cats", "CatsLounge", 12000.00, ["https://images.unsplash.com/photo-1521568547814-0a0a0d8a2d3a?w=400"], 10, ["climbing", "scratching-posts"]),
    ("Premium Dog Collar with Leash", "Adjustable leather collar with matching leash. Comfortable and durable. Multiple sizes.", "accessories", "dogs", "SafeGuard", 2500.00, ["https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f0?w=400"], 35, ["leather", "adjustable"]),
    ("Cat Harness and Leash Set", "Lightweight and safe harness for cats. Perfect for outdoor walks. Escape-proof design.", "accessories", "cats", "SafeGuard", 1800.00, ["https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f0?w=400"], 20, ["lightweight", "safe"]),
    ("Professional Dog Grooming Kit", "Complete grooming set including clippers, scissors, and brush. Suitable for all coat types.", "grooming", "dogs", "GroomPro", 5500.00, ["https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400"], 15, ["professional", "complete"]),
    ("Cat Grooming Brush", "Gentle de-matting brush for cats. Reduces shedding. Comfortable grip handle.", "grooming", "cats", "GroomPro", 1500.00, ["https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400"], 40, ["gentle", "de-matting"]),
]

@router.post("/sql")
async def seed_database_direct():
    """Seed database using direct SQL - bypasses Prisma"""
    try:
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise HTTPException(status_code=500, detail="DATABASE_URL not set")
        
        # Connect directly
        conn = await asyncpg.connect(db_url)
        
        # Seed pets
        pets_created = 0
        for pet in PETS_DATA:
            try:
                await conn.execute(
                    """INSERT INTO "Pet" (name, species, breed, age, weight, description, images, personality, "breederName", "breederRating", price, available, "createdAt", "updatedAt")
                       VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, NOW(), NOW())
                       ON CONFLICT (name) DO NOTHING""",
                    *pet
                )
                pets_created += 1
            except Exception as e:
                print(f"Pet error: {e}")
        
        # Seed products
        products_created = 0
        for product in PRODUCTS_DATA:
            try:
                await conn.execute(
                    """INSERT INTO "Product" (name, description, category, "petType", brand, price, images, stock, filters, "createdAt", "updatedAt")
                       VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, NOW(), NOW())
                       ON CONFLICT (name) DO NOTHING""",
                    *product
                )
                products_created += 1
            except Exception as e:
                print(f"Product error: {e}")
        
        await conn.close()
        
        return {
            "status": "success",
            "message": "✅ Database seeded successfully!",
            "pets_created": pets_created,
            "products_created": products_created,
            "total": pets_created + products_created
        }
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Seed failed: {str(e)}")
