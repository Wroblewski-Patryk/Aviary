# Task

## Header
- ID: PRJ-725
- Title: Shared Tokens, Surfaces, And Motif Infrastructure
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-724
- Priority: P0

## Context
The dashboard shell and later modules need shared tokens, materials, panel
variants, and motif containers before route-specific work begins.

## Goal
Plan the reusable implementation slice that adds the visual token layer and
shared surface primitives for the new motif system.

## Deliverable For This Stage
- one implementation-ready slice definition for shared tokens and surfaces
- explicit write scope in `web/`
- validation expectations for reusable UI primitives

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] token families are listed
- [x] shared surface primitives are listed
- [x] route-specific work is clearly excluded from this slice

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
  - Not run; status/documentation synchronization only.
- Manual checks:
  - Reviewed `docs/planning/dashboard-foundation-and-personality-visual-system-plan.md`.
  - Confirmed the implementation principle explicitly orders shared tokens and primitives before route composition.
  - Confirmed shared component families include shell, surface, content, and input primitives.
  - Reviewed `.codex/context/TASK_BOARD.md`; the board already records `PRJ-724..PRJ-727` as complete locally with shared motif-aware surfaces and background primitives in `web/src/index.css`.
  - Reviewed `web/src/index.css` for existing `--aion-*` token families and shared `.aion-panel*` motif/surface primitives.
  - Reviewed `web/src/App.tsx` for reuse of shared surface classes and route-level components such as `RouteHeroPanel`, `InsightPanel`, and `MotifFigurePanel`.
  - `git diff --check` passed.
- Screenshots/logs:
  - Not applicable; this task closes a stale planning slice, not a new UI implementation pass.
- High-risk checks:
  - No new CSS token layer, runtime behavior, or route-specific implementation was introduced.

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/planning/dashboard-foundation-and-personality-visual-system-plan.md`
  - `docs/ux/aion-visual-motif-system.md`
  - `docs/ux/design-memory.md`
  - `.codex/context/TASK_BOARD.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: not required for this sync slice

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference:
  - `docs/ux/assets/aion-visual-motif-reference.png`
  - `docs/ux/aion-visual-motif-system.md`
  - `docs/planning/dashboard-foundation-and-personality-visual-system-plan.md`
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - `--aion-*` CSS token family
  - `.aion-panel`, `.aion-panel-soft`, `.aion-panel-muted`
  - motif-led hero/stage classes
  - shared route hero and insight panel components
- New shared pattern introduced: no
- Design-memory entry reused:
  - Embodied cognition motif
  - Shared canonical persona figure
  - Flagship utility bar
  - Surface-first flagship closure
- Design-memory update required: no
- State checks: not applicable to planning-slice sync
- Responsive checks: desktop | tablet | mobile expectations already recorded in the planning contract
- Input-mode checks: not applicable to planning-slice sync
- Accessibility checks: no new UI surface changed
- Parity evidence:
  - Existing board entries record later screenshot-driven canonical route passes on top of these shared primitives.

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
- Reuse should happen through variants and shared primitives, not CSS copied per
  route.
- 2026-05-03 sync:
  - This task was stale in `READY`; the board already recorded
    `PRJ-724..PRJ-727` as complete locally.
  - Shared tokens and primitives exist in `web/src/index.css` and are reused by
    web shell components in `web/src/App.tsx`.
  - The recurring stale-task guardrail is already recorded in
    `.codex/context/LEARNING_JOURNAL.md`.

## Result Report
- Goal:
  - Close the stale shared-token and motif-infrastructure task without adding
    a second token system.
- Scope:
  - Task status synchronization and evidence capture only.
- Implementation Plan:
  - Verify the existing planning contract, task-board history, CSS token layer,
    and shared web components.
  - Mark PRJ-725 as complete with explicit evidence.
  - Update repository context so the next iteration can continue from the real
    queue state.
- Acceptance Criteria:
  - PRJ-725 is no longer a false `READY` item.
  - Evidence points to the existing shared token and surface infrastructure.
  - No new route-specific work or duplicate primitive layer is introduced.
- Definition of Done:
  - Satisfied with the manual checks and `git diff --check` evidence above.
- Result:
  - PRJ-725 is closed as a stale queue synchronization task.
- Next:
  - Review `PRJ-726` for stale READY/task-board drift before selecting new
    implementation work.
