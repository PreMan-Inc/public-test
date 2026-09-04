# authentication

Base URL: `https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws`

## Change the current user's password

`POST /api/v1/auth/change-password`

Changes the password for the authenticated user

**Request body** (required) — `application/json`

Type: `AuthenticationChangePasswordApiV1AuthChangePasswordPostRequest`

```json
{
  "current_password": "string",
  "new_password": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | AuthenticationChangePasswordApiV1AuthChangePasswordPostResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "message": "string"
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/auth/change-password' \
  -H 'Content-Type: application/json' \
  -d '{"current_password": "string", "new_password": "string"}'
```

---

## Request a password reset

`POST /api/v1/auth/forgot-password`

Starts the password recovery process for a forgotten password

**Request body** (required) — `application/json`

Type: `AuthenticationForgotPasswordApiV1AuthForgotPasswordPostRequest`

```json
{
  "email": "user@example.com"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | AuthenticationForgotPasswordApiV1AuthForgotPasswordPostResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "message": "string",
  "reset_token": "string"
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/auth/forgot-password' \
  -H 'Content-Type: application/json' \
  -d '{"email": "user@example.com"}'
```

---

## Log in a user

`POST /api/v1/auth/login`

Authenticates a user

**Request body** (required) — `application/json`

Type: `AuthenticationLoginApiV1AuthLoginPostRequest`

```json
{
  "email": "user@example.com",
  "password": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | AuthenticationLoginApiV1AuthLoginPostResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "access_token": "string",
  "expires_in": 0,
  "refresh_token": "string",
  "token_type": "bearer",
  "user": {
    "created_at": "2026-01-01T00:00:00Z",
    "email": "user@example.com",
    "id": "string",
    "name": "string",
    "role": "user",
    "updated_at": "2026-01-01T00:00:00Z"
  }
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/auth/login' \
  -H 'Content-Type: application/json' \
  -d '{"email": "user@example.com", "password": "string"}'
```

---

## Log out the current user

`POST /api/v1/auth/logout`

Ends the current user's authenticated session

**Request body** (required) — `application/json`

Type: `AuthenticationLogoutApiV1AuthLogoutPostRequest`

```json
{
  "refresh_token": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | — |
| `422` | Unprocessable entity | any |

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/auth/logout' \
  -H 'Content-Type: application/json' \
  -d '{"refresh_token": "string"}'
```

---

## Get the current user

`GET /api/v1/auth/me`

Retrieves information about the authenticated user

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | AuthenticationGetMeApiV1AuthMeGetResponse |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "email": "user@example.com",
  "id": "string",
  "name": "string",
  "role": "user",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X GET 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/auth/me'
```

---

## Update the current user

`PATCH /api/v1/auth/me`

Updates information for the authenticated user

**Request body** (required) — `application/json`

Type: `AuthenticationUpdateMeApiV1AuthMePatchRequest`

```json
{
  "name": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | AuthenticationUpdateMeApiV1AuthMePatchResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "email": "user@example.com",
  "id": "string",
  "name": "string",
  "role": "user",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

**Example request**

```bash
curl -X PATCH 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/auth/me' \
  -H 'Content-Type: application/json' \
  -d '{"name": "string"}'
```

---

## Refresh authentication

`POST /api/v1/auth/refresh`

Refreshes the current authentication

**Request body** (required) — `application/json`

Type: `AuthenticationRefreshApiV1AuthRefreshPostRequest`

```json
{
  "refresh_token": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | AuthenticationRefreshApiV1AuthRefreshPostResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "access_token": "string",
  "expires_in": 0,
  "refresh_token": "string",
  "token_type": "bearer",
  "user": {
    "created_at": "2026-01-01T00:00:00Z",
    "email": "user@example.com",
    "id": "string",
    "name": "string",
    "role": "user",
    "updated_at": "2026-01-01T00:00:00Z"
  }
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/auth/refresh' \
  -H 'Content-Type: application/json' \
  -d '{"refresh_token": "string"}'
```

---

## Register a user

`POST /api/v1/auth/register`

Registers a new user

**Request body** (required) — `application/json`

Type: `AuthenticationRegisterApiV1AuthRegisterPostRequest`

```json
{
  "email": "user@example.com",
  "name": "string",
  "password": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | AuthenticationRegisterApiV1AuthRegisterPostResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "access_token": "string",
  "expires_in": 0,
  "refresh_token": "string",
  "token_type": "bearer",
  "user": {
    "created_at": "2026-01-01T00:00:00Z",
    "email": "user@example.com",
    "id": "string",
    "name": "string",
    "role": "user",
    "updated_at": "2026-01-01T00:00:00Z"
  }
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/auth/register' \
  -H 'Content-Type: application/json' \
  -d '{"email": "user@example.com", "name": "string", "password": "string"}'
```

---

## Reset a password

`POST /api/v1/auth/reset-password`

Resets a user's password

**Request body** (required) — `application/json`

Type: `AuthenticationResetPasswordApiV1AuthResetPasswordPostRequest`

```json
{
  "new_password": "string",
  "reset_token": "string"
}
```

**Responses**

| Status | Description | Type |
| --- | --- | --- |
| `200` | Successful response | AuthenticationResetPasswordApiV1AuthResetPasswordPostResponse |
| `422` | Unprocessable entity | any |

**Example response**

```json
{
  "message": "string"
}
```

**Example request**

```bash
curl -X POST 'https://xixoo2yundjxsbdwl3iw2eg5hi0ckwfu.lambda-url.us-east-1.on.aws/api/v1/auth/reset-password' \
  -H 'Content-Type: application/json' \
  -d '{"new_password": "string", "reset_token": "string"}'
```

---
