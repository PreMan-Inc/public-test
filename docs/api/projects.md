# projects

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## List projects

`GET /api/v1/projects`

Retrieves the project collection

!!! info "Paginated"
    This endpoint pages: advance `$request.offset` to page through `$.items`.

**Query parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | no | — |
| `offset` | integer | no | — |
| `status` | string or null | no | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | ProjectsListProjectsApiV1ProjectsGetResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "items": [
    {
      "created_at": "2026-01-01T00:00:00Z",
      "description": "string",
      "id": "string",
      "name": "string",
      "owner_id": "string",
      "status": "active",
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
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/projects'
```

---

## Create a project

`POST /api/v1/projects`

Creates a new project

**Request body** (required) — `application/json`

Type: `ProjectsCreateProjectApiV1ProjectsPostRequest`

```json
{
  "description": "",
  "name": "string",
  "status": "active"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | ProjectsCreateProjectApiV1ProjectsPostResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "id": "string",
  "name": "string",
  "owner_id": "string",
  "status": "active",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/projects' \
  -H 'Content-Type: application/json' \
  -d '{"description": "", "name": "string", "status": "active"}'
```

---

## List projects

`GET /api/v1/projects/`

Retrieves the project collection

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | — |

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/projects/'
```

---

## Create a project

`POST /api/v1/projects/`

Creates a new project

**Request body** (required) — `application/json`

Type: `ProjectRecord`

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "id": "string",
  "name": "string",
  "owner_id": "string",
  "status": "active",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | — |

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/projects/' \
  -H 'Content-Type: application/json' \
  -d '{"created_at": "2026-01-01T00:00:00Z", "description": "string", "id": "string", "name": "string", "owner_id": "string", "status": "active", "updated_at": "2026-01-01T00:00:00Z"}'
```

---

## Get a project

`GET /api/v1/projects/{project_id}`

Retrieves the project identified by the project ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_id` | string | yes | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | ProjectsGetProjectApiV1ProjectsProjectIdGetResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "id": "string",
  "name": "string",
  "owner_id": "string",
  "status": "active",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/projects/{project_id}'
```

---

## Replace a project

`PUT /api/v1/projects/{project_id}`

Replaces the project identified by the project ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `ProjectsReplaceProjectApiV1ProjectsProjectIdPutRequest`

```json
{
  "description": "string",
  "name": "string",
  "status": "active"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | ProjectsReplaceProjectApiV1ProjectsProjectIdPutResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "id": "string",
  "name": "string",
  "owner_id": "string",
  "status": "active",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PUT 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/projects/{project_id}' \
  -H 'Content-Type: application/json' \
  -d '{"description": "string", "name": "string", "status": "active"}'
```

---

## Update a project

`PATCH /api/v1/projects/{project_id}`

Updates the project identified by the project ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `ProjectsUpdateProjectApiV1ProjectsProjectIdPatchRequest`

```json
{
  "description": "string",
  "name": "string",
  "status": "active"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | ProjectsUpdateProjectApiV1ProjectsProjectIdPatchResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "id": "string",
  "name": "string",
  "owner_id": "string",
  "status": "active",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PATCH 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/projects/{project_id}' \
  -H 'Content-Type: application/json' \
  -d '{"description": "string", "name": "string", "status": "active"}'
```

---

## Delete a project

`DELETE /api/v1/projects/{project_id}`

Deletes the project identified by the project ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `ProjectsDeleteProjectApiV1ProjectsProjectIdDeleteRequest`

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": "string",
  "id": "string",
  "name": "string",
  "owner_id": "string",
  "status": "active",
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
curl -X DELETE 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/projects/{project_id}' \
  -H 'Content-Type: application/json' \
  -d '{"created_at": "2026-01-01T00:00:00Z", "description": "string", "id": "string", "name": "string", "owner_id": "string", "status": "active", "updated_at": "2026-01-01T00:00:00Z"}'
```

---
