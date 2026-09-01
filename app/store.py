"""In-memory storage.

Deliberately not a database. The point of this service is to be something that
starts with one command and answers requests, so there is nothing to provision
before it can be exercised.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Optional

from app.models import Status, Task, TaskCreate, TaskUpdate

_tasks: dict[str, Task] = {}


def _now() -> datetime:
    return datetime.now(timezone.utc)


def reset() -> None:
    _tasks.clear()


def create(payload: TaskCreate) -> Task:
    task = Task(
        id=str(uuid.uuid4()),
        title=payload.title,
        notes=payload.notes,
        status=payload.status,
        created_at=_now(),
        updated_at=_now(),
    )
    _tasks[task.id] = task
    return task


def get(task_id: str) -> Optional[Task]:
    return _tasks.get(task_id)


def list_tasks(
    *, status: Optional[Status] = None, limit: int = 50, offset: int = 0
) -> tuple[list[Task], int]:
    matching = [t for t in _tasks.values() if status is None or t.status == status]
    matching.sort(key=lambda t: t.created_at, reverse=True)
    return matching[offset : offset + limit], len(matching)


def update(task_id: str, payload: TaskUpdate) -> Optional[Task]:
    task = _tasks.get(task_id)
    if task is None:
        return None
    fields = payload.model_dump(exclude_unset=True, exclude_none=True)
    if fields:
        task = task.model_copy(update={**fields, "updated_at": _now()})
        _tasks[task_id] = task
    return task


def delete(task_id: str) -> bool:
    return _tasks.pop(task_id, None) is not None


def counts() -> dict[str, int]:
    tally = {status.value: 0 for status in Status}
    for task in _tasks.values():
        tally[task.status.value] += 1
    return tally
