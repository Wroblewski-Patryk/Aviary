# Task

## Header
- ID: PRJ-586
- Title: Add strict release and incident evidence for retrieval-provider alignment
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-585
- Priority: P1

## Context
`PRJ-585` aligned live production retrieval with the approved
`openai_api_embeddings` baseline. Release smoke and behavior validation still
needed to turn that alignment into a strict release gate instead of leaving it
as health-only operator evidence.

## Goal
Make retrieval-provider drift release-blocking across smoke, exported incident
evidence, and CI behavior-validation gate logic.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] release smoke fails on retrieval-provider drift from `/health.memory_retrieval`
- [x] exported `incident_evidence` and incident-evidence bundles fail on retrieval-provider drift
- [x] CI behavior validation fails on invalid retrieval-provider incident-evidence posture

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `.\.venv\Scripts\python -m pytest -q tests/test_deployment_trigger_scripts.py tests/test_behavior_validation_script.py` -> `38 passed`
- Manual checks:
  - `.\scripts\run_behavior_validation.ps1 -GateMode ci -ArtifactPath artifacts/behavior_validation/report.json` -> `12 passed`
  - `.\scripts\run_release_smoke.ps1 -BaseUrl 'https://personality.luckysparrow.ch'` -> passed
- Screenshots/logs:
- High-risk checks:
  - retrieval alignment is now enforced from the same owner-level posture in `/health`, `incident_evidence`, and incident-evidence bundles

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
  - synced in `PRJ-587`

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
The strict gate intentionally reuses the existing `memory_retrieval` posture
instead of creating a second retrieval-release contract.
