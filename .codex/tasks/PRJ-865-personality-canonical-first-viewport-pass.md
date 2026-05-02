# Task

## Header
- ID: PRJ-865
- Title: Personality Canonical First Viewport Pass
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-864
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 865
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The Dashboard and Chat surfaces now use the canonical shell/sidebar direction.
The Personality route still has an extra route toolbar and a separate oversized
hero summary before the actual embodied personality map, which pushes the
canonical content too far down the first viewport.

## Goal
Bring the Personality route closer to
`docs/ux/assets/aion-personality-canonical-reference-v1.png` by tightening the
first viewport and making the embodied map, timeline, and side panels read as
one canonical screen.

## Success Signal
- User or operator problem: Personality feels less like a generic route page and
  more like the approved embodied cognition overview.
- Expected product or reliability outcome: first viewport shows the personality
  map and timeline sooner without changing backend data contracts.
- How success will be observed: desktop/mobile screenshots and layout metrics.
- Post-launch learning needed: no

## Deliverable For This Stage
Implement the focused frontend layout and density pass for `/personality`, then
verify with build and screenshots.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new runtime/API structures
- do not replace canonical assets with gradient approximations
- stay within the `/personality` route and shared shell visibility needed for
  canonical parity

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/tasks/PRJ-865-personality-canonical-first-viewport-pass.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Hide the extra desktop route toolbar for Personality like Chat and Dashboard.
2. Replace the separate large route intro card with a compact in-flow
   Personality overview bar.
3. Tighten the embodied map, callouts, timeline, and side-panel spacing.
4. Capture desktop/mobile screenshots and compare against the canonical
   Personality reference.
5. Run build and whitespace validation.

## Acceptance Criteria
- Desktop `/personality` starts with the canonical embodied map in the first
  viewport instead of a separate route header card.
- Timeline begins visibly in the first desktop viewport.
- Side panels align visually with the map and do not force excess vertical
  spacing.
- No horizontal overflow on desktop or mobile.
- Dashboard and Chat remain structurally unaffected.

## Definition of Done
- [x] Web build passes.
- [x] `git diff --check` passes.
- [x] Desktop and mobile Personality screenshots are captured.
- [x] Canonical Personality reference and latest implementation are inspected
      with `view_image`.

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
- Tests: `Push-Location .\web; npm run build; Pop-Location` passed.
- Manual checks: `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-865-personality-canonical-first-viewport-pass.md` passed with line-ending warnings only.
- Screenshots/logs:
  - `.codex/artifacts/prj865-personality-canonical-pass/desktop-before-1568x1003.png`
  - `.codex/artifacts/prj865-personality-canonical-pass/mobile-before-390x844.png`
  - `.codex/artifacts/prj865-personality-canonical-pass/desktop-1568x1003-v2.png`
  - `.codex/artifacts/prj865-personality-canonical-pass/mobile-390x844-v2.png`
  - `.codex/artifacts/prj865-personality-canonical-pass/dashboard-smoke-1568x1003.png`
- High-risk checks: no runtime or data-contract changes in scope
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence
- Architecture source reviewed: `docs/ux/canonical-web-screen-reference-set.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-personality-canonical-reference-v1.png`
- Canonical visual target: Personality canonical embodied cognition overview
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: canonical authenticated sidebar and route art
- New shared pattern introduced: no
- Design-memory entry reused: canonical route translation rules
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: preserve existing canonical persona
  figure asset
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: desktop still uses the existing cropped implementation
  behavior rather than a full native recreation of the canonical reference's
  top product nav and mobile phone side-by-side mockup; mobile screenshot shows
  the existing fixed bottom nav overlay because full-page capture preserves
  fixed elements.
- State checks: success
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop | mobile
- Input-mode checks: pointer
- Accessibility checks: no new interactive controls beyond existing route buttons
- Parity evidence:
  - reference inspected:
    `docs/ux/assets/aion-personality-canonical-reference-v1.png`
  - implementation inspected:
    `.codex/artifacts/prj865-personality-canonical-pass/desktop-1568x1003-v2.png`
  - mobile inspected:
    `.codex/artifacts/prj865-personality-canonical-pass/mobile-390x844-v2.png`

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note: revert the frontend layout/CSS changes for this task
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
The working tree already contains earlier local commits and untracked artifacts.
This task will keep edits scoped and avoid staging or pushing unrelated work.

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: web user reviewing canonical AION route quality
- Existing workaround or pain: Personality canonical map starts too far below
  the viewport.
- Smallest useful slice: first-viewport composition/density only
- Success metric or signal: screenshot parity and no overflow
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: view Personality overview
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: Playwright route screenshot
- Rollback or disable path: revert frontend changes

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: Dashboard desktop screenshot smoke captured.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: unchanged mocked route data for screenshot only
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: not applicable
- Security tests or scans: not applicable
- Fail-closed behavior: not applicable
- Residual risk: low

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report
- Task summary: tightened the Personality first viewport around the canonical
  embodied map by removing the extra route toolbar, replacing the large intro
  card with a compact overview bar, and compressing hero/timeline/side panel
  spacing.
- Files changed: `web/src/App.tsx`, `web/src/index.css`,
  `.codex/tasks/PRJ-865-personality-canonical-first-viewport-pass.md`,
  `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`.
- How tested: web build, diff whitespace check, desktop/mobile screenshots,
  canonical reference inspection, Dashboard smoke screenshot.
- What is incomplete: no full native recreation of the reference's product-top
  nav or mobile-phone mockup; those are outside the authenticated AION shell
  direction.
- Next steps: continue with the next frozen canonical surface or polish mobile
  fixed-nav capture/spacing if the user wants mobile-first parity.
- Decisions made: reused existing canonical persona asset and route data rather
  than generating or introducing a new Personality asset.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: the route toolbar and separate intro panel push canonical content below
  the first viewport.
- Gaps: first viewport does not resemble the approved Personality composition
  closely enough.
- Inconsistencies: Chat and Dashboard hide the extra route toolbar, Personality
  still shows it.
- Architecture constraints: preserve existing route data and canonical persona
  figure.

### 2. Select One Priority Task
- Selected task: Personality canonical first-viewport pass.
- Priority rationale: Personality has a frozen canonical reference and is the
  next flagship route after Dashboard and Chat.
- Why other candidates were deferred: Tools and Settings are not frozen in the
  canonical set.

### 3. Plan Implementation
- Files or surfaces to modify: `/personality` JSX and CSS only.
- Logic: no runtime logic or API changes.
- Edge cases: desktop density, mobile stacking, horizontal overflow.

### 4. Execute Implementation
- Implementation notes: hid the extra desktop route toolbar for Personality,
  introduced a compact in-flow overview bar, and reduced map, callout,
  timeline, and side-row spacing.

### 5. Verify and Test
- Validation performed: web build, diff whitespace check, desktop/mobile
  Personality screenshots, Dashboard smoke screenshot.
- Result: passed.

### 6. Self-Review
- Simpler option considered: only reducing the old intro panel padding; rejected
  because it would still push the canonical map too far down.
- Technical debt introduced: none known; reused existing route and CSS surface.
- Refinements made: kept route data, callouts, and canonical persona asset
  intact while changing only layout density and shell visibility.

### 7. Update Documentation and Knowledge
- Docs updated: task evidence only; no new canonical pattern introduced.
- Context updated: `.codex/context/TASK_BOARD.md` and
  `.codex/context/PROJECT_STATE.md`.
- Learning journal updated: not needed; no recurring pitfall confirmed.
