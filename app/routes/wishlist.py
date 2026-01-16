from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import WishlistResponse, WishlistCreate
from prisma import Prisma

router = APIRouter(prefix="/wishlist", tags=["wishlist"])
prisma = Prisma()

@router.get("/{user_id}", response_model=List[WishlistResponse])
async def get_wishlist(user_id: str):
    
    try:
        await prisma.connect()
        wishlist = await prisma.wishlist.find_many(
            where={"userId": user_id},
            order={"addedAt": "desc"}
        )
        await prisma.disconnect()
        return wishlist
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.post("/{user_id}", response_model=WishlistResponse)
async def add_to_wishlist(user_id: str, item: WishlistCreate):
    
    try:
        await prisma.connect()
        
        existing = await prisma.wishlist.find_first(
            where={
                "userId": user_id,
                "productId": item.productId,
                "petId": item.petId
            }
        )
        
        if existing:
            await prisma.disconnect()
            raise HTTPException(status_code=400, detl="Item already in wishlist")
        
        wishlist_item = await prisma.wishlist.create(
            data={
                "userId": user_id,
                "productId": item.productId,
                "petId": item.petId
            }
        )
        await prisma.disconnect()
        return wishlist_item
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.delete("/{wishlist_id}")
async def remove_from_wishlist(wishlist_id: str):
    
    try:
        await prisma.connect()
        await prisma.wishlist.delete(where={"id": wishlist_id})
        await prisma.disconnect()
        return {"message": "Item removed from wishlist"}
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))
