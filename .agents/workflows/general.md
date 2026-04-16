---
description: Workspace rules for Personality / AION
---

# General Workspace Rules

## Stack Snapshot

- Backend: Python 3.11, FastAPI, SQLAlchemy async, asyncpg
- External APIs: OpenAI Responses API, Telegram Bot API
- Infra: Docker Compose locally, Coolify-targeted compose for deployment
- Runtime constraints:
  - event-driven pipeline
  - structured contracts between stages
  - no side effects outside action/integrations
  - reflection currently runs as an app-local durable worker

## Architecture Rules

- Keep the runtime aligned with `docs/basics/02_architecture.md` and `docs/basics/15_runtime_flow.md`.
- Preserve explicit contracts between perception, context, motivation, role, planning, action, expression, memory, and reflection.
- Keep heuristics deterministic unless a task explicitly introduces a new adaptive behavior.
- Prefer existing modules over inventing new layers for one-off logic.

## Delivery Rules

- Keep changes scoped and reversible.
- Require acceptance evidence before completion.
- Follow the loop: plan -> implement -> test -> architecture review -> sync context -> repeat.
- Run `.\.venv\Scripts\python -m pytest -q` before every commit for backend/runtime work.
- Update `.codex/context/TASK_BOARD.md` and `.codex/context/PROJECT_STATE.md` when scope or project truth changes.
- Use subagents only according to `.agents/workflows/subagent-orchestration.md`.
