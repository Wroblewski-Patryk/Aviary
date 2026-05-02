# Task

## Header
- ID: PRJ-885
- Title: Canonical UI Commit Scope Audit
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-884
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 885
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are represented.
- [x] No loop step was skipped.
- [x] Exactly one priority task was selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The canonical UI rollout now includes all primary authenticated module routes
and a final route sweep. The working tree contains tracked UI changes, many
untracked task records, and at least one unrelated untracked artifact.

## Goal
Record the exact commit candidate scope for the canonical UI package without
staging, committing, or pushing.

## Scope
- Audit:
  - tracked changed files
  - untracked task records
  - untracked artifacts that should stay out of the UI commit
- Files:
  - `.codex/tasks/PRJ-885-canonical-ui-commit-scope-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - staging
  - committing
  - pushing
  - changing production code

## Success Signal
- User or operator problem: the working tree is large enough that a blind commit
  could include unrelated artifacts.
- Expected product or reliability outcome: the next commit can stage the right
  canonical UI files deliberately.
- How success will be observed: audit lists include, exclude, and decision
  needed paths.
- Post-launch learning needed: no

## Deliverable For This Stage
A release-scope audit that identifies the canonical UI commit candidate and
exclusions.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Inspect tracked changed files.
2. Inspect untracked files.
3. Identify canonical UI candidate files.
4. Identify exclusions and separate-decision files.
5. Update task board and project state.

## Acceptance Criteria
- Tracked changed files are listed.
- Untracked task records are classified.
- Unrelated artifacts are excluded from the commit candidate.
- No staging, commit, or push is performed.

## Definition of Done
- [x] Tracked changed files recorded.
- [x] Untracked files recorded.
- [x] Commit candidate and exclusions recorded.
- [x] No git mutation was performed.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- staging without explicit user request
- committing without explicit user request
- pushing without explicit user request
- including unrelated artifacts silently

## Validation Evidence
- Tests:
  - `git diff --name-only`
  - `git ls-files --others --exclude-standard`
  - `git diff --stat -- web/src/App.tsx web/src/index.css .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
- Manual checks:
  - verified only four tracked files are modified
  - verified `.codex/artifacts/` screenshot evidence remains ignored
  - verified `artifacts/behavior_validation/prj843-report.json` is unrelated to
    the canonical UI commit candidate
- Screenshots/logs: not applicable
- High-risk checks:
  - no staging, commit, or push performed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Findings
- Tracked changed files:
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `web/src/App.tsx`
  - `web/src/index.css`
- Canonical UI task records to include for the current package:
  - `.codex/tasks/PRJ-864-dashboard-canonical-density-pass.md`
  - `.codex/tasks/PRJ-865-personality-canonical-first-viewport-pass.md`
  - `.codex/tasks/PRJ-866-landing-canonical-first-viewport-pass.md`
  - `.codex/tasks/PRJ-867-tools-canonical-shell-consistency-pass.md`
  - `.codex/tasks/PRJ-868-canonical-99-layout-foundation.md`
  - `.codex/tasks/PRJ-869-public-home-landing-99-pass.md`
  - `.codex/tasks/PRJ-870-dashboard-99-canonical-evidence-pass.md`
  - `.codex/tasks/PRJ-871-personality-99-canonical-pass.md`
  - `.codex/tasks/PRJ-872-chat-99-canonical-evidence-pass.md`
  - `.codex/tasks/PRJ-873-settings-canonical-shell-polish.md`
  - `.codex/tasks/PRJ-874-tools-canonical-directory-polish.md`
  - `.codex/tasks/PRJ-875-canonical-ui-final-route-sweep.md`
  - `.codex/tasks/PRJ-876-canonical-ui-commit-scope-audit.md`
  - `.codex/tasks/PRJ-877-memory-canonical-route.md`
  - `.codex/tasks/PRJ-878-reflections-canonical-route.md`
  - `.codex/tasks/PRJ-879-plans-canonical-route.md`
  - `.codex/tasks/PRJ-880-goals-canonical-route.md`
  - `.codex/tasks/PRJ-881-insights-canonical-route.md`
  - `.codex/tasks/PRJ-882-automations-canonical-route.md`
  - `.codex/tasks/PRJ-883-integrations-canonical-route.md`
  - `.codex/tasks/PRJ-884-canonical-route-final-sweep.md`
  - `.codex/tasks/PRJ-885-canonical-ui-commit-scope-audit.md`
- Separate inclusion decision:
  - `.codex/tasks/PRJ-851-publish-and-smoke-release-smoke-summary.md`
  - `.codex/tasks/PRJ-852-chat-canonical-97-parity-closure.md`
- Exclude from canonical UI commit candidate unless explicitly requested:
  - `artifacts/behavior_validation/prj843-report.json`

## Result Report

- Task summary: Recorded the canonical UI commit candidate and exclusions after
  the final route sweep.
- Files changed:
  - `.codex/tasks/PRJ-885-canonical-ui-commit-scope-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - git status and diff scope inspection
- What is incomplete:
  - no commit was created
- Next steps:
  - stage the canonical UI candidate deliberately when the user asks for commit
    and push.
- Decisions made:
  - exclude `artifacts/behavior_validation/prj843-report.json` from the UI
    commit candidate.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: large working tree with tracked UI files and many untracked records.
- Gaps: commit candidate needed refresh after PRJ-877 through PRJ-884.
- Inconsistencies: unrelated behavior validation artifact remains untracked.
- Architecture constraints: release audit only; no code change.

### 2. Select One Priority Task
- Selected task: PRJ-885 Canonical UI Commit Scope Audit.
- Priority rationale: staging discipline is the next release risk after route
  verification.
- Why other candidates were deferred: commit/push require explicit user request.

### 3. Plan Implementation
- Files or surfaces to modify: task and context docs.
- Logic: inspect git status and classify paths.
- Edge cases: old task files and unrelated artifacts.
- Validation path: git diff/status commands.

### 4. Execute Implementation
- Implementation notes:
  - collected tracked changed files
  - collected untracked files
  - classified include, separate-decision, and exclude paths

### 5. Verify and Test
- Validation performed: git status/diff scope inspection.
- Result: passed.

### 6. Self-Review
- Simpler option considered: stage everything after build.
- Technical debt introduced: no.
- Scalability assessment: audit makes the next commit safer.
- Refinements made: PRJ-851 and PRJ-852 left as explicit separate-decision
  files because they predate the current package.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-885-canonical-ui-commit-scope-audit.md`
- Context updated: `.codex/context/TASK_BOARD.md`,
  `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
