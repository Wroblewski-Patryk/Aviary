# Task

## Header
- ID: PRJ-1129
- Title: Current v1 truth refresh after Coolify recovery
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1128
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1129
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

PRJ-1128 restored production availability and proved deploy parity for selected
candidate `3b46ed3878a8560c3adb147fcadf064818ccc322`. Some release planning
docs still framed the current state as the older `v1.0.0` marker plus a
post-v1 candidate blocked by `HOLD_REVISION_DRIFT`.

## Goal

Refresh the active v1 source-of-truth documents so the current release boundary,
release audit plan, task board, and project state no longer imply that the
selected candidate is still undeployed or that production is currently 503.

## Scope

- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/current-v1-release-boundary.md`
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `docs/operations/release-evidence-index.md`
- `.codex/tasks/PRJ-1129-current-v1-truth-refresh-after-coolify-recovery.md`

## Success Signal
- User or operator problem: source-of-truth docs still contain active-sounding
  stale release blockers after recovery.
- Expected product or reliability outcome: future agents can see that core v1
  is green for `3b46ed3` and pick the next true follow-up.
- How success will be observed: current docs name PRJ-1128 as current green
  selected-SHA evidence.
- Post-launch learning needed: no

## Deliverable For This Stage

Docs/context refresh only; no runtime code, deploy, or environment changes.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not move or create release tags
- do not push evidence-only changes that would move the deployed candidate SHA

## Implementation Plan
1. Re-read current task board, project state, release evidence index, and v1
   planning docs.
2. Update current release-boundary docs to reference PRJ-1128 and selected SHA
   `3b46ed3878a8560c3adb147fcadf064818ccc322`.
3. Mark older 503/drift evidence as historical rather than active current
   status.
4. Update current acceptance matrix and roadmap statuses where PRJ-1128 closed
   PRJ-952/PRJ-953-equivalent evidence.
5. Record PRJ-1129 in board and project state.
6. Run docs hygiene validation.

## Acceptance Criteria
- `docs/planning/current-v1-release-boundary.md` states current production is
  green for `3b46ed3878a8560c3adb147fcadf064818ccc322`.
- `docs/planning/v1-release-audit-and-execution-plan.md` no longer presents
  the old local `HOLD_REVISION_DRIFT` as current after PRJ-1128.
- `docs/operations/release-evidence-index.md` distinguishes historical
  PRJ-1125..PRJ-1127 evidence from current PRJ-1128 proof.
- `.codex/context/TASK_BOARD.md` and `.codex/context/PROJECT_STATE.md` include
  PRJ-1129 and point to the next tiny task.
- `git diff --check` passes.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for this docs-only release truth slice.
- [x] Current v1 truth refreshed after PRJ-1128.
- [x] Historical blockers remain available but are not framed as current.
- [x] Validation evidence captured.

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
  - not run; docs/context-only change
- Manual checks:
  - source-of-truth scan for active stale `HOLD_REVISION_DRIFT`, `503`, and
    PRJ-952 blocker wording in current sections; remaining matches are in
    explicitly historical or superseded evidence sections
- Screenshots/logs: not applicable
- High-risk checks:
  - `git diff --check` -> passed
  - `audit_release_reality.py --selected-sha 3b46ed3878a8560c3adb147fcadf064818ccc322`
    -> `GO_FOR_SELECTED_SHA`
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/26_env_and_config.md`
  - `docs/architecture/27_codex_instructions.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: release planning docs now point to PRJ-1128 proof
- Rollback note: unchanged; Coolify rollback remains operator-owned
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

## Notes

This task intentionally does not create a commit or move a release marker,
because doing so would create a new unsmoked candidate. The deployed selected
SHA remains `3b46ed3878a8560c3adb147fcadf064818ccc322`.

## Production-Grade Required Contract

Every task must include Goal, Scope, Implementation Plan, Acceptance Criteria,
Definition of Done, and Result Report. This task includes all required sections.

Runtime vertical slice note: no runtime behavior was changed.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: future release operators and agents
- Existing workaround or pain: stale current-state wording could send agents
  back into already-resolved recovery work
- Smallest useful slice: refresh active release truth docs after PRJ-1128
- Success metric or signal: current docs identify PRJ-1128 as current green
  selected-SHA evidence
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: release operator handoff
- SLI: source-of-truth accuracy
- SLO: current sections must not contradict latest production proof
- Error budget posture: not applicable
- Health/readiness check: PRJ-1128 release smoke remains the live proof
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: `git diff --check`
- Rollback or disable path: revert docs-only changes if wording is wrong

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: docs hygiene

## AI Testing Evidence (required for AI features)

Not applicable. This task changed no AI behavior.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: release metadata
- Trust boundaries: documentation only
- Permission or ownership checks: not applicable
- Abuse cases: avoid recording secrets or private Coolify session material
- Secret handling: no secrets touched
- Security tests or scans: not applicable
- Fail-closed behavior: not applicable
- Residual risk: AI red-team review remains a separate hardening follow-up

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: refreshed active v1 release truth after PRJ-1128 so current
  docs no longer describe the selected candidate as undeployed.
- Files changed:
  - `.codex/tasks/PRJ-1129-current-v1-truth-refresh-after-coolify-recovery.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `docs/operations/release-evidence-index.md`
- How tested:
  - `git diff --check`
  - `audit_release_reality.py --selected-sha 3b46ed3878a8560c3adb147fcadf064818ccc322`
  - targeted stale wording scan
- What is incomplete:
  - Coolify source/webhook automation reliability follow-up remains open
  - Telegram live-mode, organizer provider activation, and AI review remain
    extension/hardening follow-ups
- Next steps:
  - document Coolify source/webhook automation reliability or prepare a
    release marker decision for the already-green selected SHA
- Decisions made:
  - keep `v1.0.0` historical marker truth separate from current selected-SHA
    production proof

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - some current docs still framed PRJ-1125 drift and PRJ-1127 503 as active
    after PRJ-1128 recovery
- Gaps:
  - release audit plan and release boundary were not refreshed for current
    selected SHA
- Inconsistencies:
  - release evidence index current snapshot was green, but latest refresh
    evidence still started with older historical proof
- Architecture constraints:
  - docs must reflect production truth without redefining core v1 scope

### 2. Select One Priority Task
- Selected task: PRJ-1129 current v1 truth refresh after Coolify recovery
- Priority rationale: source-of-truth drift can misdirect future work and
  undermine release confidence
- Why other candidates were deferred: automation reliability and provider
  activation are separate follow-ups after current truth is clean

### 3. Plan Implementation
- Files or surfaces to modify: release docs and context only
- Logic: update current sections, keep historical evidence, avoid runtime changes
- Edge cases:
  - do not erase useful incident history
  - do not imply a new release tag was created
  - do not move selected SHA

### 4. Execute Implementation
- Implementation notes:
  - updated current v1 boundary and audit plan around PRJ-1128
  - added explicit history/current separation
  - added task/context entries

### 5. Verify and Test
- Validation performed:
  - stale wording scan
  - `git diff --check`
  - release reality audit for selected SHA
- Result: passed

### 6. Self-Review
- Simpler option considered: only add a note to task board
- Technical debt introduced: no
- Scalability assessment: keeps evidence chronological while making current
  truth explicit
- Refinements made: retained historical blocker evidence under historical
  wording instead of deleting it

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `docs/operations/release-evidence-index.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: no; no new recurring pitfall beyond PRJ-1128
