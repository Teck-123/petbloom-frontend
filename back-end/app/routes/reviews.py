from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from app.schemas import ReviewCreate, ReviewResponse
from app.services.prisma_client import prisma_client
from app.services.auth_helper import get_current_user_id

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("", response_model=ReviewResponse)
async def create_review(review: ReviewCreate, user_id: str = Depends(get_current_user_id)):
    """Create a review for a product or pet"""
    try:
        userId = user_id
        
        # Validate that either productId or petId is provided
        if not review.productId and not review.petId:
            raise HTTPException(status_code=400, detail="Either productId or petId must be provided")
        
        # Check if review already exists
        existing = await prisma_client.review.find_first(
            where={
                "userId": userId,
                "productId": review.productId,
                "petId": review.petId
            }
        )
        if existing:
            raise HTTPException(status_code=400, detail="You have already reviewed this item")
        
        new_review = await prisma_client.review.create(
            data={
                "userId": userId,
                "productId": review.productId,
                "petId": review.petId,
                "rating": review.rating,
                "comment": review.comment
            }
        )
        return new_review
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/product/{product_id}")
async def get_product_reviews(product_id: str):
    """Get all reviews for a product"""
    try:
        reviews = await prisma_client.review.find_many(
            where={"productId": product_id},
            order={"createdAt": "desc"}
        )
        avg_rating = 0
        if reviews:
            total_rating = sum(r.rating for r in reviews)
            avg_rating = total_rating / len(reviews)
        
        return {
            "reviews": reviews,
            "count": len(reviews),
            "averageRating": round(avg_rating, 1)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/pet/{pet_id}")
async def get_pet_reviews(pet_id: str):
    """Get all reviews for a pet"""
    try:
        reviews = await prisma_client.review.find_many(
            where={"petId": pet_id},
            order={"createdAt": "desc"}
        )
        avg_rating = 0
        if reviews:
            total_rating = sum(r.rating for r in reviews)
            avg_rating = total_rating / len(reviews)
        
        return {
            "reviews": reviews,
            "count": len(reviews),
            "averageRating": round(avg_rating, 1)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{review_id}", response_model=ReviewResponse)
async def get_review(review_id: str):
    """Get a specific review"""
    try:
        review = await prisma_client.review.find_unique(where={"id": review_id})
        if not review:
            raise HTTPException(status_code=404, detail="Review not found")
        return review
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{review_id}")
async def delete_review(review_id: str, user_id: str = Depends(get_current_user_id)):
    """Delete a review"""
    try:
        userId = user_id
        
        review = await prisma_client.review.find_unique(where={"id": review_id})
        if not review:
            raise HTTPException(status_code=404, detail="Review not found")
        
        if review.userId != userId:
            raise HTTPException(status_code=403, detail="You can only delete your own reviews")
        
        await prisma_client.review.delete(where={"id": review_id})
        return {"message": "Review deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
