# Task

## Header
- ID: PRJ-767
- Title: Freeze Aviary production host baseline
- Task Type: release
- Current Stage: implementation
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-766
- Priority: P1

## Context
The repo already serves the first-party web shell and backend routes from one
same-origin deployment surface. The new production host rename should preserve
that approved shape and must not introduce a separate API subdomain or new
cross-origin runtime path.

## Goal
Replace the active production-host baseline from
`personality.luckysparrow.ch` to `aviary.luckysparrow.ch` in current
operator-facing repo truth, while keeping the existing same-origin deploy
contract intact.

## Deliverable For This Stage
Updated operator and planning documentation plus context truth that now treat
`https://aviary.luckysparrow.ch` as the canonical production web/app host and
explicitly note that Telegram webhook routing should remain on `/event` under
that same host.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] Active repo truth points production smoke examples to `https://aviary.luckysparrow.ch`
- [x] Same-origin deployment posture is recorded explicitly
- [x] Telegram webhook target guidance is aligned to the renamed host

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
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_deployment_trigger_scripts.py tests/test_api_routes.py; Pop-Location`
  - `Push-Location .\web; npm run build; Pop-Location`
- Manual checks:
  - verified the repo remains same-origin by design (`web` uses relative `/app`, `/health`, `/event`, `/internal` paths and backend serves the SPA)
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - confirmed no separate `api.aviary.luckysparrow.ch` path is required for the approved deploy shape

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/26_env_and_config.md`
  - `docs/operations/runtime-ops-runbook.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
  - not applicable
- Follow-up architecture doc updates:
  - none

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes:
  - no new env vars required
  - existing Telegram webhook should be re-pointed to `https://aviary.luckysparrow.ch/event`
- Health-check impact:
  - release smoke should now target `https://aviary.luckysparrow.ch`
- Smoke steps updated:
  - yes
- Rollback note:
  - if DNS or proxy cutover misbehaves, temporarily point the hostname back to the previous runtime target and restore the previous Telegram webhook URL until the new host is healthy

## Review Checklist (mandatory)
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
- Assumption: the production deploy remains same-origin and should not add a
  separate API hostname.
