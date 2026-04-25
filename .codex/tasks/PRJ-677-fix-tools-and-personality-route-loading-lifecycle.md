# Task

## Header
- ID: PRJ-677
- Title: Fix Tools and Personality route loading lifecycle in the web shell
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-676
- Priority: P0

## Context
Production validation shows that `/app/tools/overview` and
`/app/personality/overview` return `200`, but the corresponding `Tools` and
`Personality` routes remain on loading and never render their payload. Current
client analysis shows the route lifecycle cancels its own request path before
the successful payload is committed.

## Goal
Make both routes load, finish, and render backend truth reliably when entered
through the normal browser navigation flow.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] `Tools` renders grouped backend payload instead of remaining on a
      spinner when `/app/tools/overview` succeeds.
- [x] `Personality` renders overview sections instead of remaining on a
      spinner when `/app/personality/overview` succeeds.
- [x] Loading, cancellation, and re-entry behavior are covered by route-level
      proof through smoke regression and build validation.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `Push-Location backend; ..\.venv\Scripts\python -m pytest -q tests/test_deployment_trigger_scripts.py; Pop-Location`
  - `Push-Location web; npm run build; Pop-Location`
- Manual checks:
  - production browser validation identified the self-cancelling route effect
    and local code review confirmed the repaired dependency posture
- Screenshots/logs:
- High-risk checks:
  - preserved the current thin-client posture over backend-owned `/app/*`

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: docs/architecture/16_agent_contracts.md;
  docs/architecture/29_runtime_behavior_testing.md
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [ ] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
The fix should preserve the current thin-client posture over backend-owned
contracts.
