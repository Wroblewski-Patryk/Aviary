# Task

## Header
- ID: PRJ-868
- Title: Canonical 99 Layout Foundation
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-867
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 868
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The user raised the target from high canonical convergence to `99%` and asked to
restart from public/private layout, then home, dashboard, and personality. The
canonical workflow requires closing shared layout before dependent route
surfaces.

## Goal
Establish a stronger public/private layout foundation for the `99%` canonical
program by removing remaining route-toolbar drift and improving mobile
authenticated navigation readability.

## Success Signal
- User or operator problem: route-level polish cannot reach 99% while shared
  layout still has visible drift.
- Expected product or reliability outcome: all authenticated routes share the
  same no-toolbar canonical shell baseline and mobile navigation does not clip
  labels.
- How success will be observed: desktop/mobile screenshots across Settings,
  Dashboard, and public Landing.
- Post-launch learning needed: no

## Deliverable For This Stage
Implement the shared shell/layout fixes only, then verify with build and
screenshots before moving back to route surfaces.

## Constraints
- use existing systems and approved mechanisms
- do not refactor route data or API contracts
- do not invent new public/private shell systems
- keep changes tiny, testable, and reversible

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/tasks/PRJ-868-canonical-99-layout-foundation.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Hide the extra authenticated desktop route toolbar for every private route,
   including Settings.
2. Increase mobile shell bottom clearance for the fixed tab bar.
3. Replace the cramped five-column mobile tabbar grid with a horizontally
   scrollable canonical tabbar that preserves labels.
4. Capture Settings, Dashboard, and public Landing screenshots for shell
   regression evidence.
5. Run build and whitespace validation.

## Acceptance Criteria
- Settings no longer shows the old desktop utility toolbar.
- Mobile authenticated nav labels are not clipped or forced into cramped grid
  cells.
- Mobile content has enough bottom clearance for the fixed nav.
- Dashboard and Landing remain visually intact after shell changes.
- No horizontal page overflow is introduced.

## Definition of Done
- [x] Web build passes.
- [x] `git diff --check` passes.
- [x] Desktop/mobile shell screenshots are captured.
- [x] Latest implementation screenshots are inspected with `view_image`.

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
- Manual checks: Settings desktop/mobile and Dashboard desktop inspected for
  shell toolbar removal, mobile nav fit, and horizontal overflow.
- Screenshots/logs:
  - `.codex/artifacts/prj868-canonical-99-layout-foundation/settings-mobile-390x844-viewport-v7.png`
  - `.codex/artifacts/prj868-canonical-99-layout-foundation/settings-mobile-390x844-v7.png`
  - `.codex/artifacts/prj868-canonical-99-layout-foundation/settings-desktop-1568x1003-v4.png`
  - `.codex/artifacts/prj868-canonical-99-layout-foundation/dashboard-desktop-1568x1003-v4.png`
  - `.codex/artifacts/prj868-canonical-99-layout-foundation/landing-mobile-390x844.png`
- High-risk checks: no runtime/data-contract changes in scope
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence
- Architecture source reviewed:
  - `docs/ux/canonical-visual-implementation-workflow.md`
  - `docs/ux/canonical-web-screen-reference-set.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: authenticated sidebar and public landing canonical
  reference set
- Canonical visual target: shared public/private layout baseline
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: canonical shell and sidebar
- New shared pattern introduced: no
- Design-memory entry reused: canonical visual workflow sequencing
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: no asset changes
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: route-specific surfaces still need dedicated 99%
  passes after the shared layout foundation
- State checks: success
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop | mobile
- Input-mode checks: pointer | touch
- Accessibility checks: nav remains button-based
- Parity evidence: pending

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note: revert shell layout JSX/CSS changes
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

## Result Report
- Task summary: completed the shared public/private layout foundation for the
  99% canonical program.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-868-canonical-99-layout-foundation.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-868-canonical-99-layout-foundation.md`
  - Chrome CDP screenshot pass for Settings mobile/desktop and Dashboard
    desktop, plus existing public Landing mobile evidence
- What is incomplete: route-specific 99% passes for public home, dashboard,
  and personality remain separate tasks.
- Next steps: start the public home/landing 99% route pass on top of this
  shared shell baseline.
- Decisions made: hide the duplicated mobile header route row below `md`, keep
  tablet header navigation, and make the phone bottom tabbar compact enough to
  show all five route labels without clipping.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: Settings still shows the old desktop utility toolbar; mobile tabbar
  uses five cramped grid cells.
- Gaps: shared layout is not yet a clean enough baseline for 99% route work.
- Inconsistencies: canonicalized routes hide the toolbar, Settings does not.
- Architecture constraints: shared shell only; no route data changes.

### 2. Select One Priority Task
- Selected task: canonical 99 layout foundation.
- Priority rationale: shared layout must close before public home/dashboard/
  personality can be judged at 99%.
- Why other candidates were deferred: route-specific polishing waits for this
  shared baseline.

### 3. Plan Implementation
- Files or surfaces to modify: authenticated shell JSX and CSS.
- Logic: no runtime logic or API changes.
- Edge cases: mobile nav overflow, bottom fixed nav clearance, Settings toolbar.

### 4. Execute Implementation
- Implementation notes: removed remaining desktop route-toolbar drift by
  hiding the authenticated toolbar globally, increased mobile private-shell
  bottom clearance, hid the duplicated phone header route row, and tuned the
  phone bottom tabbar density so all route labels fit.

### 5. Verify and Test
- Validation performed: web production build, diff whitespace check, and Chrome
  CDP screenshots with local visual API responses for private shell rendering.
- Result: passed; latest Settings mobile metrics showed
  `bodyWidth=390`, `viewportWidth=390`, `visibleToolbar=0`,
  `headerRouteRowDisplay=none`, and bottom tabbar `scrollWidth=366` /
  `clientWidth=366`.

### 6. Self-Review
- Simpler option considered: only using `scrollIntoView` for the active mobile
  tab; rejected after screenshot evidence showed a partial clip remained.
- Technical debt introduced: none expected; changes stay inside existing shell
  JSX/CSS.
- Refinements made: replaced the unreliable scroll-only behavior with compact
  tabbar sizing and removed the duplicated mobile header route row.

### 7. Update Documentation and Knowledge
- Docs updated: task contract, task board, and project state.
- Context updated: yes.
- Learning journal updated: not required; no recurring execution pitfall beyond
  the already-known need for screenshot evidence was confirmed.
