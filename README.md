# Conversational Connect — Backend Challenge (Template)

This repository is intentionally minimal on the `main` branch.

It is used during interviews to evaluate a candidate’s ability to design and implement a **production-ready Python API** (architecture, correctness, reliability, and engineering hygiene).

## Start Here

The actual starter code lives in framework-specific branches. Check out **one** of the following:

- `fastapi` — FastAPI implementation scaffold
- `flask` — Flask implementation scaffold
- `django` — Django implementation scaffold

### Checkout a branch

```bash
git fetch

# Choose ONE:
git checkout fastapi
# or
git checkout flask
# or
git checkout django
```

## What You’re Expected To Do (in the framework branch)

You will implement the API behavior and production readiness concerns within the chosen framework branch. Typical expectations include:

- Clear API design (routes, request/response schemas, status codes)
- Input validation and useful error responses
- Configuration via environment variables (no secrets committed)
- Observability basics (structured logging; health/readiness endpoints if relevant)
- Reasonable project structure and maintainable code

The branch you choose will contain the detailed prompt and any starter scaffolding.

## Notes

- The `main` branch is a template landing page only.
- If you’re an interviewer using this repo as a template, direct candidates to check out the framework branch you want them to use.
