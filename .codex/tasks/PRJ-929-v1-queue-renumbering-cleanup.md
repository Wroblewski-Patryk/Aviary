# Task

## Header
- ID: PRJ-929
- Title: V1 Queue Renumbering Cleanup
- Task Type: planning
- Current Stage: verification
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-922
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 929
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-922` is now the completed production-safe incident-evidence export task.
The older release execution plan still reserved `PRJ-922` for Deployment
Trigger SLO Evidence, which creates a duplicate identifier before final v1
execution continues.

## Goal
Remove duplicate v1 task IDs and make the remaining final-release queue
unambiguous.

## Scope
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-929-v1-queue-renumbering-cleanup.md`

## Success Signal
- User or operator problem: future v1 work can be executed by task ID without
  ambiguity.
- Expected product or reliability outcome: PRJ-922 stays tied to its completed
  strict export evidence, and future hardening tasks use free IDs.
- How success will be observed: the planning document has no duplicate PRJ-922
  future task.
- Post-launch learning needed: no

## Deliverable For This Stage
Updated source-of-truth queue with unique task IDs.

## Constraints
- do not rename completed task files
- do not change completed evidence
- do not start implementation of the next release gate in this task
- keep the release sequence intact

## Implementation Plan
1. Move the old future Deployment Trigger SLO Evidence slot from `PRJ-922` to
   a free post-cleanup ID.
2. Shift subsequent AI/security/final-release task IDs so each planned task is
   unique.
3. Record the cleanup in task board and project state.
4. Validate with text search and `git diff --check`.

## Acceptance Criteria
- `PRJ-922` appears only as the completed production-safe export task.
- Future tasks use unique IDs.
- The priority queue matches the phase task list.
- No implementation behavior changes are made.

## Definition of Done
- [x] Planning queue is renumbered.
- [x] Context docs are updated.
- [x] Search confirms no duplicate future `PRJ-922` task remains.
- [x] `git diff --check` passes.

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
- Tests: not applicable; planning-only change
- Manual checks:
  - searched planning/context files for `PRJ-922`
  - confirmed future Deployment Trigger SLO Evidence is no longer `PRJ-922`
- Screenshots/logs: not applicable
- High-risk checks: no secrets or generated artifacts touched
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `.codex/context/TASK_BOARD.md`
- Fits approved architecture: yes
- Mismatch discovered: duplicate future task ID
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert the planning/context cleanup commit
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

- Task summary: removed duplicate future v1 task IDs after PRJ-922 was used for
  production-safe incident evidence export.
- Files changed:
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-929-v1-queue-renumbering-cleanup.md`
- How tested: text search and `git diff --check`.
- What is incomplete: next release gate execution remains queued.
- Next steps: run final v1 acceptance refresh.
- Decisions made: keep completed PRJ-922 unchanged and move future planned IDs.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `PRJ-922` had both a completed task and a future planned task.
- Gaps: final v1 execution needed an unambiguous queue.
- Inconsistencies: phase list and priority queue conflicted with completed
  PRJ-922.
- Architecture constraints: source-of-truth docs must drive execution.

### 2. Select One Priority Task
- Selected task: PRJ-929 V1 Queue Renumbering Cleanup.
- Priority rationale: ID ambiguity blocks reliable autonomous execution.
- Why other candidates were deferred: final acceptance refresh depends on a
  clean queue.

### 3. Plan Implementation
- Files or surfaces to modify: planning/context docs and task record.
- Logic: preserve completed IDs and shift only future planned IDs.
- Edge cases: references to completed PRJ-922 must stay unchanged.
- Validation: search and diff check.

### 4. Execute Implementation
- Added this task record.
- Renumbered future v1 hardening/final declaration tasks.
- Updated context docs.

### 5. Verify And Test
- Search confirmed `PRJ-922` is no longer assigned to a future task.
- `git diff --check` passed.

### 6. Self-Review
- Architecture alignment: yes.
- Existing system reuse: yes, planning docs and task board only.
- Workaround check: this is source-of-truth correction, not a bypass.
- Duplication check: duplicate task ID removed.

### 7. Update Documentation And Knowledge
- Updated task board, project state, and release execution plan.
- Learning journal update: not required; one-off planning drift.
