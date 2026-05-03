# Task

## Header
- ID: PRJ-1086
- Title: Audit next frontend cleanup after dashboard figure note-list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1085
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1086
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1085` extracted dashboard figure notes. The personality route still has a
small activity-row list with a different action-bearing shape from the dashboard
recent list.

## Goal
Select the next smallest frontend cleanup after dashboard figure note-list
extraction.

## Scope
- `web/src/App.tsx`
- `web/src/components/personality.tsx`
- `.codex/tasks/PRJ-1086-next-cleanup-after-dashboard-figure-note-list-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect the personality route recent activity row map.
2. Select exactly one small extraction candidate.
3. Confirm the candidate does not collapse it with dashboard recent rows.
4. Record deferred broader candidates.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task preserves the personality-specific action label shape.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "aion-personality-activity-row|personalityRecentActivity.map|copy.common.view" -Context 1,6`
  - `Get-Content web/src/components/personality.tsx`
  - `git diff --check`
- Result: personality activity row map found; diff check passed.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Existing shared pattern reused: personality component owner
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
- Task summary: selected `PersonalityActivityRowList` extraction as the next
  tiny frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: personality activity row inspection and `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1087.
- Next steps: add and reuse `PersonalityActivityRowList`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: personality activity rows remain inline in `App.tsx`.
- Gaps: personality component owner does not cover activity row-list
  presentation.
- Inconsistencies: timeline and signal rows already have personality-owned
  wrappers.
- Architecture constraints: keep data and route panel composition in `App()`;
  avoid false sharing with dashboard recent activity rows.

### 2. Select One Priority Task
- Selected task: PRJ-1087 extract `PersonalityActivityRowList`.
- Priority rationale: small owner-aligned extraction with no behavior changes.
- Why other candidates were deferred: settings controls, tools groups, route
  data helpers, and full route extraction are broader.

### 3. Plan Implementation
- Files or surfaces to modify: personality component owner, route JSX,
  component map, docs/context.
- Logic: render `key/title/when` rows and a caller-provided `viewLabel`.
- Edge cases: preserve wrapper class and chip class.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: personality activity row inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: reuse dashboard recent activity list.
- Technical debt introduced: no
- Scalability assessment: personality-specific wrapper avoids false abstraction.
- Refinements made: `viewLabel` planned as prop.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
