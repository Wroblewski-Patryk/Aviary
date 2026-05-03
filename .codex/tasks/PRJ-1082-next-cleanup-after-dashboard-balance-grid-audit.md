# Task

## Header
- ID: PRJ-1082
- Title: Audit next frontend cleanup after dashboard balance-grid extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1081
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1082
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1081` extracted `DashboardBalanceGrid`. The dashboard cognitive flow track
still has an inline step map, but the current phase panel and full flow shell
should remain in `App()`.

## Goal
Select the next smallest frontend cleanup after dashboard balance-grid
extraction.

## Scope
- `web/src/App.tsx`
- `web/src/components/dashboard.tsx`
- `.codex/tasks/PRJ-1082-next-cleanup-after-dashboard-balance-grid-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect the dashboard cognitive flow step map.
2. Select exactly one small extraction candidate.
3. Confirm the candidate does not move the full flow panel.
4. Record deferred broader candidates.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task preserves active-step class behavior.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "dashboardCognitiveSteps|aion-dashboard-flow" -Context 1,5`
  - `git diff --check`
- Result: dashboard cognitive flow track map found; diff check passed.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Existing shared pattern reused: dashboard component owner
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; audit-only task

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Result Report
- Task summary: selected `DashboardCognitiveFlowTrack` extraction as the next
  tiny frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: dashboard cognitive flow inspection and `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1083.
- Next steps: add and reuse `DashboardCognitiveFlowTrack`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard cognitive flow steps remain inline in `App.tsx`.
- Gaps: dashboard component owner does not cover the flow track presentation.
- Inconsistencies: other dashboard repeated presentation maps now have wrappers.
- Architecture constraints: do not move the full flow shell or current phase.

### 2. Select One Priority Task
- Selected task: PRJ-1083 extract `DashboardCognitiveFlowTrack`.
- Priority rationale: small flow-track-only extraction preserving active state.
- Why other candidates were deferred: full flow panel, figure notes, settings
  controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  component map, docs/context.
- Logic: render `token/title/detail/active` steps and preserve active class.
- Edge cases: keep current phase computation in `App()`.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: dashboard cognitive flow inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: move the full flow panel.
- Technical debt introduced: no
- Scalability assessment: track-only extraction keeps the flagship layout
  stable and reversible.
- Refinements made: phase aside remains inline.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
