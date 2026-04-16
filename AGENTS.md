# AGENTS.md - Personality / AION

## Purpose

This repository uses a project-specific agent workflow so Codex and related agents can build AION without drifting away from the current Python runtime, docs, and test expectations.

## Canonical Files

- `docs/README.md`
- `docs/overview.md`
- `docs/assumptions/runtime-baseline-2026-04-15.md`
- `docs/basics/02_architecture.md`
- `docs/basics/15_runtime_flow.md`
- `docs/basics/16_agent_contracts.md`
- `docs/basics/17_logging_and_debugging.md`
- `docs/basics/26_env_and_config.md`
- `docs/basics/27_codex_instructions.md`
- `docs/planning/next-iteration-plan.md`
- `docs/planning/open-decisions.md`
- `docs/engineering/local-development.md`
- `docs/engineering/testing.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.agents/workflows/general.md`
- `.agents/workflows/subagent-orchestration.md`

## Core Rules

- Keep repository artifacts in English.
- Communicate with the user in the user's language.
- Treat docs plus `.codex/context` files as the current operating truth for this repo.
- If code and canonical docs diverge, update both in the same change or record the gap in `docs/assumptions/`.
- Respect the AION pipeline:
  - `event -> perception -> context -> motivation -> role -> planning -> action -> expression -> memory -> reflection`
- Preserve the action boundary:
  - side effects belong in the action or integration layer, not in reasoning stages.
- Keep changes tiny, testable, and reversible.
- Run relevant validation before proposing a commit.
- Do not mark work done without test or evidence notes that match the changed scope.
- For runtime, memory, reflection, language, or preference changes, leave behind focused tests and docs/context updates.
- Follow the default loop:
  - plan
  - implement
  - test
  - check whether architecture or task breakdown can be improved
  - sync task/state/docs
  - repeat

## Stack-Specific Quality Gate

Primary automated gate for this repo:

- `.\.venv\Scripts\python -m pytest -q`

Add narrower commands when useful, for example:

- `.\.venv\Scripts\python -m pytest -q tests/test_api_routes.py`
- `.\.venv\Scripts\python -m pytest -q tests/test_reflection_worker.py`

Use Docker/manual smoke when the change touches deployment or runtime wiring:

- `docker compose up --build`
- `curl http://localhost:8000/health`
- `curl -X POST http://localhost:8000/event ...`

## Agent Catalog

- Planner: `.agents/prompts/planner.md` or `.claude/agents/planner.agent.md`
- Product Docs: `.agents/prompts/product-docs.md` or `.claude/agents/product-docs.agent.md`
- Backend Builder: `.agents/prompts/backend-builder.md` or `.claude/agents/backend-builder.agent.md`
- Frontend Builder: `.agents/prompts/frontend-builder.md` or `.claude/agents/frontend-builder.agent.md`
- QA/Test: `.agents/prompts/qa-test.md` or `.claude/agents/qa-test.agent.md`
- Security: `.agents/prompts/security-auditor.md` or `.claude/agents/security-auditor.agent.md`
- DB/Migrations: `.agents/prompts/db-migrations.md` or `.claude/agents/db-migrations.agent.md`
- Ops/Release: `.agents/prompts/ops-release.md` or `.claude/agents/ops-release.agent.md`
- Code Review: `.agents/prompts/code-reviewer.md`
- Codex Documentation Agent: `.codex/agents/documentation-agent.md`
- Codex Planning Agent: `.codex/agents/planning-agent.md`
- Codex Execution Agent: `.codex/agents/execution-agent.md`
- Codex Review Agent: `.codex/agents/review-agent.md`

## Trigger Intent

If the user sends a short execution nudge such as `rob`, `dzialaj`, `start`, `go`, `next`, or `lecimy`:

1. Read `.codex/context/TASK_BOARD.md`.
2. Take the first `READY` task.
3. If no task is `READY`, derive the next smallest useful task from `docs/planning/next-iteration-plan.md` and `docs/planning/open-decisions.md`, then record it.
4. Implement exactly one small slice.
5. Run relevant validation.
6. Update task/state/docs in the same cycle.
7. Return files changed, tests run, commit message, and the next tiny task.

## UX/UI Rule

This repo is backend-first today. If a future web or admin UI is introduced:

- require a design source or approved artifact,
- check loading, empty, error, and success states,
- check desktop and mobile behavior,
- keep evidence in task notes or PR notes.

## Subagent Rule

- Delegate only bounded, non-overlapping work.
- Keep critical-path runtime changes local.
- Give delegated tasks explicit file ownership.
- Integrate and verify subagent output before closure.

## Commit Rule

Do not create a commit when the required checks for the touched scope are failing, unless the user explicitly accepts the risk.
