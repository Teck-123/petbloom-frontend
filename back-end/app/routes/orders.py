from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas import OrderResponse, OrderCreate
from app.services.prisma_client import prisma_client
from app.services.auth_helper import get_current_user_id

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("", response_model=List[OrderResponse])
async def get_user_orders(status: str = None, user_id: str = Depends(get_current_user_id)):
    try:
        where_clause = {"userId": user_id}
        if status:
            where_clause["status"] = status
        
        orders = await prisma_client.order.find_many(
            where=where_clause,
            order={"createdAt": "desc"}
        )
        return orders
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str, user_id: str = Depends(get_current_user_id)):
    try:
        order = await prisma_client.order.find_unique(where={"id": order_id})
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        if order.userId != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to view this order")
        return order
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("", response_model=OrderResponse)
async def create_order(order: OrderCreate, user_id: str = Depends(get_current_user_id)):
    try:
        cart_items = await prisma_client.cartitem.find_many(
            where={"userId": user_id}
        )
        
        if not cart_items:
            raise HTTPException(status_code=400, detail="Cart is empty")
        
        total_price = sum(item.price * item.quantity for item in cart_items)
        
        new_order = await prisma_client.order.create(
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
            await prisma_client.orderitem.create(
                data={
                    "orderId": new_order.id,
                    "productId": cart_item.productId,
                    "petId": cart_item.petId,
                    "quantity": cart_item.quantity,
                    "price": cart_item.price
                }
            )
        
        await prisma_client.cartitem.delete_many(where={"userId": user_id})
        return new_order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{order_id}/status")
async def update_order_status(order_id: str, status: str, user_id: str = Depends(get_current_user_id)):
    try:
        order = await prisma_client.order.find_unique(where={"id": order_id})
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        if order.userId != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this order")
        
        updated_order = await prisma_client.order.update(
            where={"id": order_id},
            data={"status": status}
        )
        return updated_order
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{order_id}/tracking")
async def update_tracking(order_id: str, tracking_number: str, user_id: str = Depends(get_current_user_id)):
    try:
        order = await prisma_client.order.find_unique(where={"id": order_id})
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        if order.userId != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this order")
        
        updated_order = await prisma_client.order.update(
            where={"id": order_id},
            data={"trackingNumber": tracking_number}
        )
        return updated_order
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
