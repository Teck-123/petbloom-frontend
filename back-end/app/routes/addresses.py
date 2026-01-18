from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from app.schemas import UserAddressCreate, UserAddressResponse
from app.services.prisma_client import prisma_client

router = APIRouter(prefix="/addresses", tags=["addresses"])

@router.get("")
async def get_user_addresses(authorization: Optional[str] = Header(None)):
    """Get all addresses for the current user"""
    try:
        userId = "temp_user"  # In production, extract from token
        
        addresses = await prisma_client.useraddress.find_many(
            where={"userId": userId},
            order={"createdAt": "desc"}
        )
        return addresses
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("", response_model=UserAddressResponse)
async def create_address(address: UserAddressCreate, authorization: Optional[str] = Header(None)):
    """Create a new address"""
    try:
        userId = "temp_user"  # In production, extract from token
        
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
async def get_address(address_id: str, authorization: Optional[str] = Header(None)):
    """Get a specific address"""
    try:
        userId = "temp_user"  # In production, extract from token
        
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
async def update_address(address_id: str, address: UserAddressCreate, authorization: Optional[str] = Header(None)):
    """Update an address"""
    try:
        userId = "temp_user"  # In production, extract from token
        
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
async def delete_address(address_id: str, authorization: Optional[str] = Header(None)):
    """Delete an address"""
    try:
        userId = "temp_user"  # In production, extract from token
        
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
