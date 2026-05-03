# Task

## Header
- ID: PRJ-1090
- Title: Audit next frontend cleanup after settings status-pill extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1089
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1090
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The frontend cleanup lane is keeping v1 route behavior stable while moving
small presentation-only maps out of `App.tsx`. `PRJ-1089` completed the
settings status-pill extraction. Because iteration 1090 is a TESTER iteration,
this audit prioritizes the next target by verification risk and route-smoke
coverage.

## Goal
Select the next smallest frontend cleanup that can be verified cheaply and does
not touch side-effectful tools behavior.

## Scope
- `web/src/App.tsx`
- `web/src/components/tools.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Success Signal
- User or operator problem: tools route still has inline presentation maps, but
  the directory map includes toggles and link actions.
- Expected product or reliability outcome: the next cleanup targets a
  display-only list with clear route-smoke verification.
- How success will be observed: the selected follow-up can be implemented with
  build, route smoke, and diff check evidence.
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
1. Inspect the `/tools` summary and directory maps in `App.tsx`.
2. Inspect the existing tools component owner.
3. Select a display-only target and defer side-effectful maps.
4. Sync source-of-truth planning and context.
5. Run diff validation.

## Acceptance Criteria
- [x] Exactly one next implementation target is selected.
- [x] Side-effectful tools directory work is explicitly deferred.
- [x] Validation evidence is recorded.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` was considered for the task size.
- [x] Audit result is recorded in source-of-truth files.
- [x] No behavior or runtime code changed in this audit.

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
  - `Get-Content web/src/components/tools.tsx`
  - `Get-Content web/src/App.tsx | Select-Object -Skip 4800 -First 140`
  - `Select-String -Path web/src/App.tsx -Pattern "\\]\\.map\\(\\(card\\)|ToolsSummaryCard|toolsOverview\\?\\.groups|aion-tools-group|group\\.items\\.map" -Context 2,4`
  - `git diff --check`
- Screenshots/logs: not applicable.
- High-risk checks: confirmed tools directory cards include toggles and link
  action behavior, so they are not the next small test-focused slice.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none
- Result: `ToolsSummaryCardList` was selected for `PRJ-1091`; diff check
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
- Design source reference: existing `/tools` summary card grid
- Canonical visual target: preserve current tools summary grid and card classes
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: no; no broad UI refresh
- Existing shared pattern reused: existing tools component owner
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
- Parity evidence: target preserves existing classes and card component

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
The tools group/item directory remains a valid later target, but it should be
handled only after a dedicated behavior audit because it contains user
preference toggles, provider readiness display, and Telegram link actions.

## Production-Grade Required Contract
- Goal: select the next test-focused frontend component extraction target.
- Scope: audit only tools summary/directory candidates and update
  source-of-truth files.
- Implementation Plan: inspect, select, document, validate.
- Acceptance Criteria: one selected task, side-effectful work deferred,
  context sync.
- Definition of Done: audit evidence recorded and no runtime behavior changed.
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
- Existing workaround or pain: tools route presentation is still partly inline
  in `App.tsx`
- Smallest useful slice: extract tools summary card list
- Success metric or signal: follow-up route smoke remains green for `/tools`
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: `/tools` route render
- SLI: route smoke remains green after implementation follow-up
- SLO: route mount succeeds for authenticated tools route
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
- Data classification: tools summary display labels only
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: none
- Security tests or scans: not applicable
- Fail-closed behavior: unchanged
- Residual risk: none from this audit

## Result Report
- Task summary: selected tools summary card-list extraction as the next
  smallest test-focused cleanup.
- Files changed:
  - `.codex/tasks/PRJ-1090-next-cleanup-after-settings-status-pill-list-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested: inspected tools route/component code and ran `git diff --check`.
- What is incomplete: implementation is intentionally deferred to `PRJ-1091`.
- Next steps: implement `ToolsSummaryCardList`.
- Decisions made: defer tools group/item directory extraction.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: tools summary card map remains inline; tools directory map is larger
  and behaviorful.
- Gaps: tools component owner lacks a summary-card list wrapper.
- Inconsistencies: no behavior issue; only presentation ownership remains
  concentrated.
- Architecture constraints: keep tools API data and preference handlers in
  `App()`.

### 2. Select One Priority Task
- Selected task: `PRJ-1091` extract tools summary card list.
- Priority rationale: display-only, route-smoke-covered, existing owner module.
- Why other candidates were deferred: tools groups/items include toggles and
  link actions; broader route helper movement requires separate review.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/tools.tsx`, docs/context.
- Logic: add a list wrapper around existing `ToolsSummaryCard`.
- Edge cases: duplicate titles are unlikely; follow-up can key title plus index
  if needed.

### 4. Execute Implementation
- Implementation notes: audit only; no runtime code changed in this task.

### 5. Verify and Test
- Validation performed: code inspection and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave the four-card map inline.
- Technical debt introduced: no
- Scalability assessment: tools-specific wrapper avoids premature generic list
  abstraction.
- Refinements made: selected a TESTER-friendly target with clear smoke coverage.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
