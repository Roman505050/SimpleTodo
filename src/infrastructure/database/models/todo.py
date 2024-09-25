from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import (
    UUID as PgUUID,
)
from uuid import uuid4, UUID
import datetime

from domain.entity import TodoEntity
from infrastructure.database.base import Base, created_at, updated_at


class Todo(Base):
    __tablename__ = "todos"

    uuid: Mapped[UUID] = mapped_column(
        PgUUID(as_uuid=True), primary_key=True, default=uuid4
    )
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    done: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    deadline: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    @staticmethod
    def from_entity(entity: "TodoEntity") -> "Todo":
        return Todo(
            uuid=entity.uuid,
            title=entity.title,
            description=entity.description,
            done=entity.done,
            deadline=entity.deadline,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> TodoEntity:
        return TodoEntity(
            uuid=self.uuid,
            title=self.title,
            description=self.description,
            done=self.done,
            deadline=self.deadline,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
