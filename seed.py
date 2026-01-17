import asyncio
from prisma import Prisma

async def seed():
    prisma = Prisma()
    await prisma.connect()
    
    pets_data = [
        {"name": "Max", "species": "dogs", "breed": "Golden Retriever", "age": 12, "weight": 30, "description": "Friendly and energetic golden retriever looking for a loving home", "images": ["https://via.placeholder.com/400"], "videos": [], "personality": ["friendly", "energetic", "loyal"], "breederName": "Golden Dreams Breeder", "breederRating": 4.8, "price": 1200.00, "avlble": True},
        {"name": "Whiskers", "species": "cats", "breed": "Persian", "age": 6, "weight": 4.5, "description": "Elegant and calm Persian cat, perfect for families", "images": ["https://via.placeholder.com/400"], "videos": [], "personality": ["calm", "affectionate", "independent"], "breederName": "Purrfect Cats", "breederRating": 4.9, "price": 800.00, "avlble": True},
        {"name": "Tweety", "species": "birds", "breed": "Parakeet", "age": 2, "weight": 0.03, "description": "Colorful and talkative parakeet", "images": ["https://via.placeholder.com/400"], "videos": [], "personality": ["vocal", "playful", "social"], "breederName": "Happy Birds", "breederRating": 4.7, "price": 150.00, "avlble": True}
    ]
    
    products_data = [
        {"name": "Premium Dog Food", "description": "Nutritious dry dog food for all breeds", "category": "food", "petType": "dogs", "brand": "PetProNutrition", "price": 45.99, "images": ["https://via.placeholder.com/400"], "stock": 50, "filters": ["adult", "large-breed"]},
        {"name": "Cat Bed Deluxe", "description": "Comfortable orthopedic bed for cats", "category": "habitats", "petType": "cats", "brand": "CatsLounge", "price": 65.00, "images": ["https://via.placeholder.com/400"], "stock": 25, "filters": ["comfortable", "washable"]},
        {"name": "Interactive Dog Toy Set", "description": "Set of 5 interactive toys to keep dogs entertained", "category": "toys", "petType": "dogs", "brand": "PlayPets", "price": 29.99, "images": ["https://via.placeholder.com/400"], "stock": 40, "filters": ["durable", "interactive"]},
        {"name": "Bird Cage Large", "description": "Spacious cage for multiple birds", "category": "habitats", "petType": "birds", "brand": "BirdHappy", "price": 199.99, "images": ["https://via.placeholder.com/400"], "stock": 10, "filters": ["spacious", "easy-clean"]},
        {"name": "Pet Grooming Kit", "description": "Complete grooming kit with brush, scissors, and more", "category": "grooming", "petType": None, "brand": "GroomPro", "price": 35.50, "images": ["https://via.placeholder.com/400"], "stock": 30, "filters": ["professional", "all-breeds"]}
    ]
    
    for pet in pets_data:
        await prisma.pet.create(data=pet)
    
    for product in products_data:
        await prisma.product.create(data=product)
    
    await prisma.disconnect()

if __name__ == "__main__":
    asyncio.run(seed())
