# Conversational Connect — Flask Scaffold

This branch (`flask`) provides a small, production-leaning **Flask** scaffold.

The goal is to give you a clean starting point (app structure, configuration, logging, health endpoints, and a tiny test) so you can focus on implementing the API logic during the interview.

## Quickstart

Feel free to use any other library that you are comfortable with for virtual environment and dependency manager, the below steps are just a simple guide

### 1) Create a virtual environment


```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 3) Configure environment

Env files are provided in `env/` (safe defaults, no secrets):

- `env/dev.env`
- `env/staging.env`
- `env/production.env`

### 4) Run the API

```bash
make run
```

Open: `http://127.0.0.1:8000`

## Endpoints (provided)

- `GET /api/v1/health` — API health check
- `GET /api/v1/settings` — returns selected settings (from env-backed `Settings`)

Responses include an `X-Request-ID` header (generated if not provided).

## Project Structure

```text
app/
	main.py                # Flask app wiring + error handling
	api/v1/                # Versioned routes
		endpoints/            # Route handlers
		services/             # Business logic/services
	core/
		config.py            # Pydantic settings (APP_* env vars)
		logging.py           # JSON/text logging configuration
		middleware.py        # Request ID + timing middleware
tests/
	test_health.py         # smoke tests for health endpoints
```

## Configuration

Settings are loaded from environment variables prefixed with `APP_`.

This scaffold prefers env files in the `env/` folder. By default, settings are loaded from the first existing file in this order:

1. `env/<environment>.env` (when `APP_ENVIRONMENT` is set)
2. `env/dev.env`
3. `env/.env` (legacy fallback)
4. `.env` (legacy fallback)

### Staging / Production

To load an environment-specific file, you must set `APP_ENVIRONMENT` in the **process environment** (recommended for deployments):

```bash
export APP_ENVIRONMENT=staging
flask --app app.main run --debug --port 8000
```

When `APP_ENVIRONMENT` is set, the app will also try (if present):

- `env/<environment>.env` (e.g. `env/staging.env`)

You can also explicitly point to a file using `APP_ENV_FILE`:

```bash
export APP_ENV_FILE=env/production.env
gunicorn -b 0.0.0.0:8000 app.main:app
```

For local runs, `APP_ENV_FILE` is usually the simplest because it doesn’t require pre-setting `APP_ENVIRONMENT`.

Common options:

- `APP_ENVIRONMENT` (default: `local`)
- `APP_LOG_LEVEL` (default: `INFO`)
- `APP_LOG_FORMAT` (default: `json`) — `json` or `text`
- `APP_API_V1_PREFIX` (default: `/api/v1`)

## Testing and Tooling

```bash
pytest
ruff check .
mypy app
```

## Docker

```bash
docker build -t conversational-connect-flask .
docker run --rm -p 8000:8000 conversational-connect-flask
```

## What You Implement During the Interview

The interview prompt will typically ask you to add one or more API endpoints and supporting logic.
When implementing, treat this like a production service: validate inputs, return useful errors, keep code organized, and make sensible trade-offs.
