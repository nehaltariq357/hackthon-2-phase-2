from fastapi import APIRouter, Depends
from src.models.user import UserPublic
from src.auth.jwt_bearer import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserPublic)
def get_current_user_info(current_user: UserPublic = Depends(get_current_user)):
    """
    Get current user information
    """
    return current_user