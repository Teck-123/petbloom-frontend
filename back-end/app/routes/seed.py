from fastapi import APIRouter, HTTPException
from app.services.prisma_client import prisma_client
import subprocess
import os

router = APIRouter(prefix="/seed", tags=["seed"])

@router.post("/clear")
async def clear_database():
    """Clear all data from database"""
    try:
        await prisma_client.cartitem.delete_many()
        await prisma_client.wishlist.delete_many()
        await prisma_client.orderitem.delete_many()
        await prisma_client.order.delete_many()
        await prisma_client.pet.delete_many()
        await prisma_client.product.delete_many()
        await prisma_client.user.delete_many()
        return {"message": "✅ Database cleared successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Clear failed: {str(e)}")
async def init_schema():
    """Initialize database schema using Prisma"""
    try:
        # Run prisma db push to create tables
        result = subprocess.run(
            ["prisma", "db", "push", "--skip-generate"],
            cwd=os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            return {"message": "Schema initialized", "details": result.stdout}
        
        return {"message": "✅ Schema initialized successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Schema init failed: {str(e)}")

@router.post("/init")
async def seed_database():
    """Initialize database with sample data"""
    try:
        # Check if data already exists
        existing_products = await prisma_client.product.find_many(take=1)
        if existing_products:
            return {"message": "Database already seeded"}
        
        pets_data = [
            {
                "name": "Max",
                "species": "dogs",
                "breed": "Golden Retriever",
                "age": 2,
                "weight": 30.0,
                "description": "Friendly and energetic golden retriever",
                "images": ["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400"],
                "videos": [],
                "personality": ["friendly", "energetic"],
                "breederName": "Golden Dreams",
                "breederRating": 4.8,
                "price": 156000.00,
                "available": True
            },
            {
                "name": "Whiskers",
                "species": "cats",
                "breed": "Persian",
                "age": 1,
                "weight": 4.5,
                "description": "Elegant Persian cat",
                "images": ["https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?w=400"],
                "videos": [],
                "personality": ["calm", "affectionate"],
                "breederName": "Purrfect Cats",
                "breederRating": 4.9,
                "price": 104000.00,
                "available": True
            },
            {
                "name": "Buddy",
                "species": "dogs",
                "breed": "Labrador",
                "age": 3,
                "weight": 35.0,
                "description": "Playful Labrador",
                "images": ["https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400"],
                "videos": [],
                "personality": ["playful", "loyal"],
                "breederName": "Happy Paws",
                "breederRating": 4.7,
                "price": 130000.00,
                "available": True
            }
        ]
        
        products_data = [
            {
                "name": "Premium Dog Food",
                "description": "Nutritious dry dog food",
                "category": "food",
                "petType": "dogs",
                "brand": "PetPro",
                "price": 5980.00,
                "images": ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"],
                "stock": 50,
                "filters": ["adult"]
            },
            {
                "name": "Cat Bed",
                "description": "Comfortable cat bed",
                "category": "habitats",
                "petType": "cats",
                "brand": "CatsLounge",
                "price": 8450.00,
                "images": ["https://images.unsplash.com/photo-1577023311546-cdc07a8454d9?w=400"],
                "stock": 25,
                "filters": ["comfortable"]
            },
            {
                "name": "Dog Toy Set",
                "description": "Set of 5 interactive toys",
                "category": "toys",
                "petType": "dogs",
                "brand": "PlayPets",
                "price": 3900.00,
                "images": ["https://images.unsplash.com/photo-1591769225440-811ad7d6eab3?w=400"],
                "stock": 40,
                "filters": ["durable"]
            }
        ]
        
        # Create pets
        for pet in pets_data:
            await prisma_client.pet.create(data=pet)
        
        # Create products
        for product in products_data:
            await prisma_client.product.create(data=product)
        
        return {"message": "✅ Database seeded successfully!", "pets": len(pets_data), "products": len(products_data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Seeding failed: {str(e)}")
