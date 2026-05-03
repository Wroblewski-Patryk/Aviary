# Task

## Header
- ID: PRJ-1116
- Title: Clarify stale release-review snapshots after PRJ-1115 refresh
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1115
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1116
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

PRJ-1115 refreshed current release evidence in the release evidence index and
v1 roadmap. `docs/planning/v1-final-go-no-go-review.md` still contains older
PRJ-934 snapshot rows that can read like current instructions unless clearly
scoped as historical.

## Goal

Clarify that older PRJ-934 revision rows and PRJ-936 preconditions are
historical, while the current release truth lives in PRJ-955 and the PRJ-1115
release evidence refresh.

## Scope

- `.codex/tasks/PRJ-1116-release-review-stale-snapshot-clarification.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-final-go-no-go-review.md`

## Success Signal
- User or operator problem: historical release-review tables can be mistaken
  for current deploy instructions.
- Expected product or reliability outcome: release docs distinguish historical
  review evidence from current release truth.
- How success will be observed: the final go/no-go review points operators to
  PRJ-955 and PRJ-1115 for current truth without removing historical evidence.
- Post-launch learning needed: no

## Deliverable For This Stage

A docs-only clarification preserving historical evidence and current release
source-of-truth boundaries.

## Constraints
- use existing docs and release evidence surfaces
- do not rewrite historical evidence as if it happened today
- do not change release policy or gate semantics
- do not claim local `HEAD` is deployed

## Implementation Plan
1. Clarify the PRJ-934 revision table as a historical snapshot.
2. Add a current truth pointer to PRJ-955 and PRJ-1115 evidence.
3. Rename the stale PRJ-936 action list as a historical pre-PRJ-955 list.
4. Update task board and project state.
5. Run `git diff --check`.

## Acceptance Criteria
- Historical SHA values remain visible but labeled as historical.
- Current `v1.0.0` selected SHA remains the final marker decision.
- Current local `HEAD` deploy parity remains blocked unless production matches.
- Docs/context are synchronized.

## Definition of Done
- [x] Release review wording clarified.
- [x] Context updated.
- [x] `git diff --check` passes.
- [x] No release policy change was introduced.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel release rules
- temporary bypasses or workaround-only paths
- architecture changes without explicit approval
- deleting historical evidence needed for auditability

## Validation Evidence
- Tests:
  - not applicable; docs-only release clarification
- Manual checks:
  - reviewed `docs/planning/v1-final-go-no-go-review.md` historical/current
    wording after edit
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - no deploy, smoke, release marker, or policy change was introduced
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `docs/planning/v1-final-go-no-go-review.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: final go/no-go review now points to the
  current release evidence index and PRJ-1115 refresh

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: none
- Rollback note: revert docs/context clarification
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

Docs-only release clarification. No deploy, smoke, or runtime change.

## Production-Grade Required Contract

- Goal: clarify stale release-review snapshots after current evidence refresh.
- Scope: final go/no-go review and context.
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
- Existing workaround or pain: stale historical rows can look like active
  blocker instructions.
- Smallest useful slice: clarify one release review doc.
- Success metric or signal: current evidence pointer is explicit.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: release decision
- SLI: release documentation truthfulness
- SLO: current release docs do not imply stale SHA evidence is current
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: docs diff
- Smoke command or manual smoke: not applicable
- Rollback or disable path: revert docs/context clarification

## AI Testing Evidence

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: release metadata only
- Trust boundaries: docs-only
- Permission or ownership checks: not applicable
- Abuse cases: false release claim from stale docs
- Secret handling: no secrets
- Security tests or scans: not applicable
- Fail-closed behavior: current docs point back to release evidence index
- Residual risk: external deploy proof still operator-owned

## Result Report

- Task summary: clarified that older PRJ-934 release-review SHA values are
  historical and that current release truth lives in PRJ-955, PRJ-1115, and the
  release evidence index.
- Files changed:
  - `.codex/tasks/PRJ-1116-release-review-stale-snapshot-clarification.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/planning/v1-final-go-no-go-review.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - external deploy parity remains blocked by PRJ-952.
- Next steps:
  - resolve PRJ-952 or continue narrow release-truth cleanup while blocked.
- Decisions made:
  - preserve historical PRJ-934 values, but label them as historical instead of
    rewriting history.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: one release review doc mixes historical PRJ-934 values with final
  PRJ-955 decision.
- Gaps: current PRJ-1115 evidence pointer is absent from that review.
- Inconsistencies: old PRJ-936 action language reads active despite marker
  resolution.
- Architecture constraints: preserve audit history and source-of-truth chain.

### 2. Select One Priority Task
- Selected task: PRJ-1116 release-review stale snapshot clarification.
- Priority rationale: release truth is the current v1 blocker surface.
- Why other candidates were deferred: external deploy parity still needs
  operator action.

### 3. Plan Implementation
- Files or surfaces to modify: final go/no-go review and context.
- Logic: add current-truth pointers and historical labels.
- Edge cases: do not erase historical review evidence.

### 4. Execute Implementation
- Implementation notes: added current-truth pointers and historical labels in
  the final go/no-go review; updated context.

### 5. Verify and Test
- Validation performed: `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave the stale doc untouched because it says
  superseded.
- Technical debt introduced: no
- Scalability assessment: release docs now better separate immutable audit
  history from current release truth.
- Refinements made: kept the old SHA evidence visible for auditability.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/planning/v1-final-go-no-go-review.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
