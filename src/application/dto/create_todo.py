from pydantic import BaseModel, Field
from typing import Optional
import datetime


class CreateTodoDTO(BaseModel):
    title: str = Field(default=..., max_length=64)
    description: str = Field(default=..., max_length=255)
    deadline: Optional[datetime.datetime] = Field(default=None)
