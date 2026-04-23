# Task

## Header
- ID: PRJ-582
- Title: Prove proactive delivery and anti-spam behavior in release evidence
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-581
- Priority: P1

## Context
Production proactive is now enabled for the bounded opt-in baseline, but the
shared incident-evidence contract and release-smoke gates still needed to
expose the same proactive posture that behavior validation already proves at the
scenario level.

## Goal
Make release smoke, exported incident evidence, and behavior-validation gating
prove the same proactive production baseline and fail when that posture drifts.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] `incident_evidence` includes shared proactive posture in the required policy surface set
- [x] release smoke fails when proactive health/evidence posture is missing or disabled
- [x] behavior-validation gate fails when exported proactive posture drifts from the production baseline

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `.\.venv\Scripts\python -m pytest -q tests/test_observability_policy.py tests/test_api_routes.py tests/test_deployment_trigger_scripts.py tests/test_behavior_validation_script.py` -> `126 passed`
- Manual checks:
  - `.\scripts\run_behavior_validation.ps1 -GateMode ci -ArtifactPath artifacts/behavior_validation/report.json` -> `12 passed`, `gate_status=pass`
  - `.\scripts\run_release_smoke.ps1 -BaseUrl 'https://personality.luckysparrow.ch'` -> passed
- Screenshots/logs:
  - production `/health.proactive.enabled=true`
  - production `/health.proactive.production_baseline_state=external_scheduler_target_owner`
- High-risk checks:
  - debug/incident evidence stayed aligned with the same proactive policy owner used by `/health`

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/17_logging_and_debugging.md`
  - `docs/architecture/29_runtime_behavior_testing.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:
  - synced in `PRJ-583`

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This slice deliberately widened the existing observability/export contract
instead of introducing a separate proactive-evidence subsystem.
