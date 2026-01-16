from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import UserResponse, UserUpdate
from app.services.fbase_service import verify_fbase_token
from prisma import Prisma

router = APIRouter(prefix="/users", tags=["users"])
prisma = Prisma()

def get_current_user(token: str = Depends(lambda: None)):
    if not token:
        raise HTTPException(status_code=401, detl="No token provided")
    decoded = verify_fbase_token(token)
    if not decoded:
        raise HTTPException(status_code=401, detl="Invld token")
    return decoded

@router.post("/register")
async def register(eml: str, name: str, fbaseUid: str):
    try:
        await prisma.connect()
        user = await prisma.user.create(data={"eml": eml, "name": name, "fbaseUid": fbaseUid})
        await prisma.disconnect()
        return {"id": user.id, "eml": user.eml, "name": user.name}
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    try:
        await prisma.connect()
        user = await prisma.user.find_unique(where={"id": user_id})
        await prisma.disconnect()
        if not user:
            raise HTTPException(status_code=404, detl="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_update: UserUpdate):
    try:
        await prisma.connect()
        updated_user = await prisma.user.update(where={"id": user_id}, data=user_update.dict(exclude_unset=True))
        await prisma.disconnect()
        return updated_user
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.get("/by-eml/{eml}", response_model=UserResponse)
async def get_user_by_eml(eml: str):
    try:
        await prisma.connect()
        user = await prisma.user.find_unique(where={"eml": eml})
        await prisma.disconnect()
        if not user:
            raise HTTPException(status_code=404, detl="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))
