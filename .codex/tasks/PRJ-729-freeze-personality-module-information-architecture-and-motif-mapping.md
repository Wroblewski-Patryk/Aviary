# Task

## Header
- ID: PRJ-729
- Title: Freeze Personality Module Information Architecture And Motif Mapping
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Product Docs Agent
- Depends on: PRJ-728
- Priority: P0

## Context
`personality` is the next planned module after the dashboard foundation. It
needs a detailed IA and motif mapping plan before implementation starts, so it
reuses the shared system instead of diverging into a special-case showcase.

## Goal
Freeze the product-facing personality module structure using the embodied
cognition motif and shared component language.

## Deliverable For This Stage
- one explicit personality section map
- one mapping from AION architecture concepts to visible UI zones
- one reuse contract tying personality back to dashboard primitives

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] major personality sections are defined
- [x] architecture-to-visual mapping is defined
- [x] shared-component reuse is explicit

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
  - Not run; documentation/map synchronization only.
- Manual checks:
  - Created `docs/ux/personality-module-map.md`.
  - Reviewed `docs/planning/dashboard-foundation-and-personality-visual-system-plan.md`.
  - Reviewed `.codex/context/TASK_BOARD.md` for PRJ-729/PRJ-730 lane history and later PRJ-865/PRJ-871 personality canonical proof.
  - Reviewed `web/src/App.tsx` for personality section owners, architecture-to-visual mapping, and shared component reuse.
  - Added the map to `docs/index.md` and `docs/README.md`.
  - `git diff --check` passed.
- Screenshots/logs:
  - Existing personality canonical screenshot artifacts are listed in `docs/ux/personality-module-map.md`.
- High-risk checks:
  - No new route behavior, backend contract, component extraction, or duplicate visual system was introduced.

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/ux/personality-module-map.md`
  - `docs/planning/dashboard-foundation-and-personality-visual-system-plan.md`
  - `docs/ux/aion-visual-motif-system.md`
  - `.codex/context/TASK_BOARD.md`
  - `web/src/App.tsx`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - Added module map to `docs/index.md` and `docs/README.md`.

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference:
  - `docs/ux/assets/aion-personality-canonical-reference-v1.png`
  - `docs/ux/aion-visual-motif-system.md`
  - `docs/ux/personality-module-map.md`
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - authenticated shell frame
  - shared motif hero panel
  - timeline rail panel
  - insight panel family
  - shared card/panel grammar
- New shared pattern introduced: no
- Design-memory entry reused:
  - Embodied cognition motif
  - Shared canonical persona figure
  - Surface-first flagship closure
- Design-memory update required: no
- State checks: not changed in this documentation slice
- Responsive checks: desktop | tablet | mobile expectations mapped; tablet proof remains a known gap in the map
- Input-mode checks: not changed in this documentation slice
- Accessibility checks: no new UI surface changed
- Parity evidence:
  - Existing PRJ-865 and PRJ-871 screenshot artifacts are listed in `docs/ux/personality-module-map.md`.

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated:
- Rollback note:

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
- This route should become the richest expression of the system, not a separate
  visual universe.
- 2026-05-03 sync:
  - This task is closed by adding a durable personality module map.
  - The stale-task guardrail is already recorded in
    `.codex/context/LEARNING_JOURNAL.md`.

## Result Report
- Goal:
  - Freeze personality module IA, architecture-to-visual mapping, and reuse
    contract in a durable docs artifact.
- Scope:
  - Documentation/map update only.
- Implementation Plan:
  - Inventory existing personality route structure, planning docs, and later
    proof artifacts.
  - Create a module map with section owners, architecture mapping, and reuse
    boundaries.
  - Link the map from documentation entrypoints.
  - Update task and context state.
- Acceptance Criteria:
  - Major sections are visible in one map.
  - AION architecture concepts map to UI zones and data anchors.
  - Shared-component reuse and route boundaries are explicit.
- Definition of Done:
  - Satisfied by `docs/ux/personality-module-map.md`, context updates, and
    `git diff --check`.
- Result:
  - PRJ-729 is closed as a personality IA/motif-map repair slice.
- Next:
  - Review `PRJ-730` for implementation status on shared visual foundations.
