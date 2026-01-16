from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import CartItemResponse, CartItemCreate
from prisma import Prisma

router = APIRouter(prefix="/cart", tags=["cart"])
prisma = Prisma()

@router.get("/{user_id}", response_model=List[CartItemResponse])
async def get_cart(user_id: str):
    
    try:
        await prisma.connect()
        cart_items = await prisma.cartitem.find_many(
            where={"userId": user_id},
            order={"createdAt": "desc"}
        )
        await prisma.disconnect()
        return cart_items
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.post("/{user_id}", response_model=CartItemResponse)
async def add_to_cart(user_id: str, item: CartItemCreate):
    
    try:
        await prisma.connect()
        
        price = 0
        if item.productId:
            product = await prisma.product.find_unique(where={"id": item.productId})
            price = product.price if product else 0
        elif item.petId:
            pet = await prisma.pet.find_unique(where={"id": item.petId})
            price = pet.price if pet else 0
        
        cart_item = await prisma.cartitem.create(
            data={
                "userId": user_id,
                "productId": item.productId,
                "petId": item.petId,
                "quantity": item.quantity,
                "price": price
            }
        )
        await prisma.disconnect()
        return cart_item
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.put("/{cart_item_id}", response_model=CartItemResponse)
async def update_cart_item(cart_item_id: str, quantity: int):
    
    try:
        await prisma.connect()
        updated_item = await prisma.cartitem.update(
            where={"id": cart_item_id},
            data={"quantity": quantity}
        )
        await prisma.disconnect()
        return updated_item
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.delete("/{cart_item_id}")
async def remove_from_cart(cart_item_id: str):
    
    try:
        await prisma.connect()
        await prisma.cartitem.delete(where={"id": cart_item_id})
        await prisma.disconnect()
        return {"message": "Item removed from cart"}
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.delete("/{user_id}/clear")
async def clear_cart(user_id: str):
    
    try:
        await prisma.connect()
        await prisma.cartitem.delete_many(where={"userId": user_id})
        await prisma.disconnect()
        return {"message": "Cart cleared"}
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))
