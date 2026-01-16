from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import ProductResponse, ProductCreate
from app.services.prisma_client import prisma_client

router = APIRouter(prefix="/products", tags=["products"])

@router.get("", response_model=List[ProductResponse])
async def get_products(skip: int = 0, limit: int = 20, category: str = None, petType: str = None):
    try:
        prisma = await prisma_client.connect()
        where_clause = {}
        if category:
            where_clause["category"] = category
        if petType:
            where_clause["petType"] = petType
        products = await prisma.product.find_many(where=where_clause, skip=skip, take=limit, order={"createdAt": "desc"})
        return products
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    try:
        await prisma.connect()
        product = await prisma.product.find_unique(where={"id": product_id})
        await prisma.disconnect()
        if not product:
            raise HTTPException(status_code=404, detl="Product not found")
        return product
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.post("", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    try:
        await prisma.connect()
        new_product = await prisma.product.create(data=product.dict())
        await prisma.disconnect()
        return new_product
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, product_update: ProductCreate):
    try:
        await prisma.connect()
        updated_product = await prisma.product.update(where={"id": product_id}, data=product_update.dict())
        await prisma.disconnect()
        return updated_product
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.delete("/{product_id}")
async def delete_product(product_id: str):
    try:
        await prisma.connect()
        await prisma.product.delete(where={"id": product_id})
        await prisma.disconnect()
        return {"message": "Product deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))
