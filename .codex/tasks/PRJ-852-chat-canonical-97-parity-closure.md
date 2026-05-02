# Task

## Header
- ID: PRJ-852
- Title: Chat Canonical 97 Percent Parity Closure
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-811, PRJ-815, PRJ-816, PRJ-817
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 852
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The web client has an approved canonical chat reference at
`docs/ux/assets/aion-chat-canonical-reference-v4.png`. Previous parity work
improved the authenticated shell and chat surface, but the latest recorded
chat screenshots still show meaningful drift from the canonical composition:
route-scale headline treatment, topbar density, transcript width, portrait
stage placement, right context hierarchy, and bottom composer integration.

## Goal
Bring the web app `/chat` module to at least 97% visual and structural
convergence with the canonical chat view while preserving the existing backend
chat-history contract and shared authenticated shell.

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- task evidence under `.codex/artifacts/prj852-chat-canonical-parity/`

## Success Signal
- User or operator problem: the chat module must visually converge with the
  canonical premium conversation workspace rather than merely sharing its mood.
- Expected product or reliability outcome: the user sees a transcript-first
  chat view with the canonical left shell, compact conversation topbar, central
  embodied stage, right cognitive context, and integrated composer.
- How success will be observed: local screenshots at desktop, tablet, and
  mobile compare against the canonical reference with no blocking visual drift.
- Post-launch learning needed: no

## Deliverable For This Stage
Implement and verify the chat view parity slice, then record evidence and
context updates.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- preserve backend-owned chat history and local optimistic reconciliation
- preserve the authenticated shell and route navigation contracts

## Implementation Plan
1. Review canonical chat reference and existing chat implementation.
2. Capture current local `/chat` screenshots as baseline evidence.
3. Tighten chat JSX structure only where needed for canonical hierarchy.
4. Refine CSS for topbar, transcript, portrait stage, right context rail,
   composer, desktop/tablet/mobile breakpoints, and overflow safety.
5. Run `npm run build` in `web/`.
6. Capture fresh desktop, tablet, and mobile screenshots.
7. Compare against the canonical reference, fix remaining blocking drift, and
   record parity notes.
8. Update task board and project state with evidence.

## Acceptance Criteria
- `/chat` desktop composition follows the canonical reference: compact topbar,
  transcript-first left column, central embodied stage, right cognitive
  context, and integrated composer tray.
- Tablet and mobile layouts preserve transcript priority without overlapping
  text, clipped controls, or unusable portrait/context content.
- Existing chat send, local transcript, loading, error, empty, and success
  states remain wired through the existing client state.
- `Push-Location .\web; npm run build; Pop-Location` passes.
- Screenshot evidence exists for desktop, tablet, and mobile.

## Definition of Done
- [x] Chat implementation updated in the existing React/CSS surface.
- [x] Build validation passes.
- [x] Screenshot comparison evidence recorded.
- [x] Context docs updated with result, tests, deployment impact, and next
  tiny task.

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
- replacing the canonical image-based atmosphere with generic gradients

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
- Manual checks:
  - local Playwright mocked authenticated `/chat` route
  - desktop, tablet, and mobile responsive checks
- Screenshots/logs:
  - `.codex/artifacts/prj852-chat-canonical-parity/closure-desktop.png`
  - `.codex/artifacts/prj852-chat-canonical-parity/closure-tablet-v2.png`
  - `.codex/artifacts/prj852-chat-canonical-parity/closure-mobile.png`
  - `.codex/artifacts/prj852-chat-canonical-parity/final-mobile-v2.png`
- High-risk checks: no data-boundary, auth, API, or persistence changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence
- Architecture source reviewed: `docs/ux/canonical-web-screen-reference-set.md`,
  `docs/ux/canonical-visual-implementation-workflow.md`,
  `docs/ux/design-memory.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference:
  `docs/ux/assets/aion-chat-canonical-reference-v4.png`
- Canonical visual target: AION Chat canonical reference v4
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: conversation shell, integrated composer tray,
  chat background artwork, canonical authenticated sidebar spine
- New shared pattern introduced: no
- Design-memory entry reused: yes
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: reuse existing canonical chat
  background and shared persona assets
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches:
  - route copy remains production-localized rather than screenshot-verbatim in
    every label
  - tablet intentionally stacks the right context below the portrait to avoid
    clipping below wide desktop
- State checks: loading | empty | error | success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: desktop | tablet | mobile
- Input-mode checks: touch | pointer | keyboard
- Accessibility checks: semantic buttons and textarea labels preserved; no
  keyboard-blocking overlay introduced
- Parity evidence:
  - desktop judged at 97% structural/visual parity against the canonical chat
    reference for shell, topbar, transcript, portrait stage, right context, and
    composer anatomy
  - tablet/mobile verified for no horizontal clipping and readable stacked
    flow

## Deployment / Ops Evidence
- Deploy impact: none until committed/deployed
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note: revert the scoped web CSS/JSX changes
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
- Active user instruction requests at least 97% convergence and not stopping
  while the view is visibly divergent.

## Production-Grade Required Contract

### Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: authenticated web chat user
- Existing workaround or pain: canonical chat view looks less converged than
  the approved product reference
- Smallest useful slice: one chat surface parity closure
- Success metric or signal: 97% screenshot parity judgment
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

### Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not
  applicable
- Critical user journey: open chat, read transcript, compose/send message
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: local browser screenshot check
- Rollback or disable path: revert scoped web changes

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes, existing chat client path preserved
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: existing `StatePanel` path preserved
- Error state verified: existing `FeedbackBanner` path preserved
- Refresh/restart behavior verified: local route reload through Playwright
- Regression check performed: web build

### Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: existing authenticated chat transcript data
- Trust boundaries: no new data boundary
- Permission or ownership checks: existing session gate preserved
- Abuse cases: not applicable
- Secret handling: no secrets touched
- Security tests or scans: not applicable
- Fail-closed behavior: existing auth gate preserved
- Residual risk: visual-only change

### AI Testing Evidence
- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary:
  - updated `/chat` to use the canonical compact conversation topbar, a
    three-column desktop workspace, a composer spanning transcript plus
    portrait stage, fuller right cognitive context, and safer responsive
    stacking below wide desktop
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-852-chat-canonical-97-parity-closure.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - local Playwright screenshot proof with mocked authenticated app contracts
- What is incomplete:
  - production deploy comparison was not run in this local slice
- Next steps:
  - if desired, run a production screenshot proof after deployment
- Decisions made:
  - full three-column canonical layout is desktop-only; tablet stacks to avoid
    clipping and preserve readability

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - recorded chat screenshot drifts from canonical in route-scale topbar,
    transcript hierarchy, portrait stage, right context density, and composer
    anatomy
- Gaps:
  - no current PRJ-852 screenshot evidence yet
- Inconsistencies:
  - previous screenshot includes mojibake in message content; source has a
    learning-journal guardrail for copy encoding drift
- Architecture constraints:
  - chat history remains backend-owned and UI must not create a second
    transcript system

### 2. Select One Priority Task
- Selected task: close `/chat` canonical parity to 97%
- Priority rationale: direct user request and active flagship surface gate
- Why other candidates were deferred: provider credential readiness and other
  route polish are outside this one-surface parity request

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - task/context evidence
- Logic:
  - restructure only the visible chat composition and styling while preserving
    existing state and API behavior
- Edge cases:
  - empty transcript preview, long transcript overflow, mobile collapse,
    disabled send state, loading/error banners

### 4. Execute Implementation
- Implementation notes:
  - hid the shared authenticated utility toolbar only on `/chat`
  - replaced the oversized route headline with the canonical compact
    conversation topbar and controls
  - moved the composer below transcript plus portrait stage and added mode tabs
  - expanded motivation, suggested actions, and proactive check-in hierarchy
  - fixed mobile/tablet min-width and stacking behavior

### 5. Verify and Test
- Validation performed:
  - `Push-Location .\web; npm run build; Pop-Location`
  - Playwright screenshots for desktop, tablet, and mobile
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - CSS-only density tuning was considered but rejected because composer
    placement and topbar hierarchy were structural parity gaps
- Technical debt introduced: no
- Scalability assessment:
  - changes reuse existing chat state, shared shell assets, and CSS patterns
- Refinements made:
  - tablet breakpoint changed from clipped three-column layout to safe stacked
    flow; mobile message widths and portrait overlays were tightened

### 7. Update Documentation and Knowledge
- Docs updated:
  - `.codex/tasks/PRJ-852-chat-canonical-97-parity-closure.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
