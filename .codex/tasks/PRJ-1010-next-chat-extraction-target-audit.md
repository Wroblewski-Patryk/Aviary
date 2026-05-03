# Task

## Header
- ID: PRJ-1010
- Title: Audit next chat extraction target after cognitive belt cleanup
- Task Type: documentation
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1009
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1010
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

After cognitive belt cleanup, remaining inline chat presentation includes the
topbar, transcript shell/container, and portrait/support panel.

## Goal

Choose the next safe chat extraction target with visual/ref risk documented.

## Scope

- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: the next chat extraction target could drift into
  visual-heavy or ref-sensitive work.
- Expected product or reliability outcome: next implementation slice is small
  and low-risk.
- How success will be observed: PRJ-1011 is queued with a topbar-only boundary.
- Post-launch learning needed: no

## Deliverable For This Stage

Record that chat topbar extraction is next and defer portrait/support panel and
transcript shell.

## Constraints
- do not change runtime code in this task
- do not touch portrait/support panel before visual-specific audit
- do not touch transcript shell/container before ref/loading ownership audit

## Implementation Plan
1. Inspect topbar, portrait/support panel, and transcript shell clusters.
2. Select the lowest-risk next target.
3. Update route audit, roadmap, and context.
4. Run `git diff --check`.

## Acceptance Criteria
- Next target is selected and documented.
- Deferred targets are named with rationale.
- PRJ-1011 is queued.
- `git diff --check` passes.

## Definition of Done
- [x] Boundary recorded.
- [x] Roadmap and context updated.
- [x] Diff validation completed.

## Validation Evidence
- Tests:
  - `git diff --check`
  - result: passed
- Manual checks:
  - inspected chat topbar, transcript shell, and portrait/support panel
- High-risk checks:
  - portrait/support panel and transcript shell explicitly deferred
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - PRJ-1011 queued for topbar extraction

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

- Task summary: selected chat topbar extraction as the next safe chat route
  presentation slice.
- Files changed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-1010-next-chat-extraction-target-audit.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - implementation is queued as PRJ-1011
- Next steps:
  - extract `ChatTopbar`
- Decisions made:
  - topbar is lower risk than portrait/support panel and transcript shell

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - topbar remains inline
- Gaps:
  - portrait/support panel and transcript shell still need future audits
- Inconsistencies:
  - PRJ-1010 needed to choose between remaining chat clusters
- Architecture constraints:
  - preserve canonical chat layout and avoid ref-sensitive movement

### 2. Select One Priority Task
- Selected task: PRJ-1010
- Priority rationale: it is the next queued chat route architecture step
- Why other candidates were deferred:
  - portrait/support panel is visually sensitive
  - transcript shell owns loading state and refs

### 3. Plan Implementation
- Files or surfaces to modify:
  - docs and context only
- Logic:
  - queue a small topbar component extraction
- Edge cases:
  - preferred-language display should be passed as a precomputed label

### 4. Execute Implementation
- Implementation notes:
  - queued PRJ-1011 for `ChatTopbar`

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - extract topbar immediately; deferred to keep audit and implementation separate
- Technical debt introduced: no
- Scalability assessment:
  - adequate for one more small chat route extraction
- Refinements made:
  - deferred risky visual/ref clusters explicitly

### 7. Update Documentation and Knowledge
- Docs updated:
  - frontend route cluster audit
  - v1 roadmap
- Context updated:
  - task board
  - project state
- Learning journal updated: not applicable
