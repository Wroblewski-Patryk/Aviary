# Task

## Header
- ID: PRJ-998
- Title: Audit remaining health/channel helper extraction
- Task Type: documentation
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-997
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 998
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

Learned-state helpers were extracted in PRJ-997. The remaining helper candidates
include `conversationChannelStatus`, `numberValue`, and `scaledMetricSize`.

## Goal

Decide whether the health/channel helper should move now or wait for provider
route ownership cleanup.

## Scope

- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: health helper extraction could cross a provider
  boundary too early.
- Expected product or reliability outcome: next helper extraction remains pure
  and low-risk.
- How success will be observed: audit names the next implementation task.

## Deliverable For This Stage

Update docs and context to defer health/channel extraction and select generic
metric helper extraction.

## Constraints
- do not change runtime code in this task
- preserve the provider/health boundary until route ownership is clearer
- choose a narrow next slice

## Implementation Plan
1. Inspect health/channel and metric helper call sites.
2. Compare provider coupling.
3. Defer `conversationChannelStatus`.
4. Select `numberValue`/`scaledMetricSize` extraction as PRJ-999.
5. Run `git diff --check`.

## Acceptance Criteria
- Health/channel helper decision is documented.
- PRJ-999 is added to the roadmap.
- `git diff --check` passes.

## Definition of Done
- [x] Decision recorded.
- [x] Roadmap and context updated.
- [x] Diff validation completed.

## Validation Evidence
- Tests:
  - `git diff --check`
  - result: passed
- Manual checks:
  - confirmed `conversationChannelStatus` depends on Telegram health/provider
    semantics
  - confirmed `numberValue`/`scaledMetricSize` are pure metric formatting

## Result Report

- Task summary: deferred health/channel extraction and selected metric helpers
  for PRJ-999.
- Files changed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - PRJ-999 implementation remains next
