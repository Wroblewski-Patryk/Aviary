# Task

## Header
- ID: PRJ-1046
- Title: Audit next frontend cleanup after integrations side-panel alignment
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1045
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1046
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1045` aligned `/integrations` side panels with existing shared route-keyed
components. Remaining candidates include automations flow rows, route data
helpers, and visual-specific decorative panels.

## Goal
Select one narrow frontend cleanup target that reuses an existing shared
component without changing runtime/provider/health semantics.

## Scope
- `.codex/tasks/PRJ-1046-next-cleanup-after-integrations-side-panel-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining route-local JSX candidates.
2. Compare class and data shape against existing shared components.
3. Select exactly one next implementation target.
4. Record validation and update source-of-truth files.

## Acceptance Criteria
- One next target is selected.
- Deferred candidates are documented.
- `git diff --check` passes.

## Definition of Done
- [x] Task contract is complete.
- [x] Board, project state, frontend audit, and roadmap are synchronized.
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
- Design source reference: existing `/automations` route
- Existing shared pattern reused: planned `ModuleValueRowList`
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; implementation deferred
- Remaining mismatches: automations flow rows remain route-local until PRJ-1047.

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Rollback note: revert docs/context edits.

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
Selected next task: `PRJ-1047` align automations flow rows with
`ModuleValueRowList`.

Deferred candidates:
- route data-helper extraction, because it is broader than one presentation
  cleanup.
- decorative web/orbit/switchboard panels, because they are visual-specific.
- health/provider helper movement, because it is runtime-contract-coupled.

## Production-Grade Required Contract
- Goal: select the next architecture-aligned frontend cleanup.
- Scope: docs/context only.
- Implementation Plan: inspect, select, sync docs/context, validate.
- Acceptance Criteria: selected next target and validation evidence.
- Definition of Done: source-of-truth sync with passing diff check.
- Result Report: selected automations flow-row presentation extraction.

## Integration Evidence
- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Regression check performed: `git diff --check`

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: maintainers preparing v1
- Smallest useful slice: `/automations` flow-row presentation.
- Success metric or signal: PRJ-1047 can preserve selectors through
  `ModuleValueRowList`.

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: authenticated `/automations` route mount
- Smoke command or manual smoke: planned for PRJ-1047

## AI Testing Evidence
- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Result: not applicable

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: no data changed
- Residual risk: none introduced

## Result Report
- Task summary: selected automations flow-row shared alignment.
- Files changed: task, task board, project state, frontend audit, v1 roadmap.
- How tested: `git diff --check`.
- What is incomplete: implementation deferred to PRJ-1047.
- Next steps: implement PRJ-1047.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `/automations` flow rows still duplicate the value-row presentation
  shape.
- Gaps: route-keyed value rows are used elsewhere but not here.
- Inconsistencies: `automationFlowRows` already has `token/title/detail/value`.
- Architecture constraints: keep health/proactive data ownership in `App()`.

### 2. Select One Priority Task
- Selected task: `PRJ-1046` audit next frontend cleanup after integrations
  side-panel alignment.
- Priority rationale: it is the board-indicated next slice.
- Why other candidates were deferred: route data and decorative panels are
  broader.

### 3. Plan Implementation
- Files or surfaces to modify: docs/context only.
- Logic: select class-preserving `ModuleValueRowList` reuse.
- Edge cases: verify `routeKey="automations"` and `rowKey="flow"` preserve
  `aion-automations-flow-*`.

### 4. Execute Implementation
- Implementation notes: recorded target and deferrals.

### 5. Verify and Test
- Validation performed: `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: stop after integrations cleanup.
- Technical debt introduced: no
- Scalability assessment: selected target continues existing component reuse.
- Refinements made: deferred switchboard/decorative extraction.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
