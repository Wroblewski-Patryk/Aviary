# Task

## Header
- ID: PRJ-776
- Title: Implement public home and authenticated shell frame pass
- Task Type: design
- Current Stage: implementation
- Status: IN_PROGRESS
- Owner: Frontend Builder
- Depends on: PRJ-775
- Priority: P1

## Context
`PRJ-775` froze the master audit for the biggest remaining flagship drift:
the parent authenticated shell still reads app-first, and the unauthenticated
surface still reads auth-first instead of landing-first. This task executes the
first structural slice before the dashboard-specific convergence pass.

## Goal
Rebuild the unauthenticated entry into a canonical landing-first composition
and wrap authenticated routes in a stronger flagship frame so later dashboard
work lands inside the correct parent layout.

## Deliverable For This Stage
One working frontend slice in `web/src/App.tsx` and `web/src/index.css` that:
- converts the `!me` branch into a public landing layout with integrated auth
- introduces a reusable flagship `WindowChrome` frame around the authenticated shell
- preserves existing route contracts and authentication logic

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/ux/design-memory.md`
- `.codex/tasks/PRJ-776-implement-public-home-and-authenticated-shell-frame-pass.md`

## Implementation Plan
1. Replace the old auth-first public branch with a landing-first composition:
   nav, hero, embodied trust stage, feature strip, integrated auth module, and
   trust band.
2. Reuse existing shell primitives where possible and introduce only one new
   shared primitive: `WindowChrome`.
3. Wrap authenticated routes in the new flagship frame without changing route
   contracts, chat logic, settings logic, or dashboard data flow.
4. Add responsive CSS for the new public shell and shared chrome.
5. Run focused validation and record remaining parity gaps for the next loop.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Acceptance Criteria
- unauthenticated entry is landing-first rather than form-first
- auth mechanics still work through the existing submit handlers
- authenticated routes render inside a premium framed shell
- no route contracts, API calls, or state ownership rules change

## Definition of Done
- [ ] Public home is structurally rebuilt around the canonical landing composition.
- [ ] Authenticated shell has a reusable frame pass that can host dashboard, chat, and personality.
- [ ] Focused validation for the touched frontend scope is attached.

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
  - `git diff --check -- web/src/App.tsx web/src/index.css`
- Manual checks:
  - structural review of `!me` branch and authenticated shell wrapper
- Screenshots/logs:
  - browser screenshot parity still pending in the next loop
- High-risk checks:
  - auth submit handlers and route change wiring remain untouched

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/27_codex_instructions.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference:
  - `docs/ux/assets/aion-landing-canonical-reference-v1.png`
- Canonical visual target:
  - landing-first public shell and flagship framed parent layout
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - embodied cognition motif
  - flagship utility bar
- New shared pattern introduced: yes
- Design-memory entry reused:
  - flagship utility bar
- Design-memory update required: yes
- Visual gap audit completed: yes
- Background or decorative asset strategy:
  - keep raster-first decorative fidelity where canonical framing depends on atmosphere
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches:
  - dashboard still needs its dedicated structural convergence pass
  - screenshot parity for public home and parent layout still needs a browser loop
- State checks: loading | error | success
- Responsive checks: desktop | mobile
- Input-mode checks: pointer | touch
- Accessibility checks:
  - semantic sections preserved
  - buttons remain keyboard-focusable
- Parity evidence:
  - structure now matches the audit target more closely, but canonical screenshot proof remains pending

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note:
  - revert the frontend slice commit if the new shell framing causes regression

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
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
- This task intentionally stops before the dashboard-specific structural pass.
- Browser screenshot parity remains a follow-up because this slice establishes
  the parent layout and public home contract first.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY` or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB -> validation -> error handling -> test. Partial implementations, mock-only paths, placeholders, fake data, and temporary fixes are forbidden.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: yes
- Error state verified: yes
- Refresh/restart behavior verified: yes
- Regression check performed:
  - auth state branches still route to the existing handlers and `/dashboard`

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
  - public home is now a landing-first flagship surface and the authenticated shell is framed by a reusable `WindowChrome`
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `docs/ux/design-memory.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-776-implement-public-home-and-authenticated-shell-frame-pass.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx web/src/index.css`
- What is incomplete:
  - dashboard canonical convergence and browser screenshot parity
- Next steps:
  - structural dashboard pass on top of the new framed parent layout
- Decisions made:
  - reuse existing auth and route logic; change only the public composition and shell framing
