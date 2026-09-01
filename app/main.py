"""A small task service.

Nine routes over one resource: enough for endpoint discovery to find something
worth testing, and small enough that the whole thing starts in a second.
"""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Query, Response, status

from app import store
from app.models import (
    QueueEstimate,
    QueueOrder,
    Stats,
    Status,
    Task,
    TaskCreate,
    TaskPage,
    TaskUpdate,
)

app = FastAPI(
    title="Task Service",
    version="1.0.1",
    description="A small task tracker used to exercise PreMan end to end.",
)


@app.get("/health", tags=["ops"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ready", tags=["ops"])
def ready() -> dict[str, object]:
    return {"ready": True, "tasks": len(store.list_tasks(limit=1_000_000)[0])}


@app.get("/stats", response_model=Stats, tags=["ops"])
def stats() -> Stats:
    tally = store.counts()
    return Stats(total=sum(tally.values()), **tally)


@app.get("/version", tags=["ops"])
def version() -> dict[str, str]:
    return {"service": app.title, "version": app.version}


@app.get("/tasks/{task_id}/summary", tags=["tasks"])
def task_summary(task_id: str) -> dict[str, object]:
    task = store.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {
        "id": task.id,
        "title": task.title,
        "status": task.status,
        "is_done": task.status == Status.done,
    }


@app.get("/tasks/{task_id}/neighbours", tags=["tasks"])
def task_neighbours(task_id: str) -> dict[str, object]:
    """The tasks created either side of this one, newest first."""
    items, _ = store.list_tasks(limit=1_000_000)
    position = [task.id for task in items].index(task_id)
    return {
        "task_id": task_id,
        "position": position,
        "newer": items[position - 1].id if position > 0 else None,
        "older": items[position + 1].id,
    }


@app.get("/tasks", response_model=TaskPage, tags=["tasks"])
def list_tasks(
    status_filter: Optional[Status] = Query(default=None, alias="status"),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
) -> TaskPage:
    items, total = store.list_tasks(status=status_filter, limit=limit, offset=offset)
    return TaskPage(items=items, total=total, limit=limit, offset=offset)


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["tasks"])
def create_task(payload: TaskCreate) -> Task:
    return store.create(payload)


@app.post(
    "/tasks/bulk",
    response_model=list[Task],
    status_code=status.HTTP_201_CREATED,
    tags=["tasks"],
)
def create_tasks(payload: list[TaskCreate]) -> list[Task]:
    if not payload:
        raise HTTPException(status_code=422, detail="nothing to create")
    return [store.create(item) for item in payload]


@app.get("/queue", response_model=TaskPage, tags=["queue"])
def read_queue(limit: int = Query(default=20, ge=1, le=100)) -> TaskPage:
    """Everything still to do, oldest first."""
    items, total = store.list_tasks(status=Status.todo, limit=limit, offset=0)
    items.reverse()
    return TaskPage(items=items, total=total, limit=limit, offset=0)


@app.post(
    "/queue",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
    tags=["queue"],
)
def enqueue(payload: TaskCreate) -> Task:
    """Add to the back of the queue, whatever status was asked for."""
    return store.create(payload.model_copy(update={"status": Status.todo}))


@app.get("/queue/summary", tags=["queue"])
def queue_summary() -> dict[str, object]:
    """The queue's size and its oldest waiting task in one call."""
    items, total = store.list_tasks(status=Status.todo, limit=100, offset=0)
    return {"waiting": total, "oldest": items[-1].id if items else None}


@app.get("/queue/size", tags=["queue"])
def queue_size() -> dict[str, int]:
    return {"size": store.counts()[Status.todo.value]}




@app.post("/queue/reorder", response_model=TaskPage, tags=["queue"])
def reorder_queue(payload: QueueOrder) -> TaskPage:
    """Re-read the queue oldest or newest first. Ordering only, nothing moves."""
    items, total = store.list_tasks(status=Status.todo, limit=100, offset=0)
    if payload.oldest_first:
        items.reverse()
    return TaskPage(items=items, total=total, limit=100, offset=0)


@app.get("/queue/oldest", tags=["queue"])
def oldest_waiting() -> dict[str, object]:
    """The task that has been waiting longest, or nothing if the queue is empty."""
    items, total = store.list_tasks(status=Status.todo, limit=100, offset=0)
    return {"waiting": total, "task": items[-1] if items else None}


@app.post("/queue/estimate", tags=["queue"])
def estimate_queue(payload: QueueEstimate) -> dict[str, object]:
    """How long the queue takes at a given rate. Reads only; nothing moves."""
    waiting = store.counts()[Status.todo.value]
    return {
        "waiting": waiting,
        "per_hour": payload.per_hour,
        "hours": round(waiting / payload.per_hour, 2),
    }


@app.get("/stats/{task_status}", tags=["ops"])
def stats_for(task_status: Status) -> dict[str, object]:
    tally = store.counts()
    return {"status": task_status, "count": tally[task_status.value]}


@app.get("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def get_task(task_id: str) -> Task:
    task = store.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return task


@app.patch("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def update_task(task_id: str, payload: TaskUpdate) -> Task:
    task = store.update(task_id, payload)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["tasks"])
def delete_task(task_id: str) -> Response:
    if not store.delete(task_id):
        raise HTTPException(status_code=404, detail="task not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/tasks/{task_id}/complete", response_model=Task, tags=["tasks"])
def complete_task(task_id: str) -> Task:
    task = store.update(task_id, TaskUpdate(status=Status.done))
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return task


@app.post("/tasks/{task_id}/reopen", response_model=Task, tags=["tasks"])
def reopen_task(task_id: str) -> Task:
    task = store.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    if task.status is not Status.done:
        raise HTTPException(status_code=409, detail="task is not done")
    return store.update(task_id, TaskUpdate(status=Status.todo))
