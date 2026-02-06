from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

# Forward reference for Task model
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from .task import Task

# User model for database
class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False, max_length=255)
    is_active: bool = Field(default=True)


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str = Field(nullable=False, max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to tasks
    tasks: List["Task"] = Relationship(back_populates="user")


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class UserUpdate(SQLModel):
    email: Optional[str] = None
    is_active: Optional[bool] = None


class UserLogin(BaseModel):
    email: str
    password: str


class UserPublic(UserBase):
    id: uuid.UUID