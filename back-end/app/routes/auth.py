from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.services.fbase_service import verify_fbase_token
from app.services.prisma_client import prisma_client
import jwt
from datetime import datetime, timedelta
from app.config import get_settings

router = APIRouter(prefix="/auth", tags=["auth"])
settings = get_settings()

class LoginRequest(BaseModel):
    token: str

class LoginResponse(BaseModel):
    id: str
    email: str
    name: str
    access_token: str

def create_access_token(user_id: str, email: str):
    """Create JWT access token"""
    payload = {
        "sub": user_id,
        "email": email,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """
    Login endpoint - Verifies Firebase token and creates user if needed
    """
    try:
        # Verify Firebase token
        decoded = verify_fbase_token(request.token)
        if not decoded:
            raise HTTPException(status_code=401, detail="Invalid Firebase token")
        
        firebase_uid = decoded.get("uid")
        email = decoded.get("email")
        
        if not firebase_uid or not email:
            raise HTTPException(status_code=400, detail="Invalid token - missing uid or email")
        
        # Try to find existing user
        user = await prisma_client.user.find_unique(where={"firebaseUid": firebase_uid})
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found. Please register first.")
        
        # Create JWT access token
        access_token = create_access_token(user.id, user.email)
        
        return {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "access_token": access_token
        }
    
    except HTTPException:
        raise
    except Exception as e:
        print(f"Login error: {str(e)}")
        raise HTTPException(status_code=500, detail="Login failed")
