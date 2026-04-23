# Task

## Header
- ID: PRJ-581
- Title: Enable bounded proactive follow-up in production
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-580
- Priority: P1

## Context
The production policy is now frozen for bounded proactive follow-up, but the
repo-driven Coolify baseline needed to move from `PROACTIVE_ENABLED=false` to
an enabled-by-default bounded follow-up posture. Production also had an
explicit Coolify env override that masked the repo-driven baseline until the
runtime cutover was verified live.

## Goal
Switch the production deployment baseline to bounded proactive follow-up while
keeping the existing external-scheduler cadence owner and current anti-spam
guardrails intact.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] repository-driven Coolify production defaults proactive follow-up to enabled
- [x] relevant regression coverage pins the production compose baseline
- [x] live production `/health.proactive` no longer reports `disabled_by_policy`

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `.\.venv\Scripts\python -m pytest -q tests/test_coolify_compose.py tests/test_api_routes.py tests/test_scheduler_worker.py` -> `105 passed`
- Manual checks:
  - `docker compose -f docker-compose.coolify.yml config` -> OK
  - production `GET /health` after Coolify redeploy shows:
    - `/health.proactive.enabled=true`
    - `/health.proactive.policy_owner=proactive_runtime_policy`
    - `/health.proactive.production_baseline_ready=true`
    - `/health.proactive.production_baseline_state=external_scheduler_target_owner`
    - `/health.scheduler.external_owner_policy.proactive_run_evidence.evidence_state=recent_external_run_evidence`
- Screenshots/logs:
  - Coolify production env override `PROACTIVE_ENABLED=false` had to be removed or changed to `true` so the repo-driven baseline could apply
- High-risk checks:
  - proactive activation stayed under the existing external scheduler owner and anti-spam contract
  - Telegram round-trip readiness remained healthy while proactive became enabled

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/26_env_and_config.md`
  - `docs/operations/runtime-ops-runbook.md`
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
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
Implementation should stay repo-driven through `docker-compose.coolify.yml` and
must not create a production-only side path outside the existing Coolify
baseline. The final production proof required both the repo default and the
removal of a conflicting Coolify env override.
