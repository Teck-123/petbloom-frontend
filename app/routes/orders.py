from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import OrderResponse, OrderCreate
from prisma import Prisma

router = APIRouter(prefix="/orders", tags=["orders"])
prisma = Prisma()

@router.get("/user/{user_id}", response_model=List[OrderResponse])
async def get_user_orders(user_id: str, status: str = None):
    
    try:
        await prisma.connect()
        
        where_clause = {"userId": user_id}
        if status:
            where_clause["status"] = status
        
        orders = await prisma.order.find_many(
            where=where_clause,
            order={"createdAt": "desc"}
        )
        await prisma.disconnect()
        return orders
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str):
    
    try:
        await prisma.connect()
        order = await prisma.order.find_unique(where={"id": order_id})
        await prisma.disconnect()
        
        if not order:
            raise HTTPException(status_code=404, detl="Order not found")
        
        return order
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.post("/{user_id}", response_model=OrderResponse)
async def create_order(user_id: str, order: OrderCreate):
    
    try:
        await prisma.connect()
        
        cart_items = await prisma.cartitem.find_many(
            where={"userId": user_id}
        )
        
        if not cart_items:
            await prisma.disconnect()
            raise HTTPException(status_code=400, detl="Cart is empty")
        
        total_price = sum(item.price * item.quantity for item in cart_items)
        
        new_order = await prisma.order.create(
            data={
                "userId": user_id,
                "status": "pending",
                "totalPrice": total_price,
                "shippingAddress": order.shippingAddress,
                "deliveryOption": order.deliveryOption,
                "pickupLocation": order.pickupLocation
            }
        )
        
        for cart_item in cart_items:
            await prisma.orderitem.create(
                data={
                    "orderId": new_order.id,
                    "productId": cart_item.productId,
                    "petId": cart_item.petId,
                    "quantity": cart_item.quantity,
                    "price": cart_item.price
                }
            )
        
        await prisma.cartitem.delete_many(where={"userId": user_id})
        
        await prisma.disconnect()
        return new_order
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.put("/{order_id}/status")
async def update_order_status(order_id: str, status: str):
    
    try:
        await prisma.connect()
        updated_order = await prisma.order.update(
            where={"id": order_id},
            data={"status": status}
        )
        await prisma.disconnect()
        return updated_order
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.put("/{order_id}/tracking")
async def update_tracking(order_id: str, tracking_number: str):
    
    try:
        await prisma.connect()
        updated_order = await prisma.order.update(
            where={"id": order_id},
            data={"trackingNumber": tracking_number}
        )
        await prisma.disconnect()
        return updated_order
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))
