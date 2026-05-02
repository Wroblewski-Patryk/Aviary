# Task

## Header
- ID: PRJ-946
- Title: Generated OpenAPI Reference
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Product Docs Agent
- Depends on: PRJ-945
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 946
- Operation Mode: BUILDER

## Context

The API reference is manually grounded in routes and schemas, but no generated
OpenAPI artifact is checked in or linked.

## Goal

Add a reproducible OpenAPI export and connect it to the API reference and
traceability docs.

## Scope

- discover the FastAPI OpenAPI generation path
- add generated artifact under an approved docs location
- document the regeneration command
- update `docs/api/index.md`, `docs/index.md`,
  `docs/analysis/documentation-drift.md`, and relevant task/context files
- exact files:
  - `backend/scripts/export_openapi_schema.py`
  - `docs/api/openapi.json`
  - `docs/api/index.md`
  - `docs/index.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/analysis/documentation-inventory.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-946-generated-openapi-reference.md`

## Implementation Plan

1. Inspect app factory/import path for OpenAPI generation.
2. Generate OpenAPI JSON without starting a production service.
3. Add or document the regeneration command.
4. Link the artifact from the API reference.
5. Validate JSON shape and markdown links.

## Acceptance Criteria

- [x] OpenAPI artifact exists or a blocker is documented.
- [x] Regeneration command is documented.
- [x] API reference links to the artifact.
- [x] Drift report marks the OpenAPI gap fixed or blocked.
- [x] Validation evidence is recorded.

## Definition of Done

- [x] `DEFINITION_OF_DONE.md` relevant checks are satisfied for docs scope.
- [x] No runtime behavior changes.
- [x] Validation passes.

## Deliverable For This Stage

A generated OpenAPI artifact, a reproducible export script, linked API docs,
and validation evidence.

## Constraints

- use the existing FastAPI app object in `backend/app/main.py`
- do not start the production server
- do not change route behavior or schemas
- keep generated output reproducible

## Forbidden

- invented endpoint contracts
- hand-written OpenAPI JSON
- runtime behavior changes
- provider secret access

## Validation Evidence

- Tests:
  - OpenAPI export command passed
  - OpenAPI schema shape check passed: `openapi=3.1.0`, `paths=18`,
    `info.title=AION MVP`
  - local markdown link check passed
  - `git diff --check` passed
- Manual checks:
  - inspected `backend/app/main.py` and confirmed `app = FastAPI(...)`
  - confirmed import/export works without entering application lifespan
- Screenshots/logs: not applicable
- High-risk checks: documentation/generated artifact only; no runtime code path
  changed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence

- Architecture source reviewed:
  - `docs/api/index.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
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
- Rollback note: revert generated artifact, export script, and docs links
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist

- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Result Report

- Task summary: added a reproducible FastAPI OpenAPI export and linked it from
  the API/system-map docs.
- Files changed:
  - `backend/scripts/export_openapi_schema.py`
  - `docs/api/openapi.json`
  - `docs/api/index.md`
  - `docs/index.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/analysis/documentation-inventory.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-946-generated-openapi-reference.md`
- How tested:
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\export_openapi_schema.py --output ..\docs\api\openapi.json; Pop-Location`
  - OpenAPI shape check for version, title, and path count
  - local markdown link check
  - `git diff --check`
- What is incomplete: per-route examples and generated client sync remain
  future gaps.
- Next steps: `PRJ-947` ERD And Column Model Reference.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: API docs were manually grounded but lacked generated FastAPI output.
- Gaps: no checked-in schema artifact or regeneration command.
- Inconsistencies: no architecture mismatch found.
- Architecture constraints: generated docs must reflect live FastAPI routes.

### 2. Select One Priority Task
- Selected task: PRJ-946 Generated OpenAPI Reference.
- Priority rationale: first READY task from the documentation gap repair queue.
- Why other candidates were deferred: ERD, test ownership, frontend map, and
  provider docs depend on or benefit from API schema certainty.

### 3. Plan Implementation
- Files or surfaces to modify: export script, generated JSON, API docs, system
  map docs, drift report, context files.
- Logic: import `app` from `backend/app/main.py` and call `app.openapi()`.
- Edge cases: avoid entering lifespan or reading provider secrets.

### 4. Execute Implementation
- Implementation notes: added `backend/scripts/export_openapi_schema.py` and
  generated `docs/api/openapi.json`.

### 5. Verify and Test
- Validation performed: export command, schema shape, markdown links,
  whitespace.
- Result: passed.

### 6. Self-Review
- Simpler option considered: document `/openapi.json` without checking in an
  artifact.
- Technical debt introduced: no
- Scalability assessment: the script can be reused whenever routes change.
- Refinements made: script adds backend root to `sys.path` so it works from
  `backend/scripts`.

### 7. Update Documentation and Knowledge
- Docs updated: yes
- Context updated: yes
- Learning journal updated: not applicable.
