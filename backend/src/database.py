from sqlmodel import create_engine, Session
from sqlalchemy import event
from sqlalchemy.pool import Pool
from typing import Generator
import os
from dotenv import load_dotenv

load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_app.db")

# Create engine
engine = create_engine(DATABASE_URL, echo=False)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

# Create tables if they don't exist
def create_db_and_tables():
    from src.models.user import User
    from src.models.task import Task
    from sqlmodel import SQLModel

    SQLModel.metadata.create_all(engine)