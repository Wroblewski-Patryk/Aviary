# Task

## Header
- ID: PRJ-631
- Title: Add end-to-end daily-use scenarios for conversation, web reading, learning, and organizer posture
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-630
- Priority: P0

## Context
The final acceptance bundle needs scenario-level proof that the personality behaves like a usable daily assistant, not just a healthy runtime with many separate proofs.

## Goal
Add final end-to-end no-UI `v1` daily-use scenarios.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] Behavior validation covers final daily-use `v1` scenarios.
- [x] The scenarios include conversation, website reading, bounded learning reuse, and organizer help.
- [x] Evidence is suitable for final no-UI `v1` acceptance.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: `.\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k "tool_grounded_learning_scenarios or final_v1_daily_use_scenarios"` and `.\.venv\Scripts\python -m pytest -q tests/test_behavior_validation_script.py tests/test_api_routes.py`
- Manual checks: `.\scripts\run_behavior_validation.ps1 -GateMode ci -ArtifactPath artifacts/behavior_validation/report.json`
- Screenshots/logs:
- High-risk checks: keep scenarios within approved provider/tool boundaries and truthful learning semantics

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/29_runtime_behavior_testing.md`, `docs/architecture/10_future_vision.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: testing guidance and possibly product docs

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
The target is a believable "this personality can help me today" scenario set.
