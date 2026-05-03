# Frontend Route And Component Map

Last updated: 2026-05-03

This map documents the current browser shell without requiring a broad
component refactor. It is grounded in `web/src/App.tsx`,
`web/src/routes.ts`, `web/src/components/shared.tsx`, `web/src/lib/api.ts`,
`web/src/lib/tool-formatting.ts`,
`web/src/components/shell.tsx`, `web/src/components/public-shell.tsx`, and
`web/src/components/app-icons.tsx`, `web/src/components/chat.tsx`, and
`web/src/components/dashboard.tsx`, `web/src/components/personality.tsx`,
`web/src/components/settings.tsx`, `web/src/components/tools.tsx`,
`web/src/lib/chat-markdown.tsx`, `web/src/lib/chat-transcript.ts`, `web/src/lib/learned-state-formatting.ts`,
`web/src/lib/metric-formatting.ts`,
`web/src/lib/settings-formatting.ts`, `docs/frontend/app-route-cluster-audit.md`,
and `web/src/index.css`.

## Headless Route Smoke

`web/scripts/route-smoke.mjs` provides the current route-mount smoke. Run it
after a production build:

```powershell
Push-Location .\web
npm run build
npm run smoke:routes
Pop-Location
```

The smoke serves `web/dist`, supplies synthetic app-facing API responses, runs
Chrome or Edge headlessly, and checks stable top-level route container markers
for `/`, `/login`, and every current authenticated app route in
`web/src/routes.ts`: `/dashboard`, `/chat`, `/memory`, `/reflections`,
`/plans`, `/goals`, `/insights`, `/automations`, `/integrations`, `/settings`,
`/tools`, and `/personality`. It is a route-mount guard, not a screenshot
parity suite.

## Tools Directory Characterization

`web/scripts/tools-directory-characterization.mjs` provides the focused
behavior guard for `/tools`. Run it after a production build:

```powershell
Push-Location .\web
npm run build
npm run test:tools-directory
Pop-Location
```

The characterization serves `web/dist`, supplies synthetic app-facing API
responses, drives Chrome or Edge through CDP, and checks the full tools
directory, delayed loading, empty overview, API error state, ClickUp preference
toggle request payload, and Telegram link-start/code rendering.

## Chat Transcript Characterization

`web/scripts/chat-transcript-characterization.mjs` provides the focused
behavior guard for `/chat` transcript rendering. Run it after a production
build:

```powershell
Push-Location .\web
npm run build
npm run test:chat-transcript
Pop-Location
```

The characterization serves `web/dist`, supplies synthetic app-facing API
responses, drives Chrome or Edge through CDP, and checks preview fallback rows,
durable user/assistant rows, delivered indicators, markdown rendering, an
optimistic sending row, and the delivered assistant response after a mocked
send.

## Current Ownership Model

| Area | Owner File | Responsibility |
| --- | --- | --- |
| Route list and route normalization | `web/src/routes.ts` | `RoutePath`, `ROUTES`, `normalizeRoute`, `navigate`, `navigatePublicEntry` |
| Public/auth shell | `web/src/App.tsx` | Public home, login/register modal, session bootstrap, logout/reset redirects |
| Public shell helpers | `web/src/components/public-shell.tsx` | `PublicNavLinkList`, `MotifFigurePanel`, `PublicFeatureCardList`, `PublicTrustPillList`, `PublicTrustBand`, `PublicGlyph` |
| Authenticated product shell | `web/src/App.tsx` | Sidebar layout, mobile tab bar, route rendering, route copy |
| Shell chrome helpers | `web/src/components/shell.tsx` | `SidebarIconKind`, `ShellNavButton`, `ShellNavButtonList`, `ShellRouteSwitcher`, `ShellMobileTabbar`, `AviaryWordmark`, `SidebarBrandBlock`, `ShellUtilityBar` |
| App icon primitives | `web/src/components/app-icons.tsx` | `ChevronDownIcon`, `CloseIcon`, `PlusIcon`, `MicrophoneIcon`, `SendArrowIcon` |
| Chat components | `web/src/components/chat.tsx` | `ChatFlowStage`, `ChatTopbar`, `ChatCognitiveBelt`, `ChatTranscriptShell`, `ChatTranscriptMessageList`, `ChatTranscriptMessageRow`, `ChatComposerShell`, `ChatPortraitPanel` |
| Dashboard components | `web/src/components/dashboard.tsx` | `DashboardSignalCard`, `DashboardSignalColumn`, `DashboardProgressList`, `DashboardReflectionList`, `DashboardMemoryBarChart`, `DashboardGuidanceList`, `DashboardRecentActivityList`, `DashboardBalanceGrid`, `DashboardCognitiveFlowTrack`, `DashboardFigureNoteList` |
| Personality components | `web/src/components/personality.tsx` | `PersonalityTimelineRow`, `PersonalityTimelineRowList`, `PersonalitySignalRowList`, `PersonalityPreviewCalloutList`, `PersonalityActivityRowList` |
| Settings components | `web/src/components/settings.tsx` | `SettingsCard`, `SettingsFact`, `SettingsStatusPillList`, `SettingsSelectOptionList`, `SettingsProactivePanel`, `SettingsSavePanel`, `SettingsDangerPanel` |
| Tools components | `web/src/components/tools.tsx` | `ToolsSummaryCard`, `ToolsSummaryCardList`, `ToolsFactCard`, `ToolsDetailCard`, `ToolsTechnicalDetailPanel`, `ToolsTelegramLinkPanel` |
| Shared presentational panels | `web/src/components/shared.tsx` | `StatePanel`, `FeedbackBanner`, `ModuleEntryCard`, `FlowRail`, `ModuleOverviewBar`, `ModuleStatRow`, `ModuleActivityList`, `ModuleTextCardList`, `ModuleMetaCardList`, `ModuleDotRowList`, `ModuleValueRowList`, `ModuleProgressValueRowList`, `RouteHeroPanel`, `InsightPanel`, `RouteStatCard`, `RouteStatCardList`, `RouteNoteCard`, `RouteNoteCardList`, `ModuleRouteSidePanel` |
| API client | `web/src/lib/api.ts` | Typed fetch wrapper and app-facing endpoint methods |
| Chat markdown renderer | `web/src/lib/chat-markdown.tsx` | `renderChatMarkdown` |
| Chat route display model | `web/src/lib/chat-route-model.ts` | `buildChatRouteModel` |
| Chat transcript helpers | `web/src/lib/chat-transcript.ts` | `transcriptMetadataSummary`, `chatDeliveryState`, `reconcileLocalTranscriptItems` |
| Tools formatting helpers | `web/src/lib/tool-formatting.ts` | `toolStatusClass`, `formatToolState`, `formatToolLinkState`, `summarizeToolAction` |
| Learned-state formatting helpers | `web/src/lib/learned-state-formatting.ts` | `formatTimestamp`, `stringValue`, `recentActivityRows`, `summaryLines` |
| Metric formatting helpers | `web/src/lib/metric-formatting.ts` | `numberValue`, `scaledMetricSize` |
| Settings formatting helpers | `web/src/lib/settings-formatting.ts` | `UI_LANGUAGE_OPTIONS`, `UTC_OFFSET_OPTIONS`, `normalizeUiLanguage`, `resolveUiLanguage`, `normalizeUtcOffset`, `utcOffsetOption`, `localeOptionDisplay` |
| Styling | `web/src/index.css` | Route layouts, product shell visuals, responsive behavior, state styling |

`GAP`: route rendering and many route-local UI fragments are still mostly
inside `web/src/App.tsx`; this document maps current ownership but does not
claim component-level separation beyond the extracted route contract.

## API Client Surface

| API Client Method | Endpoint | Main Consumers |
| --- | --- | --- |
| `api.getMe()` | `GET /app/me` | bootstrap, settings refresh |
| `api.register()` | `POST /app/auth/register` | auth modal |
| `api.login()` | `POST /app/auth/login` | auth modal |
| `api.logout()` | `POST /app/auth/logout` | utility bar/sign out |
| `api.patchSettings()` | `PATCH /app/me/settings` | settings route |
| `api.resetData()` | `POST /app/me/reset-data` | settings reset section |
| `api.getChatHistory()` | `GET /app/chat/history` | chat route load and post-send refresh |
| `api.sendChatMessage()` | `POST /app/chat/message` | chat composer |
| `api.getPersonalityOverview()` | `GET /app/personality/overview` | dashboard, personality, memory, reflections, plans, goals, insights, automations |
| `api.getToolsOverview()` | `GET /app/tools/overview` | tools and integrations route data |
| `api.patchToolsPreferences()` | `PATCH /app/tools/preferences` | tools route toggles |
| `api.startTelegramLink()` | `POST /app/tools/telegram/link/start` | tools route Telegram link start |
| `api.getHealth()` | `GET /health` | dashboard/automation/integration health-derived panels |

## Shared State Owners

| State | Owner | Used By |
| --- | --- | --- |
| `route` | `App()` | route rendering, sidebar, mobile tab bar |
| `authMode`, `authModalOpen`, `authBusy`, `me`, `settingsDraft` | `App()` | public/auth shell and settings route |
| `history`, `localTranscriptItems`, `chatText`, `chatSending`, `historyLoading` | `App()` | chat route |
| `overview`, `overviewLoading` | `App()` | dashboard, personality, memory, reflections, plans, goals, insights, automations |
| `toolsOverview`, `toolsLoading`, `telegramLinkStart`, `toolPreferenceBusy` | `App()` | tools and integrations routes |
| `healthSnapshot`, `healthLoading`, `healthError` | `App()` | dashboard, automations, integrations, health-status panels |
| `error`, `toast` | `App()` | global feedback banners |

## Route Map

| Route | Public/Auth | Data Source | Route Behavior | Backend Feature/Pipeline | Test Evidence |
| --- | --- | --- | --- | --- | --- |
| `/` | public | no API until auth action | Public home; `normalizeRoute("/")` maps product route state to `/login` while `navigatePublicEntry("/")` can show public entry | Public shell | `backend/tests/test_web_routes.py` |
| `/login` | public/auth | `api.login`, `api.register`, `api.getMe` bootstrap | Login/register modal and auth session bootstrap | App auth session | `backend/tests/test_api_routes.py`, `backend/tests/test_web_routes.py` |
| `/dashboard` | auth required | `api.getPersonalityOverview`, `api.getHealth`, `api.getToolsOverview` | Flagship overview assembled from learned state, health, and tool readiness summaries | Learned state overview, release/health, tools | `backend/tests/test_api_routes.py`, `backend/tests/test_web_routes.py` |
| `/chat` | auth required | `api.getChatHistory`, `api.sendChatMessage` | Optimistic local transcript, backend chat send, durable history refresh, markdown rendering | App Chat Pipeline | `backend/tests/test_api_routes.py`, `backend/tests/test_runtime_pipeline.py`, `backend/tests/test_web_routes.py` |
| `/personality` | auth required | `api.getPersonalityOverview` | Personality layers and recent learned-state presentation | Learned state overview | `backend/tests/test_api_routes.py`, `backend/tests/test_web_routes.py` |
| `/memory` | auth required | `api.getPersonalityOverview` | Memory-style route using learned-state/recent activity projections | Learned state overview, retrieval context | `backend/tests/test_api_routes.py`, `backend/tests/test_web_routes.py` |
| `/reflections` | auth required | `api.getPersonalityOverview` | Reflection-oriented route using learned-state summaries | Deferred reflection, learned state overview | `backend/tests/test_api_routes.py`, `backend/tests/test_web_routes.py` |
| `/plans` | auth required | `api.getPersonalityOverview` | Planning route assembled from current planning/continuity summaries | Foreground runtime, goals/tasks | `backend/tests/test_api_routes.py`, `backend/tests/test_web_routes.py` |
| `/goals` | auth required | `api.getPersonalityOverview` | Goal route assembled from learned-state and goal signal summaries | Goals/tasks/planned work | `backend/tests/test_api_routes.py`, `backend/tests/test_web_routes.py` |
| `/insights` | auth required | `api.getPersonalityOverview` | Insight route assembled from learned knowledge/preference summaries | Learned state overview | `backend/tests/test_api_routes.py`, `backend/tests/test_web_routes.py` |
| `/automations` | auth required | `api.getPersonalityOverview`, `api.getHealth` | Automation/proactive status route using overview, shared module shell presentation, and health-derived scheduler/proactive posture | Scheduler/proactive/planned work | `backend/tests/test_scheduler_worker.py`, `backend/tests/test_web_routes.py` |
| `/integrations` | auth required | `api.getToolsOverview`, `api.getHealth` | Integration readiness route using backend-owned tool/provider truth and shared module shell presentation | Tools Pipeline, provider readiness | `backend/tests/test_connector_policy.py`, `backend/tests/test_web_routes.py` |
| `/tools` | auth required | `api.getToolsOverview`, `api.patchToolsPreferences`, `api.startTelegramLink` | Tool directory, preference toggles, Telegram link-code start | Tools Pipeline, Telegram linking | `backend/tests/test_api_routes.py`, `backend/tests/test_connector_policy.py`, `backend/tests/test_web_routes.py` |
| `/settings` | auth required | `api.patchSettings`, `api.resetData`, `api.logout` | Account/interface settings and destructive reset flow | Profile/settings, user data reset, auth session | `backend/tests/test_api_routes.py`, `backend/tests/test_preferences.py`, `backend/tests/test_web_routes.py` |

## Component And Helper Clusters

See `docs/frontend/app-route-cluster-audit.md` for the current route-local
extraction queue after the tools route component cleanup.

| Cluster | Functions/Components | Main Routes |
| --- | --- | --- |
| Routing and labels | `normalizeRoute`, `navigate`, `routeLabel`, `routeDescription` | all routes |
| Dashboard components | `DashboardSignalCard`, `DashboardSignalColumn`, `DashboardProgressList`, `DashboardReflectionList`, `DashboardMemoryBarChart`, `DashboardGuidanceList`, `DashboardRecentActivityList`, `DashboardBalanceGrid`, `DashboardCognitiveFlowTrack`, `DashboardFigureNoteList` in `web/src/components/dashboard.tsx` | dashboard |
| Public shell | public home render branch in `web/src/App.tsx`, `AviaryWordmark` in `web/src/components/shell.tsx`, `PublicNavLinkList`, `MotifFigurePanel`, `PublicFeatureCardList`, `PublicTrustPillList`, `PublicTrustBand`, and `PublicGlyph` in `web/src/components/public-shell.tsx` | `/`, `/login` |
| Shell chrome | `SidebarGlyph`, `ShellNavButton`, `ShellNavButtonList`, `ShellRouteSwitcher`, `SidebarBrandBlock`, `AviaryWordmark`, `ShellAccountFactList`, `ShellUtilityBar` in `web/src/components/shell.tsx` | authenticated routes |
| App control icons | `ChevronDownIcon`, `CloseIcon`, `PlusIcon`, `MicrophoneIcon`, `SendArrowIcon` in `web/src/components/app-icons.tsx` | public auth modal, sidebar, chat composer |
| Shared panels | `StatePanel`, `FeedbackBanner`, `ModuleEntryCard`, `FlowRail`, `ModuleOverviewBar`, `ModuleStatRow`, `ModuleActivityList`, `ModuleTextCardList`, `ModuleMetaCardList`, `ModuleDotRowList`, `ModuleValueRowList`, `ModuleProgressValueRowList`, `RouteHeroPanel`, `InsightPanel`, `RouteStatCard`, `RouteStatCardList`, `RouteNoteCard`, `RouteNoteCardList`, `ModuleRouteSidePanel` in `web/src/components/shared.tsx` | dashboard, insights, automations, integrations, and module routes |
| Chat helpers | `renderChatMarkdown` in `web/src/lib/chat-markdown.tsx`; `buildChatRouteModel` in `web/src/lib/chat-route-model.ts`; `transcriptMetadataSummary`, `chatDeliveryState`, `reconcileLocalTranscriptItems` in `web/src/lib/chat-transcript.ts`; `ChatFlowStage`, `ChatTopbar`, `ChatCognitiveBelt`, `ChatTranscriptShell`, `ChatTranscriptMessageList`, `ChatTranscriptMessageRow`, `ChatComposerShell`, and `ChatPortraitPanel` in `web/src/components/chat.tsx` | `/chat` |
| Personality route components | `PersonalityTimelineRow`, `PersonalityTimelineRowList`, `PersonalitySignalRowList`, `PersonalityPreviewCalloutList`, `PersonalityActivityRowList` in `web/src/components/personality.tsx` | memory, reflections, plans, personality |
| Tool helpers | `toolStatusClass`, `formatToolState`, `formatToolLinkState`, `summarizeToolAction` in `web/src/lib/tool-formatting.ts` | `/tools`, `/integrations` |
| Tools components | `ToolsSummaryCard`, `ToolsSummaryCardList`, `ToolsDirectoryGroupList`, `ToolsFactCard`, `ToolsDetailCard`, `ToolsTechnicalDetailPanel`, `ToolsTelegramLinkPanel` in `web/src/components/tools.tsx` | `/tools` |
| Settings components | `SettingsCard`, `SettingsFact`, `SettingsStatusPillList`, `SettingsSelectOptionList`, `SettingsProactivePanel`, `SettingsSavePanel`, `SettingsDangerPanel` in `web/src/components/settings.tsx` | `/settings` |
| Profile/settings helpers | `normalizeUiLanguage`, `resolveUiLanguage`, `normalizeUtcOffset`, `utcOffsetOption`, `localeOptionDisplay` in `web/src/lib/settings-formatting.ts` | `/settings`, bootstrap |
| Learned-state helpers | `recentActivityRows`, `summaryLines`, `stringValue`, `formatTimestamp` in `web/src/lib/learned-state-formatting.ts`; route-derived summaries remain in `App.tsx` | dashboard, personality, memory, reflections, plans, goals, insights, automations |

## Current Frontend Cleanup Queue

`PRJ-1104` found that the remaining `App.tsx` map call sites are mostly data
projections, behaviorful tools-directory rendering, chat transcript refs, or
mobile tabbar refs. The next frontend task is `PRJ-1105`, which should
characterize `/tools` directory behavior before moving any of that route's
group/item rendering behind a component boundary.

`PRJ-1105` added that characterization. The next safe frontend task is
`PRJ-1106`, extracting the tools directory group/item presentation while
preserving route-owned API calls, toggle state, Telegram link state, and
handlers in `App()`.

`PRJ-1106` completed that extraction with `ToolsDirectoryGroupList`. The next
frontend task is `PRJ-1107`, an ARCHITECT-mode audit of the remaining
data-projection, chat transcript, public hero highlight, and mobile-tabbar ref
maps before selecting another implementation target.

`PRJ-1107` selected public hero card data-shape alignment as the next safe
small cleanup. Chat transcript and bottom mobile tabbar maps stay in `App()`
until separate ref/behavior audits.

`PRJ-1108` completed public hero data-shape alignment, so
`MotifFigurePanel` now receives `publicHomeSurface.heroCards` directly. The
next frontend cleanup should audit chat transcript render-map extraction
readiness before moving any message refs or delivery rendering.

`PRJ-1109` completed that audit and selected `PRJ-1110`, a focused chat
transcript render characterization, before any message-list component
extraction.

`PRJ-1110` added that characterization. The next safe frontend task is
`PRJ-1111`, extracting the chat transcript message-list presentation while
keeping transcript refs, delivery-label selection, timestamp formatting, and
markdown rendering explicitly passed from `App()` unless the task narrows that
ownership further.

`PRJ-1111` completed that extraction with `ChatTranscriptMessageList`. The
remaining live JSX map in `App.tsx` is the bottom mobile tabbar, which should
be audited separately because it owns scroll refs and route button registration.

`PRJ-1112` selected a shell-owned `ShellMobileTabbar` boundary. The component
should receive route/ref props explicitly while `App()` keeps the active-route
scroll-centering effect.

`PRJ-1113` completed that extraction. The remaining `App.tsx` maps are data
projections or local transcript state updates, not live JSX render maps.

`PRJ-1114` closed the current frontend presentation extraction lane. Remaining
`App.tsx` maps are data projections or local transcript state updates.

## Gaps

- `web/src/App.tsx` remains the route-rendering/component/state owner for most
  of the browser shell, while route type/list/history helpers now live in
  `web/src/routes.ts` and the first shared panels now live in
  `web/src/components/shared.tsx`. Shell branding, nav helpers, and the utility
  bar now live in `web/src/components/shell.tsx`; public glyphs now live in
  `web/src/components/public-shell.tsx`; pure control icons now live in
  `web/src/components/app-icons.tsx`; chat flow stage, topbar, cognitive belt,
  transcript shell/row, composer shell, and portrait support panel
  presentation now live in `web/src/components/chat.tsx`; dashboard signal cards now live
  in `web/src/components/dashboard.tsx`; the first personality presentational
  row now lives in `web/src/components/personality.tsx`.
- Static/fallback copy still exists for several module routes when backend
  overview fields are absent.
- The current dedicated frontend route smoke covers the public shell and core
  authenticated routes, but full interaction e2e and screenshot parity remain
  separate future work.
- Route-level data dependencies are documented here, but component extraction
  ownership is not yet a code convention.
