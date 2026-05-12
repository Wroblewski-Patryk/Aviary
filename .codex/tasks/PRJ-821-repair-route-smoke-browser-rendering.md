# Task

## Header
- ID: PRJ-821
- Title: Repair route smoke browser rendering
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-820
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 821
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-820` proved that real Chrome/CDP browser interaction can validate a
focused app chat flow when the harness avoids the previously flaky local
browser paths. `.agents/state/regression-log.md` still monitors the broader
`npm run smoke:routes` route smoke because its Chrome `--dump-dom` path times
out.

## Goal
Repair the existing route smoke harness so it uses a stable browser rendering
path and can again validate public and authenticated route markers.

## Success Signal
- User or operator problem: broad frontend route smoke is still failing even
  though focused browser proof is available.
- Expected product or reliability outcome: route-shell regressions regain a
  repeatable browser smoke gate.
- How success will be observed: `npm run smoke:routes` passes with all route
  markers found.
- Post-launch learning needed: no

## Deliverable For This Stage
One scoped update to the existing route smoke harness plus context/state
evidence.

## Scope
- `web/scripts/route-smoke.mjs`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.agents/state/current-focus.md`
- `.agents/state/next-steps.md`
- `.agents/state/system-health.md`
- `.agents/state/regression-log.md`
- `.codex/context/LEARNING_JOURNAL.md`
- `.codex/tasks/PRJ-821-repair-route-smoke-browser-rendering.md`

## Implementation Plan
1. Reuse the existing route smoke static server and synthetic app-facing API
   responses.
2. Replace the Chrome `--dump-dom` render path with a CDP Runtime-based route
   marker check that avoids the previously flaky `Page.enable`.
3. Keep route results and diagnostics structured.
4. Run route smoke, focused connector browser proof, web typecheck/build, and
   diff checks.
5. Update task board, project state, and agent state files.

## Acceptance Criteria
- `npm run smoke:routes` checks every existing route marker and passes.
- The harness remains headless and uses synthetic app-facing API data only.
- The route smoke still reports route-level diagnostics on failure.
- No product runtime, backend provider, auth, DB, secret, or deployment
  behavior changes.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] `npm run smoke:routes` passes.
- [x] Focused connector browser proof still passes.
- [x] Web typecheck and build pass.
- [x] Context/state files record the repaired route-smoke evidence.

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
  - `Push-Location .\web; npm run smoke:routes; Pop-Location` -> passed with
    `14` routes and status `ok`
  - `Push-Location .\web; npm run test:connector-confirmation-browser; Pop-Location`
    -> passed with report status `ok`
  - `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
    -> passed
  - `Push-Location .\web; npm run test:connector-confirmation-render; Pop-Location`
    -> passed
  - `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
    -> passed
  - `Push-Location .\web; npm exec -- vite build; Pop-Location` -> passed
  - `git diff --check` -> passed with LF/CRLF warnings only
- Manual checks: route smoke report verified all 14 route markers.
- Screenshots/logs: structured route smoke JSON report status `ok`.
- High-risk checks: no runtime, provider, auth, DB, env, secret, deployment,
  or health behavior changed.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/engineering/testing.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: existing route markers and route-shell structure
- Canonical visual target: not pixel parity; route render marker smoke
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: no
- Visual-direction brief reviewed: no
- Existing shared pattern reused: route smoke harness
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: not applicable
- Remaining mismatches: none for route marker smoke
- State checks: loading | success
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop route smoke only
- Input-mode checks: not applicable
- Accessibility checks: not applicable
- Parity evidence: route marker report passed for all current routes.

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: restore previous dump-dom route smoke path
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
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This is a harness repair only. It must not change route behavior or product
runtime contracts.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB
-> validation -> error handling -> test. Partial implementations, mock-only
paths, placeholders, fake data, and temporary fixes are forbidden.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: developers validating route-shell regressions
- Existing workaround or pain: focused browser tests pass, but broad route
  smoke still fails on Chrome dump-dom timeout
- Smallest useful slice: repair route smoke rendering path
- Success metric or signal: `npm run smoke:routes` passes
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## User Feedback Evidence
- `docs/governance/user-feedback-loop.md` reviewed: not applicable
- Feedback item IDs: none
- Feedback accepted: not applicable
- Feedback needs clarification: no
- Feedback conflicts: no
- Feedback deferred or rejected: none
- Active task changed by feedback: yes
- New task created from feedback: yes
- Design memory updated: no
- Learning journal updated: yes

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: route-shell smoke validation
- SLI: route smoke pass/fail
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: npm script output
- Smoke command or manual smoke:
  `Push-Location .\web; npm run smoke:routes; Pop-Location`
- Rollback or disable path: restore previous route smoke implementation

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: app-facing mock API contract path
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: yes
- Error state verified: diagnostic report on failure
- Refresh/restart behavior verified: not applicable
- Regression check performed: yes

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: synthetic app-facing smoke data only
- Trust boundaries: no auth/provider secrets, synthetic `/app/*` responses
- Permission or ownership checks: authenticated routes use synthetic `/app/me`
- Abuse cases: not applicable
- Secret handling: no secrets
- Security tests or scans: not applicable
- Fail-closed behavior: smoke failures report diagnostics and exit non-zero
- Residual risk: Chrome/CDP commands still require running browser smoke
  outside sandbox restrictions in this local desktop environment.

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: Repaired broad route-shell browser smoke by replacing the
  timing-prone Chrome dump-dom path with a CDP Runtime marker check and
  aligning the tools mock with the current app-facing API shape.
- Files changed:
  - `web/scripts/route-smoke.mjs`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.agents/state/current-focus.md`
  - `.agents/state/next-steps.md`
  - `.agents/state/system-health.md`
  - `.agents/state/regression-log.md`
  - `.codex/tasks/PRJ-821-repair-route-smoke-browser-rendering.md`
- How tested:
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `Push-Location .\web; npm run test:connector-confirmation-browser; Pop-Location`
  - `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
  - `Push-Location .\web; npm run test:connector-confirmation-render; Pop-Location`
  - `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
  - `Push-Location .\web; npm exec -- vite build; Pop-Location`
  - `git diff --check`
- What is incomplete: none for this route-smoke repair slice.
- Next steps: select the next small stability or architecture-alignment slice
  from fresh evidence.
- Decisions made: keep route smoke as a route marker gate, not a pixel or full
  interaction test.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: route smoke fails fast on Chrome dump-dom timeout.
- Gaps: broad route-shell browser smoke remains unavailable after focused
  connector confirmation browser proof was restored.
- Inconsistencies: system health marks route smoke as failing while a focused
  Chrome/CDP harness passes.
- Architecture constraints: web remains a thin client over synthetic app-facing
  contract data in route smoke.

### 2. Select One Priority Task
- Selected task: PRJ-821 repair route smoke browser rendering.
- Priority rationale: closes an active monitored stability gap before new
  feature work.
- Why other candidates were deferred: broader action-loop extensions would add
  capability while a route-shell gate is still red.

### 3. Plan Implementation
- Files or surfaces to modify: `web/scripts/route-smoke.mjs`, package docs/state.
- Logic: render routes through CDP runtime evaluation instead of Chrome
  `--dump-dom`.
- Edge cases: authenticated-route synthetic `/app/me` behavior, route marker
  diagnostics, Chrome profile cleanup.

### 4. Execute Implementation
- Implementation notes: Replaced `--dump-dom` with a CDP runtime path, added
  route-marker polling before diagnostics, and updated the `/tools` synthetic
  payload to include `skill_tool_bindings`.

### 5. Verify and Test
- Validation performed: route smoke, focused connector browser proof,
  connector source/render characterizations, web typecheck, Vite build, and
  whitespace check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: keep route smoke failing and rely on focused
  browser tests; rejected because route-shell smoke is a broader regression
  gate.
- Technical debt introduced: no
- Scalability assessment: contained harness repair only.
- Refinements made: route smoke now waits for the marker instead of sampling
  immediately after document load, preserving route-level diagnostics on
  failure.

### 7. Update Documentation and Knowledge
- Docs updated: task board, project state, learning journal, and agent state.
- Context updated: yes
- Learning journal updated: yes.
