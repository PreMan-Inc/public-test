# mock_products

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## List mock products

`GET /api/v1/mock/products`

Retrieves the mock product collection

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
| `200` | Successful response | MockProductsMockListProductsResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "items": [
    {
      "active": true,
      "category": "General",
      "created_at": "2026-01-01T00:00:00Z",
      "description": "",
      "id": "string",
      "name": "string",
      "price_cents": 0,
      "sku": "string",
      "stock_quantity": 0,
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
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/products'
```

---

## Create a mock product

`POST /api/v1/mock/products`

Creates a product in the mock product collection

**Request body** (required) — `application/json`

Type: `MockProductsMockCreateProductRequest`

```json
{
  "active": true,
  "category": "General",
  "description": "",
  "name": "string",
  "price_cents": 0,
  "sku": "string",
  "stock_quantity": 0
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockProductsMockCreateProductResponse |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "active": true,
  "category": "General",
  "created_at": "2026-01-01T00:00:00Z",
  "description": "",
  "id": "string",
  "name": "string",
  "price_cents": 0,
  "sku": "string",
  "stock_quantity": 0,
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/products' \
  -H 'Content-Type: application/json' \
  -d '{"active": true, "category": "General", "description": "", "name": "string", "price_cents": 0, "sku": "string", "stock_quantity": 0}'
```

---

## Get a mock product

`GET /api/v1/mock/products/{item_id}`

Retrieves the mock product identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockProductsMockGetProductResponse |
| `404` | Not found | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "active": true,
  "category": "General",
  "created_at": "2026-01-01T00:00:00Z",
  "description": "",
  "id": "string",
  "name": "string",
  "price_cents": 0,
  "sku": "string",
  "stock_quantity": 0,
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/products/{item_id}'
```

---

## Replace a mock product

`PUT /api/v1/mock/products/{item_id}`

Replaces the mock product identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `MockProductsMockReplaceProductRequest`

```json
{
  "active": true,
  "category": "string",
  "description": "string",
  "name": "string",
  "price_cents": 0,
  "sku": "string",
  "stock_quantity": 0
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockProductsMockReplaceProductResponse |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "active": true,
  "category": "General",
  "created_at": "2026-01-01T00:00:00Z",
  "description": "",
  "id": "string",
  "name": "string",
  "price_cents": 0,
  "sku": "string",
  "stock_quantity": 0,
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PUT 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/products/{item_id}' \
  -H 'Content-Type: application/json' \
  -d '{"active": true, "category": "string", "description": "string", "name": "string", "price_cents": 0, "sku": "string", "stock_quantity": 0}'
```

---

## Update a mock product

`PATCH /api/v1/mock/products/{item_id}`

Updates the mock product identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `MockProductsMockUpdateProductRequest`

```json
{
  "active": true,
  "category": "string",
  "description": "string",
  "name": "string",
  "price_cents": 0,
  "sku": "string",
  "stock_quantity": 0
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockProductsMockUpdateProductResponse |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "active": true,
  "category": "General",
  "created_at": "2026-01-01T00:00:00Z",
  "description": "",
  "id": "string",
  "name": "string",
  "price_cents": 0,
  "sku": "string",
  "stock_quantity": 0,
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PATCH 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/products/{item_id}' \
  -H 'Content-Type: application/json' \
  -d '{"active": true, "category": "string", "description": "string", "name": "string", "price_cents": 0, "sku": "string", "stock_quantity": 0}'
```

---

## Delete a mock product

`DELETE /api/v1/mock/products/{item_id}`

Deletes the mock product identified by the item ID

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
curl -X DELETE 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/products/{item_id}'
```

---
