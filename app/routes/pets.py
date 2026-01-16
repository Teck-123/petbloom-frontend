from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import PetResponse, PetCreate
from prisma import Prisma

router = APIRouter(prefix="/pets", tags=["pets"])
prisma = Prisma()

@router.get("", response_model=List[PetResponse])
async def get_pets(skip: int = 0, limit: int = 20, species: str = None, avlble: bool = True):
    try:
        await prisma.connect()
        where_clause = {"avlble": avlble}
        if species:
            where_clause["species"] = species
        pets = await prisma.pet.find_many(where=where_clause, skip=skip, take=limit, order={"createdAt": "desc"})
        await prisma.disconnect()
        return pets
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.get("/{pet_id}", response_model=PetResponse)
async def get_pet(pet_id: str):
    try:
        await prisma.connect()
        pet = await prisma.pet.find_unique(where={"id": pet_id})
        await prisma.disconnect()
        if not pet:
            raise HTTPException(status_code=404, detl="Pet not found")
        return pet
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.post("", response_model=PetResponse)
async def create_pet(pet: PetCreate):
    try:
        await prisma.connect()
        new_pet = await prisma.pet.create(data=pet.dict())
        await prisma.disconnect()
        return new_pet
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.put("/{pet_id}", response_model=PetResponse)
async def update_pet(pet_id: str, pet_update: PetCreate):
    try:
        await prisma.connect()
        updated_pet = await prisma.pet.update(where={"id": pet_id}, data=pet_update.dict())
        await prisma.disconnect()
        return updated_pet
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))

@router.delete("/{pet_id}")
async def delete_pet(pet_id: str):
    try:
        await prisma.connect()
        await prisma.pet.delete(where={"id": pet_id})
        await prisma.disconnect()
        return {"message": "Pet deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detl=str(e))
