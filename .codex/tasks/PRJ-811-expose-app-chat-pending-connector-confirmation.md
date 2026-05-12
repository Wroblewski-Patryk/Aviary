# Task

## Header
- ID: PRJ-811
- Title: Expose app chat pending connector confirmation
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-810
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 811
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-810 froze the confirmation handoff contract. The app chat endpoint still
returned only reply/runtime data, so the first-party shell could not see that a
connector mutation stopped safely at `confirmation_required`.

## Goal
Expose a bounded `pending_confirmation` object from `/app/chat/message` when
action stops on a confirmation-required connector mutation, and render it in
the chat composer without adding mutation execution.

## Success Signal
- User or operator problem: the product shell can distinguish a safe
  confirmation stop from a generic reply.
- Expected product or reliability outcome: future confirmation UX can build on
  a bounded app-facing contract without reading debug payloads.
- How success will be observed: API test proves bounded response shape; web
  build proves the client type and banner compile.
- Post-launch learning needed: no

## Deliverable For This Stage
A narrow backend response shape, frontend type/state, and read-only chat banner.

## Scope
- `backend/app/api/schemas.py`
- `backend/app/api/routes.py`
- `backend/tests/test_api_routes.py`
- `web/src/lib/api.ts`
- `web/src/components/chat.tsx`
- `web/src/App.tsx`
- `web/src/index.css`
- docs/context/state files for this task

## Implementation Plan
1. Add a bounded pending-confirmation response schema.
2. Build the pending-confirmation payload from action observations and matching
   connector permission gates only for app chat.
3. Add API regression coverage that confirms debug/system-debug stay hidden.
4. Add frontend response typing and a read-only composer banner.
5. Run focused backend and frontend validation.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not execute provider mutation or add a confirmation endpoint in this slice

## Acceptance Criteria
- [x] `/app/chat/message` may return `pending_confirmation` only when action
  produced a `confirmation_required` observation and a matching not-yet-allowed
  confirmation gate exists.
- [x] The response includes source event, trace, connector kind, provider,
  operation, mode, bounded candidate summary, source reference, and reason.
- [x] Public app chat response does not expose debug or system-debug payloads.
- [x] Web client types and chat UI can render the read-only blocked state.

## Definition of Done
- [x] Backend test proves the response shape.
- [x] Frontend build path succeeds through Vite.
- [x] Context and task state are updated.

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
- mutation confirmation endpoint or provider mutation execution

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "app_chat_message"; Pop-Location`
    -> `3 passed, 121 deselected`
- Manual checks:
  - `Push-Location .\web; npm exec -- tsc -b; Pop-Location` surfaced
    pre-existing unrelated TypeScript errors in `App.tsx`, `components/tools.tsx`,
    `lib/tool-formatting.ts`, and `tailwind.config.ts`
  - `Push-Location .\web; npm exec -- vite build; Pop-Location` -> passed
  - Browser plugin attempted `http://127.0.0.1:5173/chat` and
    `http://localhost:5173/chat`, but the in-app browser reported
    `net::ERR_BLOCKED_BY_CLIENT`
  - `git diff --check` passed with LF/CRLF warnings only
- Screenshots/logs: rendered screenshot unavailable because Browser navigation
  was blocked by the local in-app browser.
- High-risk checks: no provider mutation or confirmation endpoint added.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/planning/skill-guided-bounded-action-loop-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: completed in this task.

## UX/UI Evidence
- Design source type: stitch_exception
- Design source reference: existing chat composer pattern
- Canonical visual target: current chat composer
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: chat composer alert-like surface
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: limited by Browser navigation blocker
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: rendered pending state not visually verified
- State checks: success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: not completed due Browser blocker
- Input-mode checks: not completed due Browser blocker
- Accessibility checks: banner uses `aria-live="polite"`
- Parity evidence: not applicable

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not required
- Rollback note: revert PRJ-811 app response/client edits.
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

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: app chat message with confirmation-gated connector
  mutation request.
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: unchanged
- Logs, dashboard, or alert route: unchanged
- Smoke command or manual smoke: focused API test and frontend build checks
- Rollback or disable path: remove optional response field and banner

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: focused API test

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: bounded connector operation metadata and candidate
  summary.
- Trust boundaries: authenticated app session, action result, connector
  permission gate.
- Permission or ownership checks: response is emitted only for the current
  runtime result in authenticated app chat.
- Abuse cases: debug payload leakage and mutation execution were checked.
- Secret handling: no changes.
- Security tests or scans: focused API regression.
- Fail-closed behavior: missing observation or gate returns no
  `pending_confirmation`.
- Residual risk: future confirmation execution endpoint still needs its own
  replay/freshness/user-scope checks.

## Result Report
- Task summary: Added bounded pending connector confirmation to app chat.
- Files changed: backend API schema/route/test, frontend API type/chat banner,
  docs/context/state, and learning journal.
- How tested: focused API test, Vite build, Browser attempt, diff hygiene.
- What is incomplete: no confirmation execution endpoint; Browser rendered
  check blocked by `ERR_BLOCKED_BY_CLIENT`.
- Next steps: implement a dedicated confirmation submission path only as a
  separate selected slice.
- Decisions made: pending confirmation is read-only UI state, not
  authorization.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: app chat hid confirmation-required connector stops from the product
  shell.
- Gaps: no bounded app-facing response shape existed.
- Inconsistencies: none; this extends the PRJ-810 contract.
- Architecture constraints: action owns side effects; permission gates own
  authorization.

### 2. Select One Priority Task
- Selected task: PRJ-811.
- Priority rationale: expose the safe stop before implementing any mutation
  confirmation endpoint.
- Why other candidates were deferred: actual confirmation execution carries
  higher replay and authorization risk.

### 3. Plan Implementation
- Files or surfaces to modify: app chat API, app chat client types, chat UI,
  focused tests.
- Logic: derive bounded pending confirmation only from an action observation
  plus matching not-yet-allowed permission gate.
- Edge cases: missing gate, missing observation, debug leakage, raw payloads.

### 4. Execute Implementation
- Implementation notes: added optional public response field and read-only
  composer banner.

### 5. Verify and Test
- Validation performed: focused API test, Vite build, Browser attempt,
  `git diff --check`.
- Result: pass, with Browser rendered check blocked by local browser policy.

### 6. Self-Review
- Simpler option considered: expose action observations directly.
- Technical debt introduced: no
- Scalability assessment: same response shape can support later connectors.
- Refinements made: kept debug/system-debug out of app chat.

### 7. Update Documentation and Knowledge
- Docs updated: yes.
- Context updated: yes.
- Learning journal updated: yes.
