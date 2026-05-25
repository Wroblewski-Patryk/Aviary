# V1 Core Acceptance Bundle

Last updated: 2026-05-04

## Status

Core no-UI/web-supported `v1.0.1` is GO for the production revision:

- `3b46ed3878a8560c3adb147fcadf064818ccc322`

Release marker:

- current: `v1.0.1`
- historical: `v1.0.0`

This is a core runtime acceptance result, not a claim that every product,
provider, security, AI, or web-polish follow-up is complete.

`v1.0.0` remains historical marker truth for selected SHA
`5e64f494e2aac8d29cea532d95f7039ed6029213`.

## Acceptance Summary

| Gate | Health Surface | Production State | Evidence | Residual Risk |
| --- | --- | --- | --- | --- |
| Conversation reliability | `/health.conversation_channels.telegram` | `provider_backed_ready` | Release smoke passed; bot token and webhook secret configured; Telegram delivery posture exposes segmentation and formatting support | Live user/chat round-trip smoke remains `PRJ-909` before a Telegram-led launch claim |
| Learned-state inspection | `/health.learned_state` | `inspection_surface_ready` | Strict-mode incident bundle includes learned-state policy owner, inspection path, inspection sections, growth sections, and tool-grounded learning contract | No core blocker |
| Website reading | `/health.connectors.web_knowledge_tools.website_reading_workflow` | `ready_for_direct_and_search_first_review` | Health and incident bundle expose direct URL and search-first page review readiness with no blockers | No core blocker |
| Tool-grounded learning | `/health.learned_state.tool_grounded_learning` | `tool_grounded_learning_surface_ready` | Health and incident bundle expose action-owned external read summaries only, semantic memory layer, and no raw payload storage | Privacy/security hardening remains a separate `PRJ-912/PRJ-933` check |
| Time-aware planned work | `/health.v1_readiness` | `foreground_due_delivery_and_recurring_reevaluation_ready` | Behavior validation and health expose planned-work policy owner, delivery path, and recurrence owner; scheduler external evidence is recent and aligned | No core blocker |
| Deploy parity | `/health.deployment` and release smoke | runtime/web/local SHA match | Release reality audit returned `GO_FOR_SELECTED_SHA`; release smoke passed with deploy parity for `3b46ed3878a8560c3adb147fcadf064818ccc322`; `v1.0.1` marks this SHA | Every later commit requires fresh deploy parity smoke |

## Evidence Set

Local candidate validation:

- PRJ-905 backend tests: `1019 passed`
- PRJ-905 web production build: passed
- PRJ-905 behavior validation: `19 passed, 209 deselected`
- PRJ-922 backend validation: `1021 passed`
- PRJ-1122 current workspace candidate validation:
  - backend baseline: `1045 passed`
  - web build: passed
  - route smoke: `status=ok`, `route_count=14`

Production validation:

- release reality audit returned `GO_FOR_SELECTED_SHA` for:
  `3b46ed3878a8560c3adb147fcadf064818ccc322`
- release smoke passed with deploy parity for:
  `3b46ed3878a8560c3adb147fcadf064818ccc322`
- selected-tag go/no-go for `v1.0.1` returned `GO`
- release marker `v1.0.1` target:
  `3b46ed3878a8560c3adb147fcadf064818ccc322`
- strict-mode incident evidence bundle export passed with:
  `incident_evidence_source=health_snapshot_strict_mode`
- release smoke with the strict-mode incident bundle passed

Current production incident bundle:

- PRJ-1128 release-smoke incident evidence export:
  `.codex/tmp/incident-evidence-after-coolify-ui/20260503T230011Z_incident-bundle-20260503T230011Z/`
- Historical PRJ-923 final-v1 acceptance bundle:
  `.codex/artifacts/prj923-final-v1-acceptance/20260502T220616Z_prj923-final-v1-acceptance-0984440`

The bundle is local evidence output and is not committed by default.

## Behavior Scenario Coverage

The current `v1_readiness.required_behavior_scenarios` list is:

- `T13.1`
- `T14.1`
- `T14.2`
- `T14.3`
- `T15.1`
- `T15.2`
- `T16.1`
- `T16.2`
- `T16.3`
- `T17.1`
- `T17.2`
- `T18.1`
- `T18.2`
- `T19.1`
- `T19.2`

PRJ-905 behavior validation passed with `19 passed, 209 deselected` and is
attached to the strict-mode incident bundle.

## Extension And Hardening Gates

The following are not core no-UI `v1` blockers, but remain required before a
broader public or web-led release claim:

- `PRJ-909` production Telegram live-mode smoke: BLOCKED until an operator
  provides `TELEGRAM_BOT_TOKEN`, `TELEGRAM_WEBHOOK_SECRET`, and a known
  `REQUIRED_CHAT_ID`; production health currently reports
  `provider_backed_ready`
- `PRJ-911` rollback and recovery drill
- `PRJ-912` data privacy and debug posture check
- `PRJ-913` web-v1 route smoke: DONE locally with desktop/mobile route
  evidence and `/tools` mobile overflow fix
- `PRJ-914` static Personality metrics replacement: DONE locally with
  desktop/mobile focused evidence
- `PRJ-915` backend-backed dashboard summary surface: DONE locally with
  desktop/mobile focused evidence
- `PRJ-916` web empty/error state audit: DONE locally with authenticated route
  and backend-down dashboard evidence
- `PRJ-917` organizer provider credential activation runbook: DONE locally
- `PRJ-918` organizer provider activation smoke: BLOCKED until provider
  credentials are configured
- `PRJ-919` tool authorization UX tightening
- `PRJ-920` minimal external health monitor: DONE with active hourly
  `aion-production-health-monitor`
- `PRJ-921` release-evidence archive: DONE with
  `docs/planning/v1-release-evidence-archive-standard.md`
- `PRJ-930` deployment trigger SLO evidence: DONE with
  `docs/planning/v1-deployment-trigger-slo-evidence.md`; PRJ-1128 records
  approved Coolify UI fallback recovery for `v1.0.1`, while source/webhook
  automation reliability remains a future-candidate follow-up
- `PRJ-931` AI red-team scenario pack: DONE with
  `docs/security/v1-ai-red-team-scenario-pack.md`; execution results remain a
  separate release-hardening evidence item
- `PRJ-932` cross-user/session isolation audit: DONE with
  `docs/security/v1-cross-user-session-isolation-audit.md`; follow-up two-user
  regression gaps remain
- `PRJ-933` provider payload leakage audit: DONE with
  `docs/security/v1-provider-payload-leakage-audit.md`; follow-up live
  provider, red-team execution, strict-mode incident sentinel, and frontend
  fixture smoke gaps remain
- `PRJ-934` final go/no-go review: DONE with
  `docs/planning/v1-final-go-no-go-review.md`; current selected SHA is GO after
  PRJ-1128/1131
- `PRJ-935` release notes and operator handoff: DONE with
  `docs/planning/v1-release-notes-and-operator-handoff.md`
- `PRJ-955` created and pushed `v1.0.0` after the chosen release SHA had green
  production evidence; prior blocker record:
  `docs/planning/v1-release-marker-blocker.md`
- `PRJ-1131` created and pushed `v1.0.1` after the current selected SHA had
  green production evidence
- `PRJ-1133` refreshed this acceptance bundle for `v1.0.1`

## Go / No-Go

- Core no-UI v1 behavior: GO
- Production deploy parity: GO
- Production incident-evidence bundle: GO
- Core no-UI v1 declaration: GO
- Current selected release marker: GO, `v1.0.1`
- Historical release marker: GO, `v1.0.0`
- Public/web-led broader launch marker: HOLD until the remaining launch-channel,
  rollback, privacy/debug, and AI/security hardening gates are complete or
  explicitly waived by a documented release decision.

## Recommended Next Step

Rerun `PRJ-909` when Telegram operator preconditions are available. Until then,
continue with locally actionable public-launch hardening or provider activation
work. Any later candidate must be committed, pushed, deployed, and release
smoked before it can inherit this acceptance claim.
