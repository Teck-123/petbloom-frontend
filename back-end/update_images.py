#!/usr/bin/env python3
"""
Script to update products and pets in the database with image URLs from public CDN
"""

import asyncio
import os
from app.services.prisma_client import prisma_client
from app.config import get_settings

settings = get_settings()

# Free image URLs from various CDNs
PET_IMAGES = {
    "dog": [
        "https://images.unsplash.com/photo-1633722715463-d30628cqsw8d?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1633722641147-8f835f7a1e08?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1633722854212-cfe1a70f92ef?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1633722716993-d42ddaa0001e?w=400&h=400&fit=crop",
    ],
    "cat": [
        "https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1574144611937-0df059b5ef3e?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1573865526014-f3550b1ade60?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400&h=400&fit=crop",
    ],
    "rabbit": [
        "https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f4?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f4?w=400&h=400&fit=crop",
    ],
    "bird": [
        "https://images.unsplash.com/photo-1444464666175-1642a3a3b1ef?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1444464666175-1642a3a3b1ef?w=400&h=400&fit=crop",
    ]
}

PRODUCT_IMAGES = {
    "dog_food": [
        "https://images.unsplash.com/photo-1589941013453-ec89f33b5e95?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1555684586-46f694365df1?w=400&h=400&fit=crop",
    ],
    "cat_food": [
        "https://images.unsplash.com/photo-1589941013453-ec89f33b5e95?w=400&h=400&fit=crop",
    ],
    "toys": [
        "https://images.unsplash.com/photo-1535241749838-299277b6305f?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1633722715463-d30628cqsw8d?w=400&h=400&fit=crop",
    ],
    "accessories": [
        "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?w=400&h=400&fit=crop",
    ],
    "bedding": [
        "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400&h=400&fit=crop",
    ],
    "grooming": [
        "https://images.unsplash.com/photo-1625938363236-19dcd028fcfe?w=400&h=400&fit=crop",
    ]
}

async def update_pets_with_images():
    """Update all pets with image URLs"""
    try:
        pets = await prisma_client.pet.find_many()
        updated_count = 0
        
        for pet in pets:
            # Determine pet type for image selection
            pet_type = pet.species.lower() if pet.species else "dog"
            if pet_type not in PET_IMAGES:
                pet_type = "dog"  # default to dog images
            
            # Get images for this pet type
            images = PET_IMAGES.get(pet_type, PET_IMAGES["dog"])
            
            # Update pet with images
            await prisma_client.pet.update(
                where={"id": pet.id},
                data={"images": images}
            )
            updated_count += 1
        
        print(f"✓ Updated {updated_count} pets with images")
        return updated_count
    except Exception as e:
        print(f"✗ Error updating pets: {str(e)}")
        raise

async def update_products_with_images():
    """Update all products with image URLs"""
    try:
        products = await prisma_client.product.find_many()
        updated_count = 0
        
        for product in products:
            # Determine category for image selection
            category = product.category.lower() if product.category else "toys"
            category_key = category.replace(' ', '_').replace('-', '_')
            
            # Try to find matching images
            images = PRODUCT_IMAGES.get(category_key, PRODUCT_IMAGES["toys"])
            
            # Update product with images
            await prisma_client.product.update(
                where={"id": product.id},
                data={"images": images}
            )
            updated_count += 1
        
        print(f"✓ Updated {updated_count} products with images")
        return updated_count
    except Exception as e:
        print(f"✗ Error updating products: {str(e)}")
        raise

async def main():
    """Main function"""
    try:
        await prisma_client.connect()
        print("Connected to database\n")
        
        print("Updating pets with images...")
        await update_pets_with_images()
        
        print("\nUpdating products with images...")
        await update_products_with_images()
        
        print("\n✓ All items updated successfully!")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
    finally:
        await prisma_client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
