# Task

## Header
- ID: PRJ-1049
- Title: Align automations health rows with shared module dot-row list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1048
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1049
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1048` selected `/automations` health-row shared alignment. The current
rows manually render the same wrapper and row shape provided by
`ModuleDotRowList`.

## Goal
Replace local `/automations` health-row presentation with `ModuleDotRowList`
while preserving health data ownership, selectors, and route behavior.

## Scope
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1049-automations-health-row-alignment.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Replace local automations health row wrapper/map with `ModuleDotRowList`.
2. Keep `automationHealthRows` and health snapshot data construction in
   `App()`.
3. Run frontend build, route smoke, and diff validation.
4. Sync docs/context.

## Acceptance Criteria
- `/automations` health rows use `ModuleDotRowList`.
- Existing `aion-automations-health-*` selectors are preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Implementation is complete and scoped to automations health rows.
- [x] Frontend build passes.
- [x] Full route smoke passes.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- Manual checks:
  - `git diff --check`
- Result: passed; route smoke reported `status=ok`, `route_count=14`.

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
- Existing shared pattern reused: `ModuleDotRowList`
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; no intentional visual change
- Remaining mismatches: decorative panels remain route-local by design.

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
- Goal: align automations health rows with shared dot-row list.
- Scope: `web/src/App.tsx` plus task/context/docs.
- Implementation Plan: replace local map, validate, sync.
- Acceptance Criteria: shared component reuse with preserved selectors.
- Definition of Done: build, smoke, diff check, context sync.
- Result Report: automations health rows now use `ModuleDotRowList`.

## Result Report
- Task summary: automations health rows now reuse `ModuleDotRowList`.
- Files changed: `web/src/App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: decorative panels remain route-local by design.
- Next steps: audit next cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: local health row map duplicated shared dot-row list structure.
- Gaps: shared dot-row pattern was not reused in automations health details.
- Inconsistencies: integrations readiness and other module rows use shared list
  components.
- Architecture constraints: keep health data in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1049.
- Priority rationale: selected by PRJ-1048.
- Why other candidates were deferred: route data helpers and decorative panels
  are broader.

### 3. Plan Implementation
- Files or surfaces to modify: automations branch in `web/src/App.tsx` plus
  docs/context.
- Logic: pass `automationHealthRows` to `ModuleDotRowList`.
- Edge cases: preserve classes via route/row keys.

### 4. Execute Implementation
- Implementation notes: replaced only the local health row map.

### 5. Verify and Test
- Validation performed: build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave this as-is until route data helpers.
- Technical debt introduced: no
- Scalability assessment: reduces duplicated JSX without changing ownership.
- Refinements made: none required.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
