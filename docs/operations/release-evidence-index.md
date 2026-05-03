# Release Evidence Index

Last updated: 2026-05-03

## Purpose

This index is the operator-facing release truth table for the current v1 lane.
It does not replace release smoke, incident evidence, or behavior validation.
It points to the latest committed proof surfaces and records what is currently
deployed.

## Current Snapshot

| Field | Value |
| --- | --- |
| Local branch | `main` |
| Local development `HEAD` before this index update | `5ff12953289bbca680fd5d9f8b3d8780a8f4be55` |
| Local relation to `origin/main` | ahead by 86 commits at refresh |
| Release tag | `v1.0.0` |
| Release tag object | `b5d8379df1898aa5533bd72a7a1631d6044f2125` |
| Release tag target commit | `5e64f494e2aac8d29cea532d95f7039ed6029213` |
| Production backend revision | `5e64f494e2aac8d29cea532d95f7039ed6029213` |
| Production web meta revision | `5e64f494e2aac8d29cea532d95f7039ed6029213` |
| Production health | `status=ok` |
| Production release readiness | `ready=true` |
| Production v1 final acceptance | `core_v1_bundle_ready` |
| Production deploy parity | `deploy_parity_surface_ready` |
| Local `HEAD` release verdict | `HOLD_REVISION_DRIFT` |
| Current workspace local validation | `passed`; backend pytest, web build, route smoke, focused web characterizations |
| Current packaged candidate SHA | pushed packaging `HEAD`; resolve with `git rev-parse HEAD` after final amend/push |
| Coolify fallback readiness | `blocked`; missing webhook URL and secret |
| Organizer daily-use extension | `daily_use_workflows_blocked_by_provider_activation` |

## Current Decision

The deployed `v1.0.0` release marker is still coherent with production because
backend and web both report the tag target commit
`5e64f494e2aac8d29cea532d95f7039ed6029213`.

Local `main` has moved ahead after post-v1 hardening and web-confidence work.
This document update will itself advance local `HEAD` once committed. Those
newer commits must not inherit the `v1.0.0` production acceptance claim until
they are pushed, deployed, and proven by fresh release smoke.

PRJ-1115 refreshed the release evidence after frontend presentation cleanup:
the deployed `v1.0.0` marker still receives a monitor-mode `GO`, while local
`HEAD` receives `HOLD_REVISION_DRIFT` because production backend and web
revisions remain on the `v1.0.0` target commit.

## Required Proof Chain For A New Candidate

1. Select the intended candidate commit.
2. Push the candidate commit to the deployment source.
3. Confirm production backend revision and web meta revision both match the
   candidate.
4. Run production release smoke with deploy parity.
5. Refresh incident-evidence and behavior-validation pointers if the release
   claim depends on them.
6. Update this index with exact SHA, command evidence, blockers, and next
   action.
7. Create or move a release marker only after the selected SHA is green in
   production.

## Current Blockers

| Blocker | Scope | State | Next Action |
| --- | --- | --- | --- |
| New local commits are not deployed | Release marker for current `HEAD` | BLOCKED | Push/deploy selected candidate, then run release smoke |
| Candidate SHA is not frozen for local working-tree changes | Future marker for post-v1 work | BLOCKED | Commit/push intended scope before triggering source automation or fallback |
| Coolify manual fallback inputs | Deploy fallback for current `HEAD` | BLOCKED_EXTERNAL | Provide webhook URL and webhook secret before triggering fallback |
| Telegram live-mode smoke | Launch-channel extension | BLOCKED_EXTERNAL | Provide operator token, webhook secret, and known chat id |
| Organizer provider activation smoke | Organizer daily-use extension | BLOCKED_EXTERNAL | Configure ClickUp, Google Calendar, and Google Drive credentials |
| AI red-team final scoring | Security evidence | REVIEW_REQUIRED | Use a text-capturing app-chat or authorized incident-evidence runner |

## Proof Sources

| Evidence | Source |
| --- | --- |
| Release smoke and deploy parity | `backend/scripts/run_release_smoke.ps1` |
| Release reality audit | `backend/scripts/audit_release_reality.py` |
| Release go/no-go wrapper | `backend/scripts/run_release_go_no_go.py` |
| Coolify fallback readiness | `backend/scripts/check_coolify_fallback_readiness.py` |
| Release archive standard | `docs/planning/v1-release-evidence-archive-standard.md` |
| V1 reality roadmap | `docs/planning/v1-reality-audit-and-roadmap.md` |
| Runtime ops runbook | `docs/operations/runtime-ops-runbook.md` |
| Current release boundary | `docs/planning/current-v1-release-boundary.md` |
| Production backend revision | `GET https://aviary.luckysparrow.ch/health` |
| Production web revision | `GET https://aviary.luckysparrow.ch/settings` meta `aion-web-build-revision` |

## Refresh Commands

```powershell
git rev-parse HEAD
git for-each-ref refs/tags/v1.0.0 --format='%(objectname) %(objecttype) %(*objectname)'
$health = Invoke-RestMethod -Uri 'https://aviary.luckysparrow.ch/health' -TimeoutSec 30
$health.deployment.runtime_build_revision
$health.release_readiness.ready
$health.v1_readiness.final_acceptance_state
curl.exe -s -L --max-time 30 https://aviary.luckysparrow.ch/settings
Push-Location .\backend; ..\.venv\Scripts\python .\scripts\check_coolify_fallback_readiness.py --print-json; Pop-Location
Push-Location .\backend; ..\.venv\Scripts\python .\scripts\run_release_go_no_go.py --base-url https://aviary.luckysparrow.ch --selected-tag v1.0.0 --monitor-mode; Pop-Location
```

## Latest Refresh Evidence

- `git rev-parse HEAD` before this index update:
  `5ff12953289bbca680fd5d9f8b3d8780a8f4be55`
- `git status --short --branch`: `main...origin/main [ahead 86]`
- `GET /health.status`: `ok`
- `GET /health.deployment.runtime_build_revision`:
  `5e64f494e2aac8d29cea532d95f7039ed6029213`
- `GET /health.release_readiness.ready`: `true`
- `GET /health.v1_readiness.final_acceptance_state`:
  `core_v1_bundle_ready`
- `GET /settings` web meta revision:
  `5e64f494e2aac8d29cea532d95f7039ed6029213`
- `run_release_go_no_go.py --selected-tag v1.0.0 --monitor-mode`:
  `verdict=GO`; release smoke was skipped because the selected tag differs
  from local `HEAD` and `run_release_smoke.ps1` is local-HEAD-bound
- `audit_release_reality.py` for local `HEAD`:
  `verdict=HOLD_REVISION_DRIFT`; selected SHA
  `5ff12953289bbca680fd5d9f8b3d8780a8f4be55`, production backend and web
  revisions `5e64f494e2aac8d29cea532d95f7039ed6029213`
- `check_coolify_fallback_readiness.py --print-json`:
  `ready=false`; missing `webhook_url`, `webhook_secret_present`, and
  `webhook_secret_length`
- `pytest -q tests/test_deployment_trigger_scripts.py`:
  `64 passed`
- PRJ-1121 operator preflight:
  do not trigger Coolify fallback for an inferred `HEAD` unless that SHA is the
  selected pushed candidate; if the current working-tree changes are part of
  the release, commit and push them first, then rerun fallback readiness,
  deploy parity, and release smoke for the new selected SHA
- PRJ-1122 local validation refresh:
  - backend baseline:
    `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location`
    -> `1045 passed`
  - web build:
    `Push-Location .\web; npm run build; Pop-Location` -> passed
  - tools directory characterization:
    `Push-Location .\web; npm run test:tools-directory; Pop-Location` ->
    `status=ok`
  - chat transcript characterization:
    `Push-Location .\web; npm run test:chat-transcript; Pop-Location` ->
    `status=ok`
  - route smoke:
    `Push-Location .\web; npm run smoke:routes; Pop-Location` ->
    `status=ok`, `route_count=14`
  - diff hygiene:
    `git diff --check` -> passed
- PRJ-1124 candidate packaging:
  - selected candidate SHA: pushed packaging `HEAD`; resolve with
    `git rev-parse HEAD` after final amend/push
  - included audited scope from
    `docs/planning/current-workspace-candidate-scope-audit.md`
  - excluded `.codex/tmp/` and `artifacts/`
  - pushed to `origin/main`
  - next action: recover Coolify source automation or approved fallback for
    this SHA, then run production release smoke with deploy parity
