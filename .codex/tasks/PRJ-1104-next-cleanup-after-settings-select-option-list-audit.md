# Task

## Header
- ID: PRJ-1104
- Title: Audit next frontend cleanup after settings select option extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1103
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1104
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1103` moved the settings select option rendering behind
`SettingsSelectOptionList`. The remaining `web/src/App.tsx` `.map(...)`
call sites need a fresh architecture pass before another extraction is selected.

## Goal
Determine the next smallest useful frontend cleanup that keeps the v1 browser
shell aligned with the approved route/component ownership model.

## Success Signal
- User or operator problem: frontend cleanup continues without moving behavior
  into the wrong owner.
- Expected product or reliability outcome: the next task is small, testable,
  and does not create a workaround or duplicate route state.
- How success will be observed: remaining map call sites are classified and one
  next task is recorded.
- Post-launch learning needed: no

## Scope
- Inspect `web/src/App.tsx` remaining `.map(...)` call sites.
- Inspect current public shell and tools component owners.
- Update frontend source-of-truth docs and context with the selected next
  task.

## Deliverable For This Stage
An audit result and source-of-truth updates selecting the next safe frontend
cleanup task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Review current context and autonomous loop rules.
2. Classify remaining `.map(...)` call sites in `App.tsx`.
3. Compare candidates against component ownership boundaries.
4. Select exactly one next task.
5. Update the task board, project state, and frontend docs.
6. Run repository whitespace validation.

## Acceptance Criteria
- Remaining `.map(...)` call sites are grouped by risk/ownership.
- One next task is selected with a clear reason.
- Deferred candidates are documented.
- `git diff --check` passes.

## Definition of Done
- [x] Current state analyzed.
- [x] One next priority task selected.
- [x] Validation evidence recorded.
- [x] Context and docs updated.

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
- Tests: not applicable for audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 2,6`
  - `Get-Content web/src/components/public-shell.tsx`
  - `Get-Content web/src/components/tools.tsx`
  - `Get-Content web/src/App.tsx | Select-Object -Skip 3550 -First 60`
  - `Get-Content web/src/App.tsx | Select-Object -Skip 4800 -First 210`
  - `Get-Content web/src/App.tsx | Select-Object -Skip 5035 -First 45`
- Screenshots/logs: not applicable.
- High-risk checks:
  - `git diff --check`
  - result: passed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.agents/workflows/general.md`
  - `docs/governance/autonomous-engineering-loop.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: existing browser shell implementation and route
  component map
- Canonical visual target: current v1 browser shell
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable for audit-only task
- Visual-direction brief reviewed: not applicable for audit-only task
- Existing shared pattern reused: route/component ownership audit pattern
- New shared pattern introduced: no
- Design-memory entry reused: current frontend component map
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: not assessed in this audit
- State checks: loading, empty, error, and success states were considered for
  the tools directory candidate and deferred to the next test task.
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: deferred because no UI changed
- Input-mode checks: deferred because no UI changed
- Accessibility checks: deferred because no UI changed
- Parity evidence: not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: docs-only audit; revert task/context/doc changes if needed
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist (mandatory)
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
- [x] Learning journal was updated if a recurring pitfall is confirmed.

## Notes
Remaining `.map(...)` call sites are no longer obvious tiny display-only JSX
repetitions. They fall into these categories:

- pure data projections: planning names, recent channels, goal horizon rows,
  integration provider rows, chat motivation metric text, and public hero
  highlight projection
- behavior/state updates: local transcript reconciliation updates
- behaviorful render maps: tools directory groups/items with toggles, provider
  readiness, and Telegram link actions
- ref-sensitive render maps: chat transcript rows and the bottom mobile tabbar

The next smallest useful task is `PRJ-1105`: add a focused tools-directory
behavior characterization before extracting the behaviorful `/tools` directory
surface.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime
  surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

This task is audit-only and does not deliver runtime behavior.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: future frontend maintainers and v1 release
  confidence
- Existing workaround or pain: `App.tsx` still contains behaviorful route-local
  maps that should not be blindly extracted.
- Smallest useful slice: classify remaining maps and select the next test
  characterization task.
- Success metric or signal: next task is selected without architecture drift.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: tools directory preference and linking flow
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: `git diff --check`
- Rollback or disable path: revert docs/context/task updates

- `INTEGRATION_CHECKLIST.md` reviewed: yes
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: `git diff --check`

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: no data touched
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: no secrets touched
- Security tests or scans: not applicable
- Fail-closed behavior: not applicable
- Residual risk: none for audit-only change

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: Classified the remaining `App.tsx` maps and selected a
  behavior characterization task before any tools directory extraction.
- Files changed:
  - `.codex/tasks/PRJ-1104-next-cleanup-after-settings-select-option-list-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - tools directory behavior characterization is not yet implemented
- Next steps:
  - `PRJ-1105` add focused tools-directory behavior characterization
- Decisions made:
  - do not extract the tools directory, chat transcript, or mobile tabbar
    without a focused behavior/ref audit first

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - `App.tsx` still contains maps, but the remaining render maps are behaviorful
    or ref-sensitive.
- Gaps:
  - tools directory behavior lacks a dedicated frontend characterization before
    any broad component extraction.
- Inconsistencies:
  - none found.
- Architecture constraints:
  - route state, API calls, side effects, and action callbacks remain in
    `App()` unless a specific owner is approved.

### 2. Select One Priority Task
- Selected task:
  - `PRJ-1104` audit next frontend cleanup after settings select option
    extraction.
- Priority rationale:
  - ARCHITECT iteration should prevent ownership drift before another extraction.
- Why other candidates were deferred:
  - tools directory extraction has toggles/provider/link actions.
  - chat transcript mapping owns refs, delivery labels, timestamps, and markdown.
  - mobile tabbar owns refs and scroll behavior.
  - pure data projections are not presentation components.

### 3. Plan Implementation
- Files or surfaces to modify:
  - task file, task board, project state, frontend audit docs, v1 roadmap.
- Logic:
  - classify remaining maps and select the next smallest safe task.
- Edge cases:
  - avoid treating data projections as component extraction targets.

### 4. Execute Implementation
- Implementation notes:
  - audit-only docs/context updates were made; runtime code was not changed.

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - extract the public hero highlight projection immediately.
- Technical debt introduced: no
- Scalability assessment:
  - selecting a characterization task scales better because the remaining main
    candidate is behaviorful.
- Refinements made:
  - deferred extraction candidates were grouped by ownership risk.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
