from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

app = FastAPI(title="PetBloom API Test", version="1.0.0")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CORS configuration
cors_origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://petbloom-frontend-five.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test endpoints
@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "PetBloom API",
        "environment": "test"
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "PetBloom API v1.0.0 (Test Server)"}

@app.get("/api/v1/health")
async def api_health():
    """API health check"""
    return {
        "status": "healthy",
        "api_version": "v1"
    }

# Mock endpoints for testing
@app.get("/api/v1/users/profile")
async def get_profile():
    """Mock profile endpoint"""
    return {
        "id": "test-user",
        "email": "test@example.com",
        "name": "Test User"
    }

@app.get("/api/v1/products")
async def get_products():
    """Mock products endpoint"""
    return {
        "products": [
            {"id": 1, "name": "Dog Food", "price": 25.99},
            {"id": 2, "name": "Cat Toy", "price": 9.99}
        ]
    }

@app.get("/api/v1/pets")
async def get_pets():
    """Mock pets endpoint"""
    return {
        "pets": [
            {"id": 1, "name": "Buddy", "species": "Dog"},
            {"id": 2, "name": "Whiskers", "species": "Cat"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
