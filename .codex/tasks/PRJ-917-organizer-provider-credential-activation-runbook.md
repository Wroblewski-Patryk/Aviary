# Task

## Header
- ID: PRJ-917
- Title: Organizer Provider Credential Activation Runbook
- Task Type: operations
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-916
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 917
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The web product-honesty lane is complete locally. Organizer daily-use remains
blocked by provider credential activation for ClickUp, Google Calendar, and
Google Drive.

## Goal
Turn the organizer provider credential gap into an explicit operator runbook
with required settings, expected health transitions, smoke expectations, and
rollback.

## Scope
- `docs/operations/organizer-provider-activation-runbook.md`
- `docs/operations/runtime-ops-runbook.md`
- `.codex/tasks/PRJ-917-organizer-provider-credential-activation-runbook.md`
- `docs/planning/v1-organizer-provider-credential-activation-runbook.md`
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `docs/planning/v1-core-acceptance-bundle.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: provider activation should be an explicit,
  repeatable operator path, not tribal memory or a hidden code assumption.
- Expected product or reliability outcome: missing provider settings map to a
  concrete checklist before `PRJ-918` attempts live provider smoke.
- How success will be observed: production health snapshot is reviewed,
  runbook exists, runtime ops runbook links to it, and diff check passes.
- Post-launch learning needed: no

## Deliverable For This Stage
An operator runbook and release-plan updates. No secrets were added.

## Constraints
- do not store provider secrets in the repo
- do not mutate production settings from this task
- do not claim organizer daily-use readiness before provider smoke
- preserve user opt-in and mutation confirmation boundaries

## Implementation Plan
1. Inspect production `/health.connectors.organizer_tool_stack`.
2. Extract required provider settings and readiness transitions.
3. Document ClickUp, Google Calendar, and Google Drive activation.
4. Link the runbook from the runtime ops runbook.
5. Update planning and context docs.
6. Run `git diff --check`.

## Acceptance Criteria
- Required settings are listed for ClickUp, Google Calendar, and Google Drive.
- Expected health fields and transitions are documented.
- User opt-in and mutation confirmation boundaries are explicit.
- `PRJ-918` smoke expectations are listed.
- Rollback steps are documented.

## Definition of Done
- [x] Production organizer health snapshot was reviewed.
- [x] Activation runbook was created.
- [x] Runtime ops runbook links to the activation runbook.
- [x] Context and planning docs were updated.
- [x] `git diff --check` passed.

## Validation Evidence
- Tests:
  - `Invoke-RestMethod https://aviary.luckysparrow.ch/health`
  - result: production organizer stack reports `provider_credentials_missing`,
    `provider_ready_operation_count=0`, `provider_total_operation_count=5`,
    and `daily_use_workflows_blocked_by_provider_activation`
  - `git diff --check`
  - result: passed
- High-risk checks:
  - no provider secret values were added to the repository
  - production settings were not mutated

## Result Report

- Task summary: created a provider activation runbook for ClickUp, Google
  Calendar, and Google Drive.
- Files changed:
  - `docs/operations/organizer-provider-activation-runbook.md`
  - `docs/operations/runtime-ops-runbook.md`
  - `.codex/tasks/PRJ-917-organizer-provider-credential-activation-runbook.md`
  - `docs/planning/v1-organizer-provider-credential-activation-runbook.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `docs/planning/v1-core-acceptance-bundle.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Tests run:
  - production `/health` organizer snapshot review
  - `git diff --check`
- Deployment impact: documentation only.
- Next tiny task: `PRJ-918` Organizer Provider Activation Smoke, blocked until
  provider credentials are configured.
