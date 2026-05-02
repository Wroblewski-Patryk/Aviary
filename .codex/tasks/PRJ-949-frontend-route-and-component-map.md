# Task

## Header
- ID: PRJ-949
- Title: Frontend Route And Component Map
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-946, PRJ-948
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 949
- Operation Mode: BUILDER

## Context

Frontend traceability is coarse because most routes and UI state are currently
owned by `web/src/App.tsx`.

## Goal

Document the current frontend route, state, API, and component ownership map
without forcing a refactor.

## Scope

- `web/src/App.tsx`
- `web/src/lib/api.ts`
- `web/src/index.css`
- `docs/architecture/codebase-map.md`
- possible `docs/frontend/` or approved docs location
- traceability and drift docs
- exact files:
  - `docs/frontend/route-component-map.md`
  - `docs/architecture/codebase-map.md`
  - `docs/architecture/traceability-matrix.md`
  - `docs/index.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/analysis/documentation-inventory.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-949-frontend-route-and-component-map.md`
  - `.codex/tasks/PRJ-950-provider-specific-integration-docs.md`

## Implementation Plan

1. Inspect route definitions and route-specific render branches.
2. Map frontend routes to API calls, local state, backend features, and docs.
3. Mark static/fallback-only surfaces as `GAP` where backend ownership is
   missing.
4. Link the map from codebase and traceability docs.
5. Validate route coverage against `web/src/App.tsx`.

## Acceptance Criteria

- [x] Frontend route/component map exists.
- [x] Routes map to API calls or explicit static/fallback status.
- [x] Traceability matrix uses the map for frontend entries.
- [x] Validation evidence is recorded.

## Definition of Done

- [x] `DEFINITION_OF_DONE.md` relevant checks are satisfied for docs scope.
- [x] No UI behavior changes.
- [x] Validation passes.

## Deliverable For This Stage

A frontend route/component map linked from the codebase map, traceability
matrix, docs index, inventory, drift report, and queue plan.

## Constraints

- do not refactor frontend code in this slice
- mark static/fallback surfaces as gaps
- document current ownership honestly even when `App.tsx` is still monolithic

## Forbidden

- UI behavior changes
- invented API calls
- claiming component extraction exists when it does not

## Validation Evidence

- Tests:
  - route coverage check passed against `RoutePath` union and `ROUTES`
  - API client method coverage check passed
  - local markdown link check passed
  - `git diff --check` passed
- Manual checks:
  - inspected `web/src/App.tsx`
  - inspected `web/src/lib/api.ts`
  - inspected current traceability/codebase docs
- Screenshots/logs: not applicable
- High-risk checks: documentation-only; no UI behavior changed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Result Report

- Task summary: added a frontend route/component/state/API ownership map for
  the current browser shell.
- Files changed:
  - `docs/frontend/route-component-map.md`
  - `docs/architecture/codebase-map.md`
  - `docs/architecture/traceability-matrix.md`
  - `docs/index.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/analysis/documentation-inventory.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-949-frontend-route-and-component-map.md`
  - `.codex/tasks/PRJ-950-provider-specific-integration-docs.md`
- How tested: route coverage, API client method coverage, markdown links, and
  `git diff --check`.
- What is incomplete: component extraction ownership remains a gap and no
  frontend unit/e2e suite was added.
- Next steps: `PRJ-950` Provider Specific Integration Docs.
