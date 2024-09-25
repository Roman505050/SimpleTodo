from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4
import datetime


@dataclass
class TodoEntity:
    uuid: UUID
    title: str
    description: str
    done: bool
    deadline: Optional[datetime.datetime]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @staticmethod
    def factory(
        title: str,
        description: str,
        deadline: Optional[datetime.datetime] = None,
    ):
        return TodoEntity(
            uuid=uuid4(),
            title=title,
            description=description,
            done=False,
            deadline=deadline,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            updated_at=datetime.datetime.now(datetime.timezone.utc),
        )

    def mark_as_done(self):
        self.done = True
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def mark_as_undone(self):
        self.done = False
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def is_overdue(self) -> bool:
        if self.deadline and not self.done:
            return datetime.datetime.now(datetime.timezone.utc) > self.deadline
        return False

    def time_until_deadline(self) -> Optional[datetime.timedelta]:
        if self.deadline:
            return self.deadline - datetime.datetime.now(datetime.timezone.utc)
        return None

    def update_title(self, title: str):
        self.title = title
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def update_description(self, description: str):
        self.description = description
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def update_deadline(self, deadline: Optional[datetime.datetime]):
        self.deadline = deadline
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)
