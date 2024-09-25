from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from loguru import logger
from uuid import UUID

from api.v1.todo.dependencies import get_todo_service
from application.dto.create_todo import CreateTodoDTO
from application.dto.todo import TodoDTO
from application.dto.update_todo import UpdateTodoDTO
from application.exceptions.not_found import TodoNotFound
from application.services.todo_service import TodoService

router = APIRouter()


@router.get("/all", response_model=list[TodoDTO])
async def get_all_todos(todo_service: TodoService = Depends(get_todo_service)):
    try:
        return await todo_service.list_todos()
    except Exception as e:
        logger.error(f"Error getting all todos: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@router.post("", response_model=TodoDTO, status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo: CreateTodoDTO, todo_service: TodoService = Depends(get_todo_service)
):
    try:
        return await todo_service.create_todo(todo)
    except Exception as e:
        logger.error(f"Error creating todo: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@router.get("/{todo_uuid}", response_model=TodoDTO)
async def get_todo(
    todo_uuid: UUID, todo_service: TodoService = Depends(get_todo_service)
):
    try:
        return await todo_service.get_todo(todo_uuid)
    except TodoNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error getting todo: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@router.put("/{todo_uuid}", response_model=TodoDTO)
async def update_todo(
    todo_uuid: UUID,
    todo: UpdateTodoDTO,
    todo_service: TodoService = Depends(get_todo_service),
):
    try:
        return await todo_service.update_todo(todo_uuid, todo)
    except TodoNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error updating todo: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@router.delete("/{todo_uuid}")
async def delete_todo(
    todo_uuid: UUID, todo_service: TodoService = Depends(get_todo_service)
):
    try:
        await todo_service.delete_todo(todo_uuid)
        return {"message": "Todo deleted"}
    except Exception as e:
        logger.error(f"Error deleting todo: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong")
