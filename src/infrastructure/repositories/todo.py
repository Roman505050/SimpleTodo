from sqlalchemy import select, update, delete, insert
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from application.exceptions.not_found import TodoNotFound
from infrastructure.database.models.todo import Todo
from application.interfaces.repositories.todo import ITodoRepository
from domain.entity import TodoEntity


class TodoRepository(ITodoRepository):
    model = Todo

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, todo: TodoEntity) -> TodoEntity:
        stmt = insert(self.model).values(
            uuid=todo.uuid,
            title=todo.title,
            description=todo.description,
            done=todo.done,
            deadline=todo.deadline,
            created_at=todo.created_at,
            updated_at=todo.updated_at,
        )
        await self.session.execute(stmt)
        await self.session.commit()
        return todo

    async def get(self, uuid: UUID) -> TodoEntity:
        stmt = select(self.model).filter_by(uuid=uuid)
        result = await self.session.execute(stmt)
        todo = result.scalars().first()
        if not todo:
            raise TodoNotFound(f"Todo with uuid {uuid} not found")
        return todo.to_entity()

    async def list(self) -> list[TodoEntity]:
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return [todo.to_entity() for todo in result.scalars()]

    async def update(self, todo: TodoEntity) -> TodoEntity:
        stmt = (
            update(self.model)
            .filter_by(uuid=todo.uuid)
            .values(
                title=todo.title,
                description=todo.description,
                done=todo.done,
                deadline=todo.deadline,
                updated_at=todo.updated_at,
            )
        )
        await self.session.execute(stmt)
        await self.session.commit()
        return todo

    async def delete(self, uuid: UUID) -> None:
        stmt = delete(self.model).filter_by(uuid=uuid)
        await self.session.execute(stmt)
        await self.session.commit()
