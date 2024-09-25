from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from application.services.todo_service import TodoService
from infrastructure.database.connext import get_session_dependency
from infrastructure.repositories.todo import TodoRepository


def get_todo_service(
    session: AsyncSession = Depends(get_session_dependency),
) -> TodoService:
    return TodoService(TodoRepository(session))
