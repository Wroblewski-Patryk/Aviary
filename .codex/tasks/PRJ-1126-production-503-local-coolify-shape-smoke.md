# Task

## Header
- ID: PRJ-1126
- Title: Production 503 Local Coolify-Shape Smoke
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1125
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1126
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

After PRJ-1125, production changed from serving the old released revision to
returning `503 Service Unavailable` with body `no available server` for both
`/health` and `/settings`.

Selected pushed candidate:

`3b46ed3878a8560c3adb147fcadf064818ccc322`

## Goal

Determine whether the pushed candidate has an obvious repo-owned Coolify compose
startup failure, without using production secrets or adding a workaround.

## Success Signal
- User or operator problem: production is unavailable and needs a clear next
  recovery path.
- Expected product or reliability outcome: distinguish candidate image/startup
  failure from production Coolify/environment failure.
- How success will be observed: local Coolify-shape build, migration, app
  health, and settings evidence is recorded.
- Post-launch learning needed: yes

## Deliverable For This Stage

Local Docker Compose verification evidence and source-of-truth updates for the
production 503 state.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not run production fallback without operator-owned webhook URL and secret
- do not print or rely on real secrets during local compose diagnostics

## Scope

- `.codex/tasks/PRJ-1126-production-503-local-coolify-shape-smoke.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/context/LEARNING_JOURNAL.md`
- `docs/operations/release-evidence-index.md`

## Implementation Plan

1. Confirm production 503 with existing release audit and direct HTTP checks.
2. Confirm relevant deployment tests still pass locally.
3. Run a local isolated Docker Compose smoke using the existing
   `docker-compose.coolify.yml` and dummy non-secret env-file.
4. Verify local container health plus `/health` and `/settings`.
5. Tear down the local Compose project.
6. Update evidence and next action.

## Acceptance Criteria

- Production 503 state is recorded.
- Local Coolify-shape app startup is proven or disproven.
- No production secret is required for the local check.
- No deploy workaround is introduced.
- The operator next action remains exact.

## Definition of Done
- [x] Production health state checked.
- [x] Local deployment-shape smoke checked.
- [x] Local Compose project cleaned up.
- [x] Source-of-truth files updated.
- [x] `DEFINITION_OF_DONE.md` is satisfied for this release verification task.

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
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_deployment_trigger_scripts.py tests/test_web_routes.py; Pop-Location`
  - result: `69 passed`
- Manual checks:
  - `curl.exe -i -L --max-time 30 https://aviary.luckysparrow.ch/health`
    - `503 Service Unavailable`
    - body: `no available server`
  - `curl.exe -i -L --max-time 30 https://aviary.luckysparrow.ch/settings`
    - `503 Service Unavailable`
    - body: `no available server`
  - `docker compose -f docker-compose.coolify.yml --env-file .\.codex\tmp\local-compose-nonsecret.env -p aion-prj1126 up --build -d db migrate app`
    - result: build completed, `db`, `migrate`, and `app` started
  - `docker compose ... ps`
    - app: `healthy`
    - db: `healthy`
  - `docker compose ... exec -T app python -c "... /health ..."`
    - result: `200`
  - `docker compose ... exec -T app python -c "... /settings ..."`
    - result: `200`
  - `docker compose ... down`
    - result: local containers and network removed
- Screenshots/logs:
  - local app logs showed `Application startup complete`
  - migration logs reached Alembic head `20260426_0012`
- High-risk checks:
  - `.env` is ignored by git
  - `.env.example` is the only tracked env example
  - local compose smoke used dummy non-secret env-file
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docker-compose.coolify.yml`
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
- Remaining mismatches: not applicable
- State checks: not applicable
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: not applicable
- Input-mode checks: not applicable
- Accessibility checks: not applicable
- Parity evidence: not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: high
- Env or secret changes: none
- Health-check impact: production currently unavailable; local app health is
  healthy with the same compose shape.
- Smoke steps updated: release evidence refreshed; no script change.
- Rollback note: production recovery is operator-owned in Coolify. Do not move
  a marker for `3b46ed3878a8560c3adb147fcadf064818ccc322` until production
  returns healthy and deploy parity passes.
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

The local smoke does not prove production secrets, Coolify source binding, or
Coolify deployment history. It proves that the selected repo candidate can build,
migrate, start, and serve health/settings in the approved compose shape.

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

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: production user and release operator
- Existing workaround or pain: production reverse proxy has no available app
  server.
- Smallest useful slice: local deployment-shape proof plus exact operator
  recovery state.
- Success metric or signal: production returns healthy and reports selected
  candidate SHA.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: rerun release smoke after operator
  recovery.

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not
  applicable; no runtime observability behavior changed.
- Critical user journey: production web shell and API health
- SLI: public `/health` and `/settings` success
- SLO: public host has an available backend server
- Error budget posture: exhausted
- Health/readiness check: production `503`; local compose `200`.
- Logs, dashboard, or alert route: Coolify deployment logs/history are
  operator-owned and not available from this environment.
- Smoke command or manual smoke:
  - local compose smoke with dummy env-file
  - production release audit
- Rollback or disable path: operator can restore the previous healthy Coolify
  deployment or fix current deployment source/log issue.

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable; evidence-only release
  task.
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: yes, locally via compose migrate.
- Loading state verified: not applicable
- Error state verified: production `503` verified.
- Refresh/restart behavior verified: local compose fresh start verified.
- Regression check performed: targeted backend tests and local compose smoke

## AI Testing Evidence (required for AI features)

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable; no
  code or permission behavior changed.
- Data classification: release metadata and local non-secret smoke env
- Trust boundaries: production deployment secrets remain operator-owned.
- Permission or ownership checks: no production trigger was run.
- Abuse cases: avoid printing or committing local `.env` secrets.
- Secret handling: use dummy env-file for local compose diagnostics.
- Security tests or scans: `.env` git ignore and tracked env files checked.
- Fail-closed behavior: release marker remains blocked.
- Residual risk: production Coolify logs are unavailable locally.

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: production is `503 no available server`, while the selected
  candidate builds, migrates, starts, and serves `/health` and `/settings`
  locally in the Coolify compose shape.
- Files changed:
  - `.codex/tasks/PRJ-1126-production-503-local-coolify-shape-smoke.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `docs/operations/release-evidence-index.md`
- How tested:
  - targeted backend tests
  - production HTTP checks
  - local Docker Compose smoke
  - `git diff --check`
- What is incomplete: production Coolify recovery requires operator access to
  deployment logs, source binding, manual redeploy, or webhook fallback inputs.
- Next steps: recover production availability in Coolify, then rerun production
  release smoke for `3b46ed3878a8560c3adb147fcadf064818ccc322`.
- Decisions made: do not create a repo workaround because local approved
  compose shape is healthy.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: production returns `503 no available server`.
- Gaps: Coolify logs and fallback credentials are not available locally.
- Inconsistencies: local compose shape is healthy; production is unavailable.
- Architecture constraints: source automation primary, fallback operator-owned.

### 2. Select One Priority Task
- Selected task: PRJ-1126 production 503 local Coolify-shape smoke.
- Priority rationale: production availability outranks feature work.
- Why other candidates were deferred: deploy parity and health must recover
  before release marker work can continue.

### 3. Plan Implementation
- Files or surfaces to modify: task/context/release evidence/learning journal.
- Logic: verify production state, run local deployment-shape smoke, document
  exact next action.
- Edge cases: prevent local `.env` secrets from being printed or committed.

### 4. Execute Implementation
- Implementation notes: used dummy env-file and isolated Compose project
  `aion-prj1126`.

### 5. Verify and Test
- Validation performed:
  - targeted tests: `69 passed`
  - production `/health` and `/settings`: `503`
  - local compose app: `healthy`
  - local `/health` and `/settings`: `200`
  - local compose torn down
  - `git diff --check`: passed

### 6. Self-Review
- Architecture alignment: yes.
- Duplication/workaround check: no new runtime path or deploy trigger added.
- Risk: production remains down until operator-side Coolify recovery.

### 7. Update Documentation and Knowledge
- Updated:
  - task board
  - project state
  - release evidence index
  - learning journal
