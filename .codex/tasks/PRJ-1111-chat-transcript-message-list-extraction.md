# Task

## Header
- ID: PRJ-1111
- Title: Extract chat transcript message-list presentation
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1110
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1111
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1110` added a focused chat transcript render characterization. The
remaining transcript row map can now move behind a chat-owned message-list
component while `App()` keeps route-level refs, labels, timestamp formatting,
and markdown rendering as explicit callbacks.

## Goal
Move chat transcript row mapping out of `App.tsx` without changing transcript
behavior.

## Success Signal
- User or operator problem: `App.tsx` no longer owns transcript row list JSX.
- Expected product or reliability outcome: chat transcript rendering remains
  protected by the new characterization.
- How success will be observed: build, chat transcript characterization, route
  smoke, and diff check pass.
- Post-launch learning needed: no

## Scope
- Update `web/src/components/chat.tsx`.
- Update `web/src/App.tsx`.
- Update frontend docs, v1 roadmap, task board, and project state.

## Deliverable For This Stage
A verified `ChatTranscriptMessageList` extraction.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Add `ChatTranscriptMessageList` to `web/src/components/chat.tsx`.
2. Let the component own only the row map and `ChatTranscriptMessageRow`
   composition.
3. Pass route-owned delivery-state, delivery-label, timestamp, markdown, and
   ref registration behavior as explicit callbacks from `App()`.
4. Replace the inline `visibleTranscriptItems.map(...)` in `App.tsx`.
5. Run build, chat transcript characterization, route smoke, and diff check.

## Acceptance Criteria
- `App.tsx` no longer maps `visibleTranscriptItems` inline.
- `ChatTranscriptMessageList` preserves message row selectors and row
  composition.
- `App()` still owns delivery labels, timestamp formatting, markdown rendering,
  and ref registration.
- `npm run test:chat-transcript` passes.

## Definition of Done
- [x] Message-list extraction implemented.
- [x] Chat transcript characterization passes.
- [x] Route smoke passes.
- [x] Docs/context updated.

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
  - result: passed
  - `Push-Location .\web; npm run test:chat-transcript; Pop-Location`
  - result: passed with `status=ok`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: passed with `status=ok`, `route_count=14`
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 1,4`
  - result: remaining maps inspected after extraction
- Screenshots/logs: command output recorded in session.
- High-risk checks:
  - `git diff --check`
  - result: passed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
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
- Design source reference: current chat transcript implementation
- Canonical visual target: current chat transcript behavior
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable for presentation extraction
- Visual-direction brief reviewed: not applicable for presentation extraction
- Existing shared pattern reused: chat owner module extraction
- New shared pattern introduced: no
- Design-memory entry reused: frontend route/component map
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: not assessed
- State checks: preview, durable success, optimistic sending, delivered success
  through chat transcript characterization
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: route smoke only
- Input-mode checks: form submit through chat transcript characterization
- Accessibility checks: no role changes introduced
- Parity evidence: not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert `ChatTranscriptMessageList` usage if needed
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
The extraction also corrected the local transcript message ref type to
`HTMLDivElement`, matching the forwarded `ChatTranscriptMessageRow` element.

## Result Report

- Task summary:
  - extracted chat transcript message-list presentation to
    `ChatTranscriptMessageList`.
- Files changed:
  - `.codex/tasks/PRJ-1111-chat-transcript-message-list-extraction.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/src/App.tsx`
  - `web/src/components/chat.tsx`
- How tested:
  - `npm run build`
  - `npm run test:chat-transcript`
  - `npm run smoke:routes`
  - `git diff --check`
- What is incomplete:
  - bottom mobile tabbar ref map still lives in `App.tsx`.
- Next steps:
  - `PRJ-1112` audit mobile tabbar ref extraction readiness.
- Decisions made:
  - keep route-derived labels and render callbacks in `App()` for this slice.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - transcript row mapping was still inline in `App.tsx`.
- Gaps:
  - none after `PRJ-1110`; behavior characterization exists.
- Inconsistencies:
  - transcript row ref type in `App()` did not match the forwarded div element;
    corrected to `HTMLDivElement`.
- Architecture constraints:
  - route-derived labels, timestamp formatting, markdown rendering, and ref
    registration remain in `App()`.

### 2. Select One Priority Task
- Selected task:
  - `PRJ-1111` extract chat transcript message-list presentation.
- Priority rationale:
  - it is the next safe implementation after transcript characterization.
- Why other candidates were deferred:
  - mobile tabbar refs need a separate audit.
  - pure data projections are lower risk and lower impact.

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/src/components/chat.tsx`
  - `web/src/App.tsx`
  - docs/context/task files
- Logic:
  - move the map into a chat component and pass route-owned behavior as
    callbacks.
- Edge cases:
  - preview rows, delivered state, failed/sending labels, markdown, and ref
    registration.

### 4. Execute Implementation
- Implementation notes:
  - `ChatTranscriptMessageList` now composes `ChatTranscriptMessageRow` items.
  - `App()` passes callbacks for delivery state, delivery label, timestamp,
    markdown rendering, and ref registration.

### 5. Verify and Test
- Validation performed:
  - `npm run build`
  - `npm run test:chat-transcript`
  - `npm run smoke:routes`
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - move delivery-label logic into the component.
- Technical debt introduced: no
- Scalability assessment:
  - callback boundary keeps route behavior explicit while shrinking `App.tsx`.
- Refinements made:
  - corrected transcript message ref element type.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
