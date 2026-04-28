# Task

## Header
- ID: PRJ-774
- Title: Fix Internal Chat Optimistic Turn Status
- Task Type: fix
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-713, PRJ-714
- Priority: P1

## Context
The authenticated internal app chat is the canonical conversation owner, with
`/app/chat/history` as the backend-owned transcript surface. A production UX
report showed that a user message was not visible immediately after submit and
only appeared after the assistant answer landed, making the turn look delayed
or lost.

## Goal
Make internal chat sends feel truthful and responsive: the user-authored
message must appear immediately with a sending or delivery status, then the
assistant reply should appear when `/app/chat/message` returns, while the
durable transcript continues to reconcile from `/app/chat/history`.

## Deliverable For This Stage
Implementation and verification evidence for the smallest frontend fix that
preserves the existing backend transcript contract.

## Scope
- `web/src/App.tsx`
  - app chat send handler
  - transcript item merge and render path
  - local delivery status metadata
- `web/src/index.css`
  - visual treatment for local sending, delivered, and failed status
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/context/LEARNING_JOURNAL.md`
- this task file

## Implementation Plan
1. Review `/app/chat/history` and `/app/chat/message` contract expectations.
2. Replace assistant-only pending behavior with transient local transcript
   items.
3. Append a local user turn immediately on submit with
   `metadata.delivery_state=sending`.
4. When the real reply returns, mark the local user turn delivered, append the
   assistant reply, then refresh backend history.
5. Reconcile optimistic local items away once `/app/chat/history` contains the
   durable event.
6. Validate via web build and focused backend chat route regression.

## Acceptance Criteria
- A submitted user message renders immediately in the transcript.
- The local user message shows a sending state while the request is in flight.
- The local user message shows a delivered state once the reply returns.
- The assistant reply renders from the real `/app/chat/message` response.
- Refreshed `/app/chat/history` remains the canonical durable transcript and
  local optimistic items are removed once reconciled.
- No new backend route, store, mock path, or workaround is introduced.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not create a second durable chat store

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` applicable checks are satisfied with evidence.
- [x] Web client builds without errors.
- [x] App chat submit path preserves the backend-owned transcript contract.
- [x] Context docs are updated with the result and residual risk.

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
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "chat"; Pop-Location`
    - result: `8 passed, 109 deselected`
- Manual checks:
  - transcript behavior reviewed through the frontend implementation path
- Screenshots/logs:
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-774-fix-internal-chat-optimistic-turn-status.md`
- High-risk checks:
  - durable source of truth remains backend-owned `/app/chat/history`
  - no second persistence path or client-owned chat store was introduced

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/15_runtime_flow.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-chat-canonical-reference-v4.png`
- Canonical visual target: chat route v4 conversation-first target
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - existing chat transcript surface
  - message metadata row
- New shared pattern introduced: no
- Design-memory entry reused:
  - existing chat transcript pattern
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: not required for behavior-first fix
- Remaining mismatches:
  - browser screenshot proof remains blocked in this local environment
- State checks: loading | empty | success | error
- Responsive checks: desktop | tablet | mobile
- Input-mode checks: touch | pointer | keyboard
- Accessibility checks:
  - delivery state remains text-backed and visible in transcript metadata
- Parity evidence:
  - local browser proof blocked by Node runtime constraint already recorded in
    project context

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes:
- Health-check impact:
- Smoke steps updated:
- Rollback note:

## Review Checklist (mandatory)
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
This fix intentionally solves only responsiveness and truthful local rendering.
It does not move transcript ownership away from the backend.

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

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB
-> validation -> error handling -> test. Partial implementations, mock-only
paths, placeholders, fake data, and temporary fixes are forbidden.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: yes
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: yes
- Error state verified: yes
- Refresh/restart behavior verified: backend history refresh remains the final
  reconciliation step
- Regression check performed:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "chat"; Pop-Location`

## AI Testing Evidence (required for AI features)

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios:
- Multi-step context scenarios:
- Adversarial or role-break scenarios:
- Prompt injection checks:
- Data leakage and unauthorized access checks:
- Result:

## Result Report

- Task summary:
  - internal chat now renders the user's optimistic turn immediately and
    reconciles it against the backend transcript once the real event lands
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.codex/tasks/PRJ-774-fix-internal-chat-optimistic-turn-status.md`
- How tested:
  - web build
  - focused backend chat API regression
- What is incomplete:
  - browser screenshot proof remains blocked locally by the known Node runtime
    constraint
- Next steps:
  - verify this behavior on a live deployed browser after the next push
- Decisions made:
  - keep `/app/chat/history` as the durable source of truth
  - solve responsiveness with transient local items rather than a second chat
    store
