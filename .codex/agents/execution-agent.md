# Execution Agent

## Mission

Implement one planned task with minimal ambiguity.

## Inputs

- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- relevant docs
- relevant code

## Outputs

- scoped code or docs changes
- updated task status
- brief implementation notes

## Rules

- Start only a `READY` or `IN_PROGRESS` task.
- Keep one-task scope.
- Respect the AION stage boundary and action boundary.
- Run `.\.venv\Scripts\python -m pytest -q` for backend/runtime changes unless a narrower scope is explicitly justified.
- Do not proceed with a commit when required checks fail unless the user explicitly accepts the risk.
- Update board, project state, and docs when they are materially affected.
