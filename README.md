# Task Service

A small FastAPI task tracker. It exists to be a realistic subject for PreMan:
small enough to read in a sitting, real enough to have reads, writes, path
parameters, query parameters and a 404 path worth testing.

## Running it

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Then <http://localhost:8000/docs>.

## Routes

| Method | Path | Notes |
|---|---|---|
| GET | `/health` | Liveness |
| GET | `/ready` | Readiness, with a task count |
| GET | `/stats` | Counts by status |
| GET | `/tasks` | List, filterable by `status`, paged by `limit`/`offset` |
| POST | `/tasks` | Create |
| GET | `/tasks/{task_id}` | Fetch one, 404 when absent |
| PATCH | `/tasks/{task_id}` | Partial update |
| DELETE | `/tasks/{task_id}` | Remove, 204 on success |
| POST | `/tasks/{task_id}/complete` | Mark done |

`POST /tasks` and `DELETE /tasks/{task_id}` are deliberately a matched pair, so
a create can always be undone by a delete.

## There is no deployment

On purpose. Nothing here is hosted, so there is no URL to point a test at — the
condition PreMan's sandbox exists to answer, by building and running this
repository itself and testing what it started.

State is in memory and resets when the process does.
