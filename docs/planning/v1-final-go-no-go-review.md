# V1 Final Go/No-Go Review

Date: 2026-05-03
Task: `PRJ-934` / `PRJ-955`
Decision: GO for `v1.0.0` core no-UI/web-supported release marker

## Summary

The repository now has green production evidence for the selected v1 SHA, and
the `v1.0.0` release marker has been created. Several broader launch-channel or
evidence gaps remain explicit follow-ups.

This review is superseded by PRJ-955 for the release marker decision.
For current release truth after frontend closure, use PRJ-1115 and
`docs/operations/release-evidence-index.md`: deployed `v1.0.0` remains green,
while current local `HEAD` remains held by revision drift until production
serves that SHA.

## Historical PRJ-934 Revision Check

| Check | Value | Result |
| --- | --- | --- |
| Local `HEAD` | `92f7bf3af16502a1a3f661aa16bf6a9ead92e0cd` | Candidate is newer than production |
| Production `/health.deployment.runtime_build_revision` | `ed1c4d981314787d76252985b53c14ea1d7886ed` | Does not match local `HEAD` |
| Production web shell meta `aion-web-build-revision` | `ed1c4d981314787d76252985b53c14ea1d7886ed` | Matches production backend, not local `HEAD` |
| Production trigger posture | `source_automation` / `primary_automation` | Policy surface is healthy |
| Production final acceptance gate states | all inspected core states green | Core production posture is still green for deployed SHA |
| Selected `v1.0.0` SHA after PRJ-955 | `5e64f494e2aac8d29cea532d95f7039ed6029213` | Release reality audit and release smoke passed |

The first three rows are retained as the PRJ-934 historical snapshot. They are
not the current production revision after PRJ-955 and PRJ-1115.

Commands used:

```powershell
git rev-parse HEAD
Invoke-RestMethod -Uri "https://aviary.luckysparrow.ch/health" -TimeoutSec 20
Invoke-RestMethod -Uri "https://aviary.luckysparrow.ch/settings" -TimeoutSec 20
```

## Go / No-Go

| Scope | Decision | Reason |
| --- | --- | --- |
| Historical core no-UI v1 deployed at `ed1c4d9...` during PRJ-934 | GO at that time | Existing acceptance bundle and production health were green for that deployed revision. |
| Historical local repository candidate `92f7bf3...` during PRJ-934 | NO-GO / HOLD at that time | Production was not serving that SHA. |
| Public/web-led v1 launch marker before PRJ-955 | NO-GO / HOLD at that time | PRJ-935 handoff and PRJ-936 marker were not complete yet. |
| Release tag/marker | GO | `v1.0.0` was created after green production smoke and acceptance evidence. |

Current PRJ-1115 evidence keeps the same release boundary discipline: local
`HEAD` `5ff12953289bbca680fd5d9f8b3d8780a8f4be55` is not a release marker
candidate until production backend and web revisions match it.

## P0 Review

| Item | Status |
| --- | --- |
| PRJ-903 release boundary | Closed in release plan |
| PRJ-904 commit scope audit | Closed in release plan |
| PRJ-905 candidate validation | Closed in release plan |
| PRJ-906 publish candidate | Closed for earlier candidate only |
| PRJ-907 production release smoke with deploy parity | Closed for deployed SHA; must be rerun for current local HEAD |
| PRJ-908 production incident evidence bundle | Superseded by strict-mode safe export path and closed |
| PRJ-910 / PRJ-923 acceptance bundle | Closed for current documented core-v1 acceptance |
| PRJ-911 rollback and recovery drill | Closed |
| PRJ-912 data privacy/debug posture | Closed; PRJ-933 added provider-payload follow-up hardening |

## P1 / Launch-Channel Review

| Item | Status | Release effect |
| --- | --- | --- |
| PRJ-909 production Telegram live-mode smoke | BLOCKED by missing operator token, webhook secret, and known chat id | Telegram-led launch claim blocked |
| PRJ-918 organizer provider activation smoke | BLOCKED by provider credentials | Organizer daily-use claim blocked |
| PRJ-931 AI red-team scenario pack | DONE as scenario pack only | Execution results still needed or explicitly waived |
| PRJ-932 cross-user/session isolation audit | DONE with follow-up test gaps | Not a current release marker blocker if accepted as follow-up |
| PRJ-933 provider payload leakage audit | DONE with follow-up evidence gaps | Not a current release marker blocker if accepted as follow-up |
| PRJ-930 deployment-trigger SLO evidence | DONE locally | Direct Coolify deployment-history proof remains operator-owned |

## Deferred P2 Items

- `PRJ-919` tool authorization UX tightening
- multimodal Telegram plan and implementation
- mobile Expo restart from approved stack baseline

These should stay deferred unless the release claim is expanded beyond the
current core/web-supported v1 posture.

## Historical Required Actions Before PRJ-936

This list records the pre-PRJ-955 action plan. PRJ-955 resolved the `v1.0.0`
marker for selected SHA `5e64f494e2aac8d29cea532d95f7039ed6029213`; future
release candidates should use the release evidence index and v1 roadmap.

1. Decide whether the release target is the deployed SHA
   `ed1c4d981314787d76252985b53c14ea1d7886ed` or the current local candidate
   `92f7bf3af16502a1a3f661aa16bf6a9ead92e0cd`.
2. If the target is current local `HEAD`, deploy it and wait for production
   `/health.deployment.runtime_build_revision` and web meta revision to match.
3. Run production release smoke with deploy parity.
4. Complete PRJ-935 release notes and operator handoff.
5. At that time, keep PRJ-936 blocked until the chosen release SHA had green
   production evidence.

## Final Decision

`v1.0.0` is the release marker for selected SHA
`5e64f494e2aac8d29cea532d95f7039ed6029213`.

Continue post-v1 hardening and broader launch-channel evidence as follow-up
work.
