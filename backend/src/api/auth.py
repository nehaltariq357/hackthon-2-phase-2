from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Dict
from src.database import get_session
from src.models.user import UserCreate, UserLogin, UserPublic
from src.services.auth_service import AuthService

router = APIRouter()

@router.post("/register", response_model=UserPublic)
def register(user_create: UserCreate, db_session: Session = Depends(get_session)):
    """
    Register a new user
    """
    try:
        db_user = AuthService.register_user(db_session, user_create)
        # Return public user info without sensitive data
        return UserPublic(id=db_user.id, email=db_user.email, is_active=db_user.is_active)
    except Exception as e:
        raise e


@router.post("/login")
def login(user_login: UserLogin, db_session: Session = Depends(get_session)) -> Dict:
    """
    Authenticate user and return JWT token
    """
    user = AuthService.authenticate_user(db_session, user_login.email, user_login.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=AuthService.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthService.create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": UserPublic(id=user.id, email=user.email, is_active=user.is_active)
    }


@router.post("/logout")
def logout():
    """
    Invalidate user session (client-side token removal)
    """
    return {"message": "Successfully logged out"}