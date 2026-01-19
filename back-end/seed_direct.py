#!/usr/bin/env python3
"""
Direct seed script for PetBloom - uses SQLAlchemy instead of Prisma
Run locally: python seed_direct.py
Or use as backup seed method
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql://postgres:vtdBjkgxHkBPDdFYnlvmSCcPbklgEicd@postgres.railway.internal:5432/railway"

# Create engine
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

PETS_SQL = """
INSERT INTO "Pet" (name, species, breed, age, weight, description, images, personality, "breederName", "breederRating", price, available, "createdAt", "updatedAt")
VALUES 
('Max', 'dogs', 'Golden Retriever', 2, 30.0, 'Friendly and energetic golden retriever with beautiful cream coat. Perfect for active families. Fully vaccinated and dewormed.', ARRAY['https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400', 'https://images.unsplash.com/photo-1558788353-f76d92427f16?w=400'], ARRAY['friendly', 'energetic', 'loyal'], 'Golden Dreams Kennel', 4.8, 95000.00, true, NOW(), NOW()),
('Buddy', 'dogs', 'Labrador Retriever', 3, 35.0, 'Playful chocolate Labrador with excellent temperament. Great with children and other pets. Trained basic commands.', ARRAY['https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400', 'https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400'], ARRAY['playful', 'loyal', 'intelligent'], 'Happy Paws', 4.7, 85000.00, true, NOW(), NOW()),
('Rocky', 'dogs', 'German Shepherd', 1, 28.0, 'Strong and intelligent German Shepherd. Alert and protective family guardian. Excellent bloodline, trained for obedience.', ARRAY['https://images.unsplash.com/photo-1568572933382-74d440641117?w=400', 'https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400'], ARRAY['intelligent', 'protective', 'loyal'], 'Shepherd Elite', 4.9, 110000.00, true, NOW(), NOW()),
('Charlie', 'dogs', 'Beagle', 2, 12.0, 'Small but mighty Beagle with excellent hunting instincts. Friendly and curious personality. Great for apartment living.', ARRAY['https://images.unsplash.com/photo-1505628346881-b72b27e84530?w=400'], ARRAY['friendly', 'curious', 'energetic'], 'Beagle House', 4.6, 65000.00, true, NOW(), NOW()),
('Duke', 'dogs', 'Rottweiler', 4, 50.0, 'Magnificent Rottweiler with calm temperament. Despite reputation, very affectionate and family-oriented. Well-trained.', ARRAY['https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400'], ARRAY['calm', 'loyal', 'protective'], 'Noble Rotts', 4.8, 120000.00, true, NOW(), NOW()),
('Whiskers', 'cats', 'Persian', 1, 4.5, 'Elegant and refined Persian cat with luxurious long coat. Calm and affectionate. Requires regular grooming.', ARRAY['https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?w=400', 'https://images.unsplash.com/photo-1606214174585-fe31582dc1d7?w=400'], ARRAY['calm', 'affectionate', 'elegant'], 'Purrfect Cats', 4.9, 55000.00, true, NOW(), NOW()),
('Luna', 'cats', 'Siamese', 2, 3.2, 'Beautiful Siamese with striking blue eyes. Vocal and interactive. Loves attention and playtime.', ARRAY['https://images.unsplash.com/photo-1513360371669-4a8e1949883e?w=400', 'https://images.unsplash.com/photo-1606214174585-fe31582dc1d7?w=400'], ARRAY['vocal', 'playful', 'affectionate'], 'Siamese Dreams', 4.8, 48000.00, true, NOW(), NOW()),
('Shadow', 'cats', 'Black Domestic Shorthair', 3, 4.0, 'Sleek black cat with golden eyes. Independent but loving. Perfect for quiet homes. Excellent mouser.', ARRAY['https://images.unsplash.com/photo-1570158108855-a920fb1b81d9?w=400'], ARRAY['independent', 'loving', 'intelligent'], 'Shadow''s Sanctuary', 4.7, 35000.00, true, NOW(), NOW()),
('Mittens', 'cats', 'British Shorthair', 2, 5.5, 'Plump and cuddly British Shorthair with grey coat. Very calm and sociable. Great family pet.', ARRAY['https://images.unsplash.com/photo-1567517381829-ba595fac2ec0?w=400'], ARRAY['calm', 'sociable', 'cuddly'], 'British Beauties', 4.9, 52000.00, true, NOW(), NOW()),
('Tiger', 'cats', 'Orange Tabby', 1, 3.8, 'Energetic and playful orange tabby. Full of personality and mischief. Loves interactive toys.', ARRAY['https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400'], ARRAY['playful', 'energetic', 'mischievous'], 'Tabby House', 4.6, 40000.00, true, NOW(), NOW())
ON CONFLICT (name) DO NOTHING;
"""

PRODUCTS_SQL = """
INSERT INTO "Product" (name, description, category, "petType", brand, price, images, stock, filters, "createdAt", "updatedAt")
VALUES
('Premium Adult Dog Food', 'High-quality dry dog food with balanced nutrition. Rich in protein and essential vitamins. Suitable for all dog breeds.', 'food', 'dogs', 'PetPro', 3500.00, ARRAY['https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400'], 50, ARRAY['adult', 'nutritious'], NOW(), NOW()),
('Grain-Free Puppy Food', 'Specially formulated for puppies. No grains, rich in DHA for brain development. Supports healthy growth.', 'food', 'dogs', 'NutriPaws', 4200.00, ARRAY['https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400'], 35, ARRAY['puppy', 'grain-free'], NOW(), NOW()),
('Senior Dog Food', 'Low-calorie formula for senior dogs. Easy to digest with joint support ingredients.', 'food', 'dogs', 'GoldenYears', 3800.00, ARRAY['https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400'], 25, ARRAY['senior', 'low-calorie'], NOW(), NOW()),
('Premium Cat Food - Salmon', 'Delicious salmon flavor cat food. Complete nutrition for adult cats. Promotes healthy coat.', 'food', 'cats', 'FelineFresh', 2800.00, ARRAY['https://images.unsplash.com/photo-1537462715957-923ec97dd6f0?w=400'], 40, ARRAY['salmon', 'adult'], NOW(), NOW()),
('Kitten Growth Formula', 'Specially designed for kittens aged 2-12 months. High protein for development.', 'food', 'cats', 'KittyStart', 3200.00, ARRAY['https://images.unsplash.com/photo-1537462715957-923ec97dd6f0?w=400'], 30, ARRAY['kitten', 'growth'], NOW(), NOW()),
('Interactive Dog Toy Set', 'Set of 5 interactive toys to keep dogs entertained. Includes balls, ropes, and chew toys.', 'toys', 'dogs', 'PlayPets', 2200.00, ARRAY['https://images.unsplash.com/photo-1591769225440-811ad7d6eab3?w=400'], 45, ARRAY['interactive', 'durable'], NOW(), NOW()),
('Durable Rope Tug Toy', 'Strong rope toy for aggressive chewers. Great for multi-dog families. Machine washable.', 'toys', 'dogs', 'ChewMaster', 1500.00, ARRAY['https://images.unsplash.com/photo-1535241749838-299277b6305f?w=400'], 50, ARRAY['rope', 'durable'], NOW(), NOW()),
('Dog Puzzle Feeder', 'Keep your dog mentally stimulated. Improves problem-solving skills during feeding time.', 'toys', 'dogs', 'BrainPlay', 2800.00, ARRAY['https://images.unsplash.com/photo-1570158108855-a920fb1b81d9?w=400'], 20, ARRAY['puzzle', 'mental-stimulation'], NOW(), NOW()),
('Feather Wand Cat Toy', 'Interactive feather wand toy. Stimulates hunting instincts. Great for exercise.', 'toys', 'cats', 'CatPlay', 800.00, ARRAY['https://images.unsplash.com/photo-1559163499-64dd58e07650?w=400'], 60, ARRAY['interactive', 'feather'], NOW(), NOW()),
('Cat Laser Toy', 'Safe laser toy for cats. Promotes exercise and play. Includes auto-timer feature.', 'toys', 'cats', 'LaserFun', 1200.00, ARRAY['https://images.unsplash.com/photo-1559163499-64dd58e07650?w=400'], 30, ARRAY['laser', 'interactive'], NOW(), NOW()),
('Deluxe Cat Bed', 'Soft and comfortable cat bed. Machine washable cover. Cozy cave design.', 'habitats', 'cats', 'CatsLounge', 4500.00, ARRAY['https://images.unsplash.com/photo-1577023311546-cdc07a8454d9?w=400'], 25, ARRAY['comfortable', 'cave'], NOW(), NOW()),
('Multi-Level Cat Tree', '5-level cat tree with scratching posts. Provides climbing and resting areas. Sturdy construction.', 'habitats', 'cats', 'CatsLounge', 12000.00, ARRAY['https://images.unsplash.com/photo-1521568547814-0a0a0d8a2d3a?w=400'], 10, ARRAY['climbing', 'scratching-posts'], NOW(), NOW()),
('Premium Dog Collar with Leash', 'Adjustable leather collar with matching leash. Comfortable and durable. Multiple sizes.', 'accessories', 'dogs', 'SafeGuard', 2500.00, ARRAY['https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f0?w=400'], 35, ARRAY['leather', 'adjustable'], NOW(), NOW()),
('Cat Harness and Leash Set', 'Lightweight and safe harness for cats. Perfect for outdoor walks. Escape-proof design.', 'accessories', 'cats', 'SafeGuard', 1800.00, ARRAY['https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f0?w=400'], 20, ARRAY['lightweight', 'safe'], NOW(), NOW()),
('Professional Dog Grooming Kit', 'Complete grooming set including clippers, scissors, and brush. Suitable for all coat types.', 'grooming', 'dogs', 'GroomPro', 5500.00, ARRAY['https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400'], 15, ARRAY['professional', 'complete'], NOW(), NOW()),
('Cat Grooming Brush', 'Gentle de-matting brush for cats. Reduces shedding. Comfortable grip handle.', 'grooming', 'cats', 'GroomPro', 1500.00, ARRAY['https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400'], 40, ARRAY['gentle', 'de-matting'], NOW(), NOW())
ON CONFLICT (name) DO NOTHING;
"""

def main():
    try:
        print("🌱 Seeding PetBloom Database with Direct SQL")
        print("=" * 50)
        
        session = Session()
        
        # Seed pets
        print("📝 Adding 10 pets...")
        session.execute(text(PETS_SQL))
        session.commit()
        print("✅ Pets added successfully!")
        
        # Seed products
        print("📦 Adding 17 products...")
        session.execute(text(PRODUCTS_SQL))
        session.commit()
        print("✅ Products added successfully!")
        
        # Verify
        pets_count = session.execute(text("SELECT COUNT(*) FROM \"Pet\"")).scalar()
        products_count = session.execute(text("SELECT COUNT(*) FROM \"Product\"")).scalar()
        
        print("\n" + "=" * 50)
        print("✅ SEEDING COMPLETE!")
        print(f"✓ Pets in database: {pets_count}")
        print(f"✓ Products in database: {products_count}")
        print("=" * 50)
        
        session.close()
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
