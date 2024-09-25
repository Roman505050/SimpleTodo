from abc import ABC, abstractmethod
from uuid import UUID

from domain.entity import TodoEntity


class ITodoRepository(ABC):
    @abstractmethod
    async def save(self, todo: TodoEntity) -> TodoEntity:
        raise NotImplementedError

    @abstractmethod
    async def get(self, uuid: UUID) -> TodoEntity:
        raise NotImplementedError

    @abstractmethod
    async def list(self) -> list[TodoEntity]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, todo: TodoEntity) -> TodoEntity:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, uuid: UUID) -> None:
        raise NotImplementedError
