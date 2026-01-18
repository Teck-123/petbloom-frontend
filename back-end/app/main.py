from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.config import get_settings
from app.routes import users, pets, products, cart, wishlist, orders, uploads, seed, reviews, addresses, messages
from app.services.prisma_client import prisma_client
import os
import logging

settings = get_settings()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="PetBloom API", version="1.0.0")

# CORS - adjust for production
cors_origins = [settings.FRONTEND_URL]
if settings.ENVIRONMENT == "development":
    cors_origins.extend(["http://localhost:5173", "http://localhost:3000"])
# Also add Vercel preview URLs for testing
cors_origins.extend(["https://pet-bloom.vercel.app"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await prisma_client.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma_client.disconnect()

app.include_router(users.router, prefix="/api/v1")
app.include_router(pets.router, prefix="/api/v1")
app.include_router(products.router, prefix="/api/v1")
app.include_router(cart.router, prefix="/api/v1")
app.include_router(wishlist.router, prefix="/api/v1")
app.include_router(orders.router, prefix="/api/v1")
app.include_router(uploads.router, prefix="/api/v1")
app.include_router(seed.router, prefix="/api/v1")
app.include_router(reviews.router, prefix="/api/v1")
app.include_router(addresses.router, prefix="/api/v1")
app.include_router(messages.router, prefix="/api/v1")

if os.path.exists("uploads"):
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/")
async def root():
    return {"message": "PetBloom API v1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
