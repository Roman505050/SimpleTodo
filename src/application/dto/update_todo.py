from pydantic import BaseModel, Field
from typing import Optional
import datetime


class UpdateTodoDTO(BaseModel):
    title: Optional[str] = Field(default=None, max_length=64)
    description: Optional[str] = Field(default=None, max_length=255)
    done: Optional[bool] = Field(default=None)
