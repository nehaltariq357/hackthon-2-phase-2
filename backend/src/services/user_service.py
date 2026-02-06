from sqlmodel import Session, select
from typing import Optional
from fastapi import HTTPException, status
from uuid import UUID
from src.models.user import User


class UserService:
    @classmethod
    def get_current_user_by_id(cls, db_session: Session, user_id: UUID) -> Optional[User]:
        statement = select(User).where(User.id == user_id)
        user = db_session.exec(statement).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user

    @classmethod
    def verify_user_owns_resource(cls, db_session: Session, user_id: UUID, resource_user_id: UUID) -> bool:
        """
        Verify that a user owns a specific resource (used for data isolation)
        """
        return user_id == resource_user_id