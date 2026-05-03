# Task

## Header
- ID: PRJ-1123
- Title: Audit current workspace candidate scope before commit and PRJ-952
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1122
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1123
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

PRJ-1122 proved the current workspace validates locally. PRJ-952 still requires
a selected pushed SHA before deploy parity can be recovered. The next local
step is to classify the candidate scope and exclude local artifacts.

## Goal

Record the current workspace candidate scope, including files to include in a
future commit and local evidence/artifacts to exclude.

## Scope

- `.codex/tasks/PRJ-1123-current-workspace-candidate-scope-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/current-workspace-candidate-scope-audit.md`
- `docs/README.md`

## Success Signal
- User or operator problem: a commit/push handoff can accidentally include
  generated evidence files or miss new characterization scripts.
- Expected product or reliability outcome: candidate packaging has a clear
  include/exclude list.
- How success will be observed: docs list tracked changes, new task records,
  new web scripts, and excluded local artifact folders.
- Post-launch learning needed: no

## Deliverable For This Stage

A current candidate scope audit with include/exclude guidance.

## Constraints
- do not commit, stage, push, deploy, or trigger fallback in this task
- preserve existing repository structure policy
- include new source/test scripts needed by validation
- exclude generated `.codex/tmp/` and `artifacts/` unless a separate
  artifact-retention decision is made

## Implementation Plan
1. Inspect `git status`, tracked diff names/stats, untracked files, and local
   artifact folders.
2. Create a current candidate scope audit under `docs/planning/`.
3. Update `docs/README.md` discoverability.
4. Update task board and project state.
5. Run `git diff --check`.

## Acceptance Criteria
- Include scope is explicit.
- Excluded artifact scope is explicit.
- Commit readiness caveat is explicit.
- Docs/context are synchronized.

## Definition of Done
- [x] Candidate scope audited.
- [x] Include/exclude list recorded.
- [x] Docs/context updated.
- [x] `git diff --check` passes.
- [x] No commit, push, deploy, or fallback trigger executed.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated release processes
- temporary bypasses or workaround-only paths
- architecture changes without explicit approval
- sweeping generated evidence artifacts into release scope silently

## Validation Evidence
- Tests:
  - PRJ-1122 validation remains current:
    - backend `1045 passed`
    - web build passed
    - tools/chat characterization passed
    - route smoke passed with `route_count=14`
- Manual checks:
  - `git status --short --branch`
  - `git diff --name-status`
  - `git diff --stat`
  - `git ls-files --others --exclude-standard`
  - `.codex/tmp` and `artifacts` listings inspected
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - no commit, push, deploy, or fallback trigger was executed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/governance/repository-structure-policy.md`
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/operations/release-evidence-index.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: current candidate scope audit added under
  `docs/planning/` and indexed in `docs/README.md`

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: not applicable; docs-only packaging audit
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
- [x] Learning journal was updated if a recurring pitfall is confirmed.

## Notes

Scope audit only. Candidate packaging still requires an explicit commit/push
step.

## Production-Grade Required Contract

- Goal: audit current workspace candidate scope before commit and PRJ-952.
- Scope: scope audit doc and context.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: complete.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: PRJ-1122 frontend characterization evidence
- Error state verified: PRJ-1122 frontend characterization evidence
- Refresh/restart behavior verified: PRJ-1122 route smoke
- Regression check performed: `git diff --check`

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator and future agents
- Existing workaround or pain: dirty workspace can accidentally package
  generated evidence or omit source/test scripts.
- Smallest useful slice: docs-only scope audit.
- Success metric or signal: include/exclude list is explicit.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: candidate packaging
- SLI: candidate scope truthfulness
- SLO: no deploy handoff without explicit include/exclude list
- Error budget posture: not applicable
- Health/readiness check: PRJ-1122 local validation
- Logs, dashboard, or alert route: docs diff
- Smoke command or manual smoke: PRJ-1122 route smoke
- Rollback or disable path: exclude local artifacts unless separately approved

## AI Testing Evidence

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: release metadata and local artifact inventory
- Trust boundaries: local repo packaging
- Permission or ownership checks: not applicable
- Abuse cases: committing local logs/evidence artifacts by accident
- Secret handling: no secrets inspected or written
- Security tests or scans: not applicable
- Fail-closed behavior: generated artifacts remain excluded by default
- Residual risk: human/operator must still approve commit/push scope

## Result Report

- Task summary: audited current workspace candidate scope.
- Files changed:
  - `.codex/tasks/PRJ-1123-current-workspace-candidate-scope-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/planning/current-workspace-candidate-scope-audit.md`
  - `docs/README.md`
- How tested:
  - status/diff/untracked inventory
  - `git diff --check`
- What is incomplete:
  - candidate has not been committed, pushed, deployed, or smoke-tested in
    production.
- Next steps:
  - create an explicit candidate commit/push from the included scope, excluding
    local artifacts, then resolve PRJ-952.
- Decisions made:
  - include new task records and web characterization scripts
  - exclude `.codex/tmp/` and `artifacts/` by default

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dirty workspace contains source/docs/context changes plus local
  artifacts.
- Gaps: no current include/exclude scope audit after PRJ-1122 validation.
- Inconsistencies: validation is green but candidate SHA is not frozen.
- Architecture constraints: release scope must be explicit before deploy.

### 2. Select One Priority Task
- Selected task: PRJ-1123 current workspace candidate scope audit.
- Priority rationale: it is the next local prerequisite before commit/push and
  PRJ-952.
- Why other candidates were deferred: deploy requires external source
  automation or operator fallback inputs.

### 3. Plan Implementation
- Files or surfaces to modify: planning docs and context.
- Logic: classify include/exclude scope from git status and artifact listings.
- Edge cases: untracked generated artifacts must not be swept into commit.

### 4. Execute Implementation
- Implementation notes: added a current candidate scope audit under
  `docs/planning/` and indexed it.

### 5. Verify and Test
- Validation performed: status/diff inventory and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: proceed straight to commit.
- Technical debt introduced: no
- Scalability assessment: the scope audit gives future commits a reusable
  package checklist.
- Refinements made: explicit artifact exclusions added.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/planning/current-workspace-candidate-scope-audit.md`
  - `docs/README.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
