from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas import WishlistResponse, WishlistCreate
from app.services.prisma_client import prisma_client
from app.services.auth_helper import get_current_user_id

router = APIRouter(prefix="/wishlist", tags=["wishlist"])

@router.get("", response_model=List[WishlistResponse])
async def get_wishlist(user_id: str = Depends(get_current_user_id)):
    try:
        wishlist = await prisma_client.wishlist.find_many(
            where={"userId": user_id},
            order={"addedAt": "desc"}
        )
        return wishlist
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("", response_model=WishlistResponse)
async def add_to_wishlist(item: WishlistCreate, user_id: str = Depends(get_current_user_id)):
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
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{wishlist_id}")
async def remove_from_wishlist(wishlist_id: str, user_id: str = Depends(get_current_user_id)):
    try:
        # Verify item belongs to user
        wishlist_item = await prisma_client.wishlist.find_unique(where={"id": wishlist_id})
        if not wishlist_item or wishlist_item.userId != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to delete this item")
        
        await prisma_client.wishlist.delete(where={"id": wishlist_id})
        return {"message": "Item removed from wishlist"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/items", response_model=WishlistResponse)
async def add_item_to_wishlist(item: WishlistCreate, user_id: str = Depends(get_current_user_id)):
    """Alternative endpoint for adding items to wishlist"""
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
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("")
async def clear_wishlist(user_id: str = Depends(get_current_user_id)):
    try:
        await prisma_client.wishlist.delete_many(where={"userId": user_id})
        return {"message": "Wishlist cleared"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
