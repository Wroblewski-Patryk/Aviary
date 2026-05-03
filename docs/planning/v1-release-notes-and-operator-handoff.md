# V1 Release Notes And Operator Handoff

Date: 2026-05-03
Task: `PRJ-935` / `PRJ-955`
Posture: `v1.0.0` released for core no-UI/web-supported v1

## Current Decision

Release marker `v1.0.0` has been created for the selected production SHA after
release reality audit and release smoke passed.

| Revision | SHA |
| --- | --- |
| Current local `HEAD` at PRJ-934 review | `92f7bf3af16502a1a3f661aa16bf6a9ead92e0cd` |
| Production `/health.deployment.runtime_build_revision` at PRJ-934 review | `ed1c4d981314787d76252985b53c14ea1d7886ed` |
| Production web shell build revision at PRJ-934 review | `ed1c4d981314787d76252985b53c14ea1d7886ed` |
| Selected `v1.0.0` SHA | `5e64f494e2aac8d29cea532d95f7039ed6029213` |
| Release reality audit | `GO_FOR_SELECTED_SHA` |
| Production release smoke | PASSED |

## What Is Ready

- Core no-UI v1 behavior has documented acceptance evidence.
- Production health exposes green core final-acceptance gate states for the
  deployed SHA.
- Runtime and web shell revision surfaces are machine-readable.
- Strict-mode incident evidence export has a production-safe health-snapshot
  fallback.
- Rollback and recovery drill is documented.
- Deployment-trigger SLO evidence and exception-only fallback posture are
  documented.
- Provider payload leakage audit is complete locally, and the confirmed
  proposal-payload projection issue is fixed.
- Cross-user/session isolation audit is complete locally.
- AI red-team scenario pack exists as reproducible input.
- External health monitor automation exists for hourly production `/health`
  observation.

## Known Limits

- `v1.0.0` is deployed and smoke-verified; later commits still require their
  own deploy parity evidence before being claimed as production.
- PRJ-909 Telegram live-mode smoke is blocked until an operator provides:
  - `TELEGRAM_BOT_TOKEN`
  - `TELEGRAM_WEBHOOK_SECRET`
  - known `REQUIRED_CHAT_ID`
- PRJ-918 organizer provider activation smoke is blocked until ClickUp, Google
  Calendar, and Google Drive credentials are configured.
- PRJ-931 is a scenario pack only; pass/fail AI red-team execution is still a
  separate evidence item or explicit waiver.
- PRJ-932 and PRJ-933 intentionally leave follow-up regression/evidence gaps
  documented for deeper two-user, provider, incident-sentinel, and frontend
  fixture checks.
- Direct Coolify deployment-history confirmation remains operator-owned.
- PRJ-955 created the `v1.0.0` release marker after the selected release SHA had
  green production evidence.

## Required Before Release Marker

1. Choose the target release SHA.
2. If the target is the current local candidate, deploy it.
3. Confirm production `/health.deployment.runtime_build_revision` matches the
   target SHA.
4. Confirm production web shell meta `aion-web-build-revision` matches the
   backend revision.
5. Run production release smoke with deploy parity.
6. Export or reference the current incident evidence bundle when relevant.
7. Decide whether blocked launch-channel evidence is accepted as blocked,
   waived, or required before the public claim.
8. Create PRJ-936 release marker only after the selected SHA has green evidence.

## Production Smoke

Use this when validating the selected release SHA:

```powershell
.\backend\scripts\run_release_smoke.ps1 `
  -BaseUrl "https://aviary.luckysparrow.ch" `
  -WaitForDeployParity `
  -DeployParityMaxWaitSeconds 900 `
  -DeployParityPollSeconds 30 `
  -HealthRetryMaxAttempts 10 `
  -HealthRetryDelaySeconds 10
```

When a strict-mode incident evidence bundle is part of the decision:

```powershell
.\backend\scripts\run_release_smoke.ps1 `
  -BaseUrl "https://aviary.luckysparrow.ch" `
  -IncidentEvidenceBundlePath "<bundle-dir>" `
  -WaitForDeployParity
```

When source automation is delayed and webhook fallback is used:

```powershell
.\backend\scripts\trigger_coolify_deploy_webhook.ps1 `
  -EvidencePath "artifacts/deploy/coolify-webhook.json"

.\backend\scripts\run_release_smoke.ps1 `
  -BaseUrl "https://aviary.luckysparrow.ch" `
  -DeploymentEvidencePath "artifacts/deploy/coolify-webhook.json" `
  -WaitForDeployParity
```

Webhook/UI fallback is recovery evidence only. It is not proof that source
automation is healthy.

## Incident Evidence

Use the production-safe strict-mode bundle export path when debug payload access
is disabled:

```powershell
Push-Location .\backend
..\.venv\Scripts\python .\scripts\export_incident_evidence_bundle.py `
  --base-url "https://aviary.luckysparrow.ch" `
  --capture-mode incident `
  --trace-id "<incident-or-release-id>" `
  --output-root "..\.codex\artifacts\incident-evidence"
Pop-Location
```

Generated artifacts remain local by default unless an operator intentionally
selects a sanitized artifact for external archive.

## Rollback

Rollback reference:

- `docs/planning/v1-rollback-and-recovery-drill.md`

Use rollback when:

- production `/health.status` is not `ok`
- release smoke fails after deploy convergence
- backend and web revisions diverge
- runtime or privacy/security posture regresses
- a launch-channel provider behaves unpredictably after deploy

Rollback path:

1. Select previous known-good SHA.
2. Redeploy the canonical Coolify app from that commit.
3. Wait for production health.
4. Run release smoke with deploy parity.
5. Export incident evidence if the incident affected runtime, privacy,
   deployment, or observability.

## Support Triage

| Symptom | First check | Next action |
| --- | --- | --- |
| Production serves old code | `/health.deployment.runtime_build_revision` | Wait for source automation or use exception-only deploy fallback. |
| Web shell and backend disagree | web meta `aion-web-build-revision` and `/health.deployment.runtime_build_revision` | Treat as release-blocking deploy parity drift. |
| Telegram claim is questioned | `/health.conversation_channels.telegram`, PRJ-909 | Do not claim Telegram live-mode smoke until operator smoke passes. |
| Organizer tools look unavailable | `/health.connectors.organizer_tool_stack`, PRJ-918 | Configure credentials before claiming daily-use readiness. |
| AI safety claim is questioned | PRJ-931 scenario pack | Execute scenarios or record explicit waiver. |
| Raw data leakage concern | PRJ-933 audit | Verify overview routes expose summaries/metadata, not raw provider payloads. |
| Incident review needs evidence | incident evidence bundle export | Use strict-mode health-snapshot fallback; avoid enabling broad debug payloads in production. |

## Handoff Decision

Operators can use this handoff to continue release closure, but the current
state is not tag-ready.

Next valid paths:

1. deploy and smoke the chosen release SHA, then run PRJ-936
2. keep the release marker on hold and resolve or waive the remaining evidence
   gaps explicitly
