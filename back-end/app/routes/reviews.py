from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from app.schemas import ReviewCreate, ReviewResponse
from app.services.prisma_client import prisma_client
from app.routes.users import get_current_user

router = APIRouter(prefix="/reviews", tags=["reviews"])

def get_user_from_token(authorization: Optional[str] = Header(None)):
    """Extract user from token"""
    if not authorization:
        return None
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            return None
    except ValueError:
        return None
    return None  # In production, decode token here

@router.post("", response_model=ReviewResponse)
async def create_review(review: ReviewCreate, authorization: Optional[str] = Header(None)):
    """Create a review for a product or pet"""
    try:
        # In production, extract userId from token
        userId = "temp_user"
        
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
async def delete_review(review_id: str, authorization: Optional[str] = Header(None)):
    """Delete a review"""
    try:
        userId = "temp_user"  # In production, extract from token
        
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
