# Task

## Header
- ID: PRJ-800J
- Title: Public home first viewport live closure pass
- Task Type: design
- Current Stage: verification
- Status: IN_PROGRESS
- Owner: Frontend Builder
- Depends on: PRJ-800I
- Priority: P1

## Context
`PRJ-800I` improved public-home parity and production now proves the landing is
materially calmer. The latest live screenshot, however, shows that the first
viewport still drifts from the canonical landing in three concrete ways:

- the headline column still dominates too much relative to the shared persona
- the persona stage still behaves like a right panel instead of one central
  scene
- the bridge band still lands too low and too wide, which allows the auth
  surface to creep into the first read

This task targets only that first-viewport closure loop using the latest live
deploy evidence.

## Goal
Bring the public-home first viewport closer to canonical parity by reducing
headline dominance, increasing persona-stage authority, and compressing the
bridge band into a cleaner end-stop before lower content begins.

## Deliverable For This Stage
A focused implementation pass in `web/src/App.tsx` and `web/src/index.css`
that improves the first viewport on the live landing without inventing any new
public-home subsystems.

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/tasks/PRJ-800I-public-home-live-hero-bridge-parity-pass.md`
- `.codex/tasks/PRJ-800J-public-home-first-viewport-live-closure-pass.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Record the production evidence from `PRJ-800I` and close it as a completed
   proof-backed slice.
2. Reduce hero-copy dominance through proportion and type changes rather than
   new sections.
3. Expand and re-center the shared persona scene so it reads closer to the
   canonical landing composition.
4. Tighten the bridge band so it behaves like the final movement of the hero
   instead of a separate, wide support block.
5. Run focused validation and sync repo truth.

## Acceptance Criteria
- The public landing first viewport reads more as one canonical scene.
- The headline no longer overwhelms the stage.
- The bridge band ends the hero cleanly and pushes lower content out of the
  first read.
- Validation passes and repo truth reflects the new slice.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] Live evidence for `PRJ-800I` is recorded and that slice is closed honestly.
- [x] First-viewport proportions are improved in code.
- [x] Validation and source-of-truth updates match the changed scope.

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
  - `git diff --check -- web/src/index.css .codex/tasks/PRJ-800I-public-home-live-hero-bridge-parity-pass.md .codex/tasks/PRJ-800J-public-home-first-viewport-live-closure-pass.md`
- Manual checks:
  - compared fresh production evidence against the canonical landing
  - captured a local preview screenshot after the new first-viewport pass
- Screenshots/logs:
  - production evidence: `.codex/artifacts/prod-login-live-after-prj800i-wait.png`
  - local proof: `.codex/artifacts/local-login-after-prj800j.png`
  - canonical target: `docs/ux/assets/aion-landing-canonical-reference-v1.png`
- High-risk checks:
  - kept the pass within the existing public-home layout and shared persona system

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/planning/layout-sidebar-home-dashboard-canonical-parity-master-ledger.md`
  - `docs/planning/layout-sidebar-home-dashboard-micro-parity-checklist.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: `.codex/artifacts/prod-login-live-after-prj800i-wait.png`
- Canonical visual target: `docs/ux/assets/aion-landing-canonical-reference-v1.png`
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: shared persona motif panel, public shell, public bridge band
- New shared pattern introduced: no
- Design-memory entry reused: `docs/ux/design-memory.md`
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: reuse the existing painterly persona asset and route atmosphere
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches:
  - the headline column is still a touch too dominant against the canonical reference
  - the bridge band is cleaner now, but the lower story/auth boundary still needs a later pass
- State checks: loading | empty | error | success
- Responsive checks: desktop | tablet | mobile
- Input-mode checks: touch | pointer | keyboard
- Accessibility checks: existing button and link semantics preserved
- Parity evidence:
  - `.codex/artifacts/prod-login-live-after-prj800i-wait.png`
  - `.codex/artifacts/local-login-after-prj800j.png`
  - `docs/ux/assets/aion-landing-canonical-reference-v1.png`

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not needed
- Rollback note: revert this slice if hero hierarchy regresses

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
This slice remains scoped to the public landing. Dashboard parity continues in
its own lane after this first-viewport loop.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime
  surfaces
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
- Loading state verified: yes
- Error state verified: yes
- Refresh/restart behavior verified: pending
- Regression check performed:

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
  - closed `PRJ-800I` with live production evidence
  - reduced first-viewport headline dominance
  - gave the shared persona more stage authority
  - tightened the bridge band to end the hero more cleanly
- Files changed:
  - `web/src/index.css`
  - `.codex/tasks/PRJ-800I-public-home-live-hero-bridge-parity-pass.md`
  - `.codex/tasks/PRJ-800J-public-home-first-viewport-live-closure-pass.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - focused `git diff --check`
  - production screenshot comparison
  - local preview screenshot comparison
- What is incomplete:
  - final public-home lower-story/auth-priority tuning
  - dashboard continues as a separate parity lane
- Next steps:
  - push this slice and review the deployed `/` and `/login`
  - then continue either the final public-home closure or return to dashboard parity
- Decisions made:
  - solved the next drift through proportion and closure tuning, not new sections
  - kept the shared persona as the visual anchor of the landing
