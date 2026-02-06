from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from uuid import UUID
from src.auth.jwt_bearer import get_current_user
from src.models.user import User
from src.models.task import Task, TaskCreate, TaskUpdate, TaskRead
from src.services.task_service import TaskService
from sqlmodel import Session
from src.database import get_session

router = APIRouter()

@router.get("/", response_model=List[TaskRead])
def get_tasks(
    status: Optional[str] = Query(None, description="Filter tasks by status"),
    priority: Optional[str] = Query(None, description="Filter tasks by priority"),
    search: Optional[str] = Query(None, description="Search tasks by title or description"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of tasks to return"),
    offset: int = Query(0, ge=0, description="Number of tasks to skip for pagination"),
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
):
    """
    Get all tasks for the current user with optional filtering
    """
    tasks = TaskService.get_tasks_by_user_id(
        db_session, current_user.id, status, priority, search, limit, offset
    )
    return tasks


@router.post("/", response_model=TaskRead)
def create_task(
    task_create: TaskCreate,
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
):
    """
    Create a new task for the current user
    """
    return TaskService.create_task(db_session, task_create, current_user.id)


@router.get("/{task_id}", response_model=TaskRead)
def get_task(
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
):
    """
    Get a specific task by ID
    """
    return TaskService.get_task_by_id(db_session, task_id, current_user.id)


@router.put("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: UUID,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
):
    """
    Update a specific task by ID
    """
    return TaskService.update_task(db_session, task_id, task_update, current_user.id)


@router.delete("/{task_id}")
def delete_task(
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
):
    """
    Delete a specific task by ID
    """
    TaskService.delete_task(db_session, task_id, current_user.id)
    return {"message": "Task deleted successfully"}