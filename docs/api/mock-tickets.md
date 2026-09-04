# mock_tickets

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## List mock tickets

`GET /api/v1/mock/tickets`

Retrieves the mock ticket collection

!!! info "Paginated"
    This endpoint pages: advance `$request.offset` to page through `$.items`.

**Query parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | no | — |
| `offset` | integer | no | — |
| `q` | string or null | no | — |
| `sort` | string or null | no | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockTicketsMockListTicketsResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "items": [
    {
      "assignee": "",
      "created_at": "2026-01-01T00:00:00Z",
      "customer_id": "string",
      "description": "string",
      "id": "string",
      "priority": "low",
      "status": "open",
      "subject": "string",
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
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/tickets'
```

---

## Create a mock ticket

`POST /api/v1/mock/tickets`

Creates a ticket in the mock ticket collection

**Request body** (required) — `application/json`

Type: `MockTicketsMockCreateTicketRequest`

```json
{
  "assignee": "",
  "customer_id": "string",
  "description": "string",
  "priority": "low",
  "status": "open",
  "subject": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockTicketsMockCreateTicketResponse |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "assignee": "",
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "description": "string",
  "id": "string",
  "priority": "low",
  "status": "open",
  "subject": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/tickets' \
  -H 'Content-Type: application/json' \
  -d '{"assignee": "", "customer_id": "string", "description": "string", "priority": "low", "status": "open", "subject": "string"}'
```

---

## Get a mock ticket

`GET /api/v1/mock/tickets/{item_id}`

Retrieves the mock ticket identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockTicketsMockGetTicketResponse |
| `404` | Not found | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "assignee": "",
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "description": "string",
  "id": "string",
  "priority": "low",
  "status": "open",
  "subject": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/tickets/{item_id}'
```

---

## Replace a mock ticket

`PUT /api/v1/mock/tickets/{item_id}`

Replaces the mock ticket identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `MockTicketsMockReplaceTicketRequest`

```json
{
  "assignee": "string",
  "customer_id": "string",
  "description": "string",
  "priority": "low",
  "status": "open",
  "subject": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockTicketsMockReplaceTicketResponse |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "assignee": "",
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "description": "string",
  "id": "string",
  "priority": "low",
  "status": "open",
  "subject": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PUT 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/tickets/{item_id}' \
  -H 'Content-Type: application/json' \
  -d '{"assignee": "string", "customer_id": "string", "description": "string", "priority": "low", "status": "open", "subject": "string"}'
```

---

## Update a mock ticket

`PATCH /api/v1/mock/tickets/{item_id}`

Updates the mock ticket identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `MockTicketsMockUpdateTicketRequest`

```json
{
  "assignee": "string",
  "customer_id": "string",
  "description": "string",
  "priority": "low",
  "status": "open",
  "subject": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockTicketsMockUpdateTicketResponse |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "assignee": "",
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "description": "string",
  "id": "string",
  "priority": "low",
  "status": "open",
  "subject": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PATCH 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/tickets/{item_id}' \
  -H 'Content-Type: application/json' \
  -d '{"assignee": "string", "customer_id": "string", "description": "string", "priority": "low", "status": "open", "subject": "string"}'
```

---

## Delete a mock ticket

`DELETE /api/v1/mock/tickets/{item_id}`

Deletes the mock ticket identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | — |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example request**

```bash
curl -X DELETE 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/tickets/{item_id}'
```

---
