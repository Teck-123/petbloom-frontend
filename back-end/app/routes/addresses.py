from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from app.schemas import UserAddressCreate, UserAddressResponse
from app.services.prisma_client import prisma_client
from app.services.auth_helper import get_current_user_id

router = APIRouter(prefix="/addresses", tags=["addresses"])

@router.get("")
async def get_user_addresses(user_id: str = Depends(get_current_user_id)):
    """Get all addresses for the current user"""
    try:
        userId = user_id
        
        addresses = await prisma_client.useraddress.find_many(
            where={"userId": userId},
            order={"createdAt": "desc"}
        )
        return addresses
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("", response_model=UserAddressResponse)
async def create_address(address: UserAddressCreate, user_id: str = Depends(get_current_user_id)):
    """Create a new address"""
    try:
        userId = user_id
        
        # If this is set as default, unset other defaults
        if address.isDefault:
            await prisma_client.useraddress.update_many(
                where={"userId": userId},
                data={"isDefault": False}
            )
        
        new_address = await prisma_client.useraddress.create(
            data={
                "userId": userId,
                "street": address.street,
                "city": address.city,
                "state": address.state,
                "zipCode": address.zipCode,
                "country": address.country,
                "isDefault": address.isDefault
            }
        )
        return new_address
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{address_id}", response_model=UserAddressResponse)
async def get_address(address_id: str, user_id: str = Depends(get_current_user_id)):
    """Get a specific address"""
    try:
        userId = user_id
        
        address = await prisma_client.useraddress.find_unique(where={"id": address_id})
        if not address:
            raise HTTPException(status_code=404, detail="Address not found")
        
        if address.userId != userId:
            raise HTTPException(status_code=403, detail="You can only view your own addresses")
        
        return address
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{address_id}", response_model=UserAddressResponse)
async def update_address(address_id: str, address: UserAddressCreate, user_id: str = Depends(get_current_user_id)):
    """Update an address"""
    try:
        userId = user_id
        
        existing = await prisma_client.useraddress.find_unique(where={"id": address_id})
        if not existing:
            raise HTTPException(status_code=404, detail="Address not found")
        
        if existing.userId != userId:
            raise HTTPException(status_code=403, detail="You can only update your own addresses")
        
        # If setting as default, unset others
        if address.isDefault and not existing.isDefault:
            await prisma_client.useraddress.update_many(
                where={"userId": userId},
                data={"isDefault": False}
            )
        
        updated = await prisma_client.useraddress.update(
            where={"id": address_id},
            data={
                "street": address.street,
                "city": address.city,
                "state": address.state,
                "zipCode": address.zipCode,
                "country": address.country,
                "isDefault": address.isDefault
            }
        )
        return updated
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{address_id}")
async def delete_address(address_id: str, user_id: str = Depends(get_current_user_id)):
    """Delete an address"""
    try:
        userId = user_id
        
        address = await prisma_client.useraddress.find_unique(where={"id": address_id})
        if not address:
            raise HTTPException(status_code=404, detail="Address not found")
        
        if address.userId != userId:
            raise HTTPException(status_code=403, detail="You can only delete your own addresses")
        
        await prisma_client.useraddress.delete(where={"id": address_id})
        return {"message": "Address deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
