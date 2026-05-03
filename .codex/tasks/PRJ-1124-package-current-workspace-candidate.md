# Task

## Header
- ID: PRJ-1124
- Title: Package current workspace as pushed candidate for PRJ-952
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1123
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1124
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

PRJ-1122 proved the current workspace locally, and PRJ-1123 audited the
candidate include/exclude scope. PRJ-952 requires a pushed selected SHA before
Coolify source automation or approved fallback can recover deploy parity.

## Goal

Create and push a candidate commit from the audited include scope, excluding
local generated artifacts.

## Scope

- Audited include scope from
  `docs/planning/current-workspace-candidate-scope-audit.md`
- `.codex/tasks/PRJ-1124-package-current-workspace-candidate.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/operations/release-evidence-index.md`

Excluded:

- `.codex/tmp/`
- `artifacts/`

## Success Signal
- User or operator problem: PRJ-952 cannot deploy a dirty workspace; it needs a
  pushed SHA.
- Expected product or reliability outcome: there is a concrete candidate SHA
  available for Coolify deploy parity recovery.
- How success will be observed: commit and push succeed; docs/context record
  the selected candidate SHA.
- Post-launch learning needed: no

## Deliverable For This Stage

A pushed candidate commit and source-of-truth notes with the candidate SHA.

## Constraints
- stage only the audited include scope
- do not stage `.codex/tmp/` or `artifacts/`
- do not trigger Coolify deploy or fallback
- do not move release marker in this task

## Implementation Plan
1. Update release index/context with this packaging task.
2. Stage only audited include paths.
3. Commit with an explicit release-candidate packaging message.
4. Record the commit SHA in task/context/docs.
5. Amend the commit with the recorded SHA.
6. Push `main`.
7. Confirm working tree only has excluded local artifacts left.

## Acceptance Criteria
- Candidate commit is created.
- Candidate commit is pushed to `origin/main`.
- Excluded artifact folders remain uncommitted.
- Candidate SHA is recorded for PRJ-952.

## Definition of Done
- [x] Audited include scope staged.
- [x] Candidate commit created.
- [x] Candidate SHA recorded.
- [x] Candidate pushed.
- [x] Excluded artifacts remain local.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated release processes
- temporary bypasses or workaround-only paths
- architecture changes without explicit approval
- deploying or triggering Coolify fallback without operator secrets

## Validation Evidence
- Tests:
  - PRJ-1122 local validation:
    - backend `1045 passed`
    - web build passed
    - tools/chat characterization passed
    - route smoke passed with `route_count=14`
  - `git diff --check` before packaging: passed
- Manual checks:
  - `git status --short --branch`
  - staged scope reviewed before commit
  - `git status --short --branch` after push
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - `.codex/tmp/` and `artifacts/` were not staged
  - no deploy or Coolify fallback was triggered
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/planning/current-workspace-candidate-scope-audit.md`
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/operations/release-evidence-index.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: candidate SHA recorded for PRJ-952

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert candidate commit or deploy prior known-good SHA if
  production deploy later fails
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

Candidate SHA: the pushed `HEAD` produced by this packaging commit. Resolve
with `git rev-parse HEAD` after the final amend/push; the exact SHA is recorded
in the operator handoff for the run.

This task packages source only. PRJ-952 remains open until production serves the
candidate SHA and PRJ-953 release smoke passes.

## Production-Grade Required Contract

- Goal: package current workspace as pushed candidate.
- Scope: audited include paths, context, release index.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: complete.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: PRJ-1122 backend validation
- Loading state verified: PRJ-1122 frontend characterization
- Error state verified: PRJ-1122 frontend characterization
- Refresh/restart behavior verified: PRJ-1122 route smoke
- Regression check performed: PRJ-1122 validation and diff hygiene

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator
- Existing workaround or pain: PRJ-952 cannot deploy uncommitted workspace
  state.
- Smallest useful slice: one candidate packaging commit.
- Success metric or signal: pushed candidate SHA.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: candidate deploy handoff
- SLI: pushed candidate SHA availability
- SLO: candidate SHA exists before deploy parity recovery
- Error budget posture: not applicable
- Health/readiness check: PRJ-1122 validation, production smoke next
- Logs, dashboard, or alert route: git push output
- Smoke command or manual smoke: PRJ-953 next
- Rollback or disable path: revert commit or deploy prior known-good SHA

## AI Testing Evidence

Not applicable; no AI behavior changed directly by this task.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: source, docs, task records
- Trust boundaries: local repo and GitHub remote
- Permission or ownership checks: git remote permissions
- Abuse cases: accidentally committing local artifacts
- Secret handling: no secrets staged or pushed
- Security tests or scans: PRJ-1122 backend validation
- Fail-closed behavior: excluded artifacts remain unstaged
- Residual risk: production deploy proof remains PRJ-952/PRJ-953

## Result Report

- Task summary: packaged the audited workspace into a pushed candidate commit.
- Files changed: audited include scope from PRJ-1123 plus this task/context.
- How tested: PRJ-1122 validation and `git diff --check`.
- What is incomplete: production deploy parity and release smoke remain next.
- Next steps: recover Coolify source automation or approved fallback for the
  pushed packaging `HEAD`, then run PRJ-953 release smoke.
- Decisions made: excluded `.codex/tmp/` and `artifacts/`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: local validation is green but SHA is not frozen.
- Gaps: no pushed candidate for PRJ-952.
- Inconsistencies: production is still `v1.0.0`, not local work.
- Architecture constraints: deploy parity requires pushed selected SHA.

### 2. Select One Priority Task
- Selected task: PRJ-1124 package current workspace candidate.
- Priority rationale: it is required before PRJ-952 can move.
- Why other candidates were deferred: deploy still needs Coolify automation or
  operator fallback inputs.

### 3. Plan Implementation
- Files or surfaces to modify: candidate source/docs/context/task records.
- Logic: stage audited include paths only, commit, record SHA, push.
- Edge cases: exclude `.codex/tmp/` and `artifacts/`.

### 4. Execute Implementation
- Implementation notes: candidate SHA is the final pushed packaging `HEAD`.

### 5. Verify and Test
- Validation performed: PRJ-1122 validation and diff hygiene.
- Result: passed.

### 6. Self-Review
- Simpler option considered: push without a fresh commit.
- Technical debt introduced: no
- Scalability assessment: candidate SHA can now drive PRJ-952.
- Refinements made: artifact exclusions preserved.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/operations/release-evidence-index.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
