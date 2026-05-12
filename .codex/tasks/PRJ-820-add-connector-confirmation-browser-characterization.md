# Task

## Header
- ID: PRJ-820
- Title: Add connector confirmation browser characterization
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-819
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 820
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-819` added server-rendered component markup proof for app chat connector
confirmation states after local browser automation was blocked. Browser access
has now been recovered by keeping the local server outside command-process
cleanup, so the next source-of-truth task is to add repeatable browser-level
interaction evidence for the same app-facing confirmation flow.

## Goal
Add one focused real-browser characterization that proves the existing app chat
connector confirmation UI can receive a backend-projected pending confirmation,
submit the exact bounded payload to `/app/connectors/confirm`, remain
fail-closed on error with retry available, and clear the pending action on
successful confirmation.

## Success Signal
- User or operator problem: frontend confirmation controls currently have
  component-level proof but not repeatable browser interaction proof.
- Expected product or reliability outcome: the browser harness proves the
  app-facing confirmation journey without changing action/provider ownership.
- How success will be observed: a passing `npm run test:connector-confirmation-browser`
  report with pending, error retry, and success cases.
- Post-launch learning needed: no

## Deliverable For This Stage
One scoped web characterization script, one package script entry, and updated
project state evidence.

## Scope
- `web/scripts/connector-confirmation-browser-characterization.mjs`
- `web/package.json`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.agents/state/current-focus.md`
- `.agents/state/next-steps.md`
- `.agents/state/system-health.md`
- `.agents/state/regression-log.md`
- `.codex/context/LEARNING_JOURNAL.md`

## Implementation Plan
1. Reuse the existing frontend characterization harness style.
2. Serve `web/dist` with synthetic app-facing API data.
3. Launch headless Chrome with CDP and navigate to `/chat`.
4. Submit a chat message that returns a bounded pending confirmation payload.
5. Assert pending UI, request payload, fail-closed retry behavior, and success
   cleanup.
6. Add the npm script and run focused web validation.
7. Update context and state files with exact evidence.

## Acceptance Criteria
- The browser test proves the pending confirmation banner is visible after
  `POST /app/chat/message`.
- The browser test proves the confirm request body matches the server-projected
  pending payload.
- The browser test proves a failed confirm leaves the pending action visible
  and retryable.
- The browser test proves a successful confirm clears the pending action and
  shows success feedback.
- No product runtime, backend provider, auth, DB, secret, or deployment behavior
  changes.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] `npm run test:connector-confirmation-browser` passes.
- [x] Existing connector confirmation characterization tests still pass.
- [x] Web typecheck and build pass.
- [x] Context/state files record the browser evidence and residual risk.

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
  - `Push-Location .\web; npm run build; Pop-Location` -> passed
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
- Manual checks: Browser recovery confirmed separately before this task; the
  repeatable script now covers the interaction path.
- Screenshots/logs: browser characterization report shows pending, error, and
  success states with two confirmation requests.
- High-risk checks: action/provider side-effect boundary remains unchanged.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/16_agent_contracts.md`,
  `docs/architecture/29_runtime_behavior_testing.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: existing app chat confirmation controls from PRJ-816..819
- Canonical visual target: existing chat composer shell
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: no
- Visual-direction brief reviewed: no
- Existing shared pattern reused: existing app chat composer and characterization harness
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: not required for this interaction harness
- Remaining mismatches: broader `smoke:routes` Chrome DOM-dump harness remains
  a separate monitored issue from PRJ-818
- State checks: loading | empty | error | success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: desktop
- Input-mode checks: keyboard | pointer
- Accessibility checks: aria-live pending confirmation region asserted indirectly
- Parity evidence: browser harness verifies the existing chat composer state
  transitions structurally, not pixel-perfect visual parity.

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: remove the characterization script and npm entry
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
The task adds evidence only. It must not widen confirmation authority or create
new provider mutation behavior.

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
- User or operator affected: app operators validating connector confirmation UX
- Existing workaround or pain: component-only render proof without browser interaction
- Smallest useful slice: one browser-level confirmation characterization
- Success metric or signal: focused npm script passes
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
- Learning journal updated: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: connector confirmation in app chat
- SLI: focused browser characterization pass/fail
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: npm script output
- Smoke command or manual smoke:
  `Push-Location .\web; npm run test:connector-confirmation-browser; Pop-Location`
- Rollback or disable path: remove browser characterization script and package entry

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: app-facing mock API contract path
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: yes
- Refresh/restart behavior verified: not applicable
- Regression check performed: yes

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: synthetic app-facing test data only
- Trust boundaries: confirmation remains backend/action-owned; UI submits server-projected payload
- Permission or ownership checks: request-body equality assertion passed for
  both confirm attempts
- Abuse cases: fail-closed confirmation error retains pending retry
- Secret handling: no secrets
- Security tests or scans: not applicable
- Fail-closed behavior: first confirm returns `confirmation_stale`, leaves the
  pending candidate visible, and keeps retry enabled
- Residual risk: browser script uses synthetic provider responses

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: Added a repeatable real-Chrome browser characterization for
  the app chat connector confirmation flow.
- Files changed:
  - `web/scripts/connector-confirmation-browser-characterization.mjs`
  - `web/package.json`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.agents/state/current-focus.md`
  - `.agents/state/next-steps.md`
  - `.agents/state/system-health.md`
  - `.agents/state/regression-log.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.codex/tasks/PRJ-820-add-connector-confirmation-browser-characterization.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run test:connector-confirmation-browser; Pop-Location`
  - `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
  - `Push-Location .\web; npm run test:connector-confirmation-render; Pop-Location`
  - `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
  - `Push-Location .\web; npm exec -- vite build; Pop-Location`
  - `git diff --check`
- What is incomplete: broad route smoke still has the pre-existing Chrome
  DOM-dump timeout from PRJ-818.
- Next steps: choose the next small stability or architecture-alignment slice
  from fresh evidence.
- Decisions made: keep this as evidence-only QA; do not widen provider
  authority, backend replay behavior, or UI scope.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: browser access was recovered after prior local process-launch blockers.
- Gaps: confirmation controls still need repeatable browser interaction proof.
- Inconsistencies: task board still names browser proof as the next smallest task.
- Architecture constraints: action remains the only side-effect owner.

### 2. Select One Priority Task
- Selected task: PRJ-820 browser characterization for connector confirmation.
- Priority rationale: reduces regression risk before adding any new action-loop work.
- Why other candidates were deferred: broader feature work would build on a flow
  whose browser interaction evidence was still incomplete.

### 3. Plan Implementation
- Files or surfaces to modify: one web script, package script, context/state docs.
- Logic: mocked app-facing API returns pending confirmation, fail-closed confirm,
  then success confirm.
- Edge cases: stale/error confirm must preserve pending confirmation and retry.

### 4. Execute Implementation
- Implementation notes: Added `connector-confirmation-browser-characterization`
  using the existing local static server, synthetic app-facing API responses,
  and Chrome CDP harness style. The script avoids `Page.enable`, which was the
  known flaky CDP command in the local environment, and validates UI behavior
  through `Runtime.evaluate`.

### 5. Verify and Test
- Validation performed: focused browser characterization, existing
  connector-confirmation source and render characterizations, web typecheck,
  Vite build, and whitespace check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: manual screenshot only; rejected because repeatable
  browser interaction proof is more useful and matches existing harness style.
- Technical debt introduced: no
- Scalability assessment: isolated test script only; no runtime path expansion.
- Refinements made: made text assertions case-insensitive where browser
  `innerText` reflects CSS-transformed uppercase labels, and added Chrome
  process/profile cleanup hardening.

### 7. Update Documentation and Knowledge
- Docs updated: task board, project state, and agent state files.
- Context updated: yes
- Learning journal updated: yes.
