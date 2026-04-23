# Task

## Header
- ID: PRJ-580
- Title: Freeze the proactive opt-in production policy baseline
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-579
- Priority: P1

## Context
Production cadence ownership is already externalized, but `/health.proactive`
still reports `production_baseline_state=disabled_by_policy`. That no longer
matches the bounded no-UI `v1` workflow contract, where reminder capture and
follow-up must become production reality through the existing scheduler,
attention, planning, and action boundary.

## Goal
Record one explicit production baseline for bounded proactive follow-up before
runtime activation and release-evidence widening begin.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] one explicit policy records that production proactive is enabled only for bounded opt-in follow-up
- [x] delivery-target, anti-spam, and rollback posture are frozen in canonical docs, planning, and context truth
- [x] the next runtime slice can implement activation against one explicit policy instead of inferred product intent

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - none; planning and policy-freeze slice
- Manual checks:
  - reviewed `docs/architecture/16_agent_contracts.md`
  - reviewed `docs/architecture/10_future_vision.md`
  - reviewed `docs/operations/runtime-ops-runbook.md`
  - reviewed live `GET https://personality.luckysparrow.ch/health`
- Screenshots/logs:
  - live `/health.proactive.production_baseline_state=disabled_by_policy`
  - live `/health.proactive.delivery_target_baseline=recent_telegram_chat_or_numeric_user_id_fallback`
  - live `/health.proactive.candidate_selection_baseline=opted_in_users_with_active_work_or_time_checkin`
- High-risk checks:
  - confirmed external scheduler ownership is already proven before enabling outreach
  - confirmed reminder and check-in workflow architecture already depends on proactive follow-up

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/10_future_vision.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/operations/runtime-ops-runbook.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: n/a
- Follow-up architecture doc updates:
  - bounded proactive production baseline frozen for no-UI `v1`

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
Frozen production proactive baseline:

- production target:
  - `PROACTIVE_ENABLED=true`
  - scheduler cadence owner remains `external_scheduler`
- bounded eligibility:
  - explicit `proactive_opt_in` remains mandatory
  - candidate selection stays limited to opted-in users with active work or
    time-checkin triggers
  - delivery remains bounded to Telegram direct messages using recent Telegram
    chat id or the existing numeric user-id fallback
- bounded guardrails:
  - keep the current anti-spam contract as the minimum production baseline
  - keep attention-gate and delivery-guard ownership unchanged
- rollback posture:
  - return production to `PROACTIVE_ENABLED=false`
  - treat `disabled_by_policy` as the explicit safe rollback baseline if
    outreach drift, spam posture, or delivery-target ambiguity appears
