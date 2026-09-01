from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Status(str, Enum):
    todo = "todo"
    doing = "doing"
    done = "done"


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    notes: str = Field(default="", max_length=2000)
    status: Status = Status.todo


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    notes: Optional[str] = Field(default=None, max_length=2000)
    status: Optional[Status] = None


class Task(BaseModel):
    id: str
    title: str
    notes: str
    status: Status
    created_at: datetime
    updated_at: datetime


class TaskPage(BaseModel):
    items: list[Task]
    total: int
    limit: int
    offset: int


class Stats(BaseModel):
    total: int
    todo: int
    doing: int
    done: int
