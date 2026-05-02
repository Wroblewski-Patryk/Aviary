# Task

## Header
- ID: PRJ-950
- Title: Provider Specific Integration Docs
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Product Docs Agent
- Depends on: PRJ-946, PRJ-948
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 950
- Operation Mode: TESTER

## Context

The tools pipeline documents provider readiness and permission boundaries, but
provider-specific docs for ClickUp, Google Calendar, Google Drive, Telegram,
web knowledge, and browser access remain incomplete.

## Goal

Create provider-specific integration references that map configuration,
readiness, operations, routes, modules, tests, failure modes, and gaps.

## Scope

- `backend/app/integrations/`
- `backend/app/core/connector_execution.py`
- `backend/app/core/connector_policy.py`
- `backend/app/core/app_tools_policy.py`
- `docs/pipelines/tools.md`
- possible `docs/integrations/`
- traceability and drift docs
- exact files:
  - `docs/integrations/index.md`
  - `docs/pipelines/tools.md`
  - `docs/index.md`
  - `docs/architecture/codebase-map.md`
  - `docs/architecture/traceability-matrix.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/analysis/documentation-inventory.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-950-provider-specific-integration-docs.md`

## Implementation Plan

1. Inventory current provider modules and connector policy operations.
2. Create one provider docs index plus bounded provider sections.
3. Separate provider credentials, provider readiness, and policy capability.
4. Link provider docs from tools pipeline and API/data references where useful.
5. Validate provider operation coverage against connector policy snapshots.

## Acceptance Criteria

- [x] Provider integration docs exist.
- [x] Each provider lists config, readiness, operations, tests, and gaps.
- [x] Missing credentials or live smoke are marked without exposing secrets.
- [x] Traceability and drift docs are updated.
- [x] Validation evidence is recorded.

## Definition of Done

- [x] `DEFINITION_OF_DONE.md` relevant checks are satisfied for docs scope.
- [x] No secrets are read or written.
- [x] No runtime behavior changes.
- [x] Validation passes.

## Deliverable For This Stage

A provider-specific integration reference linked from the tools pipeline,
system map, codebase map, traceability matrix, drift report, and inventory.

## Constraints

- no secret values
- no live provider calls
- no runtime behavior changes
- separate provider readiness from connector authorization policy

## Forbidden

- documenting credential values
- inventing live provider readiness
- treating policy-only operations as provider-backed paths
- changing connector policy or integration code

## Validation Evidence

- Tests:
  - connector policy operation coverage check passed
  - provider section coverage check passed
  - local markdown link check passed
  - `git diff --check` passed
- Manual checks:
  - inspected `backend/app/integrations/`
  - inspected `backend/app/core/connector_execution.py`
  - inspected `backend/app/core/connector_policy.py`
- Screenshots/logs: not applicable
- High-risk checks: no secrets read or written; documentation-only
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Result Report

- Task summary: added provider-specific integration docs that map readiness,
  policy, operations, modules, tests, failure modes, and remaining gaps.
- Files changed:
  - `docs/integrations/index.md`
  - `docs/pipelines/tools.md`
  - `docs/index.md`
  - `docs/architecture/codebase-map.md`
  - `docs/architecture/traceability-matrix.md`
  - `docs/analysis/documentation-drift.md`
  - `docs/analysis/documentation-inventory.md`
  - `docs/planning/documentation-system-gap-repair-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-950-provider-specific-integration-docs.md`
- How tested: connector operation coverage, provider section coverage, local
  markdown links, and `git diff --check`.
- What is incomplete: provider request/response examples and live smoke
  evidence remain follow-up gaps when credentials are available.
- Next steps: no PRJ-945 gap repair tasks remain open.
