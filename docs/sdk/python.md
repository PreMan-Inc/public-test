# Python

Generated client for greptile-codex-backend, regenerated from the API contract on every release. Method names and request types come from the same document as the [reference](../index.md), so the two cannot disagree.

## Install

```bash
pip install greptile-codex-backend
```

## Construct the client

```python
import os

from greptile_codex_backend import Client

client = Client(
    base_url="https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws",
    # no credential required,
)
```

## Make a call

`GET /` — GET /

```python
response = client.root()
print(response)
```

Every other operation is listed in the [reference](../index.md), one page per tag.
