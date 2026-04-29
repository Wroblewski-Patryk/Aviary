# Task

## Header
- ID: PRJ-800C
- Title: Implement public-home structural convergence pass
- Task Type: design
- Current Stage: implementation
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-800A, PRJ-800B
- Priority: P1

## Context
The canonical execution order after shell and sidebar exactness is
`public home`. The landing has improved in the first viewport, but it still
reads too much like a converted auth screen instead of one editorial product
story with auth as a supporting module.

## Goal
Bring the public landing materially closer to the canonical landing reference
through stronger hero authority, a calmer bridge band, and a lower story where
auth is no longer the dominant object.

## Deliverable For This Stage
One frontend slice in `web/src/App.tsx` and `web/src/index.css` that refines:
- public nav density and integration with the landing frame
- hero copy/stage proportion and embodied-figure authority
- bridge band composition
- lower public story hierarchy and auth demotion
- trust-band closure mood

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-800C-public-home-structural-convergence-pass.md`

## Implementation Plan
1. Rebalance public nav, hero copy, and hero stage toward the canonical landing.
2. Tighten the bridge band so it reads as one continuation of the hero.
3. Restructure the lower story so editorial proof leads and auth becomes a support module.
4. Refine trust-band closure mood and responsive hierarchy.
5. Run focused frontend validation and update source-of-truth notes.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Acceptance Criteria
- the landing reads more like one canonical product story than hero plus auth grid
- the hero stage has stronger authority and better figure balance
- auth is demoted below the product story without losing usability
- build and focused diff checks pass

## Definition of Done
- [x] Hero, bridge, and lower public story are materially closer to the canonical landing.
- [x] Auth remains usable while becoming a supporting module.
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
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md .codex/tasks/PRJ-800C-public-home-structural-convergence-pass.md`
- Manual checks:
  - public landing reviewed against the canonical landing reference
- Screenshots/logs:
  - deploy screenshot parity remains a follow-up loop
- High-risk checks:
  - login/register still reachable and functional from the landing

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
  - `docs/ux/assets/aion-landing-canonical-reference-v1.png`
  - `docs/planning/layout-sidebar-home-dashboard-canonical-parity-master-ledger.md`
  - `docs/planning/layout-sidebar-home-dashboard-micro-parity-checklist.md`
- Canonical visual target:
  - public layout and landing page
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - shared canonical persona and flagship shell material system
- New shared pattern introduced: no
- Design-memory entry reused:
  - canonical public landing lane
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy:
  - preserve real persona art and painterly atmosphere
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches:
  - deploy screenshot tuning still needed
  - dashboard remains the next structural route after landing
- State checks: success
- Responsive checks: desktop | tablet | mobile
- Input-mode checks: pointer | keyboard | touch
- Accessibility checks:
  - CTA and auth controls remain keyboard reachable and readable
- Parity evidence:
  - this slice targets structural landing convergence first; screenshot proof follows

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note:
  - revert the frontend landing slice if auth discoverability regresses

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
- This slice intentionally avoids dashboard changes to preserve the canonical execution order.

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
  - landing still uses the existing auth submit and route-entry contract

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
-  rebalanced the public landing so the hero, bridge band, and lower story read
   more like one canonical editorial surface, while auth now behaves more like
   a supporting entry module than a co-equal screen
- Files changed:
-  `web/src/App.tsx`
-  `web/src/index.css`
-  `.codex/context/TASK_BOARD.md`
-  `.codex/context/PROJECT_STATE.md`
-  `.codex/tasks/PRJ-800C-public-home-structural-convergence-pass.md`
- How tested:
-  `Push-Location .\web; npm run build; Pop-Location`
-  `git diff --check -- web/src/App.tsx web/src/index.css .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md .codex/tasks/PRJ-800C-public-home-structural-convergence-pass.md`
- What is incomplete:
-  deploy screenshot tuning for the public landing
-  dashboard remains the next major structural route
- Next steps:
-  compare the deployed landing against the canonical landing reference and
   then execute the next `dashboard` convergence pass
- Decisions made:
-  kept the same auth surface and contract while demoting it compositionally
-  preserved the shared persona artwork and concentrated this slice on layout hierarchy
