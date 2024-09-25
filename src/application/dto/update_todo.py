from pydantic import BaseModel, Field
from typing import Optional
import datetime


class UpdateTodoDTO(BaseModel):
    title: str = Field(default=..., max_length=64)
    description: str = Field(default=..., max_length=255)
    done: bool = Field(default=...)
    deadline: Optional[datetime.datetime] = Field(default=None)
