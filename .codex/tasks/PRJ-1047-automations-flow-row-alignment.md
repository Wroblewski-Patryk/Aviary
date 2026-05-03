# Task

## Header
- ID: PRJ-1047
- Title: Align automations flow rows with shared module value-row list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1046
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1047
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1046` selected `/automations` flow-row shared alignment. The existing
`automationFlowRows` data already matches `ModuleValueRowList` and can preserve
all `aion-automations-flow-*` selectors through route-keyed props.

## Goal
Replace local `/automations` flow-row presentation with `ModuleValueRowList`
while preserving scheduler/proactive data ownership and route behavior.

## Scope
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1047-automations-flow-row-alignment.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Replace automations local flow-list map with `ModuleValueRowList`.
2. Keep `automationFlowRows`, scheduler summary, health data, proactive opt-in,
   and switchboard presentation in `App()`.
3. Run frontend build, route smoke, and diff validation.
4. Sync task board, project state, frontend docs, and roadmap.

## Acceptance Criteria
- `/automations` flow rows use `ModuleValueRowList`.
- Existing `aion-automations-flow-*` selectors are preserved.
- Build and route smoke pass.

## Definition of Done
- [x] Implementation is complete and scoped to automations flow rows.
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
- Design source reference: existing `/automations` route
- Existing shared pattern reused: `ModuleValueRowList`
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; no intentional visual change
- Remaining mismatches: decorative switchboard remains route-local by design.

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Rollback note: revert this refactor if visual regression appears.

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

## Notes
Next likely audit: remaining frontend cleanup should choose between route
data-helper extraction and visual-specific panels, with decorative panels still
treated carefully.

## Production-Grade Required Contract
- Goal: align automations flow-row presentation with shared route-keyed
  components.
- Scope: `web/src/App.tsx` plus task/context/docs.
- Implementation Plan: replace local map, validate, sync docs/context.
- Acceptance Criteria: shared component reuse with preserved selectors.
- Definition of Done: build, route smoke, diff check, context sync.
- Result Report: automations flow rows now use `ModuleValueRowList`.

## Integration Evidence
- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Regression check performed: frontend build and route smoke

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: maintainers preparing v1
- Smallest useful slice: `/automations` flow-row presentation.
- Success metric or signal: route smoke passes with all routes.

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: authenticated `/automations` route mount
- Smoke command or manual smoke: `npm run smoke:routes`

## AI Testing Evidence
- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Result: not applicable

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: no data changed
- Residual risk: none introduced

## Result Report
- Task summary: automations flow rows now reuse `ModuleValueRowList`.
- Files changed: `web/src/App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: decorative switchboard remains route-local by design.
- Next steps: audit the next low-risk frontend cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: local automations flow-row JSX duplicated shared value-row structure.
- Gaps: shared value-row pattern was not reused on automations.
- Inconsistencies: insights and integrations already use shared value-row lists.
- Architecture constraints: keep health/proactive data in `App()`.

### 2. Select One Priority Task
- Selected task: `PRJ-1047` align automations flow rows with shared module
  value-row list.
- Priority rationale: selected by PRJ-1046 as the smallest safe slice.
- Why other candidates were deferred: route data helpers and decorative panels
  are broader.

### 3. Plan Implementation
- Files or surfaces to modify: automations route branch in `web/src/App.tsx`
  plus docs/context.
- Logic: pass `automationFlowRows` to `ModuleValueRowList`.
- Edge cases: preserve `aion-automations-flow-*` classes via route/row keys.

### 4. Execute Implementation
- Implementation notes: replaced only the local row map.

### 5. Verify and Test
- Validation performed:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- Result: passed.

### 6. Self-Review
- Simpler option considered: defer automations because it uses health data.
- Technical debt introduced: no
- Scalability assessment: continues existing shared list pattern without moving
  runtime-coupled data.
- Refinements made: switchboard extraction explicitly deferred.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
