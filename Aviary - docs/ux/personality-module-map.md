# Personality Module Map

Last updated: 2026-05-03

This document freezes the current product-facing `/personality` information
architecture and motif mapping so future route work reuses the shared dashboard
system instead of drifting into a separate visual universe.

## Scope

- Surface: authenticated `/personality`
- Client owner: `web/src/App.tsx`
- Styling owner: `web/src/index.css`
- Backend data source: `GET /app/personality/overview`
- Canonical visual source:
  - `docs/ux/assets/aion-personality-canonical-reference-v1.png`
  - `docs/ux/aion-visual-motif-system.md`
  - `docs/planning/dashboard-foundation-and-personality-visual-system-plan.md`

## Section Map

| Section | UI Owner | Purpose | Shared Primitive |
| --- | --- | --- | --- |
| Overview bar | `aion-personality-overview-bar` | Establish route identity, status, and product framing without adding a second shell hero. | Dashboard overview/status rhythm |
| Embodied hero | `aion-personality-hero`, `aion-personality-hero-stage` | Show personality as an embodied cognition map rather than a raw debug inspector. | Motif hero panel and canonical persona figure |
| Callout pins | `personalityPreviewCallouts` | Pin identity, knowledge, planning, skills, and role to visible body-map areas. | Shared motif note/callout language |
| Mind-layer timeline | `personalityTimelineRows`, `PersonalityTimelineRow` | Turn architecture layers into a readable timeline of personality state. | Timeline rail panel |
| Conscious layer side panel | `personalityConsciousSignals` | Surface foreground cognition signals without exposing pipeline internals as primary copy. | Insight panel family |
| Subconscious layer side panel | `personalitySubconsciousSignals` | Show slower memory/reflection/background posture. | Insight panel family |
| Recent activity | `personalityRecentActivity` | Keep continuity visible without turning the route into chat history. | Recent activity list pattern |
| Layer cards | `personalityLayers`, `PersonalityLayerCard` | Summarize architecture-owned state families as product-facing capabilities. | Shared card/panel grammar |

## Architecture To Visual Mapping

| AION Concept | Visible Zone | Data/Code Anchor | Boundary |
| --- | --- | --- | --- |
| Identity | Head/identity callout and identity layer card | `identity_state`, `preferenceSummary`, `personalityPreviewCallouts` | Profile and learned preference posture only; no raw memory dump. |
| Knowledge and memory | Knowledge callout, subconscious side panel, recent activity | `memory_state`, recent activity helpers | Shows reusable signals, not full private records. |
| Role | Role callout and role/skills layer | `role_skill_state`, `selectionVisibilitySummary` | Role posture stays descriptive; execution authority remains outside the route. |
| Skills | Skills callout and catalog visibility summary | `skillRegistry`, `skillCatalogCount` | Capability visibility only; no self-modifying skill learning. |
| Planning | Planning callout and conscious layer | `planning_state`, active goals/tasks | Plans remain guidance until the action layer owns a real side effect. |
| Reflection | Timeline and subconscious layer | reflection/recent activity summaries | Slow learning layer, not live control surface. |
| Expression | Timeline and foreground cognition copy | route copy plus overview data | Product framing only; does not bypass runtime expression. |

## Reuse Contract

- Use the existing authenticated shell frame, sidebar, utility bar, and
  dashboard-derived panel grammar.
- Use shared `aion-panel*`, motif stage, timeline, and insight panel patterns.
- Keep side effects outside the personality view; this surface observes and
  explains state.
- Keep backend ownership through `GET /app/personality/overview`; do not create
  route-local mock state as a durable source of truth.
- Keep the canonical persona figure family shared with dashboard/chat while
  using personality-specific props and body-map callouts.

## Current Evidence

- `web/src/App.tsx` contains `PersonalityLayerCard`,
  `PersonalityTimelineRow`, `personalityLayers`, `personalityFlowItems`,
  `personalityPreviewCallouts`, `personalityTimelineRows`,
  `personalityConsciousSignals`, and `personalitySubconsciousSignals`.
- Later canonical proof exists in:
  - `.codex/artifacts/prj865-personality-canonical-pass/desktop-1568x1003-v2.png`
  - `.codex/artifacts/prj865-personality-canonical-pass/mobile-390x844-v2.png`
  - `.codex/artifacts/prj871-personality-99-canonical-pass/personality-desktop-after-1568x1003-v2.png`
  - `.codex/artifacts/prj871-personality-99-canonical-pass/personality-mobile-after-390x844-v3.png`

## Known Gaps

- Tablet-specific personality proof is not named in this map.
- The route remains concentrated in `web/src/App.tsx`; extraction into smaller
  components should be a later refactor only when it reduces real maintenance
  risk.
- Provider or action affordances must stay linked to their owning routes and
  backend contracts rather than moving into personality.
