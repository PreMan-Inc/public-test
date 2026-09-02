# tasks

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## List tasks for a project

`GET /api/v1/projects/{project_id}/tasks`

Retrieves the tasks associated with the identified project

!!! info "Paginated"
    This endpoint pages: advance `$request.offset` to page through `$.items`.

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_id` | string | yes | — |

**Query parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | no | — |
| `offset` | integer | no | — |
| `status` | string or null | no | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | TasksListTasksApiV1ProjectsProjectIdTasksGetResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "items": [
    {
      "created_at": "2026-01-01T00:00:00Z",
      "description": "string",
      "due_at": "2026-01-01T00:00:00Z",
      "id": "string",
      "owner_id": "string",
      "priority": "low",
      "project_id": "string",
      "status": "todo",
      "title": "string",
      "updated_at": "2026-01-01T00:00:00Z"
    }
  ],
  "limit": 0,
  "offset": 0,
  "total": 0
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/projects/{project_id}/tasks'
```

---

## Create a task for a project

`POST /api/v1/projects/{project_id}/tasks`

Creates a task under the identified project

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `TasksCreateTaskApiV1ProjectsProjectIdTasksPostRequest`

```json
{
  "description": "",
  "due_at": "2026-01-01T00:00:00Z",
  "priority": "low",
  "status": "todo",
  "title": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | TasksCreateTaskApiV1ProjectsProjectIdTasksPostResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "due_at": "2026-01-01T00:00:00Z",
  "id": "string",
  "owner_id": "string",
  "priority": "low",
  "project_id": "string",
  "status": "todo",
  "title": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/projects/{project_id}/tasks' \
  -H 'Content-Type: application/json' \
  -d '{"description": "", "due_at": "2026-01-01T00:00:00Z", "priority": "low", "status": "todo", "title": "string"}'
```

---

## Get a task

`GET /api/v1/tasks/{task_id}`

Retrieves the task identified by the task ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `task_id` | string | yes | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | TasksGetTaskApiV1TasksTaskIdGetResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "due_at": "2026-01-01T00:00:00Z",
  "id": "string",
  "owner_id": "string",
  "priority": "low",
  "project_id": "string",
  "status": "todo",
  "title": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/tasks/{task_id}'
```

---

## Replace a task

`PUT /api/v1/tasks/{task_id}`

Replaces the task identified by the task ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `task_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `TasksReplaceTaskApiV1TasksTaskIdPutRequest`

```json
{
  "description": "string",
  "due_at": "2026-01-01T00:00:00Z",
  "priority": "low",
  "status": "todo",
  "title": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | TasksReplaceTaskApiV1TasksTaskIdPutResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "due_at": "2026-01-01T00:00:00Z",
  "id": "string",
  "owner_id": "string",
  "priority": "low",
  "project_id": "string",
  "status": "todo",
  "title": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PUT 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/tasks/{task_id}' \
  -H 'Content-Type: application/json' \
  -d '{"description": "string", "due_at": "2026-01-01T00:00:00Z", "priority": "low", "status": "todo", "title": "string"}'
```

---

## Update a task

`PATCH /api/v1/tasks/{task_id}`

Updates the task identified by the task ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `task_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `TasksUpdateTaskApiV1TasksTaskIdPatchRequest`

```json
{
  "description": "string",
  "due_at": "2026-01-01T00:00:00Z",
  "priority": "low",
  "status": "todo",
  "title": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | TasksUpdateTaskApiV1TasksTaskIdPatchResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "due_at": "2026-01-01T00:00:00Z",
  "id": "string",
  "owner_id": "string",
  "priority": "low",
  "project_id": "string",
  "status": "todo",
  "title": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PATCH 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/tasks/{task_id}' \
  -H 'Content-Type: application/json' \
  -d '{"description": "string", "due_at": "2026-01-01T00:00:00Z", "priority": "low", "status": "todo", "title": "string"}'
```

---

## Delete a task

`DELETE /api/v1/tasks/{task_id}`

Deletes the task identified by the task ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `task_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `TasksDeleteTaskApiV1TasksTaskIdDeleteRequest`

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "due_at": "2026-01-01T00:00:00Z",
  "id": "string",
  "owner_id": "string",
  "priority": "low",
  "project_id": "string",
  "status": "todo",
  "title": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | — |
| `422` | Unprocessable entity | any |

**Example request**

```bash
curl -X DELETE 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/tasks/{task_id}' \
  -H 'Content-Type: application/json' \
  -d '{"created_at": "2026-01-01T00:00:00Z", "description": "string", "due_at": "2026-01-01T00:00:00Z", "id": "string", "owner_id": "string", "priority": "low", "project_id": "string", "status": "todo", "title": "string", "updated_at": "2026-01-01T00:00:00Z"}'
```

---
