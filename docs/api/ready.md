# ready

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## GET /ready

`GET /ready`

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | ReadyReadinessResponse |

**Example response**

```json
{
  "mock_storage": "...",
  "status": "string",
  "storage": "..."
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/ready'
```

---
