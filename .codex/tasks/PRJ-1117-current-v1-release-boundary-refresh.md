# Task

## Header
- ID: PRJ-1117
- Title: Refresh current v1 release boundary after v1.0.0 and PRJ-1115 evidence
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1116
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1117
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`docs/planning/current-v1-release-boundary.md` still names the pre-release
execution order (`PRJ-904` through `PRJ-910`) even though `v1.0.0` has been
created and PRJ-1115 refreshed the current deploy-parity state.

## Goal

Refresh the current v1 release boundary so future agents understand that
`v1.0.0` is the released core marker, while new local work needs a new selected
candidate, deploy parity, and release smoke.

## Scope

- `.codex/tasks/PRJ-1117-current-v1-release-boundary-refresh.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/current-v1-release-boundary.md`

## Success Signal
- User or operator problem: stale next-execution order can restart already
  closed release tasks.
- Expected product or reliability outcome: release-boundary doc points to the
  current post-v1 candidate path.
- How success will be observed: the doc separates released `v1.0.0` truth from
  future candidate requirements.
- Post-launch learning needed: no

## Deliverable For This Stage

A docs-only release-boundary refresh plus context updates.

## Constraints
- use existing release evidence and docs
- do not change the core v1 architecture gates
- do not claim local `HEAD` is deployed
- do not add a new release process

## Implementation Plan
1. Update the release-boundary date and status.
2. Add the released `v1.0.0` marker and current local `HEAD` caveat.
3. Replace stale next-execution order with current post-v1 release path.
4. Update task board and project state.
5. Run `git diff --check`.

## Acceptance Criteria
- `v1.0.0` selected SHA is documented as released core marker.
- Local `HEAD` remains explicitly not release-eligible without deploy parity.
- The next execution order no longer points at closed pre-release tasks.
- Docs/context are synchronized.

## Definition of Done
- [x] Release boundary doc refreshed.
- [x] Context updated.
- [x] `git diff --check` passes.
- [x] No release process or architecture change was introduced.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated release processes
- temporary bypasses or workaround-only paths
- architecture changes without explicit approval
- deleting current v1 core gate definitions

## Validation Evidence
- Tests:
  - not applicable; docs-only release-boundary refresh
- Manual checks:
  - reviewed `docs/planning/current-v1-release-boundary.md` after edit
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - no deploy, smoke, marker, release process, or architecture gate changed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: release-boundary doc now points to the
  current post-v1 candidate path

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert docs/context update
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was selected in this iteration.
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

## Notes

Docs-only release-boundary refresh. No runtime or deployment action.

## Production-Grade Required Contract

- Goal: refresh the current v1 release boundary after `v1.0.0`.
- Scope: release-boundary doc and context.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: complete.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: `git diff --check`

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator and future agents
- Existing workaround or pain: stale release order can reopen completed work.
- Smallest useful slice: update one release-boundary doc.
- Success metric or signal: current post-v1 execution order is explicit.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: release planning
- SLI: release-boundary accuracy
- SLO: future candidates require deploy parity before release claim
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: docs diff
- Smoke command or manual smoke: not applicable
- Rollback or disable path: revert docs/context update

## AI Testing Evidence

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: release metadata only
- Trust boundaries: docs-only
- Permission or ownership checks: not applicable
- Abuse cases: false release claim from stale release-boundary instructions
- Secret handling: no secrets
- Security tests or scans: not applicable
- Fail-closed behavior: release-boundary doc points to deploy parity gates
- Residual risk: external deploy proof remains operator-owned

## Result Report

- Task summary: refreshed current v1 release boundary after `v1.0.0` and
  PRJ-1115 evidence.
- Files changed:
  - `.codex/tasks/PRJ-1117-current-v1-release-boundary-refresh.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/planning/current-v1-release-boundary.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - external deploy parity remains blocked by PRJ-952.
- Next steps:
  - recover Coolify source automation or provide approved fallback webhook
    inputs, then run production release smoke for a selected SHA.
- Decisions made:
  - keep core v1 gates unchanged while replacing stale pre-release task order
    with the current post-v1 candidate path.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: release-boundary doc has stale pre-release task order.
- Gaps: post-v1 candidate path is not explicit there.
- Inconsistencies: `v1.0.0` exists but boundary still names pre-tag tasks.
- Architecture constraints: keep core v1 gates unchanged.

### 2. Select One Priority Task
- Selected task: PRJ-1117 current v1 release-boundary refresh.
- Priority rationale: release truth is the active v1 blocker surface.
- Why other candidates were deferred: deploy parity still needs external action.

### 3. Plan Implementation
- Files or surfaces to modify: release-boundary doc and context.
- Logic: preserve gates, update status/order.
- Edge cases: avoid expanding v1 scope.

### 4. Execute Implementation
- Implementation notes: added current marker state and replaced stale
  pre-release execution order with the current post-v1 candidate path.

### 5. Verify and Test
- Validation performed: `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: rely on release evidence index only.
- Technical debt introduced: no
- Scalability assessment: future agents now have a reusable current-candidate
  release path without reopening closed pre-release tasks.
- Refinements made: preserved core gates and separated released marker truth
  from local `HEAD` eligibility.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/planning/current-v1-release-boundary.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
