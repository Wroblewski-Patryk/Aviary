# Task

## Header
- ID: PRJ-577
- Title: Switch production attention ownership to durable inbox
- Status: IN_PROGRESS
- Owner: Backend Builder
- Depends on: PRJ-576
- Priority: P0

## Context
Durable attention cutover criteria are frozen in `PRJ-576`. Production still
uses `ATTENTION_COORDINATION_MODE=in_process`, even though repository-backed
durable inbox is implemented and readiness is green.

## Goal
Switch the production deployment baseline to `ATTENTION_COORDINATION_MODE=durable_inbox`
without regressing Telegram burst coalescing or reply delivery.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Coolify production defaults to `ATTENTION_COORDINATION_MODE=durable_inbox`
- [ ] production `/health.attention` reports repository-backed durable posture
- [ ] release smoke and focused regressions remain green after the switch

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `.\.venv\Scripts\python -m pytest -q tests/test_coolify_compose.py tests/test_api_routes.py tests/test_main_lifespan_policy.py`
  - `docker compose -f docker-compose.coolify.yml config`
- Manual checks:
  - push to `main`
  - verify production `/health.attention`
  - run release smoke against production
- Screenshots/logs:
  - pending
- High-risk checks:
  - verify Telegram round-trip remains healthy after the switch
  - verify no duplicate-reply or burst-assembly regression is visible in smoke

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/operations/runtime-ops-runbook.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
  - not applicable
- Follow-up architecture doc updates:
  - broader docs sync remains in `PRJ-579`

## Review Checklist (mandatory)
- [ ] Architecture alignment confirmed.
- [ ] Existing systems were reused where applicable.
- [ ] No workaround paths were introduced.
- [ ] No logic duplication was introduced.
- [ ] Definition of Done evidence is attached.
- [ ] Relevant validations were run.
- [ ] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
The intended implementation path is deployment-only: change the Coolify
production default, pin the compose regression, deploy, and verify the live
health posture. Broader canonical-doc sync belongs to `PRJ-579`.
