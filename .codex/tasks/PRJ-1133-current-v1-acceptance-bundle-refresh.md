# Task

## Header
- ID: PRJ-1133
- Title: Current V1 Acceptance Bundle Refresh
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1128, PRJ-1131, PRJ-1132
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1133
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`v1.0.1` is now the current release marker for selected SHA
`3b46ed3878a8560c3adb147fcadf064818ccc322`, but the core acceptance bundle and
minimal health monitor docs still pointed at historical `v1.0.0` truth. The
roadmap kept `PRJ-954` open as the acceptance-bundle refresh task.

## Goal

Refresh the current v1 acceptance bundle and monitor pointers so they use
`v1.0.1` and the exact selected SHA evidence from PRJ-1128/1131.

## Scope

- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-1133-current-v1-acceptance-bundle-refresh.md`
- `docs/planning/v1-core-acceptance-bundle.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `docs/planning/v1-release-evidence-archive-standard.md`
- `docs/operations/production-health-monitor.md`
- `docs/planning/v1-minimal-external-health-monitor.md`
- `docs/operations/release-evidence-index.md`

## Success Signal
- User or operator problem: acceptance docs still described the historical
  `v1.0.0` marker as the current v1 bundle.
- Expected product or reliability outcome: current v1 bundle points to
  `v1.0.1`, while `v1.0.0` remains historical evidence.
- How success will be observed: release audit and go/no-go for `v1.0.1` are
  green, and stale current-bundle wording is gone.
- Post-launch learning needed: no

## Deliverable For This Stage

Updated acceptance bundle, roadmap status, archive pointers, health monitor
target docs, and task/context evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not trigger deploy or create another marker
- do not store generated evidence artifacts in committed docs

## Implementation Plan

1. Inspect current acceptance bundle, roadmap, archive standard, and health
   monitor docs for stale `v1.0.0` current-marker language.
2. Run selected-tag go/no-go and release reality audit for `v1.0.1`.
3. Update current-bundle docs to point at `v1.0.1` and the selected SHA.
4. Preserve `v1.0.0` as historical marker truth.
5. Mark `PRJ-954` done in roadmap/release plan.
6. Run stale wording scan and diff hygiene.

## Acceptance Criteria
- `docs/planning/v1-core-acceptance-bundle.md` names `v1.0.1` as the current
  core no-UI/web-supported v1 marker.
- Monitor docs use `v1.0.1` in canonical revision-aware commands.
- Roadmap marks `PRJ-954` as done by this task.
- `v1.0.0` is still described as historical, not moved.
- `run_release_go_no_go.py --selected-tag v1.0.1 --monitor-mode` returns
  `GO`.

## Definition of Done
- [x] DEFINITION_OF_DONE.md satisfied for a release-doc truth refresh.
- [x] Current acceptance bundle points at `v1.0.1`.
- [x] Monitor docs point at `v1.0.1`.
- [x] Roadmap/plan status updated.
- [x] Validation evidence recorded.

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
- deploy trigger execution
- release marker movement

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\run_release_go_no_go.py --base-url https://aviary.luckysparrow.ch --selected-tag v1.0.1 --monitor-mode --output ..\.codex\tmp\release-go-no-go-prj1133-v101.json; Pop-Location`
  - result: `verdict=GO`; audit `GO_FOR_SELECTED_SHA`; smoke `exit_code=0`;
    `selected_sha_is_local_head=true`
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\audit_release_reality.py --base-url https://aviary.luckysparrow.ch --selected-tag v1.0.1 --monitor-mode --output ..\.codex\tmp\release-reality-audit-prj1133-v101-monitor.json; Pop-Location`
  - result: `GO_FOR_SELECTED_SHA`
- Manual checks:
  - `git for-each-ref refs/tags/v1.0.1 --format='%(objectname) %(objecttype) %(*objectname)'`
  - result: `b016c4f33051805cfa09664f79bbe57f5b30811b tag 3b46ed3878a8560c3adb147fcadf064818ccc322`
- Screenshots/logs: not applicable
- High-risk checks:
  - no deployment trigger, marker movement, runtime code change, env var, or
    secret change
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/10_future_vision.md`
  - `docs/planning/v1-core-acceptance-bundle.md`
  - `docs/operations/release-evidence-index.md`
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
- Smoke steps updated: monitor docs now use `v1.0.1`
- Rollback note: `v1.0.0` remains historical marker; no deploy changed
- Observability or alerting impact: documentation target changed to current
  marker
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

This task does not expand core v1 to include Telegram live-mode proof,
organizer provider activation, or AI red-team final scoring. Those remain
explicit extension or hardening follow-ups.

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
- Existing workaround or pain: current acceptance bundle still pointed at
  historical marker truth.
- Smallest useful slice: refresh current acceptance and monitor docs.
- Success metric or signal: selected-tag go/no-go remains `GO`.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: release acceptance and revision-aware monitoring
- SLI: selected tag production revision parity
- SLO: `v1.0.1` selected tag remains `GO`
- Error budget posture: healthy
- Health/readiness check: selected-tag go/no-go and release reality audit
- Logs, dashboard, or alert route: monitor docs now target `v1.0.1`
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
- Abuse cases: avoid treating extension gates as core blockers or erasing
  historical marker truth
- Secret handling: no secrets used or persisted
- Security tests or scans: not applicable
- Fail-closed behavior: future candidates still require fresh deploy parity
- Residual risk: extension and hardening gates remain explicit

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: refreshed current core acceptance bundle and monitor pointers
  to `v1.0.1`.
- Files changed:
  - `.codex/tasks/PRJ-1133-current-v1-acceptance-bundle-refresh.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/planning/v1-core-acceptance-bundle.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `docs/planning/v1-release-evidence-archive-standard.md`
  - `docs/operations/production-health-monitor.md`
  - `docs/planning/v1-minimal-external-health-monitor.md`
  - `docs/operations/release-evidence-index.md`
- How tested:
  - selected-tag go/no-go returned `GO`
  - monitor-mode release reality audit returned `GO_FOR_SELECTED_SHA`
  - tag object/target inspected
  - stale wording scan and diff hygiene passed
- What is incomplete:
  - Telegram live-mode smoke, organizer provider activation, and broader
    AI/security hardening remain explicit follow-ups.
- Next steps:
  - choose the next unblocked extension or hardening task.
- Decisions made:
  - current acceptance bundle now follows `v1.0.1`; `v1.0.0` remains
    historical.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - acceptance bundle and monitor docs still named historical `v1.0.0` as
    current.
- Gaps:
  - `PRJ-954` remained `READY`.
- Inconsistencies:
  - roadmap and release marker docs already treated `v1.0.1` as current.
- Architecture constraints:
  - core no-UI/web-supported v1 gates remain unchanged; extension gates stay
    separate.

### 2. Select One Priority Task
- Selected task: refresh current v1 acceptance bundle.
- Priority rationale: it is the remaining P0 release-truth drift after marker
  and deploy parity closure.
- Why other candidates were deferred:
  - extension/provider tasks require external credentials or are lower-priority
    hardening.

### 3. Plan Implementation
- Files or surfaces to modify:
  - acceptance bundle, roadmap/plan, archive standard, monitor docs, context.
- Logic:
  - replace current marker evidence with `v1.0.1` and preserve historical
    `v1.0.0`.
- Edge cases:
  - avoid expanding the acceptance boundary.

### 4. Execute Implementation
- Implementation notes:
  - no runtime behavior changed.
  - docs now align with release evidence index and marker truth.

### 5. Verify and Test
- Validation performed:
  - selected-tag go/no-go
  - release reality audit in monitor mode
  - tag target inspection
  - stale wording scan
  - diff hygiene
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - only updating the roadmap row; rejected because operator monitor docs and
    core bundle would still drift.
- Technical debt introduced: no
- Scalability assessment:
  - future markers have clearer update targets.
- Refinements made:
  - included monitor docs in the same release-truth slice.

### 7. Update Documentation and Knowledge
- Docs updated:
  - acceptance bundle, roadmap, release plan, archive standard, monitor docs,
    release evidence index
- Context updated:
  - task board and project state
- Learning journal updated: not applicable.
