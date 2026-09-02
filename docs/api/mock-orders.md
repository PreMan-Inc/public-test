# mock_orders

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## List mock orders

`GET /api/v1/mock/orders`

Retrieves the mock order collection

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
| `200` | Successful response | MockOrdersMockListOrdersResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "items": [
    {
      "created_at": "2026-01-01T00:00:00Z",
      "customer_id": "string",
      "id": "string",
      "items": [
        {
          "product_id": "...",
          "quantity": "..."
        }
      ],
      "notes": "",
      "shipping_address": "string",
      "status": "pending",
      "total_cents": 0,
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
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/orders'
```

---

## Create a mock order

`POST /api/v1/mock/orders`

Creates an order in the mock order collection

**Request body** (required) — `application/json`

Type: `MockOrdersMockCreateOrderRequest`

```json
{
  "customer_id": "string",
  "items": [
    {
      "product_id": "string",
      "quantity": 0
    }
  ],
  "notes": "",
  "shipping_address": "string",
  "status": "pending"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockOrdersMockCreateOrderResponse |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "id": "string",
  "items": [
    {
      "product_id": "string",
      "quantity": 0
    }
  ],
  "notes": "",
  "shipping_address": "string",
  "status": "pending",
  "total_cents": 0,
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/orders' \
  -H 'Content-Type: application/json' \
  -d '{"customer_id": "string", "items": [{"product_id": "string", "quantity": 0}], "notes": "", "shipping_address": "string", "status": "pending"}'
```

---

## Get a mock order

`GET /api/v1/mock/orders/{item_id}`

Retrieves the mock order identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockOrdersMockGetOrderResponse |
| `404` | Not found | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "id": "string",
  "items": [
    {
      "product_id": "string",
      "quantity": 0
    }
  ],
  "notes": "",
  "shipping_address": "string",
  "status": "pending",
  "total_cents": 0,
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/orders/{item_id}'
```

---

## Replace a mock order

`PUT /api/v1/mock/orders/{item_id}`

Replaces the mock order identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `MockOrdersMockReplaceOrderRequest`

```json
{
  "customer_id": "string",
  "items": [
    {
      "product_id": "string",
      "quantity": 0
    }
  ],
  "notes": "string",
  "shipping_address": "string",
  "status": "pending"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockOrdersMockReplaceOrderResponse |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "id": "string",
  "items": [
    {
      "product_id": "string",
      "quantity": 0
    }
  ],
  "notes": "",
  "shipping_address": "string",
  "status": "pending",
  "total_cents": 0,
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PUT 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/orders/{item_id}' \
  -H 'Content-Type: application/json' \
  -d '{"customer_id": "string", "items": [{"product_id": "string", "quantity": 0}], "notes": "string", "shipping_address": "string", "status": "pending"}'
```

---

## Update a mock order

`PATCH /api/v1/mock/orders/{item_id}`

Updates the mock order identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `MockOrdersMockUpdateOrderRequest`

```json
{
  "customer_id": "string",
  "items": [
    {
      "product_id": "string",
      "quantity": 0
    }
  ],
  "notes": "string",
  "shipping_address": "string",
  "status": "pending"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockOrdersMockUpdateOrderResponse |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "id": "string",
  "items": [
    {
      "product_id": "string",
      "quantity": 0
    }
  ],
  "notes": "",
  "shipping_address": "string",
  "status": "pending",
  "total_cents": 0,
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PATCH 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/orders/{item_id}' \
  -H 'Content-Type: application/json' \
  -d '{"customer_id": "string", "items": [{"product_id": "string", "quantity": 0}], "notes": "string", "shipping_address": "string", "status": "pending"}'
```

---

## Delete a mock order

`DELETE /api/v1/mock/orders/{item_id}`

Deletes the mock order identified by the item ID

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
curl -X DELETE 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/orders/{item_id}'
```

---
