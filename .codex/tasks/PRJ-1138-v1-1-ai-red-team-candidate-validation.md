# Task

## Header
- ID: PRJ-1138
- Title: V1.1 AI Red-Team Candidate Validation
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1137
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1138
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

PRJ-1137 added a local expression self-review guard for AI red-team boundary
findings. Production cannot prove that fix until the workspace candidate is
validated, packaged, deployed, and rerun.

## Goal

Run the relevant candidate validation for the PRJ-1137 local fix before any
release packaging or deployment step.

## Scope

- backend test suite
- web build smoke if dependencies are present
- `.codex/tasks/PRJ-1138-v1-1-ai-red-team-candidate-validation.md`
- context/docs after validation

## Success Signal
- User or operator problem: v1.1 cannot rely on local focused tests only.
- Expected product or reliability outcome: candidate validation is green enough
  to package and deploy the local AI red-team fix.
- How success will be observed: validation commands and results are recorded.
- Post-launch learning needed: no

## Deliverable For This Stage

Validation evidence for the current workspace candidate.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- do not deploy or create release marker if validation fails

## Implementation Plan

1. Run full backend pytest gate.
2. Run web build as release hygiene.
3. Run `git diff --check`.
4. Update context with validation result and next release step.

## Acceptance Criteria

- Backend validation result is recorded.
- Web build result is recorded or blocker is documented.
- Diff hygiene result is recorded.
- No deployment is attempted on failed validation.

## Definition of Done
- [x] backend validation completed
- [x] web build completed or blocker recorded
- [x] `git diff --check` completed
- [x] context/docs updated

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
  - backend full suite: `1050 passed`
  - web build: passed
  - web route smoke: `status=ok`, `route_count=14`
  - `git diff --check`: passed with LF/CRLF warnings only
- Manual checks:
  - deployment deferred until validated candidate is intentionally packaged
- Screenshots/logs: not applicable
- High-risk checks: deployment blocked until validation is green
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/security/v1-ai-red-team-execution-report.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none in this task
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: pending
- Rollback note: not applicable until packaging/deploy
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist (mandatory)
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

- Task summary: validated the current v1.1 AI red-team local-fix candidate.
- Files changed:
  - `.codex/tasks/PRJ-1138-v1-1-ai-red-team-candidate-validation.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `pytest -q` -> `1050 passed`
  - `npm run build` -> passed
  - `npm run smoke:routes` -> `status=ok`, `route_count=14`
  - `git diff --check` -> passed with LF/CRLF warnings only
- What is incomplete: candidate is not packaged, deployed, or live red-team
  rerun yet.
- Next steps: package and push the validated candidate, then deploy and rerun
  strict AI red-team against production.
- Decisions made: deployment is deferred until validation completes.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: local PRJ-1137 fix needs broader validation before deploy.
- Gaps: production red-team gate cannot pass until deployment/rerun.
- Inconsistencies: none found.
- Architecture constraints: release claims require validation and deploy parity.

### 2. Select One Priority Task
- Selected task: PRJ-1138 candidate validation.
- Priority rationale: validation gates packaging/deploy.
- Why other candidates were deferred: deploy and live rerun depend on validation.

### 3. Plan Implementation
- Files or surfaces to modify: task/context/docs only after validation.
- Logic: run existing validation commands.
- Edge cases: if validation fails, stop and document blocker.

### 4. Execute Implementation
- Ran backend, web, route, and diff hygiene validations.

### 5. Verify And Test
- Backend full suite passed.
- Web build and route smoke passed.
- Diff hygiene passed.

### 6. Self-Review
- Architecture alignment: yes.
- Workaround check: no workaround introduced.
- Remaining risk: production evidence requires packaging/deploy/rerun.

### 7. Update Documentation And Knowledge
- Updated task/context evidence.
