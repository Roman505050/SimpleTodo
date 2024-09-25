from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
import datetime

from domain.entity import TodoEntity


class TodoDTO(BaseModel):
    uuid: UUID
    title: str = Field(default=..., max_length=64)
    description: str = Field(default=..., max_length=256)
    done: bool
    deadline: Optional[datetime.datetime]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @staticmethod
    def from_entity(entity: TodoEntity) -> "TodoDTO":
        return TodoDTO(
            uuid=entity.uuid,
            title=entity.title,
            description=entity.description,
            done=entity.done,
            deadline=entity.deadline,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
