# Task

## Header
- ID: PRJ-947
- Title: ERD And Column Model Reference
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Product Docs Agent
- Depends on: PRJ-946
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 947
- Operation Mode: BUILDER

## Context

The data reference maps ORM models, tables, migrations, and repository groups,
but it does not include an ERD or column-by-column model reference.

## Goal

Create a reproducible data-model reference that maps tables, columns,
relationships, migrations, owners, tests, and known gaps.

## Scope

- `backend/app/memory/models.py`
- `backend/migrations/versions/`
- `docs/data/index.md`
- possible generated docs under `docs/data/`
- traceability and drift docs
- exact files:
  - `backend/scripts/export_data_model_reference.py`
  - `docs/data/columns.md`
  - `docs/data/erd.mmd`
  - `docs/data/index.md`
  - `docs/index.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/analysis/documentation-inventory.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-947-erd-and-column-model-reference.md`
  - `.codex/tasks/PRJ-948-test-feature-pipeline-ownership-ledger.md`

## Implementation Plan

1. Inspect SQLAlchemy model metadata and Alembic migration history.
2. Generate or manually produce an ERD-friendly model artifact.
3. Add a column-level reference for core tables.
4. Link models to migrations, repository methods, features, and tests.
5. Validate coverage against ORM model/table names.

## Acceptance Criteria

- [x] ERD artifact or text ERD exists.
- [x] Column-level reference covers all current ORM models or marks gaps.
- [x] Data reference links generated evidence.
- [x] Drift report is updated.
- [x] Validation evidence is recorded.

## Definition of Done

- [x] `DEFINITION_OF_DONE.md` relevant checks are satisfied for docs scope.
- [x] No DB schema changes are made.
- [x] Validation passes.

## Deliverable For This Stage

A generated column model reference, generated Mermaid ERD, regeneration script,
linked docs, and validation evidence.

## Constraints

- use `Base.metadata` from the existing SQLAlchemy models
- do not change DB schema or migrations
- do not infer database foreign keys that are not declared by the ORM
- keep logical links marked as logical/application-level only

## Forbidden

- hand-written column inventory that can drift from models
- new database constraints
- schema migration changes
- invented relationships

## Validation Evidence

- Tests:
  - data model export command passed
  - generated artifact coverage check passed for `18` tables
  - `py_compile` for export script passed
  - local markdown link check passed
  - `git diff --check` passed
- Manual checks:
  - inspected `backend/app/memory/models.py`
  - inspected migration file inventory
- Screenshots/logs: not applicable
- High-risk checks: generated artifacts only; no schema behavior changed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence

- Architecture source reviewed:
  - `docs/data/index.md`
  - `docs/architecture/codebase-map.md`
  - `docs/analysis/documentation-drift.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## Deployment / Ops Evidence

- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert generated artifacts, export script, and docs links
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Result Report

- Task summary: added reproducible generated data-model artifacts from
  SQLAlchemy metadata.
- Files changed:
  - `backend/scripts/export_data_model_reference.py`
  - `docs/data/columns.md`
  - `docs/data/erd.mmd`
  - `docs/data/index.md`
  - `docs/index.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/analysis/documentation-inventory.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-947-erd-and-column-model-reference.md`
  - `.codex/tasks/PRJ-948-test-feature-pipeline-ownership-ledger.md`
- How tested: export command, generated coverage check, `py_compile`, local
  markdown link check, and `git diff --check`.
- What is incomplete: migration-to-column mapping remains filename-level and
  repository methods are not documented one by one.
- Next steps: `PRJ-948` Test Feature Pipeline Ownership Ledger.
