# V1 Deployment Trigger SLO Evidence

Date: 2026-05-03
Task: `PRJ-930`
Status: DONE locally with operator-owned production-history proof gap

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

| Evidence | Owner | Current local status |
| --- | --- | --- |
| Coolify deployment history for canonical app | Operator / Coolify UI | UNVERIFIED locally; required before final release declaration when source automation is the claimed path |
| `/health.deployment` policy surface | Backend runtime | Covered by route tests and release-smoke validation |
| Webhook fallback evidence artifact | `backend/scripts/trigger_coolify_deploy_webhook.py` | Covered by script tests; use only when source automation is delayed or missing |
| Release smoke deploy parity | `backend/scripts/run_release_smoke.ps1` / `.sh` | Covered by deployment-trigger script tests and prior production smoke evidence |
| Evidence archive pointer | `docs/planning/v1-release-evidence-archive-standard.md` | Updated for PRJ-930 |

## Primary Path

1. Push `main`.
2. Let Coolify source automation enqueue a deployment for the canonical app:
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

Final production release still requires operator confirmation that Coolify
deployment history for the canonical app contains the intended pushed commit,
unless the release explicitly records webhook/UI fallback as exception-only
recovery evidence.
