# preman_probe

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## Get a discount probe result

`GET /api/v1/preman-probe/discount`

Retrieves the result of the discount preman probe

**Query parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `percent_off` | integer | no | — |

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | PremanProbeDiscountApiV1PremanProbeDiscountGetResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "order_id": "string",
  "percent_off": 0,
  "total": 0.0
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/preman-probe/discount'
```

---

## Get an order total probe result

`GET /api/v1/preman-probe/order-total`

Retrieves the result of the order total preman probe

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | PremanProbeOrderTotalApiV1PremanProbeOrderTotalGetResponse |

**Example response**

```json
{
  "currency": "string",
  "order_id": "string",
  "paid": true,
  "total": 0.0
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/preman-probe/order-total'
```

---

## Get a refund status probe result

`GET /api/v1/preman-probe/refund-status`

Retrieves the result of the refund status preman probe

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | PremanProbeRefundStatusApiV1PremanProbeRefundStatusGetResponse |

**Example response**

```json
{
  "amount_refunded": 0.0,
  "currency": "GBP",
  "order_id": "string",
  "refunded_at": "string",
  "state": "string"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/preman-probe/refund-status'
```

---

## Get a shipping estimate probe result

`GET /api/v1/preman-probe/shipping-estimate`

Retrieves the result of the shipping estimate preman probe

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | PremanProbeShippingEstimateApiV1PremanProbeShippingEstimateGetResponse |

**Example response**

```json
{
  "business_days": 0,
  "carrier": "string",
  "order_id": "string"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/preman-probe/shipping-estimate'
```

---
