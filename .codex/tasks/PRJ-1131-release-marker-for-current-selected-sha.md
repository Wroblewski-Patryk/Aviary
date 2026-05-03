# Task

## Header
- ID: PRJ-1131
- Title: Release Marker For Current Selected SHA
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1128, PRJ-1129, PRJ-1130
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1131
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

PRJ-1128 restored production through the approved Coolify UI fallback and proved
that selected SHA `3b46ed3878a8560c3adb147fcadf064818ccc322` is deployed,
health-green, revision-aligned, and release-smoked. PRJ-1130 refreshed the
release notes and final go/no-go review, but intentionally left marker creation
to a dedicated release-marker task.

## Goal

Create a release marker for the current selected production SHA without moving
the historical `v1.0.0` marker.

## Scope

- Git tag:
  - create and push annotated tag `v1.0.1`
  - target commit: `3b46ed3878a8560c3adb147fcadf064818ccc322`
- Source-of-truth updates:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `docs/planning/v1-release-notes-and-operator-handoff.md`
  - `docs/planning/v1-final-go-no-go-review.md`

## Success Signal
- User or operator problem: current production candidate is green but did not
  yet have a dedicated marker.
- Expected product or reliability outcome: v1 marker truth distinguishes the
  historical `v1.0.0` marker from the current deployed `v1.0.1` marker.
- How success will be observed: tag exists locally and remotely, points to the
  selected SHA, and selected-tag go/no-go returns `GO`.
- Post-launch learning needed: no

## Deliverable For This Stage

An annotated release tag for the current selected SHA plus synchronized release
truth docs and task/context evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not move `v1.0.0`; preserve it as historical marker truth
- do not create a new code commit or deployment candidate as part of this task

## Implementation Plan

1. Confirm current release docs require a dedicated marker task.
2. Create annotated tag `v1.0.1` for
   `3b46ed3878a8560c3adb147fcadf064818ccc322`.
3. Run selected-tag release go/no-go in monitor mode.
4. Push the tag to `origin`.
5. Update release truth docs and context with exact marker object and evidence.
6. Run diff hygiene.

## Acceptance Criteria
- `v1.0.1` exists as an annotated tag.
- `v1.0.1` points to `3b46ed3878a8560c3adb147fcadf064818ccc322`.
- `v1.0.0` remains unchanged and historical.
- `run_release_go_no_go.py --selected-tag v1.0.1 --monitor-mode` returns
  `verdict=GO`.
- Release docs and context name `v1.0.1` as the current selected-SHA marker.

## Definition of Done
- [x] DEFINITION_OF_DONE.md satisfied for a release-marker-only task.
- [x] Marker created and pushed.
- [x] Verification evidence recorded.
- [x] Relevant source-of-truth docs and context updated.

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
- moving or rewriting `v1.0.0`

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\run_release_go_no_go.py --base-url https://aviary.luckysparrow.ch --selected-tag v1.0.1 --monitor-mode --output ..\.codex\tmp\release-go-no-go-prj1131-v101.json; Pop-Location`
  - result: `verdict=GO`; audit verdict `GO_FOR_SELECTED_SHA`; smoke
    `exit_code=0`; `selected_sha_is_local_head=true`
- Manual checks:
  - `git for-each-ref refs/tags/v1.0.1 --format='%(objectname) %(objecttype) %(*objectname) %(taggerdate:iso8601)'`
  - result: tag object `b016c4f33051805cfa09664f79bbe57f5b30811b`;
    target `3b46ed3878a8560c3adb147fcadf064818ccc322`
  - `git push origin v1.0.1`
  - result: `[new tag] v1.0.1 -> v1.0.1`
- Screenshots/logs: not applicable
- High-risk checks:
  - `v1.0.0` was not moved.
  - no runtime code, environment variables, secrets, or deployment source
    branch changed.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-final-go-no-go-review.md`
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
- Smoke steps updated: yes, selected-tag evidence recorded in release docs
- Rollback note: previous marker `v1.0.0` remains untouched; production can
  still be redeployed to prior known-good SHA if required
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

`v1.0.1` is a release marker for the already deployed selected SHA. It does not
create a new code deployment and does not make extension claims for Telegram
live-mode, organizer provider activation, or AI red-team final scoring.

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
-> validation -> error handling -> test. This task is release-marker-only and
does not change runtime behavior.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator
- Existing workaround or pain: selected SHA was green in production but marker
  decision remained open.
- Smallest useful slice: create a new marker without moving `v1.0.0`.
- Success metric or signal: selected-tag go/no-go returns `GO`.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: release identification and rollback clarity
- SLI: production revision parity for selected tag
- SLO: selected tag target equals production backend and web revision
- Error budget posture: healthy
- Health/readiness check: production `/health` and `/settings` passed through
  release go/no-go wrapper
- Logs, dashboard, or alert route: release go/no-go JSON output
- Smoke command or manual smoke:
  `run_release_go_no_go.py --selected-tag v1.0.1 --monitor-mode`
- Rollback or disable path: retain `v1.0.0`; redeploy previous known-good SHA
  if required

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
- Data classification: public release metadata
- Trust boundaries: Git tag metadata only
- Permission or ownership checks: Git remote accepted tag push
- Abuse cases: avoid rewriting `v1.0.0`; no secrets recorded
- Secret handling: no secrets used or persisted
- Security tests or scans: not applicable
- Fail-closed behavior: no release-marker movement if go/no-go fails
- Residual risk: extension gates remain blocked/follow-up by design

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: created and pushed annotated tag `v1.0.1` for current selected
  SHA `3b46ed3878a8560c3adb147fcadf064818ccc322`.
- Files changed:
  - `.codex/tasks/PRJ-1131-release-marker-for-current-selected-sha.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `docs/planning/v1-release-notes-and-operator-handoff.md`
  - `docs/planning/v1-final-go-no-go-review.md`
- How tested:
  - selected-tag go/no-go returned `GO`
  - tag object/target inspected
  - diff hygiene run
- What is incomplete:
  - Coolify source/webhook automation reliability remains follow-up.
  - Telegram live-mode and organizer provider activation remain blocked
    extension gates.
- Next steps:
  - document Coolify source/webhook automation reliability evidence.
- Decisions made:
  - create `v1.0.1` instead of moving `v1.0.0`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - selected SHA was green in production but lacked a current marker.
- Gaps:
  - release docs still required an explicit marker task.
- Inconsistencies:
  - none after PRJ-1130; the marker gap was explicitly documented.
- Architecture constraints:
  - preserve `v1.0.0`; create or move marker only after green production
    evidence and explicit marker task.

### 2. Select One Priority Task
- Selected task: create the release marker for the current selected SHA.
- Priority rationale: marker gap was the remaining P0 process closure after
  deploy parity and go/no-go were green.
- Why other candidates were deferred:
  - Coolify automation reliability and provider activation are follow-ups and
    do not block the current selected-SHA marker.

### 3. Plan Implementation
- Files or surfaces to modify:
  - Git tag metadata and release truth docs/context.
- Logic:
  - create new tag `v1.0.1`; do not move `v1.0.0`.
- Edge cases:
  - if selected-tag go/no-go failed, the marker would not be treated as
    release truth.

### 4. Execute Implementation
- Implementation notes:
  - annotated tag `v1.0.1` created locally and pushed to `origin`.
  - docs/context updated with exact tag object and target.

### 5. Verify and Test
- Validation performed:
  - selected-tag go/no-go
  - tag object/target inspection
  - tag push confirmation
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - leaving marker decision open; rejected because production proof was already
    green and docs required a dedicated marker task.
- Technical debt introduced: no
- Scalability assessment:
  - future candidates can follow the same release evidence chain.
- Refinements made:
  - preserved `v1.0.0` as historical marker and used a new tag.

### 7. Update Documentation and Knowledge
- Docs updated:
  - release evidence index, release boundary, release audit, reality roadmap,
    release notes, final go/no-go review
- Context updated:
  - task board and project state
- Learning journal updated: not applicable.
