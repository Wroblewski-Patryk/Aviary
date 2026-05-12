# Decision Register

Last updated: 2026-05-11

This file records product, architecture, UX, data, integration, and delivery
decisions that future agents must treat as durable project memory.

| ID | Date | Source | Decision | Alternatives | Status | Impact | Follow-up |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DEC-000 | 2026-05-11 | Agent operating system | Use this register for accepted assumptions and direction-setting decisions before implementation. | Chat-only decisions; scattered planning notes | accepted | Future agents can recover product intent without hidden chat memory. | Replace sample row with real project decisions. |
| DEC-001 | 2026-05-11 | `docs/planning/current-v1-release-boundary.md`; `docs/planning/v1-core-acceptance-bundle.md`; `PRJ-933` | The architecture radar's selected scope follows the current core/web-supported v1 boundary. Organizer provider activation, proactive target sampling, future-candidate source/webhook deployment proof, and mobile restart remain visible deferred extension/follow-up rows, not hidden selected-scope blockers. | Treat all architecture rows as selected v1 blockers; remove extension rows from the radar entirely | accepted | The dashboard can report selected-scope readiness without hiding future extension work. | Reclassify rows only when the release scope explicitly expands. |
| DEC-002 | 2026-05-11 | User request; `PRJ-1150`; `docs/planning/v1.1-web-ui-responsive-plan.md` | Treat `v1.1` as the web UI responsive quality milestone across desktop, tablet, and mobile web; use it as the evidence and design bridge before native/mobile work restarts as `v1.5`. | Start native/mobile immediately; treat v1.1 as only desktop polish; leave UI quality as chat-only intent | accepted | Web responsive evidence and screenshot review become the current UI delivery frame while `ARCH-MOBILE-001` remains deferred for native/mobile. | Rank captured screenshot drift and close flagship web surfaces one at a time. |
| DEC-003 | 2026-05-11 | User UI continuation request; `PRJ-1157`; `docs/planning/mobile-client-baseline.md`; `PRJ-1158` | Start `v1.5` as a native/mobile UI lane after the verified v1.1 web responsive handoff, beginning with a conversation-first Expo shell while preserving backend-owned `/app/*` contracts. | Keep mobile deferred until a separate formal scope meeting; continue polishing web without explicit feedback | accepted | Mobile can now receive UI implementation slices, but auth transport, provider setup, internal debug, and local cognition remain out of scope. | Add focused native chat route or device/simulator proof next. |

## Open Decision Queue

- `DEC-TODO-001`: _Question to resolve_ -> owner/date/status.
