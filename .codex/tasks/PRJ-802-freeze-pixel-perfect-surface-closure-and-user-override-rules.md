# Task

## Header
- ID: PRJ-802
- Title: Freeze pixel-perfect surface-closure and user-override rules
- Task Type: docs
- Current Stage: verification
- Status: DONE
- Owner: Product Docs
- Depends on: PRJ-800M, PRJ-800F
- Priority: P1

## Context
Recent flagship UX/UI work proved that the main delivery problem is no longer
missing intent. The recurring drift came from process:

- too many surfaces were refined in parallel
- screenshot-driven parity was not used as a hard gate often enough
- canonical screenshots were sometimes treated as inspiration instead of a spec
- user-requested deviations from canonical assets were not yet captured as a
  durable rule for future slices

The repo now needs a stronger, written contract so future work closes one
surface at a time, targets a higher parity bar, and treats user notes on top of
canonical visuals as first-class specification input.

## Goal
Record a stricter pixel-perfect workflow for flagship UX/UI work, including:

- one-surface-at-a-time closure
- `95%` parity gate before moving to dependent surfaces
- canonical screenshot plus explicit user notes as the merged spec
- mandatory escalation when user notes contradict each other or the current
  canonical source

## Deliverable For This Stage
Updated repository instructions and UX workflow docs that define the stricter
surface-closure loop and the user-override decision rules, plus synced
source-of-truth context.

## Scope
- `AGENTS.md`
- `docs/ux/canonical-visual-implementation-workflow.md`
- `docs/ux/design-memory.md`
- `.codex/context/LEARNING_JOURNAL.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-802-freeze-pixel-perfect-surface-closure-and-user-override-rules.md`

## Implementation Plan
1. Tighten the UX/UI rules in repo instructions around one-surface closure and
   a `95%` parity gate.
2. Extend the canonical visual workflow with a stricter sequencing and quick
   screenshot-check loop.
3. Record the approved interpretation rule that canonical assets may be
   intentionally overridden by explicit user notes.
4. Record the recurring pitfall in the learning journal so future slices do not
   reintroduce parallel-surface drift.
5. Sync task board and project state with the new process contract.
6. Run focused documentation validation and close the task.

## Acceptance Criteria
- Repo instructions explicitly require finishing one flagship surface before
  moving to the next dependent surface.
- The canonical workflow explicitly uses a `95%` parity threshold before
  progressing.
- The docs explicitly state that canonical assets plus explicit user notes form
  the active spec.
- The docs explicitly require stopping for user decision when those notes are
  contradictory.
- Context files and learning journal are updated in the same slice.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new operational systems or tooling in this slice
- do not change runtime behavior
- keep repository artifacts in English

## Definition of Done
- [x] The stronger flagship UX/UI workflow is recorded in canonical docs.
- [x] User-override interpretation rules are recorded.
- [x] The recurring process pitfall is captured in the learning journal.
- [x] Task board and project state are updated.
- [x] Focused validation passes.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new runtime systems without approval
- fake completion without updating repository truth
- replacing canonical screenshots with looser verbal descriptions
- treating contradictory user notes as silently mergeable

## Validation Evidence
- Tests:
  - `git diff --check -- AGENTS.md docs/ux/canonical-visual-implementation-workflow.md docs/ux/design-memory.md .codex/context/LEARNING_JOURNAL.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md .codex/tasks/PRJ-802-freeze-pixel-perfect-surface-closure-and-user-override-rules.md`
- Manual checks:
  - verified that the new rules encode `one surface at a time`
  - verified that `95%` is the explicit progression threshold
  - verified that explicit user notes can override a canonical screenshot only
    as an approved interpretation layer
- Screenshots/logs:
  - not applicable

## Result Report
- Task summary:
  - froze a stricter flagship UX/UI workflow around one-surface closure,
    `95%` parity gates, and canonical-spec-plus-user-override interpretation
- Files changed:
  - `AGENTS.md`
  - `docs/ux/canonical-visual-implementation-workflow.md`
  - `docs/ux/design-memory.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-802-freeze-pixel-perfect-surface-closure-and-user-override-rules.md`
- How tested:
  - focused `git diff --check`
- What is incomplete:
  - none
- Next steps:
  - use this stricter workflow for the next flagship surface closure loop
