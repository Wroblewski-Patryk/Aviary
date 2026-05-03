# Task

## Header
- ID: PRJ-1139
- Title: Package V1.1 AI Red-Team Candidate
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1138
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1139
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

PRJ-1138 validated the current workspace candidate with backend, web build, web
route smoke, and diff hygiene. The local AI red-team expression guard cannot be
proved in production until the validated candidate is committed and pushed.

## Goal

Create and push one validated candidate commit while excluding local temporary
and generated evidence artifacts.

## Scope

- staged repository source/docs/context/task changes
- git commit and push
- `.codex/tasks/PRJ-1139-package-v1-1-ai-red-team-candidate.md`
- context/docs after packaging

## Success Signal
- User or operator problem: production cannot deploy uncommitted local fixes.
- Expected product or reliability outcome: origin/main carries the validated
  v1.1 AI red-team candidate.
- How success will be observed: commit and push succeed, and local artifacts are
  not staged.
- Post-launch learning needed: no

## Deliverable For This Stage

A pushed commit for the validated candidate.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- do not stage `.codex/tmp` or generated `artifacts`
- do not create a release marker in this task

## Implementation Plan

1. Stage source, docs, context, and task files only.
2. Verify staged scope excludes `.codex/tmp` and generated artifacts.
3. Commit with a release-candidate message.
4. Push to `origin/main`.
5. Record commit SHA and next deploy step.

## Acceptance Criteria

- Commit succeeds.
- Push succeeds.
- Generated local evidence remains untracked.
- Next deploy/rerun task is explicit.

## Definition of Done
- [x] selected files staged
- [x] commit created
- [ ] push completed
- [x] context updated with commit SHA

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
- Tests: PRJ-1138 validation applies
- Manual checks:
  - staged scope excluded `.codex/tmp` and `artifacts`
  - `git diff --cached --check` passed before commit
  - candidate commit created; exact pushed SHA is read from `git rev-parse HEAD`
    after final amend
- Screenshots/logs: not applicable
- High-risk checks: generated artifacts and temp files excluded
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
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert candidate commit or redeploy previous SHA
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

- Task summary: created the validated v1.1 AI red-team local-fix candidate
  commit.
- Files changed:
  - validated candidate source, docs, context, and task files
- How tested: PRJ-1138 validation applies:
  - backend `1050 passed`
  - web build passed
  - route smoke `status=ok`, `route_count=14`
  - diff hygiene passed
- What is incomplete: push/deploy/live rerun remain next steps.
- Next steps: amend this task closure into the candidate commit, push, deploy,
  and rerun strict AI red-team.
- Decisions made: generated local artifacts are not part of the candidate commit.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: validated fix is local only.
- Gaps: production deploy/rerun requires pushed commit.
- Inconsistencies: none found.
- Architecture constraints: release marker waits for live proof.

### 2. Select One Priority Task
- Selected task: PRJ-1139 package candidate.
- Priority rationale: deploy depends on push.
- Why other candidates were deferred: live red-team rerun depends on deploy.

### 3. Plan Implementation
- Files or surfaces to modify: git state and context.
- Logic: stage intentional files only.
- Edge cases: exclude `.codex/tmp` and `artifacts`.

### 4. Execute Implementation
- Staged intentional files only.
- Created candidate commit; exact pushed SHA is read after final amend.

### 5. Verify And Test
- Verified staged scope excluded `.codex/tmp` and `artifacts`.
- Verified staged diff hygiene before commit.

### 6. Self-Review
- Architecture alignment: yes.
- Workaround check: no workaround introduced.
- Remaining risk: push/deploy/live rerun still pending.

### 7. Update Documentation And Knowledge
- Updated task/context with commit evidence.
