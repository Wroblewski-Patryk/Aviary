# Task

## Header
- ID: PRJ-581
- Title: Enable bounded proactive follow-up in production
- Status: IN_PROGRESS
- Owner: Backend Builder
- Depends on: PRJ-580
- Priority: P1

## Context
The production policy is now frozen for bounded proactive follow-up, but the
repo-driven Coolify baseline still defaults `PROACTIVE_ENABLED` to `false`.
That leaves live `/health.proactive` in `disabled_by_policy` posture even
though the no-UI `v1` workflow baseline already depends on scheduler-owned
opt-in follow-up.

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
- [ ] repository-driven Coolify production defaults proactive follow-up to enabled
- [ ] relevant regression coverage pins the production compose baseline
- [ ] live production `/health.proactive` no longer reports `disabled_by_policy`

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks:
- Screenshots/logs:
- High-risk checks:

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
- Fits approved architecture: yes | no
- Mismatch discovered: yes | no
- Decision required from user: yes | no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

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
Implementation should stay repo-driven through `docker-compose.coolify.yml` and
must not create a production-only side path outside the existing Coolify
baseline.
