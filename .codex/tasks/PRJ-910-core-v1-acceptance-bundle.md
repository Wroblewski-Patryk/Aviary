# Task

## Header
- ID: PRJ-910
- Title: Core V1 Acceptance Bundle
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-908
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 910
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The current candidate is deployed and release-smoked, but PRJ-908 found that
the canonical production incident-evidence bundle cannot be exported under the
current strict production policy. PRJ-910 consolidates the current v1 evidence
without hiding that blocker.

## Goal
Produce one core v1 acceptance bundle mapping every final core gate to its
health surface, behavior evidence, release smoke proof, and residual risk.

## Scope
- `docs/planning/v1-core-acceptance-bundle.md`
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-910-core-v1-acceptance-bundle.md`

## Success Signal
- User or operator problem: release owner needs one readable view of whether
  core v1 is ready.
- Expected product or reliability outcome: core green gates and final blockers
  are separated.
- How success will be observed: acceptance bundle states go/no-go by gate and
  records PRJ-908 as the remaining final release blocker.
- Post-launch learning needed: no

## Deliverable For This Stage
Acceptance bundle document and context updates.

## Constraints
- do not claim final v1 release while PRJ-908 remains blocked
- do not commit generated health artifacts
- do not invent evidence that release smoke or health did not provide
- keep extension gates separate from core no-UI gates

## Definition of Done
- [x] Acceptance bundle exists.
- [x] Every core gate has a health surface and state.
- [x] Local and production evidence are summarized.
- [x] PRJ-908 blocker is explicit.
- [x] Context sources are updated.

## Validation Evidence
- Tests:
  - production release smoke passed after PRJ-908 restoration and documentation
    push
- Manual checks:
  - production `/health` snapshot captured to
    `.codex/artifacts/prj910-health-snapshot.json`
  - `git diff --check` passed
- Screenshots/logs: not applicable
- High-risk checks: no secrets or generated health snapshot committed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-production-incident-evidence-bundle.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no new mismatch
- Decision required from user: no for this bundle; yes before resolving PRJ-908
  through a new export path or contract change
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: required if PRJ-908 contract changes

## Deployment / Ops Evidence
- Deploy impact: none for the bundle itself
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: not applicable
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

- Task summary: produced the core v1 acceptance bundle.
- Files changed:
  - `docs/planning/v1-core-acceptance-bundle.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-910-core-v1-acceptance-bundle.md`
- How tested: health snapshot review, `git diff --check`, production smoke
  after push.
- What is incomplete: final v1 declaration remains blocked by PRJ-908.
- Next steps: implement or approve a production-safe incident-evidence export
  path, then rerun acceptance.
- Decisions made: core no-UI behavior is GO; final release declaration remains
  NO-GO until PRJ-908 is resolved or explicitly waived.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: core gates are green, incident bundle export is blocked.
- Gaps: final release declaration needs PRJ-908 resolution.
- Inconsistencies: none new.
- Architecture constraints: incident evidence is still part of the final
  evidence bundle.

### 2. Select One Priority Task
- Selected task: PRJ-910 Core V1 Acceptance Bundle.
- Priority rationale: it consolidates P0 evidence after PRJ-908.
- Why other candidates were deferred: rollback and privacy checks depend on
  knowing current acceptance posture.

### 3. Plan Implementation
- Files or surfaces to modify: planning and context docs.
- Logic: map each gate to health, evidence, and residual risk.
- Edge cases: do not hide PRJ-908 blocker.

### 4. Execute Implementation
- Implementation notes: captured current health snapshot and wrote acceptance
  matrix.

### 5. Verify and Test
- Validation performed: health snapshot review and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: declare v1 done from green smoke alone, rejected
  because PRJ-908 remains a final evidence blocker.
- Technical debt introduced: no
- Scalability assessment: acceptance bundle can be rerun after PRJ-908 fix.
- Refinements made: go/no-go split between core behavior and final declaration.

### 7. Update Documentation and Knowledge
- Docs updated: yes
- Context updated: yes
- Learning journal updated: not applicable.
