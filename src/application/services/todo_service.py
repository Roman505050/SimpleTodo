import datetime
from typing import Optional
from uuid import UUID

from application.dto.create_todo import CreateTodoDTO
from application.dto.todo import TodoDTO
from application.dto.update_todo import UpdateTodoDTO
from application.interfaces.repositories.todo import ITodoRepository
from domain.entity import TodoEntity


class TodoService:
    def __init__(self, todo_repository: ITodoRepository):
        self.todo_repository = todo_repository

    async def create_todo(self, todo: CreateTodoDTO) -> TodoDTO:
        todo_entity = TodoEntity.factory(
            title=todo.title,
            description=todo.description,
            deadline=todo.deadline,
        )
        todo_entity = await self.todo_repository.save(todo_entity)
        return TodoDTO.from_entity(todo_entity)

    async def update_todo(self, uuid: UUID, todo: UpdateTodoDTO) -> TodoDTO:
        todo_entity = await self.todo_repository.get(uuid)
        if todo.done is not None:
            if todo.done:
                todo_entity.mark_as_done()
            else:
                todo_entity.mark_as_undone()
        if todo.title is not None:
            todo_entity.update_title(todo.title)
        if todo.description is not None:
            todo_entity.update_description(todo.description)
        todo_entity = await self.todo_repository.update(todo_entity)
        return TodoDTO.from_entity(todo_entity)

    async def update_todo_deadline(
        self, uuid: UUID, deadline: Optional[datetime.datetime]
    ) -> TodoDTO:
        todo_entity = await self.todo_repository.get(uuid)
        todo_entity.update_deadline(deadline)
        todo_entity = await self.todo_repository.update(todo_entity)
        return TodoDTO.from_entity(todo_entity)

    async def get_todo(self, uuid: UUID) -> TodoDTO:
        todo_entity = await self.todo_repository.get(uuid)
        return TodoDTO.from_entity(todo_entity)

    async def list_todos(self) -> list[TodoDTO]:
        todo_entities = await self.todo_repository.list()
        return [TodoDTO.from_entity(entity) for entity in todo_entities]

    async def delete_todo(self, uuid: UUID) -> None:
        await self.todo_repository.delete(uuid)
