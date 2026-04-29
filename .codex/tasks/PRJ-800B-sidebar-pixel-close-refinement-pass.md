# Task

## Header
- ID: PRJ-800B
- Title: Implement sidebar pixel-close refinement pass
- Task Type: design
- Current Stage: implementation
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-800A
- Priority: P1

## Context
`PRJ-800A` calmed the authenticated shell frame. The next canonical step is to
push the desktop authenticated sidebar much closer to the frozen reference in
`docs/ux/assets/aviary-sidebar-layout-canonical-reference-v1.png`.

## Goal
Bring the authenticated desktop sidebar materially closer to the canonical
reference in brand lockup, navigation rhythm, active pill softness, and support
card composition.

## Deliverable For This Stage
One frontend slice in `web/src/App.tsx` and `web/src/index.css` that refines:
- sidebar brand alignment and scale
- nav row height, icon posture, and active treatment
- health card anatomy
- identity card density and crop
- quote closure composition

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-800B-sidebar-pixel-close-refinement-pass.md`

## Implementation Plan
1. Refine the sidebar brand block to a more delicate, left-anchored lockup.
2. Tighten nav row spacing, active pill material, and icon/label alignment.
3. Redesign health, identity, and quote cards toward the canonical anatomy.
4. Preserve current route-contract safety and existing account access behavior.
5. Run focused frontend validation and update source-of-truth notes.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Acceptance Criteria
- the desktop sidebar reads much closer to the canonical reference at a glance
- support cards feel like one coherent family instead of appended widgets
- route behavior stays unchanged for currently implemented modules
- build and focused diff checks pass

## Definition of Done
- [x] Sidebar brand, nav, and support stack are materially closer to the canonical target.
- [x] Current route behavior remains intact.
- [x] Focused frontend validation evidence is attached.

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
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md .codex/tasks/PRJ-800B-sidebar-pixel-close-refinement-pass.md`
- Manual checks:
  - desktop sidebar reviewed against the canonical sidebar reference
- Screenshots/logs:
  - deploy screenshot parity remains a follow-up loop
- High-risk checks:
  - only currently implemented routes remain interactive

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/27_codex_instructions.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:
  - not applicable

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference:
  - `docs/ux/assets/aviary-sidebar-layout-canonical-reference-v1.png`
  - `docs/planning/sidebar-layout-canonical-convergence-plan.md`
  - `docs/planning/layout-sidebar-home-dashboard-micro-parity-checklist.md`
- Canonical visual target:
  - authenticated desktop sidebar layout
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - authenticated flagship sidebar spine
- New shared pattern introduced: no
- Design-memory entry reused:
  - canonical authenticated sidebar lane
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy:
  - keep warm editorial material and quiet decorative wash
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches:
  - full canonical route inventory remains blocked by current route-contract scope
  - deploy screenshot tuning still needed
- State checks: success
- Responsive checks: desktop
- Input-mode checks: pointer | keyboard
- Accessibility checks:
  - nav and identity card remain button-based and keyboard focusable
- Parity evidence:
  - this slice targets local pixel-close refinement; deployment proof follows

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note:
  - revert the frontend sidebar slice if the rail loses clarity or usability

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
- The missing canonical modules remain intentionally out of scope for this pass.

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
- Refresh/restart behavior verified: yes
- Regression check performed:
  - sidebar still uses the existing authenticated route-change contract

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
-  refined the canonical desktop sidebar toward a more pixel-close rail by
   left-anchoring the brand block, calming nav density, softening the active
   pill, and tightening the health, identity, and quote cards
- Files changed:
-  `web/src/App.tsx`
-  `web/src/index.css`
-  `.codex/context/TASK_BOARD.md`
-  `.codex/context/PROJECT_STATE.md`
-  `.codex/tasks/PRJ-800B-sidebar-pixel-close-refinement-pass.md`
- How tested:
-  `Push-Location .\web; npm run build; Pop-Location`
-  `git diff --check -- web/src/App.tsx web/src/index.css .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md .codex/tasks/PRJ-800B-sidebar-pixel-close-refinement-pass.md`
- What is incomplete:
-  deploy screenshot parity for the sidebar
-  canonical route-inventory expansion remains out of scope
- Next steps:
-  compare the deployed sidebar against the canonical image and then move to
   `public home` structural convergence
- Decisions made:
-  preserved the current route contract and refined only the implemented
   sidebar inventory
