from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from src.services.auth_service import AuthService
from sqlmodel import Session
from src.database import get_session
from src.models.user import User
from sqlmodel import select
from typing import Optional

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db_session: Session = Depends(get_session)
) -> User:
    """
    Get current user based on JWT token
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = AuthService.decode_access_token(credentials.credentials)
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # Get user from database
    statement = select(User).where(User.id == user_id)
    user = db_session.exec(statement).first()
    if user is None:
        raise credentials_exception

    return user