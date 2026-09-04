# mock_reviews

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## List mock reviews

`GET /api/v1/mock/reviews`

Retrieves the mock review collection

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
| `200` | Successful response | MockReviewsMockListReviewsResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "items": [
    {
      "body": "string",
      "created_at": "2026-01-01T00:00:00Z",
      "customer_id": "string",
      "id": "string",
      "product_id": "string",
      "rating": 0,
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
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/reviews'
```

---

## Create a mock review

`POST /api/v1/mock/reviews`

Creates a review in the mock review collection

**Request body** (required) — `application/json`

Type: `MockReviewsMockCreateReviewRequest`

```json
{
  "body": "string",
  "customer_id": "string",
  "product_id": "string",
  "rating": 0,
  "title": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockReviewsMockCreateReviewResponse |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "body": "string",
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "id": "string",
  "product_id": "string",
  "rating": 0,
  "title": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/reviews' \
  -H 'Content-Type: application/json' \
  -d '{"body": "string", "customer_id": "string", "product_id": "string", "rating": 0, "title": "string"}'
```

---

## Get a mock review

`GET /api/v1/mock/reviews/{item_id}`

Retrieves the mock review identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockReviewsMockGetReviewResponse |
| `404` | Not found | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "body": "string",
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "id": "string",
  "product_id": "string",
  "rating": 0,
  "title": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/reviews/{item_id}'
```

---

## Replace a mock review

`PUT /api/v1/mock/reviews/{item_id}`

Replaces the mock review identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `MockReviewsMockReplaceReviewRequest`

```json
{
  "body": "string",
  "customer_id": "string",
  "product_id": "string",
  "rating": 0,
  "title": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockReviewsMockReplaceReviewResponse |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "body": "string",
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "id": "string",
  "product_id": "string",
  "rating": 0,
  "title": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PUT 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/reviews/{item_id}' \
  -H 'Content-Type: application/json' \
  -d '{"body": "string", "customer_id": "string", "product_id": "string", "rating": 0, "title": "string"}'
```

---

## Update a mock review

`PATCH /api/v1/mock/reviews/{item_id}`

Updates the mock review identified by the item ID

**Path parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | — |

**Request body** (required) — `application/json`

Type: `MockReviewsMockUpdateReviewRequest`

```json
{
  "body": "string",
  "customer_id": "string",
  "product_id": "string",
  "rating": 0,
  "title": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | MockReviewsMockUpdateReviewResponse |
| `404` | Not found | any |
| `409` | Conflict | any |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "body": "string",
  "created_at": "2026-01-01T00:00:00Z",
  "customer_id": "string",
  "id": "string",
  "product_id": "string",
  "rating": 0,
  "title": "string",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PATCH 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/reviews/{item_id}' \
  -H 'Content-Type: application/json' \
  -d '{"body": "string", "customer_id": "string", "product_id": "string", "rating": 0, "title": "string"}'
```

---

## Delete a mock review

`DELETE /api/v1/mock/reviews/{item_id}`

Deletes the mock review identified by the item ID

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
curl -X DELETE 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/reviews/{item_id}'
```

---
