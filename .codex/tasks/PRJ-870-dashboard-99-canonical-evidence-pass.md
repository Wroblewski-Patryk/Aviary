# Task

## Header
- ID: PRJ-870
- Title: Dashboard 99 Canonical Evidence Pass
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-869
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 870
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The renewed `99%` canonical program has closed shared public/private layout and
public home. The canonical workflow now moves to the authenticated dashboard,
with iteration `870` in TESTER mode, so this slice emphasizes evidence-backed
visual closure and only the smallest implementation adjustments needed by the
screenshot audit.

## Goal
Validate and improve the `/dashboard` canonical first viewport against
`docs/ux/assets/aion-dashboard-canonical-reference-v2.png` without changing
backend/API/data contracts.

## Success Signal
- User or operator problem: dashboard still needs screenshot evidence at the
  new `99%` target after previous density passes.
- Expected product or reliability outcome: dashboard first viewport reads as a
  single canonical app surface with sidebar, hero, cognitive flow, insight rail,
  and lower cards in the same visual system.
- How success will be observed: desktop and mobile screenshots with a written
  mismatch ledger.
- Post-launch learning needed: no

## Deliverable For This Stage
Run a dashboard screenshot audit, apply a focused polish patch if evidence shows
visible drift, then verify with build and screenshots.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new dashboard systems
- do not alter API contracts or persistence
- preserve canonical raster assets
- keep changes tiny, testable, and reversible

## Scope
- `web/src/App.tsx` if a narrow dashboard markup adjustment is needed
- `web/src/index.css`
- `.codex/tasks/PRJ-870-dashboard-99-canonical-evidence-pass.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Capture current dashboard desktop/mobile screenshots using local visual API
   responses.
2. Compare against the canonical dashboard reference and record visible gaps.
3. Apply the smallest CSS/JSX polish needed to improve first-viewport parity.
4. Verify no horizontal overflow and no route-toolbar regression.
5. Run build, `git diff --check`, and screenshot comparison.

## Acceptance Criteria
- Dashboard desktop preserves the canonical sidebar + main + right insight rail
  layout language.
- Hero and cognitive flow fit the first viewport with stronger reference
  hierarchy.
- Mobile remains readable with no horizontal page overflow.
- Real route data plumbing remains untouched.
- No backend/API/data-contract changes are introduced.

## Definition of Done
- [x] Web build passes.
- [x] `git diff --check` passes.
- [x] Desktop and mobile dashboard screenshots are captured.
- [x] Latest implementation screenshots are inspected with `view_image`.
- [x] Mismatch ledger is recorded in this task.

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
- Manual checks: desktop viewport, desktop full-page, and mobile full-page
  dashboard screenshots inspected against the canonical reference.
- Screenshots/logs:
  - `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-desktop-viewport-before-1568x1003.png`
  - `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-desktop-before-1568x1003.png`
  - `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-mobile-before-390x844.png`
  - `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-desktop-viewport-after-1568x1003-v3.png`
  - `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-desktop-after-1568x1003-v3.png`
  - `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-mobile-after-390x844-v2.png`
- High-risk checks: no runtime/data-contract changes in scope
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence
- Architecture source reviewed:
  - `docs/ux/canonical-visual-implementation-workflow.md`
  - `docs/ux/screen-quality-checklist.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
- Canonical visual target: dashboard first viewport
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: canonical sidebar, dashboard stage, dashboard
  hero raster, guidance rail
- New shared pattern introduced: no
- Design-memory entry reused: canonical visual workflow sequencing
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: preserve approved raster assets
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: exact browser toolbar from the older dashboard mockup is
  intentionally absent because `PRJ-868` established the no-toolbar private
  shell baseline per the user's later layout direction.
- State checks: loading | empty | error | success
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop | mobile
- Input-mode checks: pointer | touch | keyboard
- Accessibility checks: button semantics preserved
- Parity evidence:
  - reference inspected:
    - `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
  - render inspected:
    - `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-desktop-viewport-after-1568x1003-v3.png`
    - `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-desktop-after-1568x1003-v3.png`
    - `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-mobile-after-390x844-v2.png`
  - mismatch ledger:
    - hero height: reduced dashboard hero/stage density so the flow and lower
      modules begin earlier like the canonical reference
    - cognitive flow: compacted flow card, phase panel, step typography, and
      step controls to avoid oversized vertical rhythm
    - summary band: fixed balance-row layout so labels and values no longer
      overlap or split vertically
    - shell: confirmed no legacy route toolbar and no horizontal overflow
    - mobile: preserved readable stacked route order with no page-width overflow

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note: revert dashboard CSS/JSX changes
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
- Task summary: completed the dashboard `99%` canonical evidence pass in
  TESTER mode, applying only evidence-backed CSS polish to hero density,
  cognitive flow density, and summary-band typography.
- Files changed:
  - `web/src/index.css`
  - `.codex/tasks/PRJ-870-dashboard-99-canonical-evidence-pass.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-870-dashboard-99-canonical-evidence-pass.md`
  - Chrome CDP screenshots for dashboard desktop viewport, desktop full page,
    and mobile full page with local visual API responses
  - `view_image` inspection of the approved reference and latest renders
- What is incomplete: personality `99%` route pass remains.
- Next steps: start personality `99%` canonical pass.
- Decisions made: keep the no-toolbar private shell baseline from `PRJ-868`
  even though the older dashboard reference includes browser toolbar chrome.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard hero and flow were vertically too tall, pushing lower cards
  down; the summary balance card had visible text overlap in the full-page
  screenshot.
- Gaps: dashboard needs a fresh `99%` evidence pass after shared shell and
  public home closure.
- Inconsistencies: current private shell intentionally omits the old browser
  toolbar shown in the dashboard reference.
- Architecture constraints: authenticated dashboard only; no API changes.

### 2. Select One Priority Task
- Selected task: dashboard 99 canonical evidence pass.
- Priority rationale: canonical workflow closes dashboard before personality.
- Why other candidates were deferred: personality depends on dashboard closure.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard JSX/CSS only if screenshot evidence
  requires it.
- Logic: no runtime logic changes expected.
- Edge cases: visual API unavailable, mobile overflow, toolbar/sidebar
  regression.

### 4. Execute Implementation
- Implementation notes: compacted dashboard hero copy/stage density, reduced
  cognitive-flow panel and step typography, tightened phase panel controls, and
  fixed summary balance-row layout.

### 5. Verify and Test
- Validation performed: web build, diff whitespace check, Chrome CDP screenshots,
  and direct `view_image` inspection.
- Result: passed; latest desktop metrics showed `bodyWidth=1568`,
  `viewportWidth=1568`, `visibleToolbar=0`, `stageHeight=472`,
  `flowHeight=187`, `lowerTop=698`, and summary band without overlap.

### 6. Self-Review
- Simpler option considered: screenshot-only closure with no patch; rejected
  because the flow panel and summary overlap were visible, fixable mismatches.
- Technical debt introduced: none expected; changes are CSS-only and reuse
  existing dashboard classes.
- Refinements made: adjusted summary balance grid after the first fix still
  allowed long labels to split awkwardly.

### 7. Update Documentation and Knowledge
- Docs updated: task contract, task board, and project state.
- Context updated: yes.
- Learning journal updated: not required; no recurring pitfall was confirmed.
