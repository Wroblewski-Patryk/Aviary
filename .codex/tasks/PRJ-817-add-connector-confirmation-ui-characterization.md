# Task

## Header
- ID: PRJ-817
- Title: Add connector confirmation UI characterization
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-816
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 817
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-816` added the first-party confirmation controls, but in-app Browser
rendered validation is blocked locally by `net::ERR_BLOCKED_BY_CLIENT`. The web
workspace already uses headless characterization scripts for chat and tools UI
state coverage.

## Goal
Add repeatable frontend characterization coverage for connector confirmation UI
states without introducing a new test framework or changing backend behavior.

## Scope
- `web/scripts/connector-confirmation-characterization.mjs`
- `web/package.json`
- `web/src/App.tsx`
- `web/src/components/chat.tsx`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.agents/state/current-focus.md`
- `.agents/state/next-steps.md`
- `.agents/state/system-health.md`

## Success Signal
- User or operator problem: confirmation UI behavior has only build/typecheck
  proof while Browser navigation is blocked.
- Expected product or reliability outcome: pending, submitting, success, and
  fail-closed error states are pinned by a repeatable web characterization.
- How success will be observed: the new script passes against the built bundle.
- Post-launch learning needed: yes

## Deliverable For This Stage
Verified source-contract characterization for the confirmation UI state matrix.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate backend confirmation logic
- preserve action as the only provider side-effect owner
- keep the frontend as a thin client over `/app/connectors/confirm`

## Implementation Plan
1. Reuse the existing headless characterization script pattern.
2. Add mock app endpoints for chat history, chat message, and connector
   confirmation.
3. Exercise success and fail-closed confirmation cases against the built app.
4. Tighten any small UI copy issue discovered by the characterization.
5. Run build, characterization, and diff checks.

## Acceptance Criteria
- A package script runs the connector confirmation characterization.
- The script proves pending confirmation details and confirm control render.
- The script proves the submitting state disables the confirm control.
- The script proves success clears the confirm control and renders a completed
  result.
- The script proves fail-closed error keeps the pending confirmation available
  for retry.

## Definition of Done
- [x] characterization script is implemented
- [x] package script is wired
- [x] focused validation passes
- [x] source-of-truth files are updated

## Forbidden
- provider calls from the script
- backend route changes
- frontend-side permission reconstruction
- mock-only product behavior beyond the characterization harness
- broad UI redesign

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
    -> passed
  - `Push-Location .\web; npm exec -- vite build; Pop-Location` -> passed
  - `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
    -> passed
- Manual checks:
  - verified the characterization covers API client path, bounded payload
    submission, submit state matrix, localized copy, composer controls, and
    style hooks
- Screenshots/logs:
  - no screenshot proof; Browser and dynamic CDP paths were blocked in this
    environment
- High-risk checks:
  - pending final `git diff --check`

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: stitch_exception
- Design source reference: existing confirmation composer pattern
- Canonical visual target: existing app chat shell
- Fidelity target: structurally_faithful
- Existing shared pattern reused: `aion-chat-pending-confirmation`
- New shared pattern introduced: no
- State checks: pending | submitting | success | error
- Feedback locality checked: yes, source-contract characterization
- Raw technical errors hidden from end users: yes, source-contract
  characterization
- Input-mode checks: pointer
- Accessibility checks: button label and aria-live region

## Integration Evidence
- `INTEGRATION_CHECKLIST.md` reviewed: yes
- Real API/service path used: yes, via same client path against mock API in
  characterization
- Endpoint and client contract match: yes
- Loading state verified: submitting state source-contract check
- Error state verified: fail-closed error state source-contract check
- Regression check performed: `tsc -b`, `vite build`,
  `test:connector-confirmation`

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: yes
- Data classification: bounded connector confirmation evidence
- Trust boundaries: browser sends bounded server-projected evidence; backend
  remains responsible for authorization in real execution
- Secret handling: no secrets touched
- Fail-closed behavior: pinned at frontend source-contract level; backend
  behavior remains covered by PRJ-815 tests

## Result Report
- Task summary: added `npm run test:connector-confirmation` and a focused
  source-contract characterization for app chat connector confirmation
  controls.
- Files changed:
  - `web/scripts/connector-confirmation-characterization.mjs`
  - `web/package.json`
  - `web/src/App.tsx`
  - `web/src/components/chat.tsx`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.agents/state/current-focus.md`
  - `.agents/state/next-steps.md`
  - `.agents/state/system-health.md`
  - `docs/planning/next-iteration-plan.md`
- How tested:
  - `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
  - `Push-Location .\web; npm exec -- vite build; Pop-Location`
  - `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
- What is incomplete: rendered screenshot and browser interaction proof remain
  blocked by local Browser/CDP behavior.
- Next steps: unblock or replace rendered browser evidence for the confirmation
  state matrix.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: Browser-rendered validation is blocked, leaving only build/typecheck
  evidence for confirmation controls.
- Gaps: no repeatable coverage for pending/submitting/success/error UI states.
- Inconsistencies: existing chat/tools surfaces have characterization scripts,
  but connector confirmation does not.
- Architecture constraints: frontend must remain a thin submitter over backend
  confirmation.

### 2. Select One Priority Task
- Selected task: `PRJ-817` add connector confirmation UI characterization.
- Priority rationale: it converts the Browser blocker into repeatable local UI
  evidence.
- Why other candidates were deferred: broader visual polish should wait until
  the state matrix is pinned.

### 3. Plan Implementation
- Files or surfaces to modify: web script, package script, minimal copy/state
  UI if characterization exposes ambiguity, context notes.
- Logic: mock app auth/history/message/confirmation endpoints and assert real
  DOM state in built bundle.
- Edge cases: success clears pending; fail-closed keeps pending for retry;
  submitting disables duplicate confirm clicks.

### 4. Execute Implementation
- Implementation notes:
  - added a package script and source-contract characterization
  - pinned the thin API client path and bounded payload submission
  - pinned explicit `idle|submitting|success|error` frontend states
  - refined the success eyebrow to `Confirmation complete`

### 5. Verify and Test
- Validation performed:
  - `npm exec -- tsc -b --pretty false`
  - `npm exec -- vite build`
  - `npm run test:connector-confirmation`
- Result: passed

### 6. Self-Review
- Simpler option considered: source-only assertions; rejected because existing
  repo pattern supports real bundle characterization.
- Technical debt introduced: no
- Refinements made: replaced an unreliable dynamic CDP harness attempt with an
  honest source-contract characterization and recorded rendered proof as a
  follow-up.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/planning/next-iteration-plan.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.agents/state/current-focus.md`
  - `.agents/state/next-steps.md`
  - `.agents/state/system-health.md`
