# Task

## Header
- ID: PRJ-948
- Title: Test Feature Pipeline Ownership Ledger
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-946, PRJ-947
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 948
- Operation Mode: ARCHITECT

## Context

Traceability currently maps tests by file responsibility and inspected names.
Tests do not carry stable feature or pipeline IDs.

## Goal

Create a test ownership ledger or accepted inline metadata convention so
feature and pipeline coverage can be verified mechanically.

## Scope

- `backend/tests/`
- `docs/architecture/traceability-matrix.md`
- possible `docs/engineering/test-ownership-ledger.md`
- `docs/engineering/testing.md`
- drift report and context files
- exact files:
  - `docs/engineering/test-ownership-ledger.md`
  - `docs/engineering/testing.md`
  - `docs/architecture/traceability-matrix.md`
  - `docs/index.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/analysis/documentation-inventory.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-948-test-feature-pipeline-ownership-ledger.md`
  - `.codex/tasks/PRJ-949-frontend-route-and-component-map.md`

## Implementation Plan

1. Inspect test naming, markers, and existing pytest configuration.
2. Choose the smallest non-invasive ownership format.
3. Add a ledger mapping test files or cases to feature/pipeline IDs.
4. Update traceability docs to point to the ledger.
5. Validate that all traceability tests have an ownership entry or explicit gap.

## Acceptance Criteria

- [x] Test ownership ledger or metadata convention exists.
- [x] Core traceability rows link to test ownership IDs.
- [x] Unmapped tests are listed as gaps.
- [x] Validation evidence is recorded.

## Definition of Done

- [x] `DEFINITION_OF_DONE.md` relevant checks are satisfied.
- [x] Test behavior is unchanged unless deliberately adding metadata.
- [x] Validation passes.

## Deliverable For This Stage

A file-level test ownership ledger, testing docs link, traceability link, drift
update, and validation evidence.

## Constraints

- do not modify pytest behavior in this slice
- keep ownership file-level unless a later task adopts inline markers
- mark frontend test-suite absence as a gap

## Forbidden

- broad test rewrites
- invented test coverage
- marking frontend e2e coverage as present without a stable suite

## Validation Evidence

- Tests:
  - traceability referenced-test coverage check passed
  - backend test file ledger coverage check passed
  - local markdown link check passed
  - `git diff --check` passed
- Manual checks:
  - inspected backend test file inventory
  - inspected traceability matrix test references
- Screenshots/logs: not applicable
- High-risk checks: documentation-only; no test behavior changed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Result Report

- Task summary: added a stable file-level test ownership ledger linking
  backend tests to feature and pipeline IDs.
- Files changed:
  - `docs/engineering/test-ownership-ledger.md`
  - `docs/engineering/testing.md`
  - `docs/architecture/traceability-matrix.md`
  - `docs/index.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/analysis/documentation-inventory.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-948-test-feature-pipeline-ownership-ledger.md`
  - `.codex/tasks/PRJ-949-frontend-route-and-component-map.md`
- How tested: traceability referenced-test check, backend test inventory check,
  local markdown links, and `git diff --check`.
- What is incomplete: ownership is file-level, not test-function-level; no
  frontend unit/e2e suite is introduced.
- Next steps: `PRJ-949` Frontend Route And Component Map.
