# mock

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## Reset mock data

`POST /api/v1/mock/reset`

Resets the API's mock data

**Request body** (required) — `application/json`

Type: `ResourceConfig`

```json
{
  "create_model": "string",
  "plural": "string",
  "replace_model": "string",
  "response_model": "string",
  "singular": "string",
  "update_model": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | — |

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/mock/reset' \
  -H 'Content-Type: application/json' \
  -d '{"create_model": "string", "plural": "string", "replace_model": "string", "response_model": "string", "singular": "string", "update_model": "string"}'
```

---
