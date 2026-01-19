#!/usr/bin/env python3
"""
Minimal PetBloom API server - for demo purposes
Runs a basic FastAPI server without database requirements
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="PetBloom API", version="1.0.0-demo")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data
mock_products = [
    {
        "id": "1",
        "name": "Premium Dog Food",
        "price": 29.99,
        "category": "food",
        "image": "https://via.placeholder.com/200?text=Dog+Food",
        "description": "High-quality nutrition for your furry friend"
    },
    {
        "id": "2",
        "name": "Cat Toy Ball",
        "price": 9.99,
        "category": "toys",
        "image": "https://via.placeholder.com/200?text=Cat+Toy",
        "description": "Interactive toy for cats"
    },
    {
        "id": "3",
        "name": "Pet Collar",
        "price": 14.99,
        "category": "accessories",
        "image": "https://via.placeholder.com/200?text=Collar",
        "description": "Comfortable and durable pet collar"
    }
]

mock_pets = [
    {
        "id": "1",
        "name": "Fluffy",
        "type": "cat",
        "breed": "Persian",
        "age": 3
    },
    {
        "id": "2",
        "name": "Max",
        "type": "dog",
        "breed": "Golden Retriever",
        "age": 5
    }
]

@app.get("/health")
async def health():
    return {"status": "healthy", "message": "PetBloom API is running (demo mode)"}

@app.get("/")
async def root():
    return {"message": "PetBloom API v1.0.0 (Demo Mode)", "note": "Database connection not configured"}

@app.get("/api/v1/products")
async def get_products():
    return {"products": mock_products}

@app.get("/api/v1/products/{product_id}")
async def get_product(product_id: str):
    for p in mock_products:
        if p["id"] == product_id:
            return p
    return {"error": "Product not found"}, 404

@app.get("/api/v1/pets")
async def get_pets():
    return {"pets": mock_pets}

@app.post("/api/v1/auth/register")
async def register(data: dict):
    return {"message": "User registration (demo - not persisted)", "user": data}

@app.post("/api/v1/auth/login")
async def login(data: dict):
    return {
        "message": "Login successful (demo)",
        "access_token": "demo_token_12345",
        "user": {"id": "1", "email": data.get("email")}
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
