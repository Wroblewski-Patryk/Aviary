# Canonical UI Layout Index

Last updated: 2026-05-23

## Purpose

This is the canonical simplification map for the Aviary web UI.

It translates architecture, backend-backed product functions, and canonical
visual references into a stable layout index. Future UI implementation should
use this document before adding, keeping, or removing visible elements.

The goal is simpler than previous polish passes:

- one coherent shell
- fewer cards, badges, chips, and decorative controls
- only backend-backed data or clear user actions in primary surfaces
- canonical route groups with stable IDs
- a calm hierarchy that can later be regenerated for web or native mobile

## Design Sources

Primary references:

- `docs/ux/canonical-web-screen-reference-set.md`
- `docs/ux/visual-direction-brief.md`
- `docs/ux/experience-quality-bar.md`
- `docs/ux/screen-quality-checklist.md`
- `docs/ux/anti-patterns.md`
- `docs/ux/design-memory.md`
- `docs/ux/assets/aviary-sidebar-layout-canonical-reference-v1.png`
- `docs/ux/assets/aviary-landing-hero-canonical-reference-v1.png`
- `docs/ux/assets/aviary-dashboard-hero-canonical-reference-v4.png`
- `docs/ux/assets/aion-chat-canonical-reference-v5.png`
- `docs/ux/assets/aviary-persona-figure-canonical-reference-v1.png`

Recent proof sources:

- `.codex/artifacts/prj1234-flagship-last-mile-polish/screenshots/`
- `.codex/artifacts/prj1235-mobile-shell-first-viewport-polish/screenshots/`
- `.codex/artifacts/prj1236-settings-auth-accessibility-polish/screenshots/`

## Core Rule

Every visible element must answer at least one of these questions:

1. What can Aviary do here?
2. What does Aviary know from the backend here?
3. What can the user safely do next?
4. What state, risk, or blocker must the user understand?

If an element does not answer one of those questions, remove it, merge it into a
larger group, or move it behind a detail boundary.

## Data Authority

| UI data source ID | Backend/client contract | Current UI use | Allowed first-read use |
| --- | --- | --- | --- |
| DATA-ME | `/app/me`, `AppMeResponse` | identity, settings, profile, account state | account identity, display name, app language, local time, proactive opt-in |
| DATA-CHAT | `/app/chat/history`, `/app/chat/message`, `AppChatHistoryResponse`, `AppChatMessageResponse` | transcript, composer, pending confirmation | conversation thread, composer, delivery/runtime reply state, pending confirmation |
| DATA-PERSONALITY | `/app/personality/overview`, `AppPersonalityOverviewResponse` | dashboard, personality, memory, reflections, plans, goals, insights | current activity, identity, learned knowledge, planning state, role/skills, capability catalog |
| DATA-TOOLS | `/app/tools/overview`, `AppToolsOverviewResponse` | tools, integrations, automation posture | available capabilities, user-controlled toggles, link-required providers, safe next action |
| DATA-TELEGRAM | `/app/tools/telegram/link/start`, `AppTelegramLinkStartResponse` | linking flow | explicit linking code and instruction only after user intent |
| DATA-HEALTH | `/health` or app health snapshot, `AppHealthResponse` | system health, automations, scheduler posture | concise readiness/status; detailed diagnostics behind details |
| DATA-RESET | `/app/settings/reset-data`, `AppResetDataResponse` | destructive reset result | collapsed destructive boundary and local confirmation/result |

## Global Shell

| ID | Zone | Function | Required elements | Remove or demote |
| --- | --- | --- | --- | --- |
| SHELL-ROOT | App frame | Establish one product workspace | background material, content viewport, authenticated/public state | nested page frames and decorative wrappers that do not group data |
| SHELL-SIDEBAR | Desktop primary navigation | Let user move between route functions | brand, one nav stack, current route, account/status footer | duplicate route switchers, live-looking inactive controls, repeated badges |
| SHELL-MOBILE-HEADER | Mobile route frame | Identify route and account with minimal chrome | brand, route title, account trigger | workspace labels, extra proof chips, route-local nav duplicates |
| SHELL-ROUTE-RAIL | Tablet/mobile navigation | Keep route movement reachable | one horizontal nav rail with active state | second rails, tabs that duplicate route nav, non-route icons |
| SHELL-UTILITY | Desktop context/status | Show current route context and account | route title/current surface, account, passive status if needed | search/focus/capture controls until behavior exists |
| SHELL-FOOTER | Product closure/status | Optional quiet closure, mostly public route | trust/status only when it reduces uncertainty | marketing badges inside authenticated work routes |

## Component Budget

Use the smallest component that communicates the data.

| Component type | Allowed use | Budget rule |
| --- | --- | --- |
| Hero/stage | route purpose and one primary backend-backed state | one per route max |
| Panel | group related data from one source or one task | max 2 primary panels per route first viewport |
| Card | repeated items only: messages, goals, tools, insights, activity rows | avoid single decorative cards |
| Badge/chip | status that changes meaningfully or disambiguates state | max 3 chips in a route hero; no decorative chip rows |
| Button | real user action that changes route, submits data, sends a message, starts linking, saves, confirms, or opens an intentional disclosure | no inert buttons |
| Detail/disclosure | technical, provider, debug, destructive, or low-frequency information | preferred home for backend plumbing |
| Illustration | only when it explains route concept or matches canonical asset role | do not use as filler behind every route |

## First-Read Hierarchy

Every route first viewport must fit this order:

1. Where am I?
2. What does Aviary know or support here?
3. What is the one safest next action?
4. What detail can wait?

The first viewport must not open with a large grid of equal cards. If a route
has many backend-backed facts, it should still choose one primary group and one
secondary group, then move supporting data below the fold or behind disclosure.

## Noise Taxonomy

These patterns are removable by default unless a later task proves a real
backend-backed function, state, or user action:

| Noise ID | Pattern | Default decision | Replacement |
| --- | --- | --- | --- |
| NOISE-FAKE-CHROME | browser chrome, mock title bars, fake search, fake capture/action controls | remove | real shell zone or passive status text |
| NOISE-DUP-BADGE | two badges or chips with the same localized meaning | merge | one status chip or plain row text |
| NOISE-CARD-IN-CARD | cards nested inside decorative cards or framed page sections | flatten | section band plus repeated item cards only |
| NOISE-TECH-FIRST | provider, build, route-smoke, credential, or runtime plumbing in first viewport | demote | details/disclosure |
| NOISE-CTA-MANY | multiple competing CTAs where only one is real or primary | reduce | one primary action cluster |
| NOISE-UPPER-SOUP | uppercase micro-label rows, proof chips, dense decorative metadata | reduce | sentence-case labels tied to data groups |
| NOISE-ROUTE-SIDEBAR | route-local sidebar that competes with global shell navigation | remove | one route context panel when needed |
| NOISE-MOBILE-GRID | mobile first viewport dominated by stat cards before the task surface | reorder | task surface first, compact rail or summary after |

## Allowed Group Types

| Group type | Use when | Forbidden when |
| --- | --- | --- |
| Navigation | the element moves between canonical routes or disclosures | it duplicates the sidebar/rail or looks like a route but is static |
| Primary stage | the route needs one memorable visual or task anchor | it becomes a decorative frame around unrelated cards |
| Operational panel | the group represents one backend source or one user task | it mixes unrelated sources to look fuller |
| Repeated item card | the UI renders a real list: messages, tools, goals, insights, activity | the card is a one-off decoration |
| Status material | the status changes meaningfully and affects trust or next action | it repeats a nearby label or value |
| Disclosure | the content is technical, destructive, low-frequency, or provider-specific | it hides the main task or required state |

## Route Layout Index

### ROUTE-HOME

Purpose: public trust and entry.

Data authority: public copy and auth actions only.

First-read hierarchy:

1. public value proposition and persona signal
2. one clear auth continuation
3. short trust statements
4. deeper proof below the first viewport

Required groups:

- `HOME-HERO`: value proposition, persona motif, primary create/sign-in actions.
- `HOME-TRUST`: concise trust statements.
- `HOME-AUTH`: auth modal with login/register forms.

Remove or demote:

- excessive proof chips
- fake product controls
- repeated trust badges below the first trust group

### ROUTE-DASHBOARD

Purpose: one living overview of current state and next best direction.

Data authority: DATA-PERSONALITY, DATA-CHAT summaries, DATA-HEALTH.

First-read hierarchy:

1. current state and greeting
2. next best direction
3. compact memory/reflection/goal/activity signal
4. health detail only when it changes trust or action

Required groups:

- `DASH-HERO`: current greeting plus embodied overview state.
- `DASH-NEXT`: one next useful action or guidance group.
- `DASH-STATE`: compact goals/memory/reflection/activity summary.
- `DASH-HEALTH`: one quiet status, not a diagnostics console.

Remove or demote:

- equal-weight metric card stacks
- duplicate memory/reflection cards already covered by module routes
- decorative badges that do not change the user's next move

### ROUTE-CHAT

Purpose: primary conversation.

Data authority: DATA-CHAT, pending confirmations, small contextual summary from
DATA-PERSONALITY.

First-read hierarchy:

1. transcript
2. composer
3. current context belt or side context
4. confirmation/provider details only when active

Required groups:

- `CHAT-THREAD`: transcript list.
- `CHAT-COMPOSER`: message input and send state.
- `CHAT-CONTEXT`: minimal context belt or side panel for current intent/memory/action posture.
- `CHAT-CONFIRMATION`: pending connector confirmation when present.

Remove or demote:

- context cards that block reaching the composer on mobile
- repeated AI safety/status badges
- non-chat dashboards inside the conversation view

### ROUTE-PERSONALITY

Purpose: explain what Aviary currently knows and how its cognition is shaped.

Data authority: DATA-PERSONALITY.

First-read hierarchy:

1. embodied cognition map
2. current adaptive/conscious state
3. learned knowledge and recent activity
4. raw implementation labels never in first read

Required groups:

- `PERS-MAP`: embodied cognition map anchored to identity, knowledge, planning, and skills.
- `PERS-STATE`: concise current conscious/adaptive state.
- `PERS-LEARNING`: learned knowledge and recent activity.

Remove or demote:

- badges that merely restate labels on the map
- duplicated route meta from Dashboard
- raw implementation keys

### ROUTE-MODULES

Routes: `/memory`, `/reflections`, `/plans`, `/goals`, `/insights`,
`/automations`, `/integrations`.

Purpose: focused reading of one backend-backed cognitive domain.

Data authority:

- Memory/reflections/plans/goals/insights: DATA-PERSONALITY.
- Automations/integrations: DATA-TOOLS and DATA-HEALTH.

First-read hierarchy:

1. module identity and one summary sentence
2. primary backend-backed list, state, or empty state
3. one supporting risk/action detail when useful
4. repeated stats and metadata below the fold

Required groups:

- `MODULE-HERO`: route title plus one summary sentence.
- `MODULE-PRIMARY`: the main list/table/rail of backend-backed records or state.
- `MODULE-SECONDARY`: one supporting detail panel only if it adds action or risk clarity.
- `MODULE-EMPTY`: clear empty state when data is absent.

Remove or demote:

- repeated stat grids on every module
- generic route hero cards that do not show actual backend state
- badges for counts that are already visible in list content

### ROUTE-TOOLS

Purpose: show real capabilities and safe activation/linking posture.

Data authority: DATA-TOOLS, DATA-TELEGRAM.

First-read hierarchy:

1. what is available now
2. what needs linking or review
3. what the user controls
4. provider/source/debug detail behind disclosure

Required groups:

- `TOOLS-AVAILABLE`: capabilities ready now.
- `TOOLS-ACTION`: one explicit next action when linking or review is required.
- `TOOLS-CONTROL`: user-owned toggles when supported.
- `TOOLS-DETAILS`: provider, source-of-truth, skill binding, and link-state details behind disclosure.

Remove or demote:

- provider plumbing in first-read cards
- `route smoke`, credential, and source-of-truth language outside details
- duplicate availability/link-state badges

### ROUTE-SETTINGS

Purpose: user-owned profile and preference controls.

Data authority: DATA-ME, DATA-RESET.

First-read hierarchy:

1. display name and identity
2. app language, local time, proactive opt-in
3. save feedback
4. destructive reset behind disclosure

Required groups:

- `SETTINGS-PROFILE`: display name.
- `SETTINGS-APP`: app language and local time.
- `SETTINGS-FOLLOWUPS`: proactive opt-in.
- `SETTINGS-SAVE`: save state.
- `SETTINGS-RESET`: collapsed destructive reset boundary.

Remove or demote:

- runtime jargon in first-read copy
- status chips that only repeat form values
- technical confirmation details before the user opens reset

## Simplification Pass Order

1. `PASS-UI-INDEX`: keep this document and route inventory current.
2. `PASS-NOISE-AUDIT`: count first-viewport controls, cards, badges, chips,
   and button-looking elements from current screenshots; classify each one as
   keep, merge, demote, or remove using this index.
3. `PASS-SHELL`: remove duplicate global chrome and inert controls.
4. `PASS-SETTINGS-TOOLS`: simplify low-risk utility routes first.
5. `PASS-MODULES`: collapse repeated stat-card patterns into one route-appropriate primary data group.
6. `PASS-DASHBOARD`: reduce dashboard to overview, next action, and current state.
7. `PASS-CHAT`: keep conversation and composer first; keep context supportive.
8. `PASS-PERSONALITY`: preserve the canonical embodied map while removing redundant labels.

## Implementation Ownership Map

| Pass | Likely code surfaces | Validation proof |
| --- | --- | --- |
| PASS-NOISE-AUDIT | screenshots and route-smoke reports only | route-by-route table of keep/merge/demote/remove decisions |
| PASS-SHELL | `web/src/components/shell.tsx`, shared shell styles, `web/src/route-manifest.json` only if route labels change | desktop/tablet/mobile shell screenshots, navigation proof, account proof |
| PASS-SETTINGS-TOOLS | Settings and Tools route components/styles | route smoke, screenshot proof, action/control proof for save/link/reset boundaries |
| PASS-MODULES | shared module route template/components | all module route screenshots and empty-state proof |
| PASS-DASHBOARD | Dashboard route components/styles | dashboard desktop/tablet/mobile screenshots against canonical dashboard reference |
| PASS-CHAT | Chat route components/styles | transcript/composer visibility, send path, pending confirmation state, mobile first-read proof |
| PASS-PERSONALITY | Personality route components/styles | embodied-map readability and reduced callout density proof |

## Acceptance Gate For Future UI Work

A route is not accepted as simplified unless:

- every first-viewport group maps to a route group ID above
- every visible action is wired to real behavior
- every data group names its backend/client source
- no route has more than one primary hero/stage
- decorative chips are below the component budget
- desktop/tablet/mobile screenshots pass without overflow or unnamed controls
- residual raw provider/runtime/debug wording is behind a details boundary

## PRJ-1237 Lane Notes

- UX/reference lane completed read-only and confirmed the primary problem:
  excessive controls, cards, badges, fake chrome, route-local sidebars, and
  equal-weight first-viewport groups are the main source of chaos.
- Architecture/data lane was delegated but timed out before reporting. The
  coordinator therefore kept this artifact limited to known app API contracts
  and current route/client data sources. Any future route that needs new data
  must update this index after the backend contract exists.
