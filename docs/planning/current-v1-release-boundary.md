# Current V1 Release Boundary

Last updated: 2026-05-03

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

`v1.0.0` is the released core marker for selected SHA
`5e64f494e2aac8d29cea532d95f7039ed6029213`.

PRJ-1115 refreshed release evidence after frontend closure:

- production backend revision:
  `5e64f494e2aac8d29cea532d95f7039ed6029213`
- production web meta revision:
  `5e64f494e2aac8d29cea532d95f7039ed6029213`
- deployed marker verdict: `GO` in monitor mode
- current local `HEAD`: `5ff12953289bbca680fd5d9f8b3d8780a8f4be55`
- local `HEAD` verdict: `HOLD_REVISION_DRIFT`

Local post-v1 hardening and frontend work must not inherit the `v1.0.0`
release claim until a new selected SHA is pushed, deployed, and proven by fresh
release smoke.

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

1. Select the intended post-v1 candidate SHA.
2. Push that SHA to the deployment source.
3. Resolve `PRJ-952` by confirming Coolify source automation or by using the
   approved operator fallback with webhook URL and secret.
4. Rerun production release smoke with deploy parity for the selected SHA.
5. Refresh release evidence index, v1 roadmap, acceptance bundle, and operator
   handoff for the exact selected SHA.
6. Create or move a release marker only after backend revision, web revision,
   release readiness, and smoke evidence all match the selected SHA.

`PRJ-962` Telegram live-mode smoke and `PRJ-963` organizer provider activation
smoke remain extension gates unless the release claim is expanded beyond the
current core/web-supported posture.
