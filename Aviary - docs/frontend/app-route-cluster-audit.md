# App Route Cluster Audit

Last updated: 2026-05-03

This audit maps the remaining `web/src/App.tsx` route-local rendering clusters
after the route contract, shared shell, dashboard signal card, personality
timeline row, and tools component extractions.

## Current Route Branches

| Route branch | Start line in `App.tsx` | Current extraction posture | Recommended next action |
| --- | ---: | --- | --- |
| `/dashboard` | 4058 | Large visual flagship branch; partially uses `DashboardSignalCard` and shared panels | Defer broad moves until a screenshot-parity slice is active |
| `/chat` | 4353 | High-behavior branch now split across chat helpers/components; route state, API calls, send behavior, and message mapping remain in `App()` | No immediate chat extraction before a fresh behavior/state audit |
| `/memory` | 4441 | Module-style overview route using shared cards and `ModuleOverviewBar` | Inner module panels remain future candidates |
| `/reflections` | 4536 | Module-style overview route using shared cards and `ModuleOverviewBar` | Inner module panels remain future candidates |
| `/plans` | 4626 | Module-style overview route using shared cards and `ModuleOverviewBar` | Inner module panels remain future candidates |
| `/goals` | 4716 | Module-style overview route using shared cards and `ModuleOverviewBar` | Inner module panels remain future candidates |
| `/insights` | 4812 | Module-style overview route using shared note/stat/side-panel patterns | Side-panel/row chrome extracted in PRJ-995; broader route module extraction can wait |
| `/automations` | 4911 | Module-style route mixed with health-derived scheduler posture and shared side-panel patterns | Align simple overview/stat presentation with existing shared module components before health helper movement |
| `/integrations` | 5009 | Tools/health provider readiness branch; already benefits from tool helper extraction | Align simple overview/stat/readiness row presentation with existing shared module components before provider helper movement |
| `/settings` | 5112 | Form-heavy branch; preference card/fact and side panel shells live in `web/src/components/settings.tsx`; settings formatting helpers live in `web/src/lib/settings-formatting.ts` | No immediate extraction needed in this cluster |
| `/tools` | 5289 | Tools presentation cluster extracted to `web/src/components/tools.tsx`; route state remains in `App()` | No immediate extraction needed in this cluster |
| `/personality` | 5505 | Visual/personality branch; partially uses `PersonalityTimelineRow` | Defer until callout/card ownership can be split without changing canonical visuals |

## Remaining Helper Clusters

| Helper cluster | Current owner | Routes | Posture |
| --- | --- | --- | --- |
| Markdown rendering | `renderChatMarkdown` in `web/src/lib/chat-markdown.tsx`; characterization in `web/scripts/chat-markdown-characterization.mjs` | `/chat` | Extracted and characterized in PRJ-1003 |
| Chat route display model | `buildChatRouteModel` in `web/src/lib/chat-route-model.ts` | `/chat` | Extracted in PRJ-1017; API calls, state, send behavior, transcript behavior, and rendering remain in `App()` |
| Chat transcript metadata | `transcriptMetadataSummary`, `chatDeliveryState`, `reconcileLocalTranscriptItems` in `web/src/lib/chat-transcript.ts` | `/chat` | Extracted in PRJ-1001 |
| Chat transcript row | `ChatTranscriptMessageRow` in `web/src/components/chat.tsx` | `/chat` | Extracted in PRJ-1007; mapping, refs, delivery, timestamp, and markdown remain in `App()` |
| Chat transcript shell | `ChatTranscriptShell` in `web/src/components/chat.tsx` | `/chat` | Extracted in PRJ-1015; container ref, loading fallback, rows, and composer are passed explicitly |
| Chat composer shell | `ChatComposerShell` in `web/src/components/chat.tsx` | `/chat` | Extracted in PRJ-1005; send behavior remains in `App()` |
| Chat cognitive belt | `ChatCognitiveBelt` in `web/src/components/chat.tsx` | `/chat` | Extracted in PRJ-1009; card data and goal-progress derivation remain in `App()` |
| Chat topbar | `ChatTopbar` in `web/src/components/chat.tsx` | `/chat` | Extracted in PRJ-1011; active summary and posture labels remain in `App()` |
| Chat portrait/support panel | `ChatPortraitPanel` in `web/src/components/chat.tsx` | `/chat` | Extracted in PRJ-1013; focus/emphasis/learned-cue labels remain in `App()` |
| Learned-state summaries | `recentActivityRows`, `summaryLines`, `stringValue`, `formatTimestamp` in `web/src/lib/learned-state-formatting.ts` | dashboard and module routes | Extracted in PRJ-997 |
| Health/channel summaries | `conversationChannelStatus` in `App.tsx` | dashboard, automations, integrations | Deferred in PRJ-998 until provider/integration route ownership is clearer |
| Metric formatting | `numberValue`, `scaledMetricSize` in `web/src/lib/metric-formatting.ts` | dashboard, automations, integrations, tools summary projections | Extracted in PRJ-999 |
| Settings formatting | `normalizeUiLanguage`, `resolveUiLanguage`, `normalizeUtcOffset`, `utcOffsetOption`, `localeOptionDisplay` in `web/src/lib/settings-formatting.ts` | `/settings`, bootstrap | Extracted in PRJ-993 |

## Next Slice

`PRJ-991` extracted the settings preference card/fact presentation cluster.
`PRJ-992` extracted the settings side panel shell cluster. `PRJ-993` extracted
the settings formatting helpers.

`PRJ-995` extracted shared module route side-panel/row presentation for
`/insights` and `/automations`.

Chat transcript behavior and dashboard flagship visuals remain higher risk than
these module-style side-panel shells.

## Helper Extraction Decision

`PRJ-996` compared the remaining helper clusters after module side-panel
cleanup. `PRJ-997` extracted learned-state summary helpers:

- moved `recentActivityRows` and `summaryLines` behind a small learned-state
  formatting module
- keep route-specific derived arrays and UI copy in `App()`
- keep health/channel telemetry helpers in `App()` until integrations/provider
  route ownership is clearer

`PRJ-998` deferred `conversationChannelStatus` because it encodes Telegram
provider and health semantics. `PRJ-999` extracted pure metric formatting
helpers while keeping `conversationChannelStatus` in `App()`.

`PRJ-1000` selected chat transcript metadata helper extraction as the next
frontend architecture slice. `PRJ-1001` extracted it:

- moved `transcriptMetadataSummary`, `chatDeliveryState`, and
  `reconcileLocalTranscriptItems` to a small chat transcript module
- keep markdown rendering, composer behavior, optimistic send state, and route
  rendering in `App()`
- run `npm run build` and the 14-route smoke

`PRJ-1002` reviewed markdown renderer extraction readiness. `PRJ-1003` moved
the renderer to `web/src/lib/chat-markdown.tsx` and added
`npm run test:chat-markdown`, a focused characterization proof for inline code,
bold/italic, lists, paragraph line breaks, and fenced code blocks.

`PRJ-1004` selected chat composer shell extraction as the next safe chat route
slice:

- move action tray, mode tabs, composer shell, and composer note behind a chat
  component
- keep `handleSendMessage`, `chatText`, `sendingMessage`, and optimistic send
  state in `App()`
- pass quick-action, textarea, and submit behavior through explicit props

`PRJ-1005` implemented that slice with `ChatComposerShell` in
`web/src/components/chat.tsx`. The component owns only composer presentation
chrome and receives quick actions, textarea value, labels, icons, and handlers
through explicit props. `App()` still owns `handleSendMessage`, `chatText`,
`sendingMessage`, optimistic local transcript reconciliation, and durable
history refresh. The next safe chat route step is to audit transcript
message-row presentation extraction now that helper, renderer, and composer
boundaries are explicit.

`PRJ-1006` selected transcript message-row presentation extraction as the next
safe implementation slice:

- move the avatar, row alignment class, message article class, metadata chrome,
  delivery indicator element, and copy wrapper behind a chat transcript message
  row component
- keep `visibleTranscriptItems.map(...)`, `transcriptMessageRefs`,
  `chatDeliveryState`, `deliveryLabel` selection, `formatTimestamp(...)`, and
  `renderChatMarkdown(...)` in `App()` for this slice
- pass `isUser`, preview state, speaker label, timestamp label, delivery
  state/label, and rendered markdown content through explicit props

`PRJ-1007` implemented that slice with `ChatTranscriptMessageRow` in
`web/src/components/chat.tsx`. The component owns row alignment, avatar,
message article classing, metadata chrome, delivery indicator element, and the
copy wrapper. `App()` still owns transcript mapping, `transcriptMessageRefs`,
delivery-state calculation, delivery-label selection, timestamp formatting,
and markdown rendering. The next safe chat route step is to audit whether the
cognitive belt or portrait/support-panel chrome can move behind explicit data
props without changing the canonical chat layout.

`PRJ-1008` selected the cognitive belt as the next implementation slice:

- move the `aion-chat-cognitive-belt` card-list presentation behind a
  `ChatCognitiveBelt` component
- keep `chatCognitiveBelt` data construction, goal-progress derivation, and
  planning/health summaries in `App()`
- defer the portrait/support panel because it is more tightly coupled to the
  canonical chat composition and should be audited separately
- defer the transcript shell/container because it owns loading state and refs

`PRJ-1009` implemented the cognitive belt slice with `ChatCognitiveBelt` in
`web/src/components/chat.tsx`. The component owns only the card-list
presentation and progress-bar element. `App()` still owns `chatCognitiveBelt`
data construction, planning/health summary derivation, and `chatGoalCard`
progress calculation. The next safe chat step is another audit before touching
topbar, portrait/support panel, or transcript shell ownership.

`PRJ-1010` selected chat topbar extraction as the next implementation slice:

- move `aion-chat-topbar`, headline/title/live-status chrome, and route-posture
  labels behind a `ChatTopbar` component
- keep `chatActiveSummary`, linked-channel summary, preferred-language
  formatting, and all route data derivation in `App()`
- defer portrait/support panel because it is visual-composition sensitive
- defer transcript shell/container because it owns loading state and refs

`PRJ-1011` implemented that slice with `ChatTopbar` in
`web/src/components/chat.tsx`. The component owns only headline, live-status,
and route-posture presentation. `App()` still owns `chatActiveSummary`,
`chatLinkedChannelsStatus`, preferred-language fallback formatting, and all
route data derivation. Portrait/support panel and transcript shell remain
deferred until separate audits.

`PRJ-1012` selected the chat portrait/support panel as the next implementation
slice:

- move `aion-chat-portrait-panel`, support notes, planning overlay, focus
  summary, learned-cue count display, and portrait copy behind a
  `ChatPortraitPanel` component
- keep `chatCurrentFocus`, `chatIntentCard.emphasis`, learned-cue count
  formatting, and all route data derivation in `App()`
- defer transcript shell/container because it owns loading state and refs
- defer chat route data-helper extraction because it is broader than a single
  presentational slice

`PRJ-1013` implemented the portrait/support panel slice with
`ChatPortraitPanel` in `web/src/components/chat.tsx`. The component owns support
notes, planning overlay chrome, learned-cue display chrome, and portrait copy.
`App()` still owns `chatCurrentFocus`, `chatIntentCard.emphasis`,
learned-cue count fallback formatting, and all route data derivation.
Transcript shell/container and chat data-helper extraction remain deferred.

`PRJ-1014` selected a thin transcript shell extraction as the next
implementation slice:

- move the thread column and `aion-chat-transcript` container into a
  `ChatTranscriptShell` component
- pass the transcript container ref, loading fallback, message rows, and
  composer as explicit props/children
- keep `visibleTranscriptItems.map(...)`, `transcriptMessageRefs`,
  `chatDeliveryState`, delivery-label selection, timestamp formatting, and
  `renderChatMarkdown(...)` in `App()`
- defer chat route data-helper extraction because it is broader than a shell
  presentation slice

`PRJ-1015` implemented the shell slice with `ChatTranscriptShell` in
`web/src/components/chat.tsx`. The component owns the thread-column and
transcript-container classes and forwards the container ref. `App()` still owns
loading fallback selection, message mapping, message refs, delivery-state and
delivery-label calculation, timestamp formatting, markdown rendering, composer
state/handlers, and chat route data helpers.

`PRJ-1016` selected a focused chat route display-model helper extraction as the
next implementation slice:

- create `web/src/lib/chat-route-model.ts`
- move pure display projections for quick actions, current focus, linked-channel
  fallback, intent card, motivation metrics, goal card, and related-memory
  cards behind explicit summary inputs
- keep chat API calls, chat state, transcript mapping, send behavior, and route
  rendering in `App()`
- preserve current fallback strings and route display behavior

`PRJ-1017` implemented that slice with `buildChatRouteModel` in
`web/src/lib/chat-route-model.ts`. The helper owns quick actions, current
focus, linked-channel fallback, intent card, motivation metrics, goal card, and
related-memory projections from explicit summary inputs. `App()` still owns chat
API calls, chat state, transcript reconciliation, send behavior, message
mapping, and route rendering.

`PRJ-1018` re-checked current route anchors after the chat cleanup lane. The
next safe frontend architecture slice is a shared module overview bar:

- add a route-keyed `ModuleOverviewBar` shared component
- replace the repeated overview bar chrome for `/memory`, `/reflections`,
  `/plans`, and `/goals`
- preserve route-specific CSS classes, copy, status labels, values, and aria
  labels through explicit props
- defer dashboard/personality because they are flagship visual surfaces
- defer provider/health helpers until a provider-aware ownership audit

`PRJ-1019` implemented that slice with `ModuleOverviewBar` in
`web/src/components/shared.tsx`. `/memory`, `/reflections`, `/plans`, and
`/goals` now pass route key, copy, status label/value, and aria label explicitly
while preserving existing route-specific selectors and route data ownership.

`PRJ-1020` selected the repeated stat-row wrapper as the next implementation
slice:

- add a route-keyed `ModuleStatRow` shared component
- replace the repeated stat-row section wrappers for `/memory`, `/reflections`,
  `/plans`, and `/goals`
- keep stat card arrays and `RouteStatCard` usage in `App()`
- preserve route-specific aria labels and CSS selectors through explicit props

`PRJ-1021` implemented that slice with `ModuleStatRow` in
`web/src/components/shared.tsx`. `/memory`, `/reflections`, `/plans`, and
`/goals` now use a route-keyed stat-row wrapper while keeping stat card arrays
and `RouteStatCard` mapping in `App()`.

`PRJ-1022` selected the recent activity list as the next implementation slice:

- add a route-keyed `ModuleActivityList` shared component
- replace repeated recent activity row markup for `/memory` and `/reflections`
- keep `personalityRecentActivity` data ownership and slicing in `App()`
- defer decorative main panels because their visual structure is more
  route-specific

`PRJ-1023` implemented that slice with `ModuleActivityList` in
`web/src/components/shared.tsx`. `/memory` and `/reflections` now share
route-keyed recent activity row chrome while keeping panel headings,
`personalityRecentActivity` ownership, and slicing in `App()`.

`PRJ-1024` reviewed the remaining module-route inner card clusters after
activity-list extraction. The next safe implementation slice is a shared
route-keyed title/body card-list component for:

- `/reflections` prompt cards
- `/plans` next-step cards
- `/goals` signal cards

This target preserves the current route-specific class names through explicit
route/card keys, keeps all card data and copy construction in `App()`, and
avoids the higher-risk decorative goal horizon panel. Memory signal cards are
deferred because they include a `meta` field; plans/goals dot-row context lists
are deferred because their chrome differs from the simple title/body cards.

`PRJ-1025` implemented that slice with `ModuleTextCardList` in
`web/src/components/shared.tsx`. `/reflections` prompt cards, `/plans`
next-step cards, and `/goals` signal cards now share the same title/body
card-list component while preserving their route-specific class selectors and
keeping all route data arrays in `App()`. The next module cleanup target should
be audited separately before touching memory signal cards, dot-row
guidance/context lists, or decorative route panels.

`PRJ-1026` selected shared dot-row list extraction as the next implementation
slice. `/plans` context rows and `/goals` guidance rows share the same row
shape: wrapper grid, article row, decorative dot, title, and body. A
route-keyed `ModuleDotRowList` can preserve the existing
`aion-plans-context-*` and `aion-goals-guidance-*` selectors while keeping
`plansContextCards` and `goalGuidanceCards` in `App()`. Memory signal cards and
goal horizon rows remain deferred because their shapes are different.

`PRJ-1027` implemented that slice with `ModuleDotRowList` in
`web/src/components/shared.tsx`. `/plans` context rows and `/goals` guidance
rows now share route-keyed dot-row presentation while `plansContextCards` and
`goalGuidanceCards` stay in `App()`. The remaining module route cleanup
candidates are now either single-route card shapes, route data/helper slices, or
decorative panels that should be audited separately.

`PRJ-1028` selected `/integrations` shared-shell alignment as the next
implementation slice. The route still owns provider/tool data in `App()`, but
its overview bar, stat row, and readiness detail dot rows match existing shared
component shapes. The next task should reuse `ModuleOverviewBar`,
`ModuleStatRow`, and `ModuleDotRowList` for those simple presentation shells
while deferring `conversationChannelStatus`, provider/health helper movement,
and the decorative provider-map panel.

`PRJ-1029` implemented that slice. `/integrations` now uses
`ModuleOverviewBar`, `ModuleStatRow`, and `ModuleDotRowList` for the simple
route shell while preserving `aion-integrations-*` selectors and keeping
`integrationItems`, `integrationStatCards`, `integrationReadinessRows`,
provider rows, and provider readiness semantics in `App()`.

`PRJ-1030` selected `/automations` shared-shell alignment as the next
implementation slice. The route still owns health-derived scheduler and
attention data in `App()`, but its overview bar and stat row match existing
`ModuleOverviewBar` and `ModuleStatRow` usage. `conversationChannelStatus`,
integrations provider rows, memory signal cards, and decorative panels remain
deferred.

`PRJ-1031` implemented that slice. `/automations` now uses
`ModuleOverviewBar` and `ModuleStatRow` for the route shell while preserving
`aion-automations-*` selectors and keeping `automationStatCards`,
`automationFlowRows`, scheduler summary, attention metrics, and proactive state
in `App()`.

`PRJ-1032` checked the next health/channel helper candidate and found
`conversationChannelStatus` is no longer called in `App.tsx`; the only matches
are the type and function declarations. The next implementation slice is
therefore dead-code removal, not helper extraction. Live provider/health helper
movement, integrations provider rows, memory signal cards, and decorative panels
remain deferred for separate audits.

`PRJ-1033` removed that unused helper, its local `ConversationChannelStatus`
type, its `lastState` helper, and the stale `AppHealthTelegramChannel` import.
No live route behavior changed. Future provider/health cleanup should start
from currently used data projections, not from the removed channel-status
helper.

`PRJ-1034` selected integrations provider row presentation extraction as the
next live frontend cleanup. The list has a stable `token/title/detail/value`
shape and can move behind a route-keyed shared row-list component while
`integrationProviderRows`, fallback row selection, and provider readiness
semantics stay in `App()`. Memory signal cards, progress rows, route data-helper
movement, and decorative panels remain deferred.

`PRJ-1035` implemented that slice with `ModuleValueRowList` in
`web/src/components/shared.tsx`. `/integrations` provider rows now use the
shared route-keyed value-row presentation while `integrationProviderRows`,
`integrationProviderDisplayRows`, provider readiness values, and fallback
selection stay in `App()`.

`PRJ-1036` selected memory signal card extraction as the next implementation
slice. The remaining `aion-memory-signal-*` cards have a simple
`meta/title/body` shape and can move behind a route-keyed `ModuleMetaCardList`
while `memorySignalCards` stays in `App()`. Dashboard and goal progress rows
remain deferred because they include sizing/progress visuals.

`PRJ-1037` implemented that slice with `ModuleMetaCardList` in
`web/src/components/shared.tsx`. `/memory` signal cards now share route-keyed
meta-card presentation while `memorySignalCards` remains in `App()`.

`PRJ-1038` selected `/goals` horizon row extraction as the next implementation
slice. The rows have stable `aion-goals-row-*` and `aion-goals-progress`
selectors and a bounded `token/title/detail/progress/value` shape. Dashboard
progress rows remain deferred because they sit in the flagship dashboard lower
card composition and should be handled by a dedicated dashboard audit.

`PRJ-1039` implemented that slice with `ModuleProgressValueRowList` in
`web/src/components/shared.tsx`. `/goals` horizon rows now share route-keyed
progress/value row presentation while `goalHorizonRows` remains in `App()`.
The component preserves `aion-goals-list`, `aion-goals-row-*`, and
`aion-goals-progress` selectors.

`PRJ-1040` selected dashboard progress list extraction as the next
implementation slice. Because `/dashboard` is the flagship surface, the next
component should live in `web/src/components/dashboard.tsx`, not the generic
shared component module. `dashboardGoalRows` and progress-width calculations
should remain in `App()`, while the row/list presentation moves behind a
`DashboardProgressList` component.

`PRJ-1041` implemented that slice with `DashboardProgressList` in
`web/src/components/dashboard.tsx`. Dashboard progress row presentation now
lives beside `DashboardSignalCard`, while `dashboardGoalRows` and
`scaledMetricSize(...)` remain in `App()`.

`PRJ-1042` selected `/insights` shared-shell/list alignment as the next
implementation slice. The route still owns insight stat, signal, clarity, and
guidance data in `App()`, but its overview bar, stat row, and signal value rows
match existing route-keyed shared component shapes. The next task should reuse
`ModuleOverviewBar`, `ModuleStatRow`, and `ModuleValueRowList` while preserving
`aion-insights-*` selectors and deferring the decorative orbit/map panel,
dashboard route data-helper movement, provider/health-coupled rows, and broad
visual polish.

`PRJ-1043` implemented that slice. `/insights` now uses `ModuleOverviewBar`,
`ModuleStatRow`, and `ModuleValueRowList` for the simple route shell and signal
rows while preserving `aion-insights-*` selectors and keeping
`insightStatCards`, `insightSignalRows`, clarity/guidance data, and the
decorative orbit/map panel in `App()`.

`PRJ-1044` selected `/integrations` side-panel shared alignment as the next
implementation slice. The route still owns provider rows, readiness rows, and
the decorative web/map panel in `App()`, but its boundary and readiness side
panels match the existing `ModuleRouteSidePanel` contract exactly, including
the `boundary` variant class. Automations flow rows, route data-helper
movement, and decorative panels remain deferred.

`PRJ-1045` implemented that slice. `/integrations` now uses
`ModuleRouteSidePanel` for the boundary and readiness side panels while keeping
`integrationBoundaryCards`, `integrationReadinessRows`, provider rows, and the
decorative web/map panel in `App()`. The existing
`aion-integrations-side-panel` and `aion-integrations-side-panel-boundary`
classes are preserved through the shared route-keyed component.

`PRJ-1046` selected `/automations` flow-row shared alignment as the next
implementation slice. `automationFlowRows` already has the
`token/title/detail/value` shape used by `ModuleValueRowList`, and
`routeKey="automations"` with `rowKey="flow"` preserves the existing
`aion-automations-flow-*` selectors. Health/proactive data construction,
route data-helper movement, and decorative switchboard panels remain deferred.

`PRJ-1047` implemented that slice. `/automations` flow rows now use
`ModuleValueRowList` while `automationFlowRows`, scheduler summary, health
snapshot consumption, proactive state, and the decorative switchboard remain in
`App()`.

`PRJ-1048` selected `/automations` health-row shared alignment as the next
implementation slice. `automationHealthRows` has the `title/body` shape already
used by `ModuleDotRowList`, and `routeKey="automations"` with `rowKey="health"`
preserves the existing `aion-automations-health-*` selectors. Health data
construction, route data-helper movement, and decorative panels remain
deferred.

`PRJ-1049` implemented that slice. `/automations` health rows now use
`ModuleDotRowList` while `automationHealthRows` and health snapshot data
construction remain in `App()`.

`PRJ-1050` selected `/insights` guidance-row shared alignment as the next
implementation slice. `insightGuidanceCards` has the `title/body` shape already
used by `ModuleDotRowList`, and `routeKey="insights"` with
`rowKey="guidance"` preserves the existing `aion-insights-guidance-*`
selectors. Route data-helper movement and decorative panels remain deferred.

`PRJ-1051` implemented that slice. `/insights` guidance rows now use
`ModuleDotRowList` while `insightGuidanceCards` and the side-panel composition
remain in `App()`. The stale `ModuleRouteSideRow` import was removed from
`App.tsx`.

`PRJ-1052` selected unused `ModuleRouteSideRow` removal as the next
implementation slice. The last live call site was removed in `PRJ-1051`; the
only remaining code reference is the exported component in
`web/src/components/shared.tsx`. The next task should remove that export and
refresh the active frontend component map while leaving historical task
evidence untouched.

`PRJ-1053` implemented that slice. `ModuleRouteSideRow` was removed from
`web/src/components/shared.tsx`, and the active frontend component map no
longer lists it. Historical task evidence still mentions the component where it
was part of earlier extraction work.

`PRJ-1054` selected shared route note-card list extraction as the next
implementation slice. `/insights`, `/automations`, and `/integrations` repeat
the same `mt-5 grid gap-3` wrapper around `RouteNoteCard` maps, and the
extraction can preserve all `aion-*-note-card` selectors by reusing the
existing card component.

`PRJ-1055` implemented that slice. `RouteNoteCardList` now lives in
`web/src/components/shared.tsx` and is used by the insights clarity,
automations boundary, and integrations boundary side panels while their route
data arrays remain in `App()`.

`PRJ-1056` selected shared route stat-card list extraction as the next
implementation slice. Memory, reflections, plans, goals, insights,
automations, and integrations repeat the same `RouteStatCard` map inside
`ModuleStatRow`. A `RouteStatCardList` wrapper can preserve every
`aion-*-stat-card` selector by reusing the existing card component while route
stat data arrays remain in `App()`.

`PRJ-1057` implemented that slice. `RouteStatCardList` now lives in
`web/src/components/shared.tsx` and is used inside the existing `ModuleStatRow`
wrappers for memory, reflections, plans, goals, insights, automations, and
integrations while stat data arrays remain in `App()`.

`PRJ-1058` selected shared personality timeline-row list extraction as the next
implementation slice. Memory continuity rows, reflection flow rows, planning
flow rows, and the personality route timeline all repeat the same
`PersonalityTimelineRow` map while using different wrapper classes. A
`PersonalityTimelineRowList` can preserve those wrappers through a `className`
prop while route data arrays remain in `App()`.

`PRJ-1059` implemented that slice. `PersonalityTimelineRowList` now lives in
`web/src/components/personality.tsx` and is used by memory continuity,
reflections flow, plans flow, and the personality timeline while preserving
their wrapper classes through `className`.

`PRJ-1060` selected stale `RouteStatCard` import removal as the next
implementation slice. After `PRJ-1057`, `App.tsx` uses `RouteStatCardList` for
all route stat-card maps and no longer calls `RouteStatCard` directly. The next
task should remove only that stale route-shell import while keeping
`RouteStatCard` exported for `RouteStatCardList`.

`PRJ-1061` implemented that slice. `App.tsx` no longer imports
`RouteStatCard` directly; `RouteStatCardList` remains the route-shell stat-card
boundary and the shared card export remains available inside
`web/src/components/shared.tsx`.

`PRJ-1062` selected shared personality signal-row list extraction as the next
implementation slice. The conscious and subconscious personality side panels
repeat the same `aion-personality-signal-row` map around `label/value` items. A
`PersonalitySignalRowList` can preserve the existing `grid gap-3` wrapper and
selectors while keeping signal data arrays in `App()`.

`PRJ-1063` implemented that slice. `PersonalitySignalRowList` now lives in
`web/src/components/personality.tsx` and is used by both conscious and
subconscious personality side panels while preserving the existing
`aion-personality-signal-*` selectors and route-owned signal data arrays.

`PRJ-1064` selected dashboard signal-column extraction as the next
implementation slice. The dashboard hero left and right columns both filter
`dashboardSignalCards` by `placement` and render the existing
`DashboardSignalCard`. A `DashboardSignalColumn` can preserve the
`aion-dashboard-signal-column` wrapper and card props while avoiding broader
flagship layout, figure, flow, or route data changes.

`PRJ-1065` implemented that slice. `DashboardSignalColumn` now lives in
`web/src/components/dashboard.tsx` and is used for the dashboard hero left and
right signal columns while preserving the existing wrapper class, card props,
and route-owned `dashboardSignalCards` data.

`PRJ-1066` selected public trust-pill list extraction as the next
implementation slice. The public micro-proof row and proof-bridge list both
render `publicHomeSurface.trustBand.slice(0, 3)` with `PublicGlyph`, using
different wrapper, item, and icon classes. A class-configurable
`PublicTrustPillList` can preserve both visual call sites while keeping the
footer trust band and public copy data in `App()`.

`PRJ-1067` implemented that slice. `PublicTrustPillList` now lives in
`web/src/components/public-shell.tsx` and is used by the public micro-proof row
and proof-bridge trust list while preserving each call site's wrapper, item,
and icon classes.

`PRJ-1068` selected public feature-card list extraction as the next
implementation slice. The public feature strip maps `publicHomeSurface.pillars`
through the same `PublicGlyph` owner module and can move into
`PublicFeatureCardList` while preserving `aion-public-feature-*` classes and
keeping public route copy/data in `App()`.

`PRJ-1069` implemented that slice. `PublicFeatureCardList` now lives in
`web/src/components/public-shell.tsx` and renders the public feature strip with
the existing `PublicGlyph` and `aion-public-feature-*` classes while public
route copy/data stays in `App()`.

`PRJ-1070` selected public footer trust-band extraction as the next
implementation slice. The public footer maps `publicHomeSurface.trustBand`
into `aion-public-trust-item` articles with `PublicGlyph`; a dedicated
`PublicTrustBand` can preserve that article structure without overloading the
proof pill list semantics.

`PRJ-1071` implemented that slice. `PublicTrustBand` now lives in
`web/src/components/public-shell.tsx` and renders the public footer trust band
with the existing footer semantics, `PublicGlyph`, and
`aion-public-trust-*` classes while public route data stays in `App()`.

`PRJ-1072` selected dashboard reflection-list extraction as the next
implementation slice. The reflection highlight card maps `dashboardReflectionRows`
into `aion-dashboard-reflection-row` elements with a static `title/tag` shape.
`DashboardReflectionList` can preserve those classes while leaving dynamic
memory bars, guidance CTA rows, and dashboard figure/flow pieces deferred.

`PRJ-1073` implemented that slice. `DashboardReflectionList` now lives in
`web/src/components/dashboard.tsx` and renders dashboard reflection highlights
with the existing `aion-dashboard-reflection-*` classes while
`dashboardReflectionRows` stays in `App()`.

`PRJ-1074` selected dashboard memory bar-chart extraction as the next
implementation slice. The memory card maps `dashboardMemoryBars` into
`aion-dashboard-bar-*` elements with dynamic `height` values already computed
in `App()`. `DashboardMemoryBarChart` can preserve the inline height style and
classes while keeping scaled metric calculations in the route shell.

`PRJ-1075` implemented that slice. `DashboardMemoryBarChart` now lives in
`web/src/components/dashboard.tsx` and renders the dashboard memory bar chart
with the existing `aion-dashboard-bar-*` classes and inline `height` style
while `dashboardMemoryBars` remains in `App()`.

`PRJ-1076` selected dashboard guidance-list extraction as the next
implementation slice. The guidance panel maps `dashboardGuidanceCards.slice(0, 4)`
into rows with `title/body/action` content and passive buttons. A
`DashboardGuidanceList` can preserve the lead-row class, button classes, and
button type while leaving data and CTA behavior unchanged.

`PRJ-1077` implemented that slice. `DashboardGuidanceList` now lives in
`web/src/components/dashboard.tsx` and renders the dashboard guidance rows with
the existing lead-row class and passive button markup while
`dashboardGuidanceCards` remains in `App()`.

`PRJ-1078` selected dashboard recent-activity list extraction as the next
implementation slice. The dashboard recent panel maps
`personalityRecentActivity.slice(0, 4)` into `aion-dashboard-recent-row`
elements with a `title/when` shape. A dashboard-specific
`DashboardRecentActivityList` can preserve that markup while leaving the
different personality activity rows deferred.

`PRJ-1079` implemented that slice. `DashboardRecentActivityList` now lives in
`web/src/components/dashboard.tsx` and renders the dashboard recent activity
rows with the existing `aion-dashboard-recent-row` and text classes while the
`slice(0, 4)` data selection stays in `App()`.

`PRJ-1080` selected dashboard balance-grid extraction as the next
implementation slice. The dashboard summary balance section maps
`dashboardBalanceRows` into `aion-dashboard-summary-balance-row` elements with
index-based token classes. `DashboardBalanceGrid` can preserve that small grid
without moving the full summary band or harmony copy.

`PRJ-1081` implemented that slice. `DashboardBalanceGrid` now lives in
`web/src/components/dashboard.tsx` and renders dashboard summary balance rows
with the existing `aion-dashboard-summary-balance-*` classes and index-based
token class numbering while `dashboardBalanceRows` stays in `App()`.

`PRJ-1082` selected dashboard cognitive flow-track extraction as the next
implementation slice. The flow intro maps `dashboardCognitiveSteps` into
`aion-dashboard-flow-step` cards with an active-step modifier. A
`DashboardCognitiveFlowTrack` can preserve the track and step classes while
leaving the full flow shell and current phase panel in `App()`.

`PRJ-1083` implemented that slice. `DashboardCognitiveFlowTrack` now lives in
`web/src/components/dashboard.tsx` and renders dashboard cognitive flow steps
with the existing track, step, icon, text, and active-step classes while the
current phase aside remains in `App()`.

`PRJ-1084` selected dashboard figure-note extraction as the next implementation
slice. The hero figure stage maps `dashboardFigureNotes` into
`aion-dashboard-figure-note-*` articles. `DashboardFigureNoteList` can preserve
the caller-owned note classes while leaving the hero image, halo, badge, and
overall figure layout in `App()`.

`PRJ-1085` implemented that slice. `DashboardFigureNoteList` now lives in
`web/src/components/dashboard.tsx` and renders dashboard hero figure notes with
the existing caller-owned note classes while the figure image, halo, badge, and
stage layout stay in `App()`.

`PRJ-1086` selected personality activity-row list extraction as the next
implementation slice. The personality side panel maps `personalityRecentActivity`
into `aion-personality-activity-row` entries with a visible action chip. A
`PersonalityActivityRowList` can preserve that personality-specific shape while
avoiding false sharing with dashboard recent activity rows.

`PRJ-1087` implemented that slice. `PersonalityActivityRowList` now lives in
`web/src/components/personality.tsx` and renders personality recent activity
rows with the existing `aion-personality-activity-row` and chip classes while
`personalityRecentActivity` stays in `App()`.

`PRJ-1088` selected settings hero status-pill list extraction as the next
implementation slice. The `/settings` hero still maps `settingsHeroChips` into
`aion-settings-status-pill` elements inline, while `web/src/components/settings.tsx`
already owns settings presentation shells. A `SettingsStatusPillList` can
preserve the current grid and pill selectors while leaving settings data and
draft state in `App()`. Tools group/item cards and broader route data helpers
remain deferred because they touch actions, toggles, or wider route ownership.

`PRJ-1089` implemented that slice. `SettingsStatusPillList` now lives in
`web/src/components/settings.tsx` and renders the existing status grid and pill
classes while `settingsHeroChips` remains in `App()`.

`PRJ-1090` selected tools summary card-list extraction as the next
implementation slice. The `/tools` hero summary still maps four display-only
cards into `ToolsSummaryCard`, while the tools directory maps include user
preference toggles, provider readiness, and Telegram linking actions. A
`ToolsSummaryCardList` can preserve the current summary grid and card component
while leaving `toolsOverview` data, tool toggles, and link handlers in `App()`.

`PRJ-1091` implemented that slice. `ToolsSummaryCardList` now lives in
`web/src/components/tools.tsx`, reuses `ToolsSummaryCard`, and preserves the
existing summary grid while `toolsSummaryCards` data remains in `App()`.

`PRJ-1092` selected personality hero preview-callout extraction as the next
implementation slice. The `/personality` hero still maps
`personalityPreviewCallouts` into caller-classed articles inside
`aion-personality-hero-figure`. A `PersonalityPreviewCalloutList` can preserve
the current article typography and callout classes while leaving callout data in
`App()`. Tools directory cards, shell navigation, form option maps, and route
data projections remain deferred because they are behaviorful, control-specific,
or not presentation extraction targets.

`PRJ-1093` implemented that slice. `PersonalityPreviewCalloutList` now lives in
`web/src/components/personality.tsx` and renders the personality hero callout
articles while `personalityPreviewCallouts` and the hero figure/stage layout
remain in `App()`.

`PRJ-1094` selected public home nav-link list extraction as the next
implementation slice. The public shell still maps `publicHomeSurface.nav` into
`aion-public-nav-link` anchors inline. A `PublicNavLinkList` can preserve the
current wrapper, anchor classes, and `#aviary-home` target while leaving public
copy/data in `App()`. Tools directory cards, shell account facts, form option
maps, shell route navigation, and route data projections remain deferred.

`PRJ-1095` implemented that slice. `PublicNavLinkList` now lives in
`web/src/components/public-shell.tsx` and renders the existing public nav
wrapper and anchors while `publicHomeSurface.nav` stays in `App()`.

`PRJ-1096` selected shell account fact-list extraction as the next
implementation slice. `accountSummaryItems` is still mapped inline in the
desktop account popover and mobile account panel with different wrappers but
the same `label/value` data shape. A shell-owned `ShellAccountFactList` can
preserve both desktop and mobile classes through a variant prop while leaving
account data, account-panel state, route navigation, and sign-out actions in
`App()`.

`PRJ-1097` implemented that slice. `ShellAccountFactList` now lives in
`web/src/components/shell.tsx` and renders the desktop popover and mobile
account fact variants while `accountSummaryItems`, account-panel state, route
navigation, and actions remain in `App()`.

`PRJ-1098` selected desktop sidebar nav button-list extraction as the next
implementation slice. `App.tsx` still maps `shellNavItems` into the
`aion-sidebar-nav` wrapper and existing `ShellNavButton` components. A
`ShellNavButtonList` can preserve the wrapper, active/disabled props, and
existing button component while `changeRoute`, active route state, and nav item
data stay in `App()`. Mobile tabbar remains deferred because it owns scroll
refs; settings option maps, tools directory behavior, and route data projections
remain deferred.

`PRJ-1099` implemented that slice. `ShellNavButtonList` now lives in
`web/src/components/shell.tsx`, renders the existing `aion-sidebar-nav` wrapper
and `ShellNavButton` instances, and receives active route plus route-change
callback from `App()`.

`PRJ-1100` selected shell route-switcher extraction as the next implementation
slice. The route header still maps `ROUTES` into the tablet/desktop switcher
inside `aion-mobile-route-header`, but unlike the bottom mobile tabbar it does
not own refs. A `ShellRouteSwitcher` can preserve the existing border wrapper,
scroll row, button classes, active state, and route-change callback while route
labels and route state stay in `App()`.

`PRJ-1101` implemented that slice. `ShellRouteSwitcher` now lives in
`web/src/components/shell.tsx`, renders the existing route-header switcher
wrapper/buttons, and receives routes, active route, label function, and
route-change callback from `App()`.

`PRJ-1102` selected settings select option-list extraction as the next
implementation slice. The UI language and UTC offset selects still map option
items inline in `App.tsx`, but the select state, normalization, and `onChange`
handlers should stay in `App()`. A small `SettingsSelectOptionList` can render
the option elements through a caller-provided label function while leaving form
ownership unchanged.

`PRJ-1103` implemented that slice. `SettingsSelectOptionList` now lives in
`web/src/components/settings.tsx` and renders both UI language and UTC offset
options while select values, normalization, language-aware labels, and handlers
remain in `App()`.

`PRJ-1104` re-audited the remaining `App.tsx` maps after settings select option
cleanup. The remaining candidates are not another obvious display-only JSX
list:

- pure route data projections remain in `App()` for now
- tools directory groups/items are behaviorful because they include user
  preference toggles, provider readiness display, and Telegram link actions
- chat transcript rows are ref/message-behavior sensitive
- bottom mobile tabbar owns route refs and scroll behavior

The next safe frontend architecture step is `PRJ-1105`, a TESTER-mode
tools-directory behavior characterization before any tools directory extraction.

`PRJ-1105` added that tools behavior characterization. `PRJ-1106` then moved
the `/tools` group/item presentation behind `ToolsDirectoryGroupList` in
`web/src/components/tools.tsx` while keeping route-owned data, busy state,
Telegram link state, and handlers in `App()`. After this extraction, the
remaining `App.tsx` maps are data projections, local transcript state updates,
the chat transcript render map, public hero highlight projection, and the
mobile tabbar ref map. The next safe step is `PRJ-1107`, an ARCHITECT-mode
boundary audit rather than an immediate extraction.

`PRJ-1107` completed that boundary audit. Chat transcript rendering and bottom
mobile tabbar rendering remain deferred because they own refs and
route-specific behavior. The next small implementation target is `PRJ-1108`,
which aligns the public hero card data shape with `MotifFigurePanel`'s
`label/value` highlights to remove the one-off JSX projection.

`PRJ-1108` completed that alignment. The public hero data now uses
`label/value` directly and `MotifFigurePanel` receives
`publicHomeSurface.heroCards` without a local projection. The remaining
implementation candidates should start with a fresh audit of the chat
transcript render map because it owns refs, delivery labels, timestamps, and
markdown rendering.

`PRJ-1109` completed that chat transcript readiness audit. Existing coverage
characterizes markdown rendering and transcript helper behavior, but not the
full row composition, refs, delivery labels, timestamps, preview fallback, or
optimistic delivery states together. The next safe task is `PRJ-1110`, a
focused chat transcript render characterization before any message-list
extraction.

`PRJ-1110` added that characterization, and `PRJ-1111` moved transcript row
mapping behind `ChatTranscriptMessageList` while `App()` still passes delivery
state, delivery-label copy, timestamp formatting, markdown rendering, and ref
registration callbacks explicitly. The remaining live JSX map in `App.tsx` is
the bottom mobile tabbar, which owns scroll refs and route button registration
and needs a separate readiness audit.

`PRJ-1112` completed that readiness audit. The safe next boundary is a
shell-owned `ShellMobileTabbar` that receives `routes`, `activeRoute`,
`labelForRoute`, `onRouteChange`, `scrollRef`, and `registerRouteRef` while
the active-route scroll-centering effect remains in `App()`.

`PRJ-1113` completed that extraction. `App.tsx` no longer has live JSX render
maps for route/component lists; the remaining `.map(...)` calls are data
projections or local transcript state updates. The next frontend task should be
a closure audit for those remaining data projections rather than another
presentational extraction.

`PRJ-1114` completed that closure audit. The remaining `App.tsx` maps are data
projections or local transcript state updates, not live JSX render maps. The
current frontend presentation extraction lane is closed; further frontend work
should be helper/data-model work only when a concrete v1 payoff is identified.
