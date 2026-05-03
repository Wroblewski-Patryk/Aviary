# V1 Deployment Trigger SLO Evidence

Date: 2026-05-04
Task: `PRJ-930`, refreshed by `PRJ-1132`
Status: current `v1.0.1` release parity green; source/webhook reliability is a future-candidate follow-up

## Purpose

This document collects the release-facing evidence for the Coolify
deployment-trigger SLO. It does not introduce a new deployment system. It ties
together the existing deployment policy, webhook fallback evidence, release
smoke, and release archive rules.

## SLO Baseline

The machine-visible baseline is exposed through `/health.deployment` by
`backend/app/core/deployment_policy.py`:

| Field | Expected value |
| --- | --- |
| `deployment_automation_policy_owner` | `coolify_repo_deploy_automation` |
| `runtime_trigger_mode` | `source_automation` for the primary path |
| `runtime_trigger_class` | `primary_automation` for the primary path |
| `deployment_automation_baseline.primary_trigger_mode` | `source_automation` |
| `deployment_automation_baseline.fallback_trigger_modes` | `webhook_manual_fallback`, `ui_manual_fallback` |
| `deployment_trigger_slo.delivery_success_rate_percent` | `99.0` |
| `deployment_trigger_slo.manual_redeploy_exception_rate_percent` | `5.0` |
| `deployment_trigger_slo.evidence_owner` | `coolify_webhook_plus_release_smoke` |

## Evidence Classes

| Evidence | Owner | Current status |
| --- | --- | --- |
| Coolify deployment history for canonical app | Operator / Coolify UI | VERIFIED for PRJ-1128 UI fallback recovery; source automation did not converge during PRJ-1125 |
| `/health.deployment` policy surface | Backend runtime | Covered by route tests and release-smoke validation |
| Webhook fallback evidence artifact | `backend/scripts/trigger_coolify_deploy_webhook.py` | Covered by script tests; currently blocked locally by missing webhook URL and secret |
| Release smoke deploy parity | `backend/scripts/run_release_smoke.ps1` / `.sh` | Passed for current selected SHA and tag `v1.0.1` |
| Evidence archive pointer | `docs/planning/v1-release-evidence-archive-standard.md` | Updated for PRJ-930 |

## Current V1.0.1 Evidence

`v1.0.1` is the current selected-SHA release marker:

- selected SHA:
  `3b46ed3878a8560c3adb147fcadf064818ccc322`
- tag object:
  `b016c4f33051805cfa09664f79bbe57f5b30811b`
- production backend revision:
  `3b46ed3878a8560c3adb147fcadf064818ccc322`
- production web meta revision:
  `3b46ed3878a8560c3adb147fcadf064818ccc322`
- selected-tag go/no-go:
  `run_release_go_no_go.py --selected-tag v1.0.1 --monitor-mode` ->
  `verdict=GO`, audit `GO_FOR_SELECTED_SHA`, smoke `exit_code=0`

For this candidate, deployment-trigger evidence is:

1. PRJ-1125: push to `origin/main` did not converge through source automation
   within the bounded deploy-parity wait.
2. PRJ-1128: approved Coolify UI fallback on canonical app
   `jr1oehwlzl8tcn3h8gh2vvih` deployed commit `3b46ed3` successfully.
3. PRJ-1131: `v1.0.1` was created only after release audit and release smoke
   were green.
4. PRJ-1132: webhook fallback readiness is still `blocked` until
   `COOLIFY_DEPLOY_WEBHOOK_URL` and `COOLIFY_DEPLOY_WEBHOOK_SECRET` are
   available to the operator task.

This means the current release is green, but future selected candidates should
not claim source/webhook automation reliability until Coolify source history or
webhook fallback evidence proves that path for the new candidate.

## Primary Path

1. Push `main`.
2. Let Coolify source automation enqueue a deployment for the canonical app:
   - source repository: `Wroblewski-Patryk/Aviary`
   - note: `Personality` is the former repository name, not the active
     production deploy source
   - project: `icmgqml9uw3slzch9m9ok23z`
   - environment: `qxooi9coxat272krzjx221fv`
   - application: `jr1oehwlzl8tcn3h8gh2vvih`
3. Verify the pushed commit in Coolify deployment history.
4. Run release smoke with deploy parity:

```powershell
.\backend\scripts\run_release_smoke.ps1 `
  -BaseUrl "https://aviary.luckysparrow.ch" `
  -WaitForDeployParity `
  -DeployParityMaxWaitSeconds 900 `
  -DeployParityPollSeconds 30 `
  -HealthRetryMaxAttempts 10 `
  -HealthRetryDelaySeconds 10
```

## PRJ-952 Operator Preflight

Before recovering Coolify source automation or using the exception-only
fallback for a post-v1 candidate, freeze the selected SHA. Do not trigger a
deploy for `HEAD` if the intended release scope still exists only as
uncommitted local changes.

Historical PRJ-1115/PRJ-1121 posture:

- deployed `v1.0.0` selected SHA:
  `5e64f494e2aac8d29cea532d95f7039ed6029213`
- local `HEAD` before this preflight:
  `5ff12953289bbca680fd5d9f8b3d8780a8f4be55`
- local worktree has uncommitted post-v1 hardening/docs/frontend changes
- fallback readiness is blocked until an operator provides webhook URL and
  webhook secret

Current operator sequence for the next selected candidate:

1. Decide whether the next candidate is the current committed `HEAD` or a new
   commit that includes the local working-tree changes.
2. If the local working tree is part of the release, commit and push that exact
   scope first.
3. Record the selected `after_sha` and its `before_sha`.
4. Run the read-only fallback readiness check:

```powershell
Push-Location .\backend
..\.venv\Scripts\python .\scripts\check_coolify_fallback_readiness.py `
  --after-sha "<selected_after_sha>" `
  --before-sha "<selected_before_sha>" `
  --print-json
Pop-Location
```

5. Prefer Coolify source automation if it enqueues the selected SHA.
6. If source automation is missing or delayed and the operator provides
   `COOLIFY_DEPLOY_WEBHOOK_URL` plus `COOLIFY_DEPLOY_WEBHOOK_SECRET`, run the
   existing webhook fallback for the same selected SHA:

```powershell
.\backend\scripts\trigger_coolify_deploy_webhook.ps1 `
  -WebhookUrl "<coolify_webhook_url>" `
  -WebhookSecret "<coolify_webhook_secret>" `
  -Repository "Wroblewski-Patryk/Aviary" `
  -Branch "main" `
  -BeforeSha "<selected_before_sha>" `
  -AfterSha "<selected_after_sha>" `
  -EvidencePath "artifacts/deploy/coolify-webhook.json"
```

7. Rerun production release smoke with deploy parity and fallback evidence when
   available:

```powershell
.\backend\scripts\run_release_smoke.ps1 `
  -BaseUrl "https://aviary.luckysparrow.ch" `
  -DeploymentEvidencePath "artifacts/deploy/coolify-webhook.json" `
  -WaitForDeployParity `
  -DeployParityMaxWaitSeconds 900 `
  -DeployParityPollSeconds 30 `
  -HealthRetryMaxAttempts 10 `
  -HealthRetryDelaySeconds 10
```

Only after backend revision, web revision, release readiness, and release smoke
all match the selected SHA should release marker work move forward for a future
candidate. `v1.0.1` already satisfies that requirement for
`3b46ed3878a8560c3adb147fcadf064818ccc322`.

## Exception-Only Fallback

Manual redeploy is not primary proof that source automation is healthy. Use it
only when source automation is delayed or missing.

Fallback order:

1. Trigger the existing Coolify deploy webhook helper and capture evidence:

```powershell
.\backend\scripts\trigger_coolify_deploy_webhook.ps1 `
  -EvidencePath "artifacts/deploy/coolify-webhook.json"
```

2. If webhook trigger is unavailable, use Coolify UI redeploy for the same
   canonical app.
3. Run release smoke and include the fallback evidence artifact when available:

```powershell
.\backend\scripts\run_release_smoke.ps1 `
  -BaseUrl "https://aviary.luckysparrow.ch" `
  -DeploymentEvidencePath "artifacts/deploy/coolify-webhook.json" `
  -WaitForDeployParity
```

When `trigger_class=manual_fallback`, the evidence proves bounded recovery
posture, not source-automation reliability.

## Local Validation

Focused command:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_deployment_trigger_scripts.py -k "deployment_evidence or deploy_parity or runtime_build_revision or trigger_main or backend_operator_scripts"; Pop-Location
```

Result: `20 passed, 32 deselected`.

Expected coverage:

- webhook trigger helper writes success evidence
- webhook trigger helper writes failure evidence and returns non-zero
- release smoke verifies fresh successful deployment evidence
- release smoke rejects stale or unsuccessful deployment evidence
- release smoke checks runtime build revision and deploy parity
- release smoke waits for deploy parity when requested
- backend operator scripts expose help from the backend working directory

## Release Posture

PRJ-930 is locally closed because the SLO, evidence schema, fallback posture,
and release-smoke enforcement are documented and regression-covered.

For `v1.0.1`, final production release evidence records UI fallback as the
exception-only recovery path. The next selected candidate should either prove
that Coolify source automation enqueued and deployed the pushed commit, or
capture webhook fallback evidence with the existing helper before release
smoke.
