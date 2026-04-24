# Task

## Header
- ID: PRJ-594
- Title: Add behavior and smoke evidence for work-partner organizer-tool posture
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-593
- Priority: P1

## Context
The first production organizer-tool stack is now frozen and exposed through
`/health.connectors.organizer_tool_stack`, but release smoke and behavior
validation do not yet prove the same bounded ClickUp/Calendar/Drive posture.

## Goal
Make the organizer-tool production boundary machine-verifiable through release
smoke, incident-evidence surfaces, and behavior-level work-partner scenarios.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] release smoke validates the organizer-tool stack contract from health and incident evidence
- [ ] behavior validation and runtime behavior scenarios prove the bounded work-partner organizer flows
- [ ] task board and project state are updated with validation evidence

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `.\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py tests/test_deployment_trigger_scripts.py tests/test_behavior_validation_script.py tests/test_api_routes.py` -> `228 passed`
  - `.\scripts\run_behavior_validation.ps1 -GateMode ci -ArtifactPath artifacts/behavior_validation/report.json` -> `13 passed`, `gate_status=pass`
- Manual checks:
  - `.\scripts\run_release_smoke.ps1 -BaseUrl 'https://personality.luckysparrow.ch'` currently fails on production because live deploy is still behind the richer learned-state contract (`learned_state inspection_sections` missing), confirming this slice is repo-side complete but not yet deployed
- Screenshots/logs:
- High-risk checks:
  - release smoke now validates organizer-tool stack posture from `/health.connectors.organizer_tool_stack` and from incident-evidence bundle snapshots

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: docs/architecture/16_agent_contracts.md; docs/architecture/17_logging_and_debugging.md; docs/architecture/29_runtime_behavior_testing.md
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
- [x] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
Keep the organizer-tool proof bounded to the frozen first production stack:
ClickUp create/list/update, Google Calendar read availability, and Google Drive
metadata list.
