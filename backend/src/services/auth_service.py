from datetime import datetime, timedelta
from typing import Optional
from sqlmodel import Session, select
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi import HTTPException, status
from src.models.user import User, UserCreate, UserLogin

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT configuration - these should come from settings in production
SECRET_KEY = "your-super-secret-jwt-key-change-in-production"  # Should be loaded from env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class AuthService:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        # Truncate password to 72 characters to avoid bcrypt limit
        truncated_password = password[:72] if len(password) > 72 else password
        return pwd_context.hash(truncated_password)

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_access_token(token: str) -> Optional[dict]:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: str = payload.get("sub")
            if user_id is None:
                return None
            return {"user_id": user_id}
        except JWTError:
            return None

    @classmethod
    def authenticate_user(cls, db_session: Session, email: str, password: str) -> Optional[User]:
        statement = select(User).where(User.email == email)
        user = db_session.exec(statement).first()
        if not user or not cls.verify_password(password, user.hashed_password):
            return None
        return user

    @classmethod
    def register_user(cls, db_session: Session, user_create: UserCreate) -> User:
        # Check if user already exists
        statement = select(User).where(User.email == user_create.email)
        existing_user = db_session.exec(statement).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

        # Hash the password
        hashed_password = cls.get_password_hash(user_create.password)

        # Create new user
        db_user = User(email=user_create.email, hashed_password=hashed_password)
        db_session.add(db_user)
        db_session.commit()
        db_session.refresh(db_user)

        return db_user