# Task

## Header
- ID: PRJ-1134
- Title: Release Handoff Marker Blocker Stale Path Cleanup
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1131, PRJ-1133
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1134
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

After `v1.0.1` marker and acceptance-bundle refresh, a targeted stale wording
scan still found release handoff and marker-blocker docs that described
creating a marker for the current selected SHA as a next path. The runtime
runbook also still showed the old `v1.0.0` monitor-mode example in a current
release-check section.

## Goal

Remove stale marker/handoff wording so current release instructions consistently
say `v1.0.1` already exists and future marker instructions apply only to future
selected candidates.

## Scope

- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-1134-release-handoff-marker-blocker-stale-path-cleanup.md`
- `docs/planning/v1-release-notes-and-operator-handoff.md`
- `docs/planning/v1-release-marker-blocker.md`
- `docs/operations/runtime-ops-runbook.md`
- `docs/operations/release-evidence-index.md`

## Success Signal
- User or operator problem: handoff docs could still imply the current selected
  SHA needs a marker task.
- Expected product or reliability outcome: current release instructions no
  longer conflict with `v1.0.1`.
- How success will be observed: stale wording scan has no active-current hits
  in the touched docs and selected-tag go/no-go remains `GO`.
- Post-launch learning needed: no

## Deliverable For This Stage

Updated handoff, marker blocker, runbook, release evidence index, and task
context evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not move tags, trigger deploy, or mutate production
- preserve historical `v1.0.0` evidence

## Implementation Plan

1. Scan release docs for active-current stale marker language.
2. Verify current `v1.0.1` go/no-go.
3. Update release handoff next paths so `v1.0.1` is the current path and marker
   creation is future-only.
4. Refresh marker-blocker doc to include current `v1.0.1` resolution.
5. Update runtime runbook monitor-mode example from current `v1.0.0` to
   current `v1.0.1`.
6. Record evidence in release index and context.
7. Run stale wording scan and diff hygiene.

## Acceptance Criteria
- Release handoff no longer tells operators to create a marker for
  `3b46ed3878a8560c3adb147fcadf064818ccc322`.
- Marker blocker doc says `v1.0.1` is resolved for the current selected SHA.
- Runtime runbook current monitor-mode example uses `v1.0.1`.
- Historical `v1.0.0` truth remains explicit.
- `run_release_go_no_go.py --selected-tag v1.0.1 --monitor-mode` returns
  `GO`.

## Definition of Done
- [x] DEFINITION_OF_DONE.md satisfied for a release-doc cleanup task.
- [x] Relevant docs/context updated.
- [x] Current selected-tag go/no-go evidence recorded.
- [x] Stale wording scan run.
- [x] Diff hygiene passed.

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
- deployment trigger execution
- release marker movement

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\run_release_go_no_go.py --base-url https://aviary.luckysparrow.ch --selected-tag v1.0.1 --monitor-mode --output ..\.codex\tmp\release-go-no-go-prj1134-v101.json; Pop-Location`
  - result: `verdict=GO`; audit `GO_FOR_SELECTED_SHA`; smoke `exit_code=0`
- Manual checks:
  - `codex_app.automation_update mode=view id=aion-production-health-monitor`
    rendered the existing automation card; no local `automation.toml` was
    available under the standard user `.codex\automations` path to edit safely
  - stale wording scan over touched docs
- Screenshots/logs: not applicable
- High-risk checks:
  - no deployment, production mutation, env var, secret, or tag change
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-release-notes-and-operator-handoff.md`
  - `docs/planning/v1-release-marker-blocker.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence (required for UX tasks)
- Design source type: not applicable
- Design source reference: not applicable
- Canonical visual target: not applicable
- Fidelity target: not applicable
- Stitch used: no
- Experience-quality bar reviewed: not applicable
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: not applicable
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: not applicable
- Remaining mismatches: none
- State checks: not applicable
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: not applicable
- Input-mode checks: not applicable
- Accessibility checks: not applicable
- Parity evidence: not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: runbook current monitor-mode example now targets
  `v1.0.1`
- Rollback note: `v1.0.0` remains historical; no deploy changed
- Observability or alerting impact: docs now target current marker
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

The Codex app could render the existing health monitor automation card, but no
local automation definition was available through the standard filesystem path.
This task therefore updates repository truth only and does not guess automation
fields.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime
  surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB
-> validation -> error handling -> test. This task is release-doc/ops truth
only and does not change runtime behavior.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator
- Existing workaround or pain: handoff next paths contradicted current marker
  truth.
- Smallest useful slice: update stale handoff/marker blocker/runbook wording.
- Success metric or signal: selected-tag go/no-go remains `GO`.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: release handoff and monitor command correctness
- SLI: selected tag production revision parity
- SLO: `v1.0.1` selected tag remains `GO`
- Error budget posture: healthy
- Health/readiness check: selected-tag go/no-go
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke:
  `run_release_go_no_go.py --selected-tag v1.0.1 --monitor-mode`
- Rollback or disable path: no deploy changed

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: selected-tag go/no-go

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: release metadata
- Trust boundaries: public health/release metadata only
- Permission or ownership checks: not applicable
- Abuse cases: avoid stale marker instructions causing wrong tag/deploy action
- Secret handling: no secrets used or persisted
- Security tests or scans: not applicable
- Fail-closed behavior: future marker creation remains gated on green evidence
- Residual risk: actual app automation fields were not changed because they
  were not available through the standard filesystem path

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: cleaned stale current-marker handoff and blocker wording after
  `v1.0.1`.
- Files changed:
  - `.codex/tasks/PRJ-1134-release-handoff-marker-blocker-stale-path-cleanup.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/planning/v1-release-notes-and-operator-handoff.md`
  - `docs/planning/v1-release-marker-blocker.md`
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/operations/release-evidence-index.md`
- How tested:
  - selected-tag go/no-go returned `GO`
  - stale wording scan and diff hygiene passed
- What is incomplete:
  - actual Codex automation metadata was not found locally, so no automation
    schedule update was performed.
- Next steps:
  - continue with extension/hardening gates or inspect app automation through a
    richer automation management surface if needed.
- Decisions made:
  - current handoff paths now treat `v1.0.1` as done and future marker work as
    future-only.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - release handoff and marker blocker docs still had stale current-marker
    instructions.
- Gaps:
  - local automation metadata was not available from the standard path.
- Inconsistencies:
  - repo truth already said `v1.0.1`; handoff next paths lagged.
- Architecture constraints:
  - do not move marker; do not trigger deploy; preserve historical evidence.

### 2. Select One Priority Task
- Selected task: stale handoff/marker blocker cleanup.
- Priority rationale: it removes a current-operator instruction drift.
- Why other candidates were deferred:
  - extension and provider gates need external inputs or are broader hardening.

### 3. Plan Implementation
- Files or surfaces to modify:
  - release handoff, marker blocker, runbook, release index, context.
- Logic:
  - current marker is `v1.0.1`; future marker instructions are future-only.
- Edge cases:
  - preserve historical `v1.0.0` text.

### 4. Execute Implementation
- Implementation notes:
  - docs/context only; no runtime behavior changed.

### 5. Verify and Test
- Validation performed:
  - selected-tag go/no-go
  - stale wording scan
  - diff hygiene
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - only changing release notes; rejected because marker blocker and runbook
    would still drift.
- Technical debt introduced: no
- Scalability assessment:
  - future marker work has clearer instructions.
- Refinements made:
  - documented automation metadata limitation instead of guessing.

### 7. Update Documentation and Knowledge
- Docs updated:
  - release handoff, marker blocker, runtime runbook, release index
- Context updated:
  - task board and project state
- Learning journal updated: not applicable.
