# Task

## Header
- ID: PRJ-1088
- Title: Audit next frontend cleanup after personality activity-row list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1087
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1088
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The frontend v1 cleanup lane is reducing route-local presentation maps in
`web/src/App.tsx` while keeping route data, route state, and API effects in the
route owner. `PRJ-1087` moved personality recent activity rows into the
personality component owner.

## Goal
Select the next smallest frontend cleanup that improves component ownership
without changing runtime behavior, visuals, route data ownership, or API
contracts.

## Scope
- `web/src/App.tsx`
- `web/src/components/settings.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Success Signal
- User or operator problem: frontend route presentation remains too concentrated
  in `App.tsx`, increasing v1 change risk.
- Expected product or reliability outcome: the next cleanup target is narrow,
  architecture-aligned, and ready for implementation.
- How success will be observed: a concrete follow-up task is selected with
  deferred larger candidates documented.
- Post-launch learning needed: no

## Deliverable For This Stage
An audit result selecting exactly one implementation target for the next slice.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Inspect the remaining inline route-local maps in `App.tsx`.
2. Check whether an existing component owner already exists for the safest
   candidate.
3. Select one implementation target and defer broader candidates.
4. Sync source-of-truth planning and context.
5. Run diff validation.

## Acceptance Criteria
- [x] Exactly one next implementation target is selected.
- [x] Larger or riskier candidates are explicitly deferred.
- [x] Docs and context identify the selected follow-up task.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` was considered for the task size.
- [x] Audit result is recorded in source-of-truth files.
- [x] Validation evidence is attached.

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
- Tests: not applicable; audit-only source-of-truth slice.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "settingsHeroChips|aion-settings-status|toolsGroups|\\.map\\(" -Context 2,5`
  - `Get-Content web/src/components/settings.tsx`
  - `git diff --check`
- Screenshots/logs: not applicable.
- High-risk checks: no runtime, API, DB, or visual behavior changed.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none
- Result: `SettingsStatusPillList` was selected for `PRJ-1089`; diff check
  passed.

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
- Design source reference: existing `/settings` route implementation and CSS
  selectors
- Canonical visual target: preserve current settings hero status pills
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: no; no broad UI refresh
- Existing shared pattern reused: existing settings component owner
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no; audit-only
- Remaining mismatches: none introduced
- State checks: success
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: no markup change in this task
- Input-mode checks: not applicable
- Accessibility checks: no interactive markup change in this task
- Parity evidence: target preserves existing classes and text output

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert documentation/context updates for this audit
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
`SettingsStatusPillList` is smaller and lower-risk than extracting `/tools`
group/item cards because the settings hero chips are static display-only
presentation and `web/src/components/settings.tsx` is already the route owner.

## Production-Grade Required Contract
- Goal: select the next safe frontend component extraction target.
- Scope: audit only the settings/tools route-local map candidates and update
  source-of-truth files.
- Implementation Plan: inspect, select, document, validate.
- Acceptance Criteria: one selected task, deferred broader work, context sync.
- Definition of Done: audit evidence recorded and no code behavior changed.
- Result Report: see below.

## Integration Evidence
- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: `git diff --check`

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: maintainers preparing v1
- Existing workaround or pain: route-local presentation maps remain in
  `App.tsx`
- Smallest useful slice: extract settings hero status-pill list
- Success metric or signal: reduced inline markup while preserving route data
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: `/settings` route render
- SLI: route smoke remains green after implementation follow-up
- SLO: route mount succeeds for authenticated settings route
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: follow-up implementation should run frontend
  build and route smoke
- Rollback or disable path: revert the follow-up component extraction

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
- Data classification: UI display labels only
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: none
- Security tests or scans: not applicable
- Fail-closed behavior: unchanged
- Residual risk: none from this audit

## Result Report
- Task summary: selected settings hero status-pill list extraction as the next
  smallest frontend cleanup.
- Files changed:
  - `.codex/tasks/PRJ-1088-next-cleanup-after-personality-activity-row-list-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested: inspected candidate code and ran `git diff --check`.
- What is incomplete: implementation is intentionally deferred to `PRJ-1089`.
- Next steps: implement `SettingsStatusPillList`.
- Decisions made: defer tools groups/items and broader route data helper moves.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `App.tsx` still maps settings hero chips inline.
- Gaps: settings component owner lacks a dedicated status-pill list wrapper.
- Inconsistencies: route data ownership is correct; only presentation ownership
  is still inline.
- Architecture constraints: keep route state/data in `App()`, move only
  presentational markup.

### 2. Select One Priority Task
- Selected task: `PRJ-1089` extract settings hero status-pill list.
- Priority rationale: smallest display-only route-local map with existing owner.
- Why other candidates were deferred: `/tools` groups/items include toggles,
  link actions, and backend preference state; broader route helpers need a
  separate architecture review.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/settings.tsx`, frontend
  docs/context.
- Logic: add a list component that accepts string chips and preserves CSS
  selectors.
- Edge cases: duplicate chip values are possible in theory, so the follow-up
  should key by chip plus index if needed.

### 4. Execute Implementation
- Implementation notes: audit only; no runtime code changed in this task.

### 5. Verify and Test
- Validation performed: code inspection and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave the three-chip map inline.
- Technical debt introduced: no
- Scalability assessment: the selected follow-up narrows settings ownership
  without creating a new generic abstraction.
- Refinements made: chose settings-specific owner over generic shared chip list.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
