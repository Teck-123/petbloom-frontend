from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from app.schemas import MessageCreate, MessageResponse
from app.services.prisma_client import prisma_client

router = APIRouter(prefix="/messages", tags=["messages"])

@router.get("/inbox")
async def get_inbox(authorization: Optional[str] = Header(None)):
    """Get all messages for the current user"""
    try:
        userId = "temp_user"  # In production, extract from token
        
        messages = await prisma_client.message.find_many(
            where={"recipientId": userId},
            order={"createdAt": "desc"}
        )
        return messages
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/conversation/{sender_id}")
async def get_conversation(sender_id: str, authorization: Optional[str] = Header(None)):
    """Get conversation with a specific user"""
    try:
        userId = "temp_user"  # In production, extract from token
        
        messages = await prisma_client.message.find_many(
            where={
                "OR": [
                    {"senderId": userId, "recipientId": sender_id},
                    {"senderId": sender_id, "recipientId": userId}
                ]
            },
            order={"createdAt": "asc"}
        )
        
        # Mark as read
        await prisma_client.message.update_many(
            where={
                "senderId": sender_id,
                "recipientId": userId,
                "read": False
            },
            data={"read": True}
        )
        
        return messages
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("", response_model=MessageResponse)
async def send_message(message: MessageCreate, authorization: Optional[str] = Header(None)):
    """Send a message"""
    try:
        senderId = "temp_user"  # In production, extract from token
        
        if senderId == message.recipientId:
            raise HTTPException(status_code=400, detail="You cannot send messages to yourself")
        
        new_message = await prisma_client.message.create(
            data={
                "senderId": senderId,
                "recipientId": message.recipientId,
                "content": message.content,
                "read": False
            }
        )
        return new_message
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{message_id}", response_model=MessageResponse)
async def get_message(message_id: str, authorization: Optional[str] = Header(None)):
    """Get a specific message"""
    try:
        userId = "temp_user"  # In production, extract from token
        
        message = await prisma_client.message.find_unique(where={"id": message_id})
        if not message:
            raise HTTPException(status_code=404, detail="Message not found")
        
        # Only sender and recipient can view
        if message.senderId != userId and message.recipientId != userId:
            raise HTTPException(status_code=403, detail="You don't have permission to view this message")
        
        return message
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{message_id}/read")
async def mark_message_read(message_id: str, authorization: Optional[str] = Header(None)):
    """Mark a message as read"""
    try:
        userId = "temp_user"  # In production, extract from token
        
        message = await prisma_client.message.find_unique(where={"id": message_id})
        if not message:
            raise HTTPException(status_code=404, detail="Message not found")
        
        if message.recipientId != userId:
            raise HTTPException(status_code=403, detail="You can only mark your own messages as read")
        
        updated = await prisma_client.message.update(
            where={"id": message_id},
            data={"read": True}
        )
        return updated
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
