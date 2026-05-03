# V1 Release Notes And Operator Handoff

Date: 2026-05-04
Task: `PRJ-935` / `PRJ-955`, refreshed by `PRJ-1134`
Posture: current selected SHA is production-green and marked by `v1.0.1`

## Current Decision

Release marker `v1.0.1` has been created for the current selected production
SHA after selected-tag go/no-go returned `GO`.

Current release truth after PRJ-1128 and PRJ-1129:

- `v1.0.1` is the current release marker for selected SHA
  `3b46ed3878a8560c3adb147fcadf064818ccc322`
- `v1.0.0` remains the historical released core marker for selected SHA
  `5e64f494e2aac8d29cea532d95f7039ed6029213`
- current selected SHA `3b46ed3878a8560c3adb147fcadf064818ccc322` is deployed,
  release-smoked, and revision-aligned in production
- release audit for the current selected SHA returns `GO_FOR_SELECTED_SHA`
- selected-tag go/no-go for `v1.0.1` returns `GO`
- future marker work must keep this SHA frozen or select a new SHA, then rerun
  deploy parity and release smoke before any new release claim

| Revision | SHA |
| --- | --- |
| Current local `HEAD` at PRJ-934 review | `92f7bf3af16502a1a3f661aa16bf6a9ead92e0cd` |
| Production `/health.deployment.runtime_build_revision` at PRJ-934 review | `ed1c4d981314787d76252985b53c14ea1d7886ed` |
| Production web shell build revision at PRJ-934 review | `ed1c4d981314787d76252985b53c14ea1d7886ed` |
| Selected `v1.0.0` SHA | `5e64f494e2aac8d29cea532d95f7039ed6029213` |
| Current selected SHA after PRJ-1128 | `3b46ed3878a8560c3adb147fcadf064818ccc322` |
| Current release tag after PRJ-1131 | `v1.0.1` |
| Current release tag object | `b016c4f33051805cfa09664f79bbe57f5b30811b` |
| Current release reality audit | `GO_FOR_SELECTED_SHA` |
| Current production release smoke | PASSED |

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

- `v1.0.0` is historical marker truth; `v1.0.1` is the current release marker
  for selected SHA `3b46ed3878a8560c3adb147fcadf064818ccc322`.
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
- Direct Coolify deployment-history confirmation for PRJ-1128 was completed by
  explicit operator UI access; source/webhook automation reliability remains a
  follow-up.
- PRJ-955 created the `v1.0.0` release marker after the historical selected
  release SHA had green production evidence.
- PRJ-1131 created and pushed the `v1.0.1` release marker after the current
  selected SHA had green production evidence.

## Required Before A Future Release Marker

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
8. Create or move a release marker only after the selected SHA has green
   evidence.

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

Operators can use this handoff for the current `v1.0.1` marker truth,
historical `v1.0.0` marker truth, and future post-v1 release candidates.

Next valid paths:

1. keep `v1.0.1` as the current released core marker truth
2. keep `v1.0.0` as historical released core marker truth
3. for a future candidate, deploy and smoke the selected SHA before creating or
   moving any marker
4. resolve external launch-channel gaps (`PRJ-909`, `PRJ-918`) before expanding
   the public claim beyond the current core/web-supported posture
