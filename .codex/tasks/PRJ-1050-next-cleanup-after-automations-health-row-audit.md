# Task

## Header
- ID: PRJ-1050
- Title: Audit next frontend cleanup after automations health-row alignment
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1049
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1050
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1049` aligned `/automations` health rows with `ModuleDotRowList`.
Remaining safe frontend cleanup candidates should continue avoiding route data
helper movement and decorative panel extraction.

## Goal
Select the next small architecture-aligned frontend cleanup after automations
health-row alignment.

## Scope
- `.codex/tasks/PRJ-1050-next-cleanup-after-automations-health-row-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining simple route-local list wrappers.
2. Compare selectors and data shape against existing shared components.
3. Select exactly one next implementation target.
4. Sync docs/context and validate whitespace.

## Acceptance Criteria
- One target is selected.
- Deferred candidates are documented.
- `git diff --check` passes.

## Definition of Done
- [x] Task contract is complete.
- [x] Docs and context are synchronized.
- [x] Validation evidence is recorded.

## Validation Evidence
- Tests: not run; docs-only audit.
- Manual checks:
  - `git diff --check`
- Result: passed.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/frontend/app-route-cluster-audit.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Existing shared pattern reused: planned `ModuleDotRowList`
- New shared pattern introduced: no
- Remaining mismatches: insights guidance rows remain locally mapped until
  PRJ-1051.

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none

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

## Production-Grade Required Contract
- Goal: select the next frontend cleanup.
- Scope: docs/context only.
- Implementation Plan: inspect, select, sync, validate.
- Acceptance Criteria: selected next target and validation evidence.
- Definition of Done: docs/context synchronized.
- Result Report: selected insights guidance-row list extraction.

## Result Report
- Task summary: selected insights guidance-row shared alignment.
- Files changed: task, task board, project state, frontend audit, v1 roadmap.
- How tested: `git diff --check`.
- What is incomplete: implementation deferred to PRJ-1051.
- Next steps: implement PRJ-1051.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: insights guidance rows still use a local wrapper and
  `ModuleRouteSideRow` map.
- Gaps: the same wrapper/row shape already exists as `ModuleDotRowList`.
- Inconsistencies: plans, goals, integrations, and automations now reuse shared
  dot-row lists for similar title/body rows.
- Architecture constraints: keep route data arrays and decorative panels in
  `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1050.
- Priority rationale: smallest remaining presentation-only cleanup.
- Why other candidates were deferred: route data helpers and decorative panels
  are broader.

### 3. Plan Implementation
- Files or surfaces to modify: docs/context only.
- Logic: select `ModuleDotRowList` reuse for insights guidance rows.
- Edge cases: preserve `aion-insights-guidance-*` selectors.

### 4. Execute Implementation
- Implementation notes: recorded target and deferrals.

### 5. Verify and Test
- Validation performed: `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: move directly to route data helper extraction.
- Technical debt introduced: no
- Scalability assessment: selected target continues established shared list
  reuse.
- Refinements made: route data helper movement remains deferred.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
