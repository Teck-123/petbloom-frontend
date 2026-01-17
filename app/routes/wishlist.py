from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import WishlistResponse, WishlistCreate
from app.services.prisma_client import prisma_client

router = APIRouter(prefix="/wishlist", tags=["wishlist"])

@router.get("/{user_id}", response_model=List[WishlistResponse])
async def get_wishlist(user_id: str):
    try:
        wishlist = await prisma_client.wishlist.find_many(
            where={"userId": user_id},
            order={"addedAt": "desc"}
        )
        return wishlist
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{user_id}", response_model=WishlistResponse)
async def add_to_wishlist(user_id: str, item: WishlistCreate):
    try:
        existing = await prisma_client.wishlist.find_first(
            where={
                "userId": user_id,
                "productId": item.productId,
                "petId": item.petId
            }
        )
        
        if existing:
            raise HTTPException(status_code=400, detail="Item already in wishlist")
        
        wishlist_item = await prisma_client.wishlist.create(
            data={
                "userId": user_id,
                "productId": item.productId,
                "petId": item.petId
            }
        )
        return wishlist_item
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{wishlist_id}")
async def remove_from_wishlist(wishlist_id: str):
    try:
        await prisma_client.wishlist.delete(where={"id": wishlist_id})
        return {"message": "Item removed from wishlist"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
