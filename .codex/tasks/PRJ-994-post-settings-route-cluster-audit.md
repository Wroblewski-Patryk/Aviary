# Task

## Header
- ID: PRJ-994
- Title: Re-audit next route-local extraction target after settings cleanup
- Task Type: documentation
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-993
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 994
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

Tools and settings now have clearer component/helper ownership. The next route
extraction target should be selected from the current `App.tsx` state.

## Goal

Re-audit remaining route-local clusters and select the next smallest
behavior-preserving extraction target.

## Scope

- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: next route refactor could drift toward a broad UI
  rewrite.
- Expected product or reliability outcome: the next implementation task is
  small, code-grounded, and traceable.
- How success will be observed: audit names the next task and rationale.
- Post-launch learning needed: no

## Deliverable For This Stage

Update the route cluster audit and roadmap after settings cleanup.

## Constraints
- base the audit on current `web/src/App.tsx`
- do not change runtime code in this task
- do not pick chat/dashboard as the next target unless their higher risk is
  explicitly justified

## Implementation Plan
1. Re-read route branches and helper clusters after settings extraction.
2. Compare remaining route-local clusters by behavior and visual risk.
3. Select the next implementation task.
4. Update audit, roadmap, task board, and project state.
5. Run `git diff --check`.

## Acceptance Criteria
- Audit reflects settings helper extraction.
- Next implementation task is selected.
- `git diff --check` passes.

## Definition of Done
- [x] Audit updated.
- [x] Roadmap and context updated.
- [x] Diff validation completed.

## Validation Evidence
- Tests:
  - `git diff --check`
  - result: passed
- Manual checks:
  - confirmed current route branch anchors in `web/src/App.tsx`
- High-risk checks:
  - no runtime code changed
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
  - roadmap now names the next module route side-panel extraction

## UX/UI Evidence
- Design source type: not applicable
- Design source reference: no UI code changed
- Canonical visual target: unchanged
- Fidelity target: not applicable
- Remaining mismatches: dashboard/chat remain high-risk route-local branches
- State checks: not applicable
- Responsive checks: not applicable
- Accessibility checks: not applicable
- Parity evidence: not applicable

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Rollback note: revert audit/planning/context doc updates
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

- Task summary: selected module route side-panel extraction as the next slice.
- Files changed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - PRJ-995 implementation remains next
- Next steps:
  - extract shared module route side panel/row presentation for insights and
    automations
- Decisions made:
  - defer chat/dashboard because they carry higher behavior/visual parity risk

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: remaining route-local clusters need a next target after settings.
- Gaps: module side panels still repeat similar chrome.
- Inconsistencies: tools/settings ownership is clearer than module routes.
- Architecture constraints: keep slices small and behavior-preserving.

### 2. Select One Priority Task
- Selected task: PRJ-994 post-settings route cluster audit.
- Priority rationale: prevent next extraction from becoming a broad rewrite.
- Why other candidates were deferred: implementation follows the audit.

### 3. Plan Implementation
- Files or surfaces to modify: docs/context only.
- Logic: compare route branch risk and select the next slice.
- Edge cases: avoid overclaiming parity because no UI code changes.

### 4. Execute Implementation
- Implementation notes: selected insights/automations side panel row extraction.

### 5. Verify and Test
- Validation performed: `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: continue directly into integrations.
- Technical debt introduced: no
- Scalability assessment: audit keeps route extraction queue grounded.
- Refinements made: selected side panels because they are less risky than chat
  transcript or dashboard visuals.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
