# Task

## Header
- ID: PRJ-1089
- Title: Extract settings hero status-pill list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1088
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1089
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1088` selected the `/settings` hero status-pill map as the next smallest
frontend cleanup. The route already owns settings state and data in `App()`,
while `web/src/components/settings.tsx` owns settings presentation shells.

## Goal
Move the settings hero status-pill presentation into the existing settings
component owner without changing settings data, state, copy, CSS selectors, or
route behavior.

## Scope
- `web/src/App.tsx`
- `web/src/components/settings.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Success Signal
- User or operator problem: `App.tsx` still owns small route-local presentation
  maps that make v1 harder to review.
- Expected product or reliability outcome: `/settings` keeps the same visual
  output while status-pill markup moves to the settings owner.
- How success will be observed: frontend build and route smoke pass with the
  settings route still mounted.
- Post-launch learning needed: no

## Deliverable For This Stage
A verified component extraction with source-of-truth updates and validation
evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Add `SettingsStatusPillList` to `web/src/components/settings.tsx`.
2. Replace the inline `settingsHeroChips.map(...)` markup in `App.tsx`.
3. Keep `settingsHeroChips` data construction in `App()`.
4. Sync route component map, audit notes, roadmap, task board, and project
   state.
5. Run frontend build, route smoke, and diff validation.

## Acceptance Criteria
- [x] `App.tsx` no longer maps `settingsHeroChips` inline.
- [x] Existing `aion-settings-status-grid` and `aion-settings-status-pill`
  selectors are preserved.
- [x] Settings route data and state remain in `App()`.
- [x] Frontend validation passes.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` was considered for the task size.
- [x] Implementation is tiny, testable, and reversible.
- [x] No temporary solutions, mocks, bypasses, or duplicated logic were added.
- [x] Source-of-truth docs and context are synchronized.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- Manual checks:
  - `git diff --check`
- Screenshots/logs: route smoke covers `/settings` mount marker.
- High-risk checks: no API, DB, auth, AI, or deployment path changed.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none
- Result: passed; build completed, route smoke reported `status=ok` with
  `route_count=14`, and diff check returned exit code 0.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing `/settings` hero status-pill implementation
- Canonical visual target: preserve current status-pill grid and pill classes
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: no; no broad UI refresh
- Existing shared pattern reused: settings route component owner
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no; markup-only extraction covered by
  build and route smoke
- Remaining mismatches: none introduced
- State checks: success
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: existing CSS selectors preserved
- Input-mode checks: not applicable
- Accessibility checks: non-interactive text pills only
- Parity evidence: `aion-settings-status-grid` and
  `aion-settings-status-pill` are unchanged

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert `SettingsStatusPillList` usage and docs/context updates
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
Keys use chip text plus index so duplicate display labels cannot collide.

## Production-Grade Required Contract
- Goal: extract settings hero status-pill presentation into the settings owner.
- Scope: settings presentation component, `App.tsx` call site, and
  source-of-truth docs/context.
- Implementation Plan: add component, replace inline map, validate.
- Acceptance Criteria: selectors preserved, data ownership unchanged,
  validation passes.
- Definition of Done: evidence recorded and no behavior drift.
- Result Report: see below.

## Integration Evidence
- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: frontend build, route smoke, diff check

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: maintainers preparing v1
- Existing workaround or pain: small presentation map was still inline in
  `App.tsx`
- Smallest useful slice: settings status-pill list extraction
- Success metric or signal: route smoke remains green with `/settings` mounted
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: authenticated `/settings` route render
- SLI: route smoke passes for `/settings`
- SLO: route mount succeeds for authenticated settings route
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke:
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- Rollback or disable path: revert this component extraction

## AI Testing Evidence
- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: no AI behavior touched

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: settings display labels only
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: none
- Security tests or scans: not applicable
- Fail-closed behavior: unchanged
- Residual risk: none from this refactor

## Result Report
- Task summary: added `SettingsStatusPillList` and reused it for the settings
  hero status pills.
- Files changed:
  - `.codex/tasks/PRJ-1089-settings-status-pill-list-extraction.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/src/App.tsx`
  - `web/src/components/settings.tsx`
- How tested: frontend build, route smoke, and diff check passed.
- What is incomplete: nothing known.
- Next steps: audit the next smallest frontend cleanup.
- Decisions made: keep settings data and draft state in `App()`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: settings hero status-pill markup was still inline in `App.tsx`.
- Gaps: settings component owner lacked a list wrapper for the status pills.
- Inconsistencies: no behavior inconsistency; only ownership concentration.
- Architecture constraints: preserve route state/data ownership in `App()`.

### 2. Select One Priority Task
- Selected task: extract `SettingsStatusPillList`.
- Priority rationale: smallest display-only extraction selected by `PRJ-1088`.
- Why other candidates were deferred: tools item cards include actions and
  preference state, and route data helpers need a separate audit.

### 3. Plan Implementation
- Files or surfaces to modify: `settings.tsx`, `App.tsx`, docs/context.
- Logic: render the same status grid and pills from a string list.
- Edge cases: duplicate label keys handled with label plus index.

### 4. Execute Implementation
- Implementation notes: `SettingsStatusPillList` renders the existing grid and
  pill classes; `App.tsx` passes `settingsHeroChips`.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed; build completed, route smoke reported `status=ok` with
  `route_count=14`, and diff check returned exit code 0.

### 6. Self-Review
- Simpler option considered: leave the three-chip map inline.
- Technical debt introduced: no
- Scalability assessment: route-specific component avoids a premature generic
  chip-list abstraction.
- Refinements made: duplicate-safe key construction added.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
