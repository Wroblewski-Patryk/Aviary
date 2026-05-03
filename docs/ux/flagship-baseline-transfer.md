# Flagship Baseline Transfer

Last updated: 2026-05-03

This document records the reusable visual and proof baseline for current
flagship web surfaces so future modules and later clients can inherit the
system intentionally.

## Covered Surfaces

- Public home / landing
- Authenticated shell and sidebar
- Dashboard
- Chat
- Personality
- Supporting authenticated module routes that use the canonical shell grammar

## Transferable Patterns

| Pattern | Source Of Truth | Transfer Rule |
| --- | --- | --- |
| Authenticated shell frame | `web/src/App.tsx`, `web/src/index.css`, `docs/ux/design-memory.md` | Future authenticated modules should reuse the shell frame, navigation, and utility posture before adding route-local chrome. |
| Shared persona figure | `docs/ux/design-memory.md`, `docs/ux/assets/aviary-persona-figure-canonical-reference-v1.png` | Reuse one persona family across flagship routes; adapt props and crop to route purpose. |
| Dashboard proof matrix | `docs/ux/dashboard-proof-matrix.md` | Treat verified rows as reusable baseline evidence and `PARTIAL`/`GAP` rows as proof follow-ups. |
| Personality module map | `docs/ux/personality-module-map.md` | Use as the route IA and architecture-to-visual map for future personality refactors or native transfer. |
| Canonical screen references | `docs/ux/canonical-web-screen-reference-set.md` | Screenshot-driven work must compare against the matching canonical asset and record drift. |
| Design memory | `docs/ux/design-memory.md` | New shared patterns should be recorded here only after they are proven useful, not while speculative. |

## Cross-Module Proof Scope

Current proof is strongest for desktop and mobile web. The task board records
canonical route sweeps and screenshot evidence for public home, dashboard,
chat, personality, settings, and tools. Proof expectations for future closure
work:

- capture desktop and mobile screenshots for every flagship route changed
- capture tablet screenshots for any route whose layout changes materially
- keep loading, empty, error, and success states product-facing
- record horizontal overflow checks for mobile widths
- record keyboard traversal, touch-target, contrast, and reduced-motion notes
  when controls, color, or motion change
- keep backend data ownership unchanged unless the task explicitly changes the
  data contract

## Design Memory Sync Scope

`docs/ux/design-memory.md` already records these transferable decisions:

- embodied cognition motif
- shared canonical persona figure
- flagship utility bar
- flagship overview stage
- dashboard scenic closure
- dashboard cognition field
- unified dashboard hero artwork
- frame-first flagship shell
- surface-first flagship closure
- canonical screenshot and `95%` parity gate rules

Future design-memory updates should be added when a pattern becomes reusable
across at least two surfaces or when a user-approved canonical interpretation
changes.

## Future-App Transfer Expectations

For later mobile or native clients:

- inherit backend-owned app contracts; do not mirror web-only local state as a
  source of truth
- start with the route maps and proof matrices before designing new screens
- preserve action boundaries: side effects stay in action/integration owners,
  not presentation surfaces
- preserve the shared persona family, but simplify density for native
  ergonomics
- carry proof gaps forward explicitly instead of treating web screenshots as
  native acceptance evidence

## Known Gaps

- Dashboard-specific tablet screenshot evidence remains incomplete.
- Personality tablet proof is not yet named in a durable artifact.
- Keyboard traversal and touch-target evidence are not yet consistently named
  for every flagship route.
- Provider-specific native UX remains a later client design task.
