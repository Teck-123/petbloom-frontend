#!/usr/bin/env python3
"""
Comprehensive seed data script for PetBloom database
Uses direct SQL to avoid Prisma import issues
"""

import asyncpg
import asyncio
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database connection string
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/petbloom")

# Image URLs organized by category
PET_IMAGES = {
    "dog": [
        "https://images.unsplash.com/photo-1633722715463-d30628cqsw8d?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1633722641147-8f835f7a1e08?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1633722854212-cfe1a70f92ef?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1633722716993-d42ddaa0001e?w=600&h=600&fit=crop",
    ],
    "cat": [
        "https://images.unsplash.com/photo-1574158622682-e40e69881006?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1574144611937-0df059b5ef3e?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1573865526014-f3550b1ade60?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1574158622682-e40e69881006?w=600&h=600&fit=crop",
    ],
    "rabbit": [
        "https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f4?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f4?w=600&h=600&fit=crop",
    ],
    "bird": [
        "https://images.unsplash.com/photo-1444464666175-1642a3a3b1ef?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1444464666175-1642a3a3b1ef?w=600&h=600&fit=crop",
    ]
}

PRODUCT_IMAGES = {
    "dog_food": [
        "https://images.unsplash.com/photo-1589941013453-ec89f33b5e95?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1555684586-46f694365df1?w=600&h=600&fit=crop",
    ],
    "cat_food": [
        "https://images.unsplash.com/photo-1589941013453-ec89f33b5e95?w=600&h=600&fit=crop",
    ],
    "toys": [
        "https://images.unsplash.com/photo-1535241749838-299277b6305f?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1633722715463-d30628cqsw8d?w=600&h=600&fit=crop",
    ],
    "accessories": [
        "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=600&h=600&fit=crop",
        "https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?w=600&h=600&fit=crop",
    ],
    "bedding": [
        "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=600&h=600&fit=crop",
    ],
    "grooming": [
        "https://images.unsplash.com/photo-1625938363236-19dcd028fcfe?w=600&h=600&fit=crop",
    ]
}

# Comprehensive pet data
PETS_DATA = [
    # Dogs
    {
        "name": "Golden Retriever - Sunny",
        "species": "dog",
        "breed": "Golden Retriever",
        "age": 2,
        "weight": 32.5,
        "description": "Beautiful golden coat, friendly and energetic. Perfect family companion.",
        "personality": ["friendly", "energetic", "loyal", "intelligent"],
        "breederName": "Golden Dreams Kennel",
        "breederRating": 4.8,
        "price": 1200.00,
        "available": True,
        "images": PET_IMAGES["dog"][:3]
    },
    {
        "name": "Labrador - Max",
        "species": "dog",
        "breed": "Labrador Retriever",
        "age": 1,
        "weight": 30.0,
        "description": "Chocolate colored lab, excellent with kids and other pets.",
        "personality": ["friendly", "loyal", "playful", "intelligent"],
        "breederName": "Labrador Lovers",
        "breederRating": 4.9,
        "price": 1100.00,
        "available": True,
        "images": PET_IMAGES["dog"][:3]
    },
    {
        "name": "German Shepherd - King",
        "species": "dog",
        "breed": "German Shepherd",
        "age": 3,
        "weight": 35.0,
        "description": "Strong and protective, highly trainable and intelligent.",
        "personality": ["protective", "intelligent", "loyal", "confident"],
        "breederName": "Royal Guard Kennels",
        "breederRating": 4.7,
        "price": 1500.00,
        "available": True,
        "images": PET_IMAGES["dog"]
    },
    {
        "name": "Beagle - Charlie",
        "species": "dog",
        "breed": "Beagle",
        "age": 1,
        "weight": 12.0,
        "description": "Small, playful beagle with excellent hunting instincts.",
        "personality": ["playful", "curious", "friendly", "energetic"],
        "breederName": "Beagle Buddies",
        "breederRating": 4.6,
        "price": 800.00,
        "available": True,
        "images": PET_IMAGES["dog"][:2]
    },
    {
        "name": "Poodle - Princess",
        "species": "dog",
        "breed": "Standard Poodle",
        "age": 2,
        "weight": 25.0,
        "description": "Intelligent and elegant, hypoallergenic coat. Perfect apartment dog.",
        "personality": ["intelligent", "elegant", "friendly", "obedient"],
        "breederName": "Poodle Palace",
        "breederRating": 4.8,
        "price": 1400.00,
        "available": True,
        "images": PET_IMAGES["dog"]
    },
    # Cats
    {
        "name": "Persian - Luna",
        "species": "cat",
        "breed": "Persian",
        "age": 2,
        "weight": 4.5,
        "description": "Beautiful long-haired Persian with calm temperament.",
        "personality": ["calm", "affectionate", "quiet", "gentle"],
        "breederName": "Persian Perfection",
        "breederRating": 4.9,
        "price": 800.00,
        "available": True,
        "images": PET_IMAGES["cat"][:3]
    },
    {
        "name": "Siamese - Milo",
        "species": "cat",
        "breed": "Siamese",
        "age": 1,
        "weight": 3.5,
        "description": "Vocal and social Siamese cat, loves human interaction.",
        "personality": ["social", "vocal", "affectionate", "intelligent"],
        "breederName": "Siamese Serenity",
        "breederRating": 4.7,
        "price": 600.00,
        "available": True,
        "images": PET_IMAGES["cat"]
    },
    {
        "name": "Bengal - Tiger",
        "species": "cat",
        "breed": "Bengal",
        "age": 2,
        "weight": 5.0,
        "description": "Exotic spotted coat, highly active and playful.",
        "personality": ["active", "playful", "intelligent", "loyal"],
        "breederName": "Bengal Beauties",
        "breederRating": 4.8,
        "price": 1200.00,
        "available": True,
        "images": PET_IMAGES["cat"][:2]
    },
    {
        "name": "Maine Coon - Zeus",
        "species": "cat",
        "breed": "Maine Coon",
        "age": 3,
        "weight": 7.0,
        "description": "Large gentle giant, friendly and sociable.",
        "personality": ["gentle", "friendly", "intelligent", "playful"],
        "breederName": "Coon Castle",
        "breederRating": 4.9,
        "price": 900.00,
        "available": True,
        "images": PET_IMAGES["cat"]
    },
    # Rabbits
    {
        "name": "Holland Lop - Fuzzy",
        "species": "rabbit",
        "breed": "Holland Lop",
        "age": 1,
        "weight": 1.5,
        "description": "Cute floppy ears, gentle and good for families.",
        "personality": ["gentle", "cute", "friendly", "quiet"],
        "breederName": "Bunny Haven",
        "breederRating": 4.8,
        "price": 150.00,
        "available": True,
        "images": PET_IMAGES["rabbit"]
    },
    {
        "name": "Angora - Snowball",
        "species": "rabbit",
        "breed": "Angora",
        "age": 2,
        "weight": 2.0,
        "description": "Fluffy white coat, requires grooming but very friendly.",
        "personality": ["fluffy", "friendly", "calm", "social"],
        "breederName": "Angora Angels",
        "breederRating": 4.7,
        "price": 200.00,
        "available": True,
        "images": PET_IMAGES["rabbit"]
    },
    # Birds
    {
        "name": "African Grey - Koko",
        "species": "bird",
        "breed": "African Grey Parrot",
        "age": 5,
        "weight": 1.0,
        "description": "Highly intelligent, can mimic words. Requires commitment.",
        "personality": ["intelligent", "vocal", "social", "long-lived"],
        "breederName": "Parrot Paradise",
        "breederRating": 4.9,
        "price": 1500.00,
        "available": False,
        "images": PET_IMAGES["bird"]
    },
    {
        "name": "Cockatiel - Tweety",
        "species": "bird",
        "breed": "Cockatiel",
        "age": 1,
        "weight": 0.1,
        "description": "Small, friendly parrot. Great for beginners.",
        "personality": ["friendly", "playful", "melodious", "affectionate"],
        "breederName": "Bird Breeding Co.",
        "breederRating": 4.6,
        "price": 250.00,
        "available": True,
        "images": PET_IMAGES["bird"]
    },
]

# Comprehensive product data
PRODUCTS_DATA = [
    # Dog Food
    {
        "name": "Premium Dog Food - Chicken & Rice",
        "category": "food",
        "petType": "dog",
        "brand": "PetNutrition Pro",
        "description": "Balanced nutrition with real chicken and brown rice. Supports healthy coat and digestion.",
        "price": 45.99,
        "stock": 150,
        "filters": ["dry_food", "chicken", "high_protein"],
        "images": PRODUCT_IMAGES["dog_food"][:2]
    },
    {
        "name": "Wet Dog Food - Beef & Vegetables",
        "category": "food",
        "petType": "dog",
        "brand": "FreshPaw",
        "description": "100% natural wet food. Rich in vegetables and lean beef.",
        "price": 8.99,
        "stock": 200,
        "filters": ["wet_food", "beef", "natural"],
        "images": PRODUCT_IMAGES["dog_food"]
    },
    {
        "name": "Grain-Free Dog Food - Salmon",
        "category": "food",
        "petType": "dog",
        "brand": "WildHeart",
        "description": "Grain-free formula with omega-3 rich salmon. Perfect for sensitive stomachs.",
        "price": 52.99,
        "stock": 100,
        "filters": ["grain_free", "salmon", "sensitive_stomach"],
        "images": PRODUCT_IMAGES["dog_food"][:2]
    },
    # Cat Food
    {
        "name": "Premium Cat Food - Salmon & Tuna",
        "category": "food",
        "petType": "cat",
        "brand": "FelixFeast",
        "description": "Rich in omega-3s for healthy skin and coat. Cats love the taste!",
        "price": 38.99,
        "stock": 120,
        "filters": ["dry_food", "fish", "high_protein"],
        "images": PRODUCT_IMAGES["cat_food"]
    },
    {
        "name": "Wet Cat Food - Chicken Feast",
        "category": "food",
        "petType": "cat",
        "brand": "WhiskerDelight",
        "description": "Tender chicken pieces in gravy. Highly palatable and nutritious.",
        "price": 6.99,
        "stock": 250,
        "filters": ["wet_food", "chicken", "high_palatability"],
        "images": PRODUCT_IMAGES["cat_food"]
    },
    # Toys
    {
        "name": "Interactive Fetch Ball",
        "category": "toys",
        "petType": "dog",
        "brand": "PlayPup",
        "description": "Durable rubber ball that bounces unpredictably. Hours of entertainment.",
        "price": 12.99,
        "stock": 300,
        "filters": ["ball", "fetch", "durable"],
        "images": PRODUCT_IMAGES["toys"][:2]
    },
    {
        "name": "Rope Tug Toy",
        "category": "toys",
        "petType": "dog",
        "brand": "ChewMaster",
        "description": "Sturdy rope toy for tug-of-war. Great for dental health.",
        "price": 9.99,
        "stock": 200,
        "filters": ["rope", "tug_toy", "dental"],
        "images": PRODUCT_IMAGES["toys"]
    },
    {
        "name": "Feather Cat Wand",
        "category": "toys",
        "petType": "cat",
        "brand": "PawsomePlay",
        "description": "Colorful feathers on a wand. Keeps cats active and engaged.",
        "price": 7.99,
        "stock": 250,
        "filters": ["interactive", "feather", "exercise"],
        "images": PRODUCT_IMAGES["toys"][:2]
    },
    {
        "name": "Laser Pointer Toy",
        "category": "toys",
        "petType": "cat",
        "brand": "LightSpeed",
        "description": "Safe laser pointer for interactive play. USB rechargeable.",
        "price": 11.99,
        "stock": 180,
        "filters": ["laser", "interactive", "rechargeable"],
        "images": PRODUCT_IMAGES["toys"]
    },
    {
        "name": "Chew Stick Pack",
        "category": "toys",
        "petType": "dog",
        "brand": "NaturalChew",
        "description": "12-pack of natural chew sticks. Long-lasting and safe.",
        "price": 18.99,
        "stock": 150,
        "filters": ["chew", "natural", "long_lasting"],
        "images": PRODUCT_IMAGES["toys"][:2]
    },
    # Accessories
    {
        "name": "Premium Leather Collar",
        "category": "accessories",
        "petType": "dog",
        "brand": "EliteLeash",
        "description": "Soft leather collar with adjustable fit. Available in multiple colors.",
        "price": 29.99,
        "stock": 80,
        "filters": ["collar", "leather", "adjustable"],
        "images": PRODUCT_IMAGES["accessories"][:2]
    },
    {
        "name": "Reflective LED Collar",
        "category": "accessories",
        "petType": "dog",
        "brand": "SafeLight",
        "description": "Glowing LED collar for nighttime visibility. USB rechargeable.",
        "price": 24.99,
        "stock": 100,
        "filters": ["collar", "led", "safety"],
        "images": PRODUCT_IMAGES["accessories"]
    },
    {
        "name": "Cat Collar with Bell",
        "category": "accessories",
        "petType": "cat",
        "brand": "JingleBell",
        "description": "Cute collar with adjustable safety clasp and jingle bell.",
        "price": 8.99,
        "stock": 120,
        "filters": ["collar", "safety", "bell"],
        "images": PRODUCT_IMAGES["accessories"][:2]
    },
    {
        "name": "Dog Leash - 6ft Nylon",
        "category": "accessories",
        "petType": "dog",
        "brand": "StrongHold",
        "description": "Durable nylon leash with comfortable grip handle.",
        "price": 15.99,
        "stock": 150,
        "filters": ["leash", "nylon", "durable"],
        "images": PRODUCT_IMAGES["accessories"]
    },
    {
        "name": "Retractable Leash",
        "category": "accessories",
        "petType": "dog",
        "brand": "FlexiFit",
        "description": "16ft retractable leash for small to medium dogs.",
        "price": 22.99,
        "stock": 90,
        "filters": ["leash", "retractable", "convenient"],
        "images": PRODUCT_IMAGES["accessories"][:2]
    },
    # Bedding
    {
        "name": "Orthopedic Dog Bed - Large",
        "category": "bedding",
        "petType": "dog",
        "brand": "ComfortRest",
        "description": "Memory foam bed with washable cover. Supports joint health.",
        "price": 89.99,
        "stock": 50,
        "filters": ["bed", "orthopedic", "memory_foam"],
        "images": PRODUCT_IMAGES["bedding"]
    },
    {
        "name": "Pet Blanket - Fleece",
        "category": "bedding",
        "petType": "dog",
        "brand": "CozyKnit",
        "description": "Soft fleece blanket. Machine washable.",
        "price": 19.99,
        "stock": 200,
        "filters": ["blanket", "fleece", "washable"],
        "images": PRODUCT_IMAGES["bedding"]
    },
    {
        "name": "Cat Bed - Igloo Style",
        "category": "bedding",
        "petType": "cat",
        "brand": "CozyCat",
        "description": "Enclosed cat bed for security and warmth.",
        "price": 34.99,
        "stock": 70,
        "filters": ["bed", "enclosed", "warm"],
        "images": PRODUCT_IMAGES["bedding"]
    },
    {
        "name": "Elevated Pet Bed",
        "category": "bedding",
        "petType": "dog",
        "brand": "AirFlow",
        "description": "Breathable mesh bed that keeps pets cool in summer.",
        "price": 44.99,
        "stock": 60,
        "filters": ["bed", "elevated", "cooling"],
        "images": PRODUCT_IMAGES["bedding"]
    },
    # Grooming
    {
        "name": "Dog Grooming Brush Set",
        "category": "grooming",
        "petType": "dog",
        "brand": "GlossyCoat",
        "description": "5-piece brush set for all coat types. Professional quality.",
        "price": 39.99,
        "stock": 80,
        "filters": ["brush", "grooming", "professional"],
        "images": PRODUCT_IMAGES["grooming"]
    },
    {
        "name": "Cat Grooming Brush",
        "category": "grooming",
        "petType": "cat",
        "brand": "FurSoft",
        "description": "Gentle brush for cats. Reduces shedding.",
        "price": 14.99,
        "stock": 150,
        "filters": ["brush", "shedding", "gentle"],
        "images": PRODUCT_IMAGES["grooming"]
    },
    {
        "name": "Pet Nail Clippers",
        "category": "grooming",
        "petType": "dog",
        "brand": "SnapCut",
        "description": "Ergonomic nail clippers with safety guard.",
        "price": 16.99,
        "stock": 100,
        "filters": ["clippers", "nails", "safety"],
        "images": PRODUCT_IMAGES["grooming"]
    },
    {
        "name": "Dry Dog Shampoo",
        "category": "grooming",
        "petType": "dog",
        "brand": "FreshScent",
        "description": "No-rinse dry shampoo for quick cleaning.",
        "price": 12.99,
        "stock": 120,
        "filters": ["shampoo", "dry", "quick"],
        "images": PRODUCT_IMAGES["grooming"]
    },
    {
        "name": "Pet Dental Chews",
        "category": "grooming",
        "petType": "dog",
        "brand": "BrightSmile",
        "description": "Chews that promote dental health and fresh breath.",
        "price": 13.99,
        "stock": 200,
        "filters": ["dental", "chew", "health"],
        "images": PRODUCT_IMAGES["grooming"]
    },
]


async def seed_pets(conn):
    """Seed pets into database"""
    try:
        logger.info(f"Starting to seed {len(PETS_DATA)} pets...")
        created_count = 0
        
        for pet_data in PETS_DATA:
            try:
                # Check if exists
                existing = await conn.fetchval(
                    "SELECT id FROM \"Pet\" WHERE name = $1",
                    pet_data["name"]
                )
                
                if existing:
                    logger.info(f"  → Pet '{pet_data['name']}' already exists, skipping...")
                    continue
                
                # Insert pet
                await conn.execute(
                    """INSERT INTO "Pet" (name, species, breed, age, weight, description, personality, "breederName", "breederRating", price, available, images)
                       VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)""",
                    pet_data["name"],
                    pet_data["species"],
                    pet_data["breed"],
                    pet_data["age"],
                    pet_data["weight"],
                    pet_data["description"],
                    pet_data["personality"],  # Array
                    pet_data["breederName"],
                    pet_data["breederRating"],
                    pet_data["price"],
                    pet_data["available"],
                    pet_data["images"]  # Array
                )
                created_count += 1
                logger.info(f"  ✓ Created: {pet_data['name']}")
            except Exception as e:
                logger.error(f"  ✗ Error with '{pet_data['name']}': {str(e)}")
                continue
        
        logger.info(f"\n✓ Successfully created {created_count}/{len(PETS_DATA)} pets\n")
        return created_count
    except Exception as e:
        logger.error(f"Error in seed_pets: {str(e)}")
        raise


async def seed_products(conn):
    """Seed products into database"""
    try:
        logger.info(f"Starting to seed {len(PRODUCTS_DATA)} products...")
        created_count = 0
        
        for product_data in PRODUCTS_DATA:
            try:
                # Check if exists
                existing = await conn.fetchval(
                    "SELECT id FROM \"Product\" WHERE name = $1",
                    product_data["name"]
                )
                
                if existing:
                    logger.info(f"  → Product '{product_data['name']}' already exists, skipping...")
                    continue
                
                # Insert product
                await conn.execute(
                    """INSERT INTO "Product" (name, category, "petType", brand, description, price, stock, filters, images)
                       VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)""",
                    product_data["name"],
                    product_data["category"],
                    product_data["petType"],
                    product_data["brand"],
                    product_data["description"],
                    product_data["price"],
                    product_data["stock"],
                    product_data["filters"],  # Array
                    product_data["images"]  # Array
                )
                created_count += 1
                logger.info(f"  ✓ Created: {product_data['name']}")
            except Exception as e:
                logger.error(f"  ✗ Error with '{product_data['name']}': {str(e)}")
                continue
        
        logger.info(f"\n✓ Successfully created {created_count}/{len(PRODUCTS_DATA)} products\n")
        return created_count
    except Exception as e:
        logger.error(f"Error in seed_products: {str(e)}")
        raise


async def main():
    """Main seeding function"""
    try:
        logger.info("=" * 80)
        logger.info("PetBloom Database Comprehensive Seeding")
        logger.info("=" * 80 + "\n")
        
        # Connect to database
        conn = await asyncpg.connect(DATABASE_URL)
        logger.info("✓ Connected to PostgreSQL database\n")
        
        pets_count = await seed_pets(conn)
        products_count = await seed_products(conn)
        
        await conn.close()
        logger.info("✓ Database connection closed")
        
        logger.info("\n" + "=" * 80)
        logger.info("✓ SEEDING COMPLETE!")
        logger.info(f"  • Pets created: {pets_count}")
        logger.info(f"  • Products created: {products_count}")
        logger.info(f"  • Total items: {pets_count + products_count}")
        logger.info("=" * 80 + "\n")
        
    except Exception as e:
        logger.error(f"\n✗ FATAL ERROR: {str(e)}\n")
        raise
    finally:
        try:
            await conn.close()
        except:
            pass


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("\n✗ Seeding cancelled by user\n")
    except Exception as e:
        logger.error(f"\n✗ Fatal error: {str(e)}\n")
        exit(1)
