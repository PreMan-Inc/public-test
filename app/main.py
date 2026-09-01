"""A small task service.

Nine routes over one resource: enough for endpoint discovery to find something
worth testing, and small enough that the whole thing starts in a second.
"""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Query, Response, status

from app import store
from app.models import Stats, Status, Task, TaskCreate, TaskPage, TaskUpdate

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
