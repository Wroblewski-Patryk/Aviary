# Task

## Header
- ID: PRJ-1127
- Title: Production 503 Operator Handoff
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1126
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1127
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

Production remains unavailable after the selected candidate was pushed. Local
verification in PRJ-1126 proved that the selected candidate can build, migrate,
start, and serve `/health` and `/settings` in the approved Coolify compose
shape.

Selected pushed candidate:

`3b46ed3878a8560c3adb147fcadf064818ccc322`

Canonical Coolify app:

`jr1oehwlzl8tcn3h8gh2vvih`

## Goal

Create an operator-facing handoff for the current production `503 no available
server` state, using the existing architecture and without inventing a deploy
path.

## Success Signal
- User or operator problem: production needs recovery, but local automation
  lacks Coolify logs and fallback credentials.
- Expected product or reliability outcome: operator gets exact checks and
  selected SHA for recovery.
- How success will be observed: production returns healthy and release smoke
  passes for the selected candidate.
- Post-launch learning needed: yes

## Deliverable For This Stage

Source-of-truth handoff notes and a runbook checklist for repeated
`503 no available server` after deploy convergence retry budget is exhausted.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not trigger manual deploy without operator-owned webhook URL and secret
- do not create a new release candidate commit for evidence-only changes

## Scope

- `.codex/tasks/PRJ-1127-production-503-operator-handoff.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/context/LEARNING_JOURNAL.md`
- `docs/operations/release-evidence-index.md`
- `docs/operations/runtime-ops-runbook.md`

## Implementation Plan

1. Recheck production release reality for the selected candidate.
2. Confirm no Coolify/deploy webhook credentials are available locally.
3. Attempt incident-evidence export and record that public `/health` fails with
   `503`.
4. Add a concise runbook checklist for repeated `503 no available server`.
5. Update task board, project state, release index, and learning journal.

## Acceptance Criteria

- Exact selected SHA and canonical app id are recorded.
- Production `503 no available server` is recorded.
- Operator checks for Coolify source binding, deployment history, `db`,
  `migrate`, `app`, and sidecars are listed.
- No new deploy path or workaround is introduced.
- Validation evidence is attached.

## Definition of Done
- [x] Production state rechecked.
- [x] Existing incident exporter behavior recorded.
- [x] Runbook updated with the current repeated-503 decision point.
- [x] Source-of-truth files updated.
- [x] `DEFINITION_OF_DONE.md` is satisfied for this release handoff task.

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
  - PRJ-1126 targeted tests remain current: `69 passed`
- Manual checks:
  - `audit_release_reality.py --selected-sha 3b46ed3878a8560c3adb147fcadf064818ccc322`
    - `verdict=HOLD_HEALTH_OR_WEB_REVISION_MISSING`
    - production `/health`: `HTTP Error 503: Service Unavailable`
    - production `/settings`: `HTTP Error 503: Service Unavailable`
  - environment variable name check:
    - no `COOLIFY`, `DEPLOY`, `WEBHOOK`, or `AVIARY` deploy variables available
  - `export_incident_evidence_bundle.py --base-url https://aviary.luckysparrow.ch`
    - failed while calling `/health`
    - error: `HTTP 503 ... no available server`
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - deploy fallback not triggered
  - no secret value required or recorded
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/operations/release-evidence-index.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: repeated-503 operator checklist added to
  the runtime ops runbook

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: high
- Env or secret changes: none
- Health-check impact: production health unavailable.
- Smoke steps updated: runbook checklist updated.
- Rollback note: operator can restore the previous known-good production
  deployment or redeploy selected candidate; release marker must wait for
  fresh deploy parity.
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

This task stops at operator handoff because the environment has no Coolify
deployment logs, no UI access, and no deploy webhook credentials.

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
- Existing workaround or pain: public production host has no available app
  server.
- Smallest useful slice: exact operator recovery checklist and selected SHA.
- Success metric or signal: production `/health` returns `200` and reports the
  selected SHA.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: rerun release smoke after recovery.

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not
  applicable; no observability code changed.
- Critical user journey: production web shell and API health
- SLI: public `/health` success and backend/web revision parity
- SLO: public host has available app server and selected revision
- Error budget posture: exhausted
- Health/readiness check: production `503`
- Logs, dashboard, or alert route: Coolify UI/logs are operator-owned.
- Smoke command or manual smoke:
  - release reality audit
  - incident exporter attempt
- Rollback or disable path: restore previous known-good Coolify deployment or
  fix/redeploy selected candidate.

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable; release handoff only.
- Real API/service path used: yes
- Endpoint and client contract match: blocked by production `503`
- DB schema and migrations verified: PRJ-1126 local compose migrate passed.
- Loading state verified: not applicable
- Error state verified: production `503`
- Refresh/restart behavior verified: production recovery remains operator-side.
- Regression check performed: PRJ-1126 targeted tests and local compose smoke

## AI Testing Evidence (required for AI features)

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable; no
  code or permission behavior changed.
- Data classification: non-secret release metadata
- Trust boundaries: Coolify UI, deployment logs, and webhook credentials remain
  operator-owned.
- Permission or ownership checks: no unauthorized deployment trigger attempted.
- Abuse cases: avoid inventing deploy credentials or bypassing source
  automation.
- Secret handling: no secret values added.
- Security tests or scans: not applicable
- Fail-closed behavior: release marker remains blocked.
- Residual risk: production remains unavailable until operator recovery.

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: added operator handoff for repeated production
  `503 no available server` after local Coolify-shape smoke passed.
- Files changed:
  - `.codex/tasks/PRJ-1127-production-503-operator-handoff.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/operations/runtime-ops-runbook.md`
- How tested:
  - release reality audit
  - incident exporter attempt
  - `git diff --check`
- What is incomplete: production recovery remains blocked by operator-owned
  Coolify access or webhook fallback inputs.
- Next steps: operator inspects Coolify canonical app
  `jr1oehwlzl8tcn3h8gh2vvih`, restores healthy app server, then reruns release
  smoke for `3b46ed3878a8560c3adb147fcadf064818ccc322`.
- Decisions made: do not create a new candidate commit for evidence-only
  changes and do not use unapproved deploy paths.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: production returns `503 no available server`.
- Gaps: no Coolify logs/UI/API or webhook credentials are available locally.
- Inconsistencies: local compose shape passes; production has no available app
  server.
- Architecture constraints: source automation primary; webhook/UI fallback
  exception-only and operator-owned.

### 2. Select One Priority Task
- Selected task: PRJ-1127 production 503 operator handoff.
- Priority rationale: production availability blocks release progress.
- Why other candidates were deferred: no feature/doc cleanup can substitute for
  operator-side production recovery.

### 3. Plan Implementation
- Files or surfaces to modify: task/context/runbook/release evidence.
- Logic: add exact checklist and selected SHA without moving release candidate.
- Edge cases: incident exporter cannot build evidence bundle when `/health`
  itself returns `503`.

### 4. Execute Implementation
- Implementation notes: source-of-truth handoff only; no runtime or deploy
  behavior changed.

### 5. Verify and Test
- Validation performed:
  - release reality audit: `HOLD_HEALTH_OR_WEB_REVISION_MISSING`
  - incident exporter attempt: blocked by `HTTP 503`
  - `git diff --check`: passed

### 6. Self-Review
- Architecture alignment: yes.
- Duplication/workaround check: no new deploy path added.
- Risk: production remains unavailable until operator recovery.

### 7. Update Documentation and Knowledge
- Updated:
  - task board
  - project state
  - release evidence index
  - runtime ops runbook
  - learning journal
