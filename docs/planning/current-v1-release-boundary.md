# Current V1 Release Boundary

Last updated: 2026-05-04

## Purpose

This document freezes what `v1` means for this repository and how post-v1 local
work can become a future release candidate. It exists so release work can
package, validate, publish, and smoke one explicit scope instead of silently
expanding `v1` with every useful follow-up feature.

## Frozen Core V1

The core `v1` release remains the no-UI life-assistant bundle already described
by the architecture and release-readiness docs:

1. stable Telegram or API conversation
2. learned-state inspection and later reuse
3. bounded website reading
4. tool-grounded learning
5. time-aware planned work
6. deployment parity in live production

These six gates were the P0 release blockers for the core marker and remain the
baseline for any future candidate. A candidate is not release-eligible until
the selected commit is validated locally, published, and proven in production
with release-smoke evidence tied to the deployed revision.

## Current Marker State

`v1.0.1` is the current selected-SHA release marker for selected SHA
`3b46ed3878a8560c3adb147fcadf064818ccc322`.

`v1.0.0` remains the historical released core marker for selected SHA
`5e64f494e2aac8d29cea532d95f7039ed6029213`.

PRJ-1115 refreshed release evidence after frontend closure:

- production backend revision:
  `5e64f494e2aac8d29cea532d95f7039ed6029213`
- production web meta revision:
  `5e64f494e2aac8d29cea532d95f7039ed6029213`
- deployed marker verdict: `GO` in monitor mode
- current local `HEAD`: `5ff12953289bbca680fd5d9f8b3d8780a8f4be55`
- local `HEAD` verdict: `HOLD_REVISION_DRIFT`

PRJ-1115 remains historical evidence for the `v1.0.0` marker.

The current selected production candidate after PRJ-1128 is
`3b46ed3878a8560c3adb147fcadf064818ccc322`:

- production backend revision:
  `3b46ed3878a8560c3adb147fcadf064818ccc322`
- production web meta revision:
  `3b46ed3878a8560c3adb147fcadf064818ccc322`
- production health: HTTP `200`
- selected candidate verdict: `GO_FOR_SELECTED_SHA`
- release smoke with deploy parity: passed
- incident evidence bundle export: available again
- release marker: `v1.0.1`
- release marker task: `PRJ-1131`

PRJ-1131 created and pushed annotated tag `v1.0.1` after selected-tag
go/no-go returned `GO`. Do not move `v1.0.0`; it remains historical marker
truth.

## Included Candidate Surface

The current web shell and canonical route work are included in the release
candidate as a product-facing companion surface, but they do not redefine the
core no-UI `v1` architecture gate.

For a future candidate that includes the current web shell, the web shell must
satisfy:

- committed and pushed source scope
- successful `npm run build`
- route smoke evidence for the authenticated shell and primary routes
- deployed revision parity in release smoke

Remaining static decorative values or polish gaps are tracked as web-v1 follow
ups unless they block route rendering, authenticated use, or revision parity.

## Extension Gates

The following are extension gates, not core `v1` blockers:

- organizer provider activation for ClickUp, Google Calendar, and Google Drive
- richer daily-use organizer workflows
- multimodal Telegram input and output
- mobile/Expo client restart
- external observability beyond the existing health, smoke, and incident
  evidence mechanisms

Each extension may become a release blocker only through an explicit scope
decision that updates this document and the relevant architecture or planning
source of truth.

## Hardening Gates

The following hardening work is required for a world-class public claim, but it
must stay separate from core feature invention:

- production release smoke with deployed revision parity
- incident evidence bundle for the current candidate
- rollback and recovery drill notes
- data privacy and debug posture check
- AI red-team scenario evidence for prompt injection, data leakage, and
  unauthorized access risks

## Non-Goals For The Current Candidate

- no new runtime architecture
- no new provider integration system
- no new parallel web shell
- no temporary bypass for failing production parity
- no release claim based only on local tests

## Current Post-V1 Execution Order

1. Keep selected SHA `3b46ed3878a8560c3adb147fcadf064818ccc322` frozen unless
   a new candidate is explicitly chosen.
2. Preserve PRJ-1128 release smoke and deploy parity as the current production
   proof.
3. Preserve `v1.0.1` as the current selected-SHA marker and `v1.0.0` as the
   historical marker.
4. Document Coolify source/webhook automation reliability if future candidates
   should avoid the UI fallback exception.
5. Keep Telegram live-mode, organizer provider activation, and AI review as
   extension or hardening follow-ups unless the release scope is expanded.

`PRJ-962` Telegram live-mode smoke and `PRJ-963` organizer provider activation
smoke remain extension gates unless the release claim is expanded beyond the
current core/web-supported posture.

## Current V1.1 Candidate Boundary

`PRJ-1135` records the current v1.1 gate map. This section is a planning
boundary, not a release claim. Do not mark v1.1 achieved until every selected
gate has direct evidence and the selected release marker is created after
production parity is green.

The current v1.1 candidate should build on the `v1.0.1` core/web-supported
baseline instead of redefining core v1. Its current gate posture is:

| Gate | Current Posture | Evidence Need |
| --- | --- | --- |
| Core/web-supported baseline | GREEN | preserve `v1.0.1` production parity and go/no-go evidence |
| Public/web route confidence | GREEN_FOR_CURRENT_SCOPE | keep web build and route smoke current for any new candidate |
| AI red-team scoring | LOCAL_FIX_PENDING_DEPLOY | `PRJ-1136` captures `reply.message`; `PRJ-1137` adds local expression self-review for unsafe boundary replies; package, deploy, and rerun the strict pack before v1.1 can claim this gate |
| Coolify source/webhook reliability | UNBLOCKED_OR_OPERATOR_ASSISTED | prove source automation for the next candidate or capture approved webhook fallback readiness once URL and secret are provided |
| Telegram live-mode launch channel | BLOCKED_EXTERNAL | operator token, webhook secret, and known chat id are required before smoke |
| Organizer provider activation | BLOCKED_EXTERNAL | ClickUp, Google Calendar, and Google Drive credentials are required before smoke |
| Multimodal/mobile expansion | DEFERRED | requires explicit scope decision before entering a v1.1 blocker set |

The first v1.1 hardening implementation target was closed by `PRJ-1136`: the
existing `/event` runner now captures redacted assistant reply text from the
approved `reply.message` contract. `PRJ-1137` locally fixes the clearest
expression-boundary review patterns from the strict run. The next unblocked
v1.1 target is to package and deploy the local guard, then rerun the strict
pack against the deployed revision.
