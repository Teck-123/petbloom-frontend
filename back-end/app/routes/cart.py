from fastapi import APIRouter, HTTPException, Depends, Header
from typing import List
from app.schemas import CartItemResponse, CartItemCreate
from app.services.prisma_client import prisma_client
from app.services.auth_helper import get_current_user_id

router = APIRouter(prefix="/cart", tags=["cart"])

@router.get("", response_model=List[CartItemResponse])
async def get_cart(user_id: str = Depends(get_current_user_id)):
    try:
        cart_items = await prisma_client.cartitem.find_many(
            where={"userId": user_id},
            order={"createdAt": "desc"}
        )
        return cart_items
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("", response_model=CartItemResponse)
async def add_to_cart(item: CartItemCreate, user_id: str = Depends(get_current_user_id)):
    try:
        price = 0
        if item.productId:
            product = await prisma_client.product.find_unique(where={"id": item.productId})
            price = product.price if product else 0
        elif item.petId:
            pet = await prisma_client.pet.find_unique(where={"id": item.petId})
            price = pet.price if pet else 0
        
        cart_item = await prisma_client.cartitem.create(
            data={
                "userId": user_id,
                "productId": item.productId,
                "petId": item.petId,
                "quantity": item.quantity,
                "price": price
            }
        )
        return cart_item
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{cart_item_id}", response_model=CartItemResponse)
async def update_cart_item(cart_item_id: str, quantity: int, user_id: str = Depends(get_current_user_id)):
    try:
        # Verify item belongs to user
        cart_item = await prisma_client.cartitem.find_unique(where={"id": cart_item_id})
        if not cart_item or cart_item.userId != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this item")
        
        updated_item = await prisma_client.cartitem.update(
            where={"id": cart_item_id},
            data={"quantity": quantity}
        )
        return updated_item
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{cart_item_id}")
async def remove_from_cart(cart_item_id: str, user_id: str = Depends(get_current_user_id)):
    try:
        # Verify item belongs to user
        cart_item = await prisma_client.cartitem.find_unique(where={"id": cart_item_id})
        if not cart_item or cart_item.userId != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to delete this item")
        
        await prisma_client.cartitem.delete(where={"id": cart_item_id})
        return {"message": "Item removed from cart"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("")
async def clear_cart(user_id: str = Depends(get_current_user_id)):
    try:
        await prisma_client.cartitem.delete_many(where={"userId": user_id})
        return {"message": "Cart cleared"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
