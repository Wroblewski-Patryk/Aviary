# Task

## Header
- ID: PRJ-598
- Title: Add machine-visible release evidence for deployment automation posture
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-597
- Priority: P0

## Context
Coolify deployment automation now has a frozen canonical baseline, but release
truth still cannot distinguish between the primary source-driven automation
path and bounded fallback paths such as webhook or manual UI redeploy.

## Goal
Make deployment provenance machine-visible through shared runtime, release
smoke, and incident-evidence surfaces without introducing a new deploy system
or bypassing the current Coolify contract.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] `/health.deployment` exposes the canonical deployment-automation owner and trigger baseline.
- [ ] deploy evidence artifacts record trigger provenance and canonical Coolify app identity.
- [ ] release smoke and incident-evidence checks fail clearly when deployment provenance is missing or ambiguous.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `.\.venv\Scripts\python -m pytest -q tests/test_observability_policy.py tests/test_api_routes.py tests/test_deployment_trigger_scripts.py` -> `115 passed`
- Manual checks:
  - `.\scripts\run_release_smoke.ps1 -BaseUrl 'https://personality.luckysparrow.ch'` now fails fast on old production with `deployment is missing deployment_automation_policy_owner`, proving missing deploy provenance is no longer silently accepted
- Screenshots/logs:
- High-risk checks:
  - deploy webhook evidence now records trigger provenance and canonical Coolify app identity
  - release smoke now validates deployment automation posture from `/health`, deploy evidence artifacts, and incident-evidence payloads or bundles

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/operations/runtime-ops-runbook.md`, `docs/architecture/17_logging_and_debugging.md`
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
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
Primary proof still belongs to source automation plus Coolify deploy history.
Fallback evidence is explicitly bounded to webhook and manual UI deploy flows.
