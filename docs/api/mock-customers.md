# mock_customers

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## List mock customers

`GET /api/v1/mock/customers`

Retrieves the mock customer collection

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
| `200` | Successful response | MockCustomersMockListCustomersResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "items": [
    {
      "company": "",
      "created_at": "2026-01-01T00:00:00Z",
      "email": "user@example.com",
      "id": "string",
      "name": "string",
      "phone": "",
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
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/customers'
```

---

## Create a mock customer

`POST /api/v1/mock/customers`

Creates a customer in the mock customer collection

**Request body** (required) — `application/json`

Type: `MockCustomersMockCreateCustomerRequest`

```json
{
  "company": "",
  "email": "user@example.com",
  "name": "string",
  "phone": "",
  "status": "active"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockCustomersMockCreateCustomerResponse |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "company": "",
  "created_at": "2026-01-01T00:00:00Z",
  "email": "user@example.com",
  "id": "string",
  "name": "string",
  "phone": "",
  "status": "active",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/customers' \
  -H 'Content-Type: application/json' \
  -d '{"company": "", "email": "user@example.com", "name": "string", "phone": "", "status": "active"}'
```

---

## Get a mock customer

`GET /api/v1/mock/customers/{item_id}`

Retrieves the mock customer identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockCustomersMockGetCustomerResponse |
| `404` | Not found | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "company": "",
  "created_at": "2026-01-01T00:00:00Z",
  "email": "user@example.com",
  "id": "string",
  "name": "string",
  "phone": "",
  "status": "active",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/customers/{item_id}'
```

---

## Replace a mock customer

`PUT /api/v1/mock/customers/{item_id}`

Replaces the mock customer identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `MockCustomersMockReplaceCustomerRequest`

```json
{
  "company": "string",
  "email": "user@example.com",
  "name": "string",
  "phone": "string",
  "status": "active"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockCustomersMockReplaceCustomerResponse |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "company": "",
  "created_at": "2026-01-01T00:00:00Z",
  "email": "user@example.com",
  "id": "string",
  "name": "string",
  "phone": "",
  "status": "active",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PUT 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/customers/{item_id}' \
  -H 'Content-Type: application/json' \
  -d '{"company": "string", "email": "user@example.com", "name": "string", "phone": "string", "status": "active"}'
```

---

## Update a mock customer

`PATCH /api/v1/mock/customers/{item_id}`

Updates the mock customer identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `MockCustomersMockUpdateCustomerRequest`

```json
{
  "company": "string",
  "email": "user@example.com",
  "name": "string",
  "phone": "string",
  "status": "active"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockCustomersMockUpdateCustomerResponse |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "company": "",
  "created_at": "2026-01-01T00:00:00Z",
  "email": "user@example.com",
  "id": "string",
  "name": "string",
  "phone": "",
  "status": "active",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PATCH 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/customers/{item_id}' \
  -H 'Content-Type: application/json' \
  -d '{"company": "string", "email": "user@example.com", "name": "string", "phone": "string", "status": "active"}'
```

---

## Delete a mock customer

`DELETE /api/v1/mock/customers/{item_id}`

Deletes the mock customer identified by the item ID

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
curl -X DELETE 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/customers/{item_id}'
```

---
