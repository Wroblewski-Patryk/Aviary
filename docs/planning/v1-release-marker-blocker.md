# V1 Release Marker Blocker

Date: 2026-05-03
Task: `PRJ-936`
Status: BLOCKED

## Decision

No release tag or marker was created.

This is intentional. PRJ-934 recorded `NO-GO / HOLD` because production is not
serving the current local candidate SHA.

## Blocking Facts

| Check | Value |
| --- | --- |
| Current local candidate at PRJ-934 review | `92f7bf3af16502a1a3f661aa16bf6a9ead92e0cd` |
| Production backend revision at PRJ-934 review | `ed1c4d981314787d76252985b53c14ea1d7886ed` |
| Production web revision at PRJ-934 review | `ed1c4d981314787d76252985b53c14ea1d7886ed` |
| Current pushed candidate after PRJ-937 | `4d9d3a40fc07b83a6441c974bc31f78879353db7` |
| Production backend revision after 900-second deploy-parity wait | `ed1c4d981314787d76252985b53c14ea1d7886ed` |
| Production web revision after deploy-parity wait | `ed1c4d981314787d76252985b53c14ea1d7886ed` |
| PRJ-938 release smoke result | BLOCKED: production did not converge to pushed candidate within 900 seconds |
| Release marker posture | `NO-GO / HOLD` |

## Unblock Checklist

Before creating a release marker:

- choose the target release SHA
- deploy that SHA to production if it is not already deployed
- verify `/health.deployment.runtime_build_revision` matches the target SHA
- verify production web shell meta `aion-web-build-revision` matches the target
  SHA
- run production release smoke with deploy parity
- confirm incident evidence bundle posture if it is part of the release
  decision
- decide whether PRJ-909, PRJ-918, PRJ-931 execution, and other follow-up
  evidence gaps are blocked, waived, deferred, or required for the release
  claim
- update release notes and acceptance bundle if the target SHA or decision
  changes

Current operator unblock path after PRJ-938:

- verify Coolify deployment history/source connection for canonical app
  `jr1oehwlzl8tcn3h8gh2vvih`
- if source automation did not enqueue the pushed SHA, run the existing
  webhook fallback with operator-provided webhook URL/secret, or use Coolify UI
  redeploy as the documented exception-only fallback
- rerun production release smoke with deploy parity

## Allowed Next Commands

Production release smoke:

```powershell
.\backend\scripts\run_release_smoke.ps1 `
  -BaseUrl "https://aviary.luckysparrow.ch" `
  -WaitForDeployParity `
  -DeployParityMaxWaitSeconds 900 `
  -DeployParityPollSeconds 30 `
  -HealthRetryMaxAttempts 10 `
  -HealthRetryDelaySeconds 10
```

After green evidence only:

```powershell
git tag <release-tag> <selected-release-sha>
```

Do not run the tag command until the unblock checklist is satisfied.
