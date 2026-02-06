from sqlmodel import Session, select
from typing import List, Optional
from fastapi import HTTPException, status
from uuid import UUID
from src.models.task import Task, TaskCreate, TaskUpdate
from src.models.user import User
from datetime import datetime


class TaskService:
    @classmethod
    def create_task(cls, db_session: Session, task_create: TaskCreate, user_id: UUID) -> Task:
        # Create task with the provided user_id
        task_dict = task_create.dict()
        db_task = Task(**task_dict, user_id=user_id)
        db_session.add(db_task)
        db_session.commit()
        db_session.refresh(db_task)
        return db_task

    @classmethod
    def get_tasks_by_user_id(cls, db_session: Session, user_id: UUID,
                            status: Optional[str] = None,
                            priority: Optional[str] = None,
                            search: Optional[str] = None,
                            limit: int = 50,
                            offset: int = 0) -> List[Task]:
        statement = select(Task).where(Task.user_id == user_id)

        # Apply filters if provided
        if status:
            statement = statement.where(Task.status == status)
        if priority:
            statement = statement.where(Task.priority == priority)
        if search:
            from sqlalchemy import or_
            # Simple search that looks in title; if description exists, also search there
            statement = statement.where(Task.title.contains(search))
            # For now, just search in title to avoid issues with null descriptions

        # Apply pagination
        statement = statement.offset(offset).limit(limit)

        tasks = db_session.exec(statement).all()
        return tasks

    @classmethod
    def get_task_by_id(cls, db_session: Session, task_id: UUID, user_id: UUID) -> Optional[Task]:
        statement = select(Task).where(Task.id == task_id).where(Task.user_id == user_id)
        task = db_session.exec(statement).first()
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        return task

    @classmethod
    def update_task(cls, db_session: Session, task_id: UUID, task_update: TaskUpdate, user_id: UUID) -> Task:
        db_task = cls.get_task_by_id(db_session, task_id, user_id)

        # Update fields that were provided
        update_data = task_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)

        # Update the timestamp
        db_task.updated_at = datetime.utcnow()

        # If status is completed, set completed_at timestamp
        if db_task.status == "completed" and not db_task.completed_at:
            db_task.completed_at = datetime.utcnow()

        db_session.add(db_task)
        db_session.commit()
        db_session.refresh(db_task)
        return db_task

    @classmethod
    def delete_task(cls, db_session: Session, task_id: UUID, user_id: UUID) -> bool:
        db_task = cls.get_task_by_id(db_session, task_id, user_id)

        db_session.delete(db_task)
        db_session.commit()
        return True