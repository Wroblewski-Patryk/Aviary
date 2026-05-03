# Task

## Header
- ID: PRJ-1032
- Title: Audit next frontend architecture slice after automations shell alignment
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1031
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1032
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-1031 aligned `/automations` with shared module shell components. Remaining
frontend candidates include health/channel helpers, integrations provider rows,
memory signal cards, route data helpers, and decorative panels.

## Goal
Select the next frontend architecture slice after automations shell alignment
based on actual code usage.

## Scope
- `web/src/App.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: docs still list health/channel helper ownership as
  a future candidate even though one helper may no longer be used.
- Expected product or reliability outcome: dead code is removed before it can
  become misleading architecture surface.
- How success will be observed: docs select one concrete cleanup task.
- Post-launch learning needed: no

## Deliverable For This Stage
A completed audit selecting the next implementation task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- verify usage before deleting or moving helper code

## Implementation Plan
1. Inspect remaining health/channel helper candidates in `App.tsx`.
2. Verify whether `conversationChannelStatus` is called.
3. Compare dead-code removal against provider row and memory signal extraction.
4. Select one next implementation slice.
5. Update docs, roadmap, task board, and project state.
6. Run `git diff --check`.

## Acceptance Criteria
- Exactly one next task is selected.
- The selected task is grounded in code usage evidence.
- Deferred candidates and reasons are documented.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for a docs-only planning slice.
- [x] Audit result recorded in frontend docs.
- [x] Task board and project state updated.
- [x] `git diff --check` passes.

## Validation Evidence
- Tests:
  - `git diff --check`
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "conversationChannelStatus"`
- High-risk checks:
  - no runtime code changed

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - add PRJ-1033 as dead channel status helper removal

## Notes
`conversationChannelStatus` and its `ConversationChannelStatus` type are
present in `web/src/App.tsx`, but the only matches are the type declaration and
function declaration. There is no call site. The safest next step is removal,
not extraction.

Deferred:
- integrations provider rows because they include route-specific fallback list
  behavior.
- memory signal cards because they are a single-route `meta` shape.
- provider/health helper movement because the remaining live candidates need a
  separate ownership audit.
- decorative panels because they are visual-sensitive.

## Result Report

- Task summary: selected removal of unused `conversationChannelStatus` helper
  as the next frontend architecture slice.
- Files changed:
  - `.codex/tasks/PRJ-1032-next-frontend-architecture-after-automations-audit.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - implementation is deferred to PRJ-1033
- Next steps:
  - remove unused channel status helper and stale import
- Decisions made:
  - remove dead code before extracting live provider helpers

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - `conversationChannelStatus` remains in `App.tsx` without call sites
- Gaps:
  - docs still treated channel status helper ownership as future work
- Inconsistencies:
  - code contains dead health/channel helper not tied to route behavior
- Architecture constraints:
  - do not invent helper ownership for unused code

### 2. Select One Priority Task
- Selected task:
  - PRJ-1032 audit next frontend architecture slice
- Priority rationale:
  - usage evidence points to dead-code removal
- Why other candidates were deferred:
  - they are live or route-specific and need separate audits

### 3. Plan Implementation
- Files or surfaces to modify:
  - docs and context only
- Logic:
  - select next cleanup task
- Edge cases:
  - avoid removing code in the audit-only task

### 4. Execute Implementation
- Implementation notes:
  - selected PRJ-1033

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - extract helper to a lib, but no caller exists
- Technical debt introduced: no
- Scalability assessment:
  - removing dead helper reduces false architecture surface
- Refinements made:
  - provider/helper movement remains deferred

### 7. Update Documentation and Knowledge
- Docs updated:
  - route cluster audit, v1 roadmap
- Context updated:
  - task board, project state
- Learning journal updated: not applicable
