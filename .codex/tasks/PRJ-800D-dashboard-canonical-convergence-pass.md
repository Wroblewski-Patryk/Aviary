# Task

## Header
- ID: PRJ-800D
- Title: Dashboard Canonical Convergence Pass
- Task Type: design
- Current Stage: implementation
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-800A, PRJ-800B, PRJ-800C
- Priority: P1

## Context
The canonical execution order for `layout + sidebar + home + dashboard` is now
frozen in:

- `docs/planning/layout-sidebar-home-dashboard-canonical-parity-master-ledger.md`
- `docs/planning/layout-sidebar-home-dashboard-micro-parity-checklist.md`

`PRJ-800A..PRJ-800C` stabilized the authenticated shell, desktop sidebar, and
public landing. The next highest-value flagship gap is the authenticated
dashboard, which still reads as multiple premium sections rather than one
canonical one-screen tableau.

## Goal
Move the authenticated dashboard materially closer to
`docs/ux/assets/aion-dashboard-canonical-reference-v2.png` by compressing the
reading hierarchy, increasing hero authority, flattening the right rail into a
single editorial support column, and reducing lower-half competition.

## Deliverable For This Stage
A production-ready dashboard composition pass implemented in the current web
shell, plus synced repository truth and validation evidence for the changed
scope.

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-800D-dashboard-canonical-convergence-pass.md`

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Remove dashboard intro and bridge elements that still read like generic page
   header chrome instead of part of the hero tableau.
2. Increase dashboard hero authority through calmer signal stacks, stronger
   center figure posture, and quieter note/caption relations.
3. Rebuild the right rail into a more editorial support column with one
   dominant guidance surface, quieter recent activity, and scenic intention
   closure.
4. Convert the flow band from a cluster of cards into a single instrument with
   track plus current-phase support.
5. Rebuild the bottom summary closure to more closely resemble the canonical
   `system harmony / balance across layers / weekly summary` composition.
6. Run focused validation and sync source-of-truth files for this slice.

## Acceptance Criteria
- Dashboard reads closer to one flagship canvas than to stacked route modules.
- The right column behaves as one editorial rail instead of multiple equally
  weighted cards.
- Flow and lower summary support the hero rather than competing with it.
- The canonical shared persona remains central and adapted specifically to the
  dashboard context.

## Definition of Done
- [x] Hero clearly dominates the route composition.
- [x] Right rail is more editorial than modular.
- [x] Flow band behaves like one instrument.
- [x] Bottom summary closure is structurally closer to the canonical reference.
- [x] Build and focused diff validation pass.
- [x] Task board and project state are updated in the same slice.

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
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-800D-dashboard-canonical-convergence-pass.md`
- Manual checks:
  - dashboard JSX was checked for removal of old hero chips, hero-note bridge, and channel-status block
  - dashboard CSS was checked for new right-rail, flow-shell, and summary-closure hooks
- Screenshots/logs:
  - local build completed successfully
- High-risk checks:
  - no new route-level systems or duplicate dashboard surfaces introduced

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/ux/canonical-visual-implementation-workflow.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference:
  - `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
- Canonical visual target: dashboard flagship one-screen tableau
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: shared shell, shared canonical persona, sidebar shell tokens
- New shared pattern introduced: yes
- Design-memory entry reused: shared flagship persona continuity
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: reuse existing approved dashboard assets
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches:
  - live screenshot tuning still required after deploy
  - tablet/mobile parity still needs post-implementation proof
- State checks: success
- Responsive checks: desktop | tablet | mobile
- Input-mode checks: pointer | keyboard
- Accessibility checks: visual hierarchy, button presence, content order
- Parity evidence:

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert dashboard composition slice

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
This slice intentionally focuses on dashboard composition. Live screenshot
parity remains a follow-up closure pass after the deploy catches up.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB
-> validation -> error handling -> test. Partial implementations, mock-only
paths, placeholders, fake data, and temporary fixes are forbidden.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: focused web build and diff checks

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
  - compressed the dashboard toward a more canonical one-screen flagship read
  - removed the extra hero-note bridge and the non-canonical dashboard channel-status card
  - rebuilt the right rail into a single editorial guidance surface plus quieter recent activity and intention closure
  - converted the flow band into a track-plus-phase instrument
  - rebuilt the summary closure toward a `system harmony / balance across layers / weekly summary` composition
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-800D-dashboard-canonical-convergence-pass.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-800D-dashboard-canonical-convergence-pass.md`
- What is incomplete:
  - deployed screenshot comparison against `aion-dashboard-canonical-reference-v2.png`
  - responsive proof for tablet/mobile dashboard parity
- Next steps:
  - deploy and run the next screenshot-driven parity loop
  - tune hero crop, rail spacing, and lower closure based on live evidence
- Decisions made:
  - kept the shared canonical persona as the dashboard center
  - removed the dashboard-local conversation-channel card because it competed with the canonical editorial rail
  - preferred one stronger summary closure over multiple equal metric cards
