import asyncio
from prisma import Prisma

async def seed():
    prisma = Prisma()
    await prisma.connect()
    
    pets_data = [
        {"name": "Max", "species": "dogs", "breed": "Golden Retriever", "age": 2, "weight": 30, "description": "Friendly and energetic golden retriever", "images": ["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400"], "videos": [], "personality": ["friendly", "energetic"], "breederName": "Golden Dreams", "breederRating": 4.8, "price": 1200.00, "available": True},
        {"name": "Whiskers", "species": "cats", "breed": "Persian", "age": 1, "weight": 4.5, "description": "Elegant Persian cat", "images": ["https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?w=400"], "videos": [], "personality": ["calm", "affectionate"], "breederName": "Purrfect Cats", "breederRating": 4.9, "price": 800.00, "available": True},
        {"name": "Buddy", "species": "dogs", "breed": "Labrador", "age": 3, "weight": 35, "description": "Playful Labrador", "images": ["https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400"], "videos": [], "personality": ["playful", "loyal"], "breederName": "Happy Paws", "breederRating": 4.7, "price": 1000.00, "available": True}
    ]
    
    products_data = [
        {"name": "Premium Dog Food", "description": "Nutritious dry dog food", "category": "food", "petType": "dogs", "brand": "PetPro", "price": 45.99, "images": ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"], "stock": 50, "filters": ["adult"]},
        {"name": "Cat Bed", "description": "Comfortable cat bed", "category": "habitats", "petType": "cats", "brand": "CatsLounge", "price": 65.00, "images": ["https://images.unsplash.com/photo-1577023311546-cdc07a8454d9?w=400"], "stock": 25, "filters": ["comfortable"]},
        {"name": "Dog Toy Set", "description": "Set of 5 interactive toys", "category": "toys", "petType": "dogs", "brand": "PlayPets", "price": 29.99, "images": ["https://images.unsplash.com/photo-1591769225440-811ad7d6eab3?w=400"], "stock": 40, "filters": ["durable"]}
    ]
    
    # Create pets
    pets = []
    for pet in pets_data:
        created_pet = await prisma.pet.create(data=pet)
        pets.append(created_pet)
    
    # Create products
    products = []
    for product in products_data:
        created_product = await prisma.product.create(data=product)
        products.append(created_product)
    
    # Create sample reviews for products
    if len(products) > 0:
        await prisma.review.create(data={
            "userId": "temp_user",
            "productId": products[0].id,
            "rating": 5,
            "comment": "Excellent quality dog food! My pets love it.",
            "createdAt": None
        })
        await prisma.review.create(data={
            "userId": "demo_user",
            "productId": products[0].id,
            "rating": 4,
            "comment": "Good product, reasonable price.",
            "createdAt": None
        })
    
    # Create sample reviews for pets
    if len(pets) > 0:
        await prisma.review.create(data={
            "userId": "temp_user",
            "petId": pets[0].id,
            "rating": 5,
            "comment": "Max is the sweetest dog! Perfect family pet.",
            "createdAt": None
        })
    
    # Create sample addresses
    await prisma.useraddress.create(data={
        "userId": "temp_user",
        "street": "123 Main Street",
        "city": "Nairobi",
        "state": "Nairobi County",
        "zipCode": "00100",
        "country": "Kenya",
        "isDefault": True
    })
    await prisma.useraddress.create(data={
        "userId": "temp_user",
        "street": "456 Oak Avenue",
        "city": "Mombasa",
        "state": "Coast County",
        "zipCode": "80100",
        "country": "Kenya",
        "isDefault": False
    })
    
    # Create sample messages
    await prisma.message.create(data={
        "senderId": "demo_user",
        "recipientId": "temp_user",
        "content": "Hi! I'm interested in the Golden Retriever. Is Max still available?",
        "read": False
    })
    await prisma.message.create(data={
        "senderId": "temp_user",
        "recipientId": "demo_user",
        "content": "Yes, Max is available! When would you like to schedule a viewing?",
        "read": False
    })
    
    print("✅ Database seeded successfully!")
    print("   - Created 3 pets")
    print("   - Created 3 products")
    print("   - Created 3 reviews (2 product + 1 pet)")
    print("   - Created 2 addresses")
    print("   - Created 2 messages")
    await prisma.disconnect()

if __name__ == "__main__":
    asyncio.run(seed())
