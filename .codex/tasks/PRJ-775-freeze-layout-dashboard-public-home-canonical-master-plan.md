# Task

## Header
- ID: PRJ-775
- Title: Freeze Layout, Dashboard, Public Home Canonical Master Plan
- Task Type: design
- Current Stage: planning
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-743
- Priority: P1

## Context
The flagship visual convergence lane already improved `dashboard`, `chat`, and
`personality`, but the user explicitly called out that large structural
differences still remain. The highest-value remaining surfaces are no longer
route-local polish only. They are the parent layout, public layout, public
home, and dashboard composition.

## Goal
Produce one detailed master audit and implementation plan that decomposes the
remaining canonical drift for the shared authenticated shell, public landing
experience, and dashboard.

## Scope
- `docs/planning/layout-dashboard-public-home-canonical-master-audit.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/context/TASK_BOARD.md`
- this planning task file

## Deliverable For This Stage
A planning-grade audit and implementation sequence that:

- identifies structural gaps
- groups them by reusable layer
- defines implementation order
- states asset requirements
- leaves an implementation-ready backlog

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Review canonical landing and dashboard references plus current shell code.
2. Audit public layout, authenticated parent layout, and dashboard separately.
3. Regroup route-level differences into reusable layout layers.
4. Write a single master plan with sequence, asset strategy, and acceptance
   criteria.
5. Sync task board and project state with the new planning baseline.

## Acceptance Criteria
- The audit distinguishes parent-layout drift from route-local drift.
- Public home and dashboard have explicit gap inventories and execution order.
- The plan names required decorative asset work instead of collapsing it into
  CSS-only approximations.
- A next implementation lane is obvious from the written plan.

## Definition of Done
- [x] A detailed master audit exists for layout, public home, and dashboard.
- [x] The audit records reusable-layer gaps, route-specific gaps, and asset needs.
- [x] Context files are updated to reflect the new planning baseline.

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
  - not applicable for planning-only slice
- Manual checks:
  - reviewed canonical landing and dashboard references
  - reviewed current shell/public/dashboard implementation in `web/src/App.tsx`
    and `web/src/index.css`
- Screenshots/logs:
  - canonical assets reviewed directly from repo
- High-risk checks:
  - route-contract assumption documented: public home is the unauthenticated
    surface and dashboard is the authenticated home surface

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/27_codex_instructions.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
  - not applicable
- Follow-up architecture doc updates:
  - none in this planning slice

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference:
  - `docs/ux/assets/aion-landing-canonical-reference-v1.png`
  - `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
- Canonical visual target:
  - public landing
  - authenticated parent layout
  - dashboard
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - current shell, utility bar, rail, panel, and flagship route families were
    used as the baseline for the audit
- New shared pattern introduced: no
- Design-memory entry reused:
  - existing flagship shell and motif direction
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy:
  - preserve current raster-backed atmosphere where already present
  - prepare dedicated public landing assets
  - consider dedicated dashboard connector/ornament asset only if CSS remains
    too flat during implementation
- Canonical asset extraction required: yes
- Screenshot comparison pass completed: no
- Remaining mismatches:
  - documented in the master audit
- State checks: not applicable in planning-only slice
- Responsive checks: desktop | tablet | mobile target expectations documented
- Input-mode checks: pointer target expectations noted indirectly via shell
  planning; no implementation verification in this stage
- Accessibility checks:
  - not executed in planning stage
- Parity evidence:
  - canonical-source review plus implementation audit document

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes:
  - none
- Health-check impact:
  - none
- Smoke steps updated:
  - no
- Rollback note:
  - not applicable

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
- This planning slice intentionally stops before implementation.
- The master audit should drive the next coordinated flagship implementation
  lane rather than more isolated visual micro-passes.

## Result Report
- Task summary:
  - created a detailed canonical master audit for the parent layout, public
    layout/home, and dashboard
- Files changed:
  - `docs/planning/layout-dashboard-public-home-canonical-master-audit.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/tasks/PRJ-775-freeze-layout-dashboard-public-home-canonical-master-plan.md`
- How tested:
  - reviewed canonical assets and current implementation files
- What is incomplete:
  - implementation of the planned layout and dashboard reconstruction
- Next steps:
  - execute the shell/public/dashboard lane in the order defined by the master
    audit
- Decisions made:
  - treat public home as the unauthenticated landing surface
  - treat dashboard as the authenticated home surface
