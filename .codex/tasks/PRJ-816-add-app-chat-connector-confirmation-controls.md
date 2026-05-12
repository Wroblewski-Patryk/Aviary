# Task

## Header
- ID: PRJ-816
- Title: Add app chat connector confirmation controls
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-815
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 816
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-815` completed the backend confirmation execution path. The web chat
currently renders pending connector confirmation evidence as a read-only blocked
banner, so the first-party app cannot yet submit the bounded confirmation
payload to the approved `/app/connectors/confirm` endpoint.

## Goal
Let an authenticated app user confirm a pending connector mutation from the chat
composer while preserving the backend-owned action boundary and fail-closed
confirmation contract.

## Scope
- `web/src/lib/api.ts`
- `web/src/App.tsx`
- `web/src/components/chat.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.agents/state/current-focus.md`
- `.agents/state/next-steps.md`
- `.agents/state/system-health.md`

## Success Signal
- User or operator problem: pending connector actions are visible but cannot be
  confirmed from the app.
- Expected product or reliability outcome: the app submits the existing bounded
  pending-confirmation payload and renders executed or fail-closed outcomes.
- How success will be observed: focused web typecheck and build pass, and the
  source reflects loading, success, and error states.
- Post-launch learning needed: yes

## Deliverable For This Stage
Verified implementation of the smallest app UI slice for connector confirmation
submission.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- preserve action as the only provider side-effect owner
- submit only the backend-provided pending confirmation payload

## Implementation Plan
1. Add typed client support for `/app/connectors/confirm`.
2. Add app-level pending-confirmation submit state, success text, and error text.
3. Extend `ChatComposerShell` with a confirm button and accessible busy/error
   states.
4. Style the controls using the existing composer banner pattern.
5. Run focused frontend validation and update source-of-truth notes.

## Acceptance Criteria
- The pending confirmation banner has a confirm action when a payload exists.
- The confirm action disables while submitting and calls
  `/app/connectors/confirm` with the existing pending payload.
- A successful execution clears the pending confirmation and renders bounded
  result feedback.
- Fail-closed API errors are shown locally without clearing the pending
  confirmation.
- No provider-specific or action-execution logic is introduced in the frontend.

## Definition of Done
- [x] UI, client API, state, and error handling are implemented.
- [x] Relevant frontend validation has been run.
- [x] Source-of-truth files are updated with result and evidence.

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
- free-form chat text as confirmation authority
- provider mutation calls from the UI

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
    -> passed
  - `Push-Location .\web; npm exec -- vite build; Pop-Location` -> passed
- Manual checks:
  - source review confirmed the frontend submits only the existing
    `pendingConfirmation` payload to `api.confirmConnectorAction`
  - source review confirmed success clears pending payload and error keeps it
    available for retry
- Screenshots/logs:
  - Browser rendered check attempted at `http://127.0.0.1:5173/chat`; the
    in-app browser blocked the local URL with `net::ERR_BLOCKED_BY_CLIENT`
- High-risk checks:
  - `git diff --check` -> passed with LF/CRLF warnings only
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence
- Design source type: stitch_exception
- Design source reference: existing chat composer pending-confirmation banner
- Canonical visual target: existing app chat shell
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: no
- Visual-direction brief reviewed: no
- Existing shared pattern reused: `aion-chat-pending-confirmation`
- New shared pattern introduced: no
- Design-memory entry reused: existing composer controls
- Design-memory update required: no
- Visual gap audit completed: source-level only; rendered Browser access was
  blocked
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no, local Browser navigation blocked
- Remaining mismatches: rendered state matrix still needs browser proof
- State checks: error | success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: source-level only unless Browser validation succeeds
- Input-mode checks: pointer | keyboard
- Accessibility checks: button label and aria-live region
- Parity evidence: not applicable

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert frontend client/composer changes to return to read-only
  pending-confirmation banner
- Observability or alerting impact: none
- Staged rollout or feature flag: no

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

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: authenticated app user confirming connector action
- Existing workaround or pain: no first-party confirm control
- Smallest useful slice: composer button plus endpoint client call
- Success metric or signal: pending confirmation can reach backend confirmation
  route from app UI
- Feature flag, staged rollout, or disable path: no
- Post-launch feedback or metric check: yes

## Integration Evidence
- `INTEGRATION_CHECKLIST.md` reviewed: yes
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: source-level and typecheck
- Error state verified: source-level and typecheck
- Refresh/restart behavior verified: build-level only
- Regression check performed: `tsc -b`, `vite build`, `git diff --check`

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: yes
- Data classification: bounded connector confirmation evidence
- Trust boundaries: browser submits only server-projected evidence; backend
  authenticates and rechecks user, freshness, source event, and drift
- Permission or ownership checks: backend-owned
- Abuse cases: stale or drifted confirmation remains fail-closed by API
- Secret handling: no secrets touched
- Security tests or scans: inherited from PRJ-815 backend tests
- Fail-closed behavior: API error remains visible without clearing pending
  confirmation
- Residual risk: rendered browser validation may be limited by local Browser
  plugin blocking localhost

## AI Testing Evidence
- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: backend-covered in PRJ-815
- Result: not applicable

## Result Report
- Task summary: added app chat controls for submitting bounded pending
  connector confirmations to `/app/connectors/confirm`.
- Files changed:
  - `web/src/lib/api.ts`
  - `web/src/App.tsx`
  - `web/src/components/chat.tsx`
  - `web/src/index.css`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.agents/state/current-focus.md`
  - `.agents/state/next-steps.md`
  - `.agents/state/system-health.md`
  - `docs/planning/next-iteration-plan.md`
- How tested:
  - `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
  - `Push-Location .\web; npm exec -- vite build; Pop-Location`
  - Browser attempted at `http://127.0.0.1:5173/chat` but local navigation was
    blocked by `net::ERR_BLOCKED_BY_CLIENT`
  - `git diff --check`
- What is incomplete: rendered screenshot and interaction proof are still
  blocked by local Browser access.
- Next steps: add broader rendered UX/a11y state-matrix evidence when Browser
  can reach local Vite.
- Decisions made: keep the frontend as a thin submitter over the backend
  confirmation endpoint; do not mirror action replay or provider logic in UI.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: UI lacks a confirmation submit control.
- Gaps: frontend API type and composer states are missing.
- Inconsistencies: backend execution exists but the app remains read-only.
- Architecture constraints: frontend must not authorize or execute provider
  mutations itself.

### 2. Select One Priority Task
- Selected task: `PRJ-816` add app chat connector confirmation controls.
- Priority rationale: it closes the first-party app handoff after backend replay.
- Why other candidates were deferred: broader UX/a11y state matrix can follow
  after the core endpoint path exists.

### 3. Plan Implementation
- Files or surfaces to modify: API client, app state, chat composer, composer
  styles, source-of-truth notes.
- Logic: submit current pending payload, show busy/success/error, clear pending
  only after executed response.
- Edge cases: no pending payload, double submit, fail-closed API error, stale
  confirmation.

### 4. Execute Implementation
- Implementation notes:
  - added `AppConnectorConfirmationResponse` and `api.confirmConnectorAction`
  - added app-level confirmation submit state and local feedback
  - extended the existing pending-confirmation composer banner with a confirm
    button, submitting state, success feedback, and error feedback
  - added mobile-safe layout styles for the confirmation action stack

### 5. Verify and Test
- Validation performed:
  - `npm exec -- tsc -b --pretty false`
  - `npm exec -- vite build`
  - Browser navigation attempt to local Vite
  - `git diff --check`
- Result: automated checks passed; Browser rendered validation blocked by
  `net::ERR_BLOCKED_BY_CLIENT`.

### 6. Self-Review
- Simpler option considered: keep banner read-only; rejected because backend
  handoff is now implemented and the selected task is app submission.
- Technical debt introduced: no
- Scalability assessment: state remains local to the chat composer and can be
  promoted later only if another surface needs the same control.
- Refinements made: success feedback remains visible after clearing the pending
  payload, and fail-closed errors keep the pending payload available for retry.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/planning/next-iteration-plan.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.agents/state/current-focus.md`
  - `.agents/state/next-steps.md`
  - `.agents/state/system-health.md`
- Learning journal updated: not applicable.
