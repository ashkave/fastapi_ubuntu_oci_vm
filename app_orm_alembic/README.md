# FastAPI ORM + Alembic

A learning project that exposes a REST API for users, posts, and votes. It uses FastAPI, SQLAlchemy ORM, PostgreSQL, JWT bearer authentication, and Alembic for database schema migrations.

## Features

- User registration and lookup
- OAuth2 password login with JWT access tokens
- Authenticated post creation, listing, update, and deletion
- Post search and pagination
- One vote per user per post, with vote totals in post responses
- Versioned PostgreSQL schema migrations through Alembic

## Project layout

```text
app_orm_alembic/
|-- main.py             # FastAPI application and router registration
|-- database.py         # SQLAlchemy engine, session, and dependency
|-- models.py           # ORM models
|-- schemas.py          # Request and response schemas
|-- config.py           # Environment-based settings
|-- oauth2.py           # JWT helpers and current-user dependency
|-- utils.py            # Password hashing utilities
`-- routers/            # Auth, user, post, and vote endpoints

alembic/
|-- env.py              # Alembic configuration and metadata discovery
`-- versions/           # Database migration revisions
```

## Prerequisites

- Python 3.10 or newer
- PostgreSQL
- A PostgreSQL database and user with permission to create and modify tables

## Setup

From the repository root, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file in the repository root. Do not commit it.

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=replace-with-a-password
SECRET_KEY=replace-with-a-long-random-secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Create the database if it does not already exist, then apply the migrations:

```powershell
alembic upgrade head
```

Start the API from the repository root:

```powershell
uvicorn app_orm_alembic.main:app --reload
```

The interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## API endpoints

| Method | Path | Description | Authentication |
| --- | --- | --- | --- |
| `GET` | `/` | Health/welcome response | No |
| `GET` | `/sqlalchemy` | SQLAlchemy connectivity example response | No |
| `POST` | `/users` | Register a user | No |
| `GET` | `/users/{id}` | Get a user by ID | No |
| `POST` | `/login` | Obtain a bearer access token | No |
| `GET` | `/posts` | List posts with vote totals | Bearer token |
| `POST` | `/posts` | Create a post | Bearer token |
| `GET` | `/posts/{id}` | Get a post with its vote total | Bearer token |
| `PUT` | `/posts/{id}` | Update an owned post | Bearer token |
| `DELETE` | `/posts/{id}` | Delete an owned post | Bearer token |
| `POST` | `/vote/` | Add or remove a vote | Bearer token |

`GET /posts` accepts optional `limit`, `skip`, and `search` query parameters. Send `dir: 1` to add a vote or `dir: 0` to remove one.

## Authentication example

Register a user:

```powershell
curl -X POST http://127.0.0.1:8000/users -H "Content-Type: application/json" -d '{"email":"user@example.com","password":"password"}'
```

Log in using form data, then use the returned token as `Authorization: Bearer <access_token>` for protected routes:

```powershell
curl -X POST http://127.0.0.1:8000/login -H "Content-Type: application/x-www-form-urlencoded" -d "username=user@example.com&password=password"
```

## Alembic workflow

The Alembic environment reads the database connection settings from `.env` and imports the ORM metadata from `app_orm_alembic.models`.

Apply all pending migrations:

```powershell
alembic upgrade head
```

Create a migration after changing the models:

```powershell
alembic revision --autogenerate -m "describe the change"
```

Review generated migration code before applying it, then run `alembic upgrade head`. To inspect the current revision, use:

```powershell
alembic current
```

## Notes

- Table names are suffixed with `_alembic` (`posts_alembic`, `users_alembic`, and `votes_alembic`) to distinguish this project from the other examples in the repository.
- Passwords are hashed before storage; never store or share production credentials in source control.
- CORS currently permits all origins. Restrict `allow_origins` before deploying to production.
