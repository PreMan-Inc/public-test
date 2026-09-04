# system

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## Check system health

`GET /health`

Retrieves the system's health status

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | SystemHealthHealthGetResponse |

**Example response**

```json
{
  "environment": "string",
  "service": "string",
  "status": "ok",
  "storage": "string",
  "timestamp": "2026-01-01T00:00:00Z",
  "version": "string"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/health'
```

---
