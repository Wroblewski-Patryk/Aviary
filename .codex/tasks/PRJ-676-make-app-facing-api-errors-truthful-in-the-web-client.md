# Task

## Header
- ID: PRJ-676
- Title: Make app-facing API errors truthful in the web client
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-675
- Priority: P0

## Context
The current shared browser API helper parses every non-empty response body as
JSON. When backend routes fail with plain-text `Internal Server Error`, the
first-party web shell surfaces a JSON parser exception instead of the real
route failure, which hides the actual product issue and makes debugging
misleading.

## Goal
Repair the shared web API helper so the browser client reports app-facing
backend failures truthfully across success, error, empty-body, and non-JSON
error responses.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] Shared client transport logic no longer throws JSON parser noise for
      plain-text backend failures.
- [x] Browser-visible error messages preserve truthful route failure detail or
      a stable fallback instead of parser exceptions.
- [x] Focused regression coverage protects the repaired behavior through
      backend route failures plus web production build validation.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `Push-Location backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py tests/test_web_routes.py tests/test_deployment_trigger_scripts.py; Pop-Location`
  - `Push-Location web; npm run build; Pop-Location`
- Manual checks:
  - production probing confirmed plain-text `Internal Server Error` responses
    are now handled intentionally in the shared helper code path
- Screenshots/logs:
- High-risk checks:
  - no route-specific parsing branch was introduced

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: docs/architecture/16_agent_contracts.md;
  docs/architecture/27_codex_instructions.md
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
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
The repair must stay inside the existing web transport helper instead of
creating route-specific parsing paths.
