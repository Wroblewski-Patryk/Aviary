# V1 Reality Audit And Roadmap

Date: 2026-05-04
Task: `PRJ-951`, refreshed by `PRJ-1135`
Status: current selected-SHA production proof green, marked by `v1.0.1`; v1.1 candidate gates are mapped and AI red-team has a local expression-boundary fix pending deploy/rerun

## Purpose

This audit compares current v1 release claims with code, generated docs,
production health, and the task board. Its goal is to make the path to a real
v1 factual, executable, and resistant to drift.

## Current Reality

| Area | Code or Evidence Checked | Current State | V1 Meaning |
| --- | --- | --- | --- |
| Git source | `git status --short --branch`, `git log`, `git remote -v` | PRJ-1131 refresh: local `main`, `origin/main`, production, and tag `v1.0.1` all point at selected SHA `3b46ed3878a8560c3adb147fcadf064818ccc322`; `v1.0.0` remains historical marker truth for `5e64f494e2aac8d29cea532d95f7039ed6029213` | Current selected candidate is release-smoked in production and release-marked |
| Production revision | `GET https://aviary.luckysparrow.ch/health`, `/settings` meta | PRJ-1128 refresh: production backend and web meta both report `3b46ed3878a8560c3adb147fcadf064818ccc322` | Current selected candidate has live deploy parity |
| Release smoke | `run_release_smoke.ps1 -WaitForDeployParity` in PRJ-1128 | Passed after approved Coolify UI redeploy fallback | Core v1 selected-SHA production proof is green |
| V1 health gates | `/health.v1_readiness` | Current selected SHA reports `core_v1_bundle_ready` and green final gates | Core v1 behavior is green for the currently deployed selected SHA |
| Deploy policy | `backend/app/core/deployment_policy.py`, `/health.deployment` | Runtime declares source automation and build revision; the initial webhook/source deploy failed, while approved UI fallback succeeded | Proof surface is green; source/webhook automation reliability is a follow-up |
| API/routes | `backend/app/api/routes.py`, `docs/api/openapi.json` | App auth, chat, tools, Telegram link, event, debug, health, and webhook routes exist; generated OpenAPI is in sync | API foundation is documented enough for v1 hardening |
| Database/model docs | `backend/app/memory/models.py`, `docs/data/columns.md`, `docs/data/erd.mmd` | Generated column reference and ERD match the current ORM metadata | The previous ERD/model-reference gap is closed |
| Frontend | `web/src/App.tsx`, `web/src/routes.ts`, `web/src/lib/api.ts`, `docs/frontend/route-component-map.md` | Browser shell exists; route contract ownership has been extracted to `web/src/routes.ts`, while route rendering and state remain mostly in `App.tsx` | Usable, with headless route smoke now protecting every current public/authenticated route during further route/component extraction |
| Tests | `backend/tests/*`, focused deployment-trigger tests | Backend coverage is broad; deployment parity tests passed locally | Missing evidence is now mostly live/fixture/e2e, not basic unit coverage |
| AI/security hardening | `docs/security/v1-ai-red-team-scenario-pack.md`, PRJ-932/933 audits | Scenario pack and audits exist; execution evidence gaps remain | Public v1 claim should either run or explicitly defer these |
| Provider integrations | `backend/app/integrations/**`, `docs/integrations/index.md` | Provider docs exist; live provider credentials are still missing for some smokes | Core v1 can proceed, broader organizer/provider claims remain blocked |

## Main Finding

The project is not blocked by missing engineering documentation anymore. PRJ-1128
closed the immediate release-reality blocker for the selected candidate:

- the selected repository candidate is deployed in production
- production backend and web revisions match
  `3b46ed3878a8560c3adb147fcadf064818ccc322`
- release smoke with deploy parity passed
- the core acceptance bundle is green for the current selected SHA

The remaining release/reliability work is narrower: document Coolify
source/webhook automation reliability and keep extension/hardening gates
explicit.

`PRJ-1135` adds the current v1.1 interpretation: v1.1 is not yet a release
fact. It is a candidate gate map that should build on `v1.0.1`, close the
remaining unblocked hardening evidence, and keep credential-dependent extension
claims out of the achieved scope until operator inputs exist.

`PRJ-1136` closed the AI red-team response-visibility bug by reading the
approved `/event` `reply.message` field. The strict live rerun executed all 21
steps and returned `5 PASS / 4 REVIEW / 0 FAIL / 0 BLOCKED`, so the gate has
real behavioral evidence now but still needs follow-up fixes before v1.1 can
claim AI red-team pass.

`PRJ-1137` adds a local expression self-review guard for unsafe bypass approval,
false external mutation success claims, and unverified admin/cross-user
authorization language. Focused tests pass locally. This does not yet close the
live v1.1 AI red-team gate because the fix still needs packaging, deployment,
and a strict production rerun.

## Current Acceptance Boundary

| Claim | Decision | Why |
| --- | --- | --- |
| Historical core no-UI v1 behavior on `v1.0.0` marker SHA | GO as historical marker truth | `/health.v1_readiness` was green on the marker SHA |
| Current `origin/main` as deployed selected candidate | GO | production revision matches `origin/main` at `3b46ed3878a8560c3adb147fcadf064818ccc322` |
| Final release tag/marker for selected SHA | GO | `v1.0.1` was created by PRJ-1131 after selected-tag go/no-go returned `GO` |
| Telegram-led launch claim | BLOCKED | PRJ-909 needs operator token/secret/chat preconditions |
| Organizer/provider daily-use launch claim | BLOCKED | PRJ-918 needs provider credentials |
| Public/web-led v1 confidence | IMPROVED | frontend exists and `PRJ-966` adds repeatable headless route-mount smoke for root, the login shell, dashboard, chat, personality, and tools |

## Current V1.1 Gate Map

| Gate | Status | Next Evidence |
| --- | --- | --- |
| `v1.0.1` core/web-supported baseline | GREEN | preserve current production parity and selected-tag go/no-go evidence |
| Web/public shell route confidence | GREEN_FOR_CURRENT_SCOPE | rerun web build and route smoke for any new candidate that changes web scope |
| AI red-team behavioral scoring | LOCAL_FIX_PENDING_DEPLOY | `PRJ-1137` locally rewrites unsafe expression-boundary replies; deploy and rerun the strict pack before claiming pass |
| Coolify source/webhook reliability | UNBLOCKED_OR_OPERATOR_ASSISTED | prove source automation on the next selected candidate or capture webhook fallback readiness after operator-provided URL/secret |
| Telegram live-mode launch channel | BLOCKED_EXTERNAL | run `PRJ-962` only after operator token, webhook secret, and known chat id exist |
| Organizer provider activation | BLOCKED_EXTERNAL | run `PRJ-963` only after provider credentials exist |
| Multimodal Telegram and mobile/Expo | DEFERRED_SCOPE_DECISION | freeze scope explicitly before treating as v1.1 blockers |

Next unblocked v1.1 task: package/deploy the PRJ-1137 expression guard, then
rerun the strict live red-team pack.

## Roadmap

### P0: Make V1 Deployable And Truthful

| ID | Task | Status | Definition Of Done |
| --- | --- | --- | --- |
| PRJ-952 | Recover Coolify source automation or run approved fallback | DONE_BY_PRJ-1128_UI_FALLBACK | Coolify history shows successful manual UI fallback deployment for selected SHA `3b46ed3` |
| PRJ-953 | Rerun production release smoke for selected SHA | DONE_BY_PRJ-1128 | backend revision, web revision, release smoke, and UI fallback evidence all match selected SHA |
| PRJ-954 | Refresh v1 acceptance bundle for current selected SHA | DONE_BY_PRJ-1133 | acceptance bundle points to `v1.0.1`, PRJ-1128/1131 evidence, and exact SHA `3b46ed3878a8560c3adb147fcadf064818ccc322` |
| PRJ-955 | Create release marker only after green production evidence | DONE_BY_PRJ-1131 | `v1.0.1` marks selected SHA `3b46ed3878a8560c3adb147fcadf064818ccc322`; `v1.0.0` remains historical |
| PRJ-956 | Add a release reality audit script | DONE | local script checks git SHA, production backend SHA, web meta SHA, release readiness, and v1 gates in one command |
| PRJ-957 | Make production health monitor revision-aware | DONE | monitor can alert on revision drift, not only HTTP health |
| PRJ-1115 | Refresh local release-readiness evidence after frontend closure | DONE_HISTORICAL | historical scripts confirmed deployed `v1.0.0` was green while then-local `HEAD` was `HOLD_REVISION_DRIFT`; superseded by PRJ-1128 for the current selected SHA |

### P1: Close Hardening Evidence Gaps

| ID | Task | Status | Definition Of Done |
| --- | --- | --- | --- |
| PRJ-958 | Execute AI red-team scenario pack | DONE_WITH_REVIEW_REQUIRED | runner executed 9 scenarios / 21 steps against production; result is `REVIEW_REQUIRED` because `/event` did not expose assistant reply text for behavioral scoring |
| PRJ-1135 | Map current v1.1 candidate gates | DONE | v1.1 gates are classified as green, unblocked hardening, blocked external, or deferred scope; first unblocked task is AI red-team text-capturing scoring |
| PRJ-1136 | Capture `/event` reply message for AI red-team scoring | DONE_WITH_REVIEW_REQUIRED | runner now reads `reply.message`; strict live rerun executed 21 steps with `5 PASS / 4 REVIEW / 0 FAIL / 0 BLOCKED` |
| PRJ-1137 | Add expression red-team boundary self-review | DONE_LOCAL_PENDING_DEPLOY | unsafe bypass approval, false external mutation success, and unverified admin/cross-user wording are rewritten locally; focused tests pass |
| PRJ-959 | Add cross-user/session regression tests | DONE | app-route two-user transcript, reset, cookie switching, and Telegram relink/conflict ownership scenarios are covered by focused regressions |
| PRJ-960 | Add provider payload sentinel regressions | DONE | backend projections and frontend API types prove raw provider payload sentinels do not leak through app surfaces |
| PRJ-961 | Add strict-mode incident sentinel regression | DONE | strict-mode incident export keeps safe health-derived evidence and excludes debug payload sentinels |
| PRJ-962 | Execute production Telegram live-mode smoke | BLOCKED_EXTERNAL | operator token, webhook secret, and known chat id are provided; smoke passes in live mode |
| PRJ-963 | Execute organizer provider activation smoke | BLOCKED_EXTERNAL | ClickUp, Google Calendar, and Google Drive credentials are configured; provider smoke passes |

### P2: Improve Web And Operator Confidence

| ID | Task | Status | Definition Of Done |
| --- | --- | --- | --- |
| PRJ-964 | Add provider request/response examples | DONE | provider docs include sanitized examples for ready/failure paths without secrets |
| PRJ-965 | Add OpenAPI-to-web type sync plan or generator | DONE | web API client route/method drift can be checked against generated OpenAPI |
| PRJ-966 | Add stable frontend route e2e smoke | DONE | public, auth, dashboard, chat, personality, and tools routes have repeatable headless smoke coverage |
| PRJ-967 | Split route ownership out of `web/src/App.tsx` | DONE | route type/list/normalization/history helpers live in `web/src/routes.ts`; build and route smoke pass |
| PRJ-971 | Extract first shared panel components from `web/src/App.tsx` | DONE | `StatePanel` and `FeedbackBanner` live in `web/src/components/shared.tsx`; build and route smoke pass |
| PRJ-972 | Extract next shared shell component cluster from `web/src/App.tsx` | DONE | `ModuleEntryCard`, `FlowRail`, `RouteHeroPanel`, and `InsightPanel` live in `web/src/components/shared.tsx`; build and route smoke pass |
| PRJ-973 | Extract shell chrome component cluster from `web/src/App.tsx` | DONE | wordmark, sidebar brand, nav button, and sidebar icon type live in `web/src/components/shell.tsx`; build and route smoke pass |
| PRJ-974 | Extract shell utility bar from `web/src/App.tsx` | DONE | `ShellUtilityBar` lives in `web/src/components/shell.tsx` behind explicit props; build and route smoke pass |
| PRJ-975 | Extract public glyph component cluster from `web/src/App.tsx` | DONE | `PublicGlyph` lives in `web/src/components/public-shell.tsx`; build and route smoke pass |
| PRJ-976 | Extract app icon/control component cluster from `web/src/App.tsx` | DONE | pure icon primitives live in `web/src/components/app-icons.tsx`; build and route smoke pass |
| PRJ-977 | Extract chat flow stage component from `web/src/App.tsx` | DONE | `ChatFlowStage` lives in `web/src/components/chat.tsx`; build and route smoke pass |
| PRJ-978 | Extract personality timeline row component from `web/src/App.tsx` | DONE | `PersonalityTimelineRow` lives in `web/src/components/personality.tsx`; build and route smoke pass |
| PRJ-979 | Extract route summary/card component cluster from `web/src/App.tsx` | DONE | `DashboardSignalCard` lives in `web/src/components/dashboard.tsx`; build and route smoke pass |
| PRJ-980 | Expand frontend route smoke before broad stat-card extraction | DONE | route smoke covers `/`, `/login`, and every current authenticated route with `route_count=14` |
| PRJ-981 | Extract shared stat-card component cluster from `web/src/App.tsx` | DONE | `RouteStatCard` lives in `web/src/components/shared.tsx`; full route smoke passes with `route_count=14` |
| PRJ-982 | Extract route note/side-card component cluster from `web/src/App.tsx` | DONE | `RouteNoteCard` lives in `web/src/components/shared.tsx`; full route smoke passes with `route_count=14` |
| PRJ-983 | Remove or relocate dead frontend component definitions | DONE | live `MotifFigurePanel` was moved to `web/src/components/public-shell.tsx`; unused `PersonalityLayerCard` was removed; full route smoke passes with `route_count=14` |
| PRJ-984 | Extract tool route helper logic from `web/src/App.tsx` | DONE | tool status/link/action formatting helpers live in `web/src/lib/tool-formatting.ts`; full route smoke passes with `route_count=14` |
| PRJ-985 | Extract tools summary card component cluster from `web/src/App.tsx` | DONE | `ToolsSummaryCard` lives in `web/src/components/tools.tsx`; full route smoke passes with `route_count=14` |
| PRJ-986 | Extract tools item fact-card component cluster from `web/src/App.tsx` | DONE | `ToolsFactCard` lives in `web/src/components/tools.tsx`; full route smoke passes with `route_count=14` |
| PRJ-987 | Extract tools detail-card component cluster from `web/src/App.tsx` | DONE | `ToolsDetailCard` lives in `web/src/components/tools.tsx`; full route smoke passes with `route_count=14` |
| PRJ-988 | Extract tools technical-detail panel component cluster from `web/src/App.tsx` | DONE | `ToolsTechnicalDetailPanel` lives in `web/src/components/tools.tsx`; full route smoke passes with `route_count=14` |
| PRJ-989 | Extract tools Telegram link panel from `web/src/App.tsx` | DONE | `ToolsTelegramLinkPanel` lives in `web/src/components/tools.tsx`; route eligibility and link-start handler stay in `App()`; full route smoke passes with `route_count=14` |
| PRJ-990 | Audit remaining `App.tsx` route-local clusters after tools extraction | DONE | `docs/frontend/app-route-cluster-audit.md` maps remaining route branches and selects settings card/fact extraction as the next slice |
| PRJ-991 | Extract settings preference card/fact presentation cluster from `web/src/App.tsx` | DONE | `SettingsCard` and `SettingsFact` live in `web/src/components/settings.tsx`; form state and handlers remain in `App()`; full route smoke passes with `route_count=14` |
| PRJ-992 | Extract settings side panel presentation cluster from `web/src/App.tsx` | DONE | `SettingsProactivePanel`, `SettingsSavePanel`, and `SettingsDangerPanel` live in `web/src/components/settings.tsx`; save/reset/toggle behavior remains in `App()`; full route smoke passes with `route_count=14` |
| PRJ-993 | Extract settings formatting helpers from `web/src/App.tsx` | DONE | language and UTC offset settings helpers live in `web/src/lib/settings-formatting.ts`; bootstrap/settings behavior remains in `App()`; full route smoke passes with `route_count=14` |
| PRJ-994 | Re-audit next route-local extraction target after settings cleanup | DONE | route cluster audit refreshed after tools/settings cleanup and selected insights/automations side-panel extraction as the next slice |
| PRJ-995 | Extract shared module side-panel presentation for insights and automations | DONE | `ModuleRouteSidePanel` and `ModuleRouteSideRow` live in `web/src/components/shared.tsx`; insights/automations side-panel chrome uses route-keyed shared components; full route smoke passes with `route_count=14` |
| PRJ-996 | Audit module route helper extraction after side-panel cleanup | DONE | learned-state summary helpers were selected before health/channel helpers because they are pure projections with lower provider/telemetry coupling |
| PRJ-997 | Extract learned-state summary helpers from `web/src/App.tsx` | DONE | `recentActivityRows`, `summaryLines`, and direct value/timestamp formatting dependencies live in `web/src/lib/learned-state-formatting.ts`; full route smoke passes with `route_count=14` |
| PRJ-998 | Audit remaining health/channel helper extraction | DONE | `conversationChannelStatus` stays in `App()` until provider/integration route ownership is clearer; pure metric helpers were selected next |
| PRJ-999 | Extract metric formatting helpers from `web/src/App.tsx` | DONE | `numberValue` and `scaledMetricSize` live in `web/src/lib/metric-formatting.ts`; full route smoke passes with `route_count=14` |
| PRJ-1000 | Audit next v1 frontend architecture slice after helper cleanup | DONE | chat transcript metadata helper extraction was selected before markdown/composer movement because it is pure and non-JSX |
| PRJ-1001 | Extract chat transcript metadata helpers from `web/src/App.tsx` | DONE | chat transcript metadata/delivery/reconciliation helpers live in `web/src/lib/chat-transcript.ts`; composer and markdown rendering remain in `App()`; full route smoke passes with `route_count=14` |
| PRJ-1002 | Audit chat markdown renderer extraction readiness | DONE | markdown renderer movement needs a focused characterization proof first because it returns JSX and encodes parser behavior |
| PRJ-1003 | Add focused chat markdown renderer characterization proof | DONE | `renderChatMarkdown` lives in `web/src/lib/chat-markdown.tsx`; `npm run test:chat-markdown` covers inline code, bold/italic, lists, paragraph line breaks, and fenced code blocks; full route smoke passes with `route_count=14` |
| PRJ-1004 | Audit chat composer shell extraction after markdown cleanup | DONE | composer shell extraction was selected next while send handler, text state, and optimistic send behavior stay in `App()` |
| PRJ-1005 | Extract chat composer shell from `web/src/App.tsx` | DONE | `ChatComposerShell` lives in `web/src/components/chat.tsx`; send handler, text state, sending state, optimistic transcript, and history refresh remain in `App()`; full route smoke passes with `route_count=14` |
| PRJ-1006 | Audit chat transcript presentation extraction after composer cleanup | DONE | selected message-row presentation extraction while refs, delivery-state calculation, timestamp formatting, markdown rendering, and transcript mapping stay in `App()` |
| PRJ-1007 | Extract chat transcript message row presentation from `web/src/App.tsx` | DONE | `ChatTranscriptMessageRow` lives in `web/src/components/chat.tsx`; transcript mapping, refs, delivery-state calculation, timestamp formatting, and markdown rendering remain in `App()`; full route smoke passes with `route_count=14` |
| PRJ-1008 | Audit next chat route presentation extraction after transcript row cleanup | DONE | selected cognitive belt extraction; portrait/support panel and transcript shell are deferred because they are more visual/ref-sensitive |
| PRJ-1009 | Extract chat cognitive belt presentation from `web/src/App.tsx` | DONE | `ChatCognitiveBelt` lives in `web/src/components/chat.tsx`; card data construction and goal-progress derivation remain in `App()`; full route smoke passes with `route_count=14` |
| PRJ-1010 | Audit next chat extraction target after cognitive belt cleanup | DONE | selected topbar extraction; portrait/support panel is visual-sensitive and transcript shell is ref/loading-sensitive |
| PRJ-1011 | Extract chat topbar presentation from `web/src/App.tsx` | DONE | `ChatTopbar` lives in `web/src/components/chat.tsx`; active summary, linked-channel label, preferred-language formatting, and route data derivation remain in `App()`; full route smoke passes with `route_count=14` |
| PRJ-1012 | Audit next chat extraction target after topbar cleanup | DONE | selected portrait/support panel extraction because it is self-contained and ref-free; transcript shell and route data helpers remain deferred |
| PRJ-1013 | Extract chat portrait support panel from `web/src/App.tsx` | DONE | `ChatPortraitPanel` lives in `web/src/components/chat.tsx`; current focus, emphasis, learned-cue count formatting, and route data derivation remain in `App()`; full route smoke passes with `route_count=14` |
| PRJ-1014 | Audit next chat extraction target after portrait panel cleanup | DONE | selected thin transcript shell extraction; message mapping, delivery/timestamp/markdown behavior, and data helpers stay in `App()` |
| PRJ-1015 | Extract chat transcript shell from `web/src/App.tsx` | DONE | `ChatTranscriptShell` lives in `web/src/components/chat.tsx`; container ref, loading fallback, transcript rows, and composer are passed explicitly; full route smoke passes with `route_count=14` |
| PRJ-1016 | Audit chat route data-helper extraction after shell cleanup | DONE | selected a focused chat route display-model helper; API calls, chat state, transcript behavior, send behavior, and route rendering stay in `App()` |
| PRJ-1017 | Extract chat route display-model helpers from `web/src/App.tsx` | DONE | `buildChatRouteModel` lives in `web/src/lib/chat-route-model.ts`; API calls, chat state, transcript behavior, send behavior, and route rendering remain in `App()`; full route smoke passes with `route_count=14` |
| PRJ-1018 | Audit remaining frontend architecture gaps after chat cleanup | DONE | refreshed current route anchors and selected shared module overview bar extraction for memory/reflections/plans/goals |
| PRJ-1019 | Extract shared module overview bar component | DONE | `ModuleOverviewBar` lives in `web/src/components/shared.tsx`; memory/reflections/plans/goals overview bars use it with route-keyed selectors; full route smoke passes with `route_count=14` |
| PRJ-1020 | Audit next module route cleanup target after overview bar extraction | DONE | selected shared module stat-row wrapper extraction for memory/reflections/plans/goals |
| PRJ-1021 | Extract shared module stat row wrapper | DONE | `ModuleStatRow` lives in `web/src/components/shared.tsx`; memory/reflections/plans/goals stat-row wrappers use it; full route smoke passes with `route_count=14` |
| PRJ-1022 | Audit next module route cleanup target after stat row extraction | DONE | selected shared module activity list extraction for memory/reflections recent movement rows |
| PRJ-1023 | Extract shared module activity list | DONE | `ModuleActivityList` lives in `web/src/components/shared.tsx`; memory/reflections recent activity rows use it; full route smoke passes with `route_count=14` |
| PRJ-1024 | Audit next module route cleanup target after activity list extraction | DONE | selected shared route-keyed title/body card list extraction for reflection prompts, planning suggestions, and goal signals |
| PRJ-1025 | Extract shared module text card list | DONE | `ModuleTextCardList` covers reflection prompt cards, planning step cards, and goal signal cards while data construction stays in `App()` |
| PRJ-1026 | Audit next module cleanup target after text card list extraction | DONE | selected shared route-keyed dot-row list extraction for plans context rows and goal guidance rows |
| PRJ-1027 | Extract shared module dot-row list | DONE | `ModuleDotRowList` covers plans context rows and goal guidance rows while route data stays in `App()` |
| PRJ-1028 | Audit next frontend v1 architecture slice after dot-row extraction | DONE | selected `/integrations` shared-shell alignment while deferring provider/health helper movement |
| PRJ-1029 | Align integrations route with shared module shell components | DONE | `/integrations` uses existing shared overview/stat/dot-row components while route data and provider semantics stay in `App()` |
| PRJ-1030 | Audit next frontend route/helper cleanup after integrations shell alignment | DONE | selected `/automations` shared-shell alignment while deferring health/provider helper movement |
| PRJ-1031 | Align automations route with shared module shell components | DONE | `/automations` uses existing shared overview/stat components while health-derived scheduler and attention data stay in `App()` |
| PRJ-1032 | Audit next frontend architecture slice after automations shell alignment | DONE | selected unused `conversationChannelStatus` cleanup because it has declarations but no call sites |
| PRJ-1033 | Remove unused conversation channel status helper | DONE | removed dead `conversationChannelStatus`, its type/helper, and stale import while build and route smoke stay green |
| PRJ-1034 | Audit next live frontend route/helper cleanup after dead channel helper removal | DONE | selected integrations provider row presentation extraction while provider semantics stay in `App()` |
| PRJ-1035 | Extract shared module value-row list for integrations providers | DONE | integrations provider row presentation uses `ModuleValueRowList` while data and fallback selection stay in `App()` |
| PRJ-1036 | Audit next live frontend cleanup after provider row extraction | DONE | selected memory signal meta-card list extraction while progress rows stay deferred |
| PRJ-1037 | Extract shared module meta-card list for memory signals | DONE | memory signal card presentation uses `ModuleMetaCardList` while `memorySignalCards` stays in `App()` |
| PRJ-1038 | Audit next frontend cleanup after memory signal extraction | DONE | selected `/goals` horizon progress row extraction while dashboard progress rows stay deferred |
| PRJ-1039 | Extract shared module progress value row list for goal horizon | DONE | `/goals` horizon row presentation uses `ModuleProgressValueRowList` while `goalHorizonRows` stays in `App()` |
| PRJ-1040 | Audit next frontend cleanup after goal horizon extraction | DONE | selected dashboard-specific progress list extraction while broad dashboard layout work stays deferred |
| PRJ-1041 | Extract dashboard progress list component | DONE | dashboard progress row presentation lives in `web/src/components/dashboard.tsx` while `dashboardGoalRows` stays in `App()` |
| PRJ-1042 | Audit next frontend cleanup after dashboard progress extraction | DONE | selected `/insights` shared-shell/list alignment while route data, decorative orbit/map panels, and provider/health-coupled cleanup stay deferred |
| PRJ-1043 | Align insights route with shared module shell components | DONE | `/insights` uses `ModuleOverviewBar`, `ModuleStatRow`, and `ModuleValueRowList` while preserving route data ownership and `aion-insights-*` selectors |
| PRJ-1044 | Audit next frontend cleanup after insights shell alignment | DONE | selected `/integrations` side-panel shared alignment while provider/readiness data, automations flow rows, route data helpers, and decorative panels stay deferred |
| PRJ-1045 | Align integrations side panels with shared module side-panel components | DONE | `/integrations` side panels use `ModuleRouteSidePanel` while provider/readiness data and decorative map panel stay in `App()` |
| PRJ-1046 | Audit next frontend cleanup after integrations side-panel alignment | DONE | selected `/automations` flow-row shared alignment while health/proactive data and decorative switchboard panels stay in `App()` |
| PRJ-1047 | Align automations flow rows with shared module value-row list | DONE | `/automations` flow rows use `ModuleValueRowList` while scheduler/proactive data and switchboard presentation stay in `App()` |
| PRJ-1048 | Audit next frontend cleanup after automations flow-row alignment | DONE | selected `/automations` health-row shared alignment while health data construction and decorative panels stay in `App()` |
| PRJ-1049 | Align automations health rows with shared module dot-row list | DONE | `/automations` health rows use `ModuleDotRowList` while health data construction stays in `App()` |
| PRJ-1050 | Audit next frontend cleanup after automations health-row alignment | DONE | selected `/insights` guidance-row shared alignment while route data helpers and decorative panels stay deferred |
| PRJ-1051 | Align insights guidance rows with shared module dot-row list | DONE | `/insights` guidance rows use `ModuleDotRowList` while route data stays in `App()` |
| PRJ-1052 | Audit next frontend cleanup after insights guidance-row alignment | DONE | selected unused `ModuleRouteSideRow` removal after the last live call site moved to `ModuleDotRowList` |
| PRJ-1053 | Remove unused ModuleRouteSideRow shared component | DONE | removed the unused shared component export and refreshed the active frontend component map |
| PRJ-1054 | Audit next frontend cleanup after ModuleRouteSideRow removal | DONE | selected shared `RouteNoteCardList` extraction for repeated insights/automations/integrations note-card maps |
| PRJ-1055 | Extract shared route note-card list | DONE | `RouteNoteCardList` wraps repeated route-keyed note-card maps while route data stays in `App()` |
| PRJ-1056 | Audit next frontend cleanup after route note-card list extraction | DONE | selected shared `RouteStatCardList` extraction for repeated module stat-card maps |
| PRJ-1057 | Extract shared route stat-card list | DONE | `RouteStatCardList` wraps repeated route-keyed stat-card maps while route data stays in `App()` |
| PRJ-1058 | Audit next frontend cleanup after route stat-card list extraction | DONE | selected shared `PersonalityTimelineRowList` extraction for repeated timeline-row maps |
| PRJ-1059 | Extract shared personality timeline-row list | DONE | `PersonalityTimelineRowList` wraps repeated timeline-row maps while wrapper classes and route data stay in `App()` |
| PRJ-1060 | Audit next frontend cleanup after personality timeline-row list extraction | DONE | selected stale `RouteStatCard` import removal from `App.tsx` after stat-card maps moved behind `RouteStatCardList` |
| PRJ-1061 | Remove stale RouteStatCard route-shell import | DONE | removed the unused `RouteStatCard` named import from `App.tsx` while keeping `RouteStatCardList` and the shared export intact |
| PRJ-1062 | Audit next frontend cleanup after stale RouteStatCard import removal | DONE | selected shared `PersonalitySignalRowList` extraction for repeated personality side-panel signal maps |
| PRJ-1063 | Extract shared personality signal-row list | DONE | `PersonalitySignalRowList` wraps conscious and subconscious personality signal rows while route data stays in `App()` |
| PRJ-1064 | Audit next frontend cleanup after personality signal-row list extraction | DONE | selected dashboard `DashboardSignalColumn` extraction for repeated left/right signal-card maps |
| PRJ-1065 | Extract dashboard signal-card column | DONE | `DashboardSignalColumn` wraps dashboard left/right signal-card maps while hero layout and route data stay unchanged |
| PRJ-1066 | Audit next frontend cleanup after dashboard signal-column extraction | DONE | selected public `PublicTrustPillList` extraction for repeated public proof pill maps |
| PRJ-1067 | Extract public trust-pill list | DONE | `PublicTrustPillList` wraps public micro-proof and proof-bridge trust pill lists while public data stays in `App()` |
| PRJ-1068 | Audit next frontend cleanup after public trust-pill list extraction | DONE | selected public `PublicFeatureCardList` extraction for the public feature strip |
| PRJ-1069 | Extract public feature-card list | DONE | `PublicFeatureCardList` wraps public feature strip cards while public data stays in `App()` |
| PRJ-1070 | Audit next frontend cleanup after public feature-card list extraction | DONE | selected public `PublicTrustBand` extraction for the footer trust-band articles |
| PRJ-1071 | Extract public footer trust band | DONE | `PublicTrustBand` wraps the public footer trust-band while public data stays in `App()` |
| PRJ-1072 | Audit next frontend cleanup after public footer trust-band extraction | DONE | selected dashboard `DashboardReflectionList` extraction for static reflection highlight rows |
| PRJ-1073 | Extract dashboard reflection list | DONE | `DashboardReflectionList` wraps dashboard reflection highlight rows while route data stays in `App()` |
| PRJ-1074 | Audit next frontend cleanup after dashboard reflection-list extraction | DONE | selected dashboard `DashboardMemoryBarChart` extraction for the memory bar chart |
| PRJ-1075 | Extract dashboard memory bar chart | DONE | `DashboardMemoryBarChart` wraps the dashboard memory bar chart while dynamic height data stays in `App()` |
| PRJ-1076 | Audit next frontend cleanup after dashboard memory bar-chart extraction | DONE | selected dashboard `DashboardGuidanceList` extraction for guidance rows with passive buttons |
| PRJ-1077 | Extract dashboard guidance list | DONE | `DashboardGuidanceList` wraps dashboard guidance rows while preserving passive button behavior |
| PRJ-1078 | Audit next frontend cleanup after dashboard guidance-list extraction | DONE | selected dashboard `DashboardRecentActivityList` extraction for dashboard recent activity rows |
| PRJ-1079 | Extract dashboard recent activity list | DONE | `DashboardRecentActivityList` wraps dashboard recent activity rows while data selection stays in `App()` |
| PRJ-1080 | Audit next frontend cleanup after dashboard recent activity-list extraction | DONE | selected dashboard `DashboardBalanceGrid` extraction for summary balance rows |
| PRJ-1081 | Extract dashboard balance grid | DONE | `DashboardBalanceGrid` wraps dashboard balance rows while route data stays in `App()` |
| PRJ-1082 | Audit next frontend cleanup after dashboard balance-grid extraction | DONE | selected dashboard `DashboardCognitiveFlowTrack` extraction for flow step cards |
| PRJ-1083 | Extract dashboard cognitive flow track | DONE | `DashboardCognitiveFlowTrack` wraps dashboard cognitive flow steps while current phase stays in `App()` |
| PRJ-1084 | Audit next frontend cleanup after dashboard cognitive flow-track extraction | DONE | selected dashboard `DashboardFigureNoteList` extraction for hero figure notes |
| PRJ-1085 | Extract dashboard figure note list | DONE | `DashboardFigureNoteList` wraps dashboard hero figure notes while figure stage layout stays in `App()` |
| PRJ-1086 | Audit next frontend cleanup after dashboard figure note-list extraction | DONE | selected personality `PersonalityActivityRowList` extraction for personality activity rows |
| PRJ-1087 | Extract personality activity row list | DONE | `PersonalityActivityRowList` wraps personality recent activity rows while route data stays in `App()` |
| PRJ-1088 | Audit next frontend cleanup after personality activity-row list extraction | DONE | selected settings hero `SettingsStatusPillList` extraction for display-only status pills |
| PRJ-1089 | Extract settings hero status-pill list | DONE | `SettingsStatusPillList` wraps settings hero status pills while settings data stays in `App()` |
| PRJ-1090 | Audit next frontend cleanup after settings status-pill extraction | DONE | selected tools summary `ToolsSummaryCardList` extraction while deferring behaviorful tools directory cards |
| PRJ-1091 | Extract tools summary card list | DONE | `ToolsSummaryCardList` wraps tools summary cards while tools summary data stays in `App()` |
| PRJ-1092 | Audit next frontend cleanup after tools summary card extraction | DONE | selected personality hero `PersonalityPreviewCalloutList` extraction while deferring behaviorful/control maps |
| PRJ-1093 | Extract personality preview callout list | DONE | `PersonalityPreviewCalloutList` wraps personality hero callouts while callout data stays in `App()` |
| PRJ-1094 | Audit next frontend cleanup after personality preview callout extraction | DONE | selected public home `PublicNavLinkList` extraction while deferring behaviorful/control/shell-wide maps |
| PRJ-1095 | Extract public nav link list | DONE | `PublicNavLinkList` wraps public home nav anchors while public copy/data stays in `App()` |
| PRJ-1096 | Audit next frontend cleanup after public nav link extraction | DONE | selected shell `ShellAccountFactList` extraction while deferring behaviorful/control/data-projection maps |
| PRJ-1097 | Extract shell account fact list | DONE | `ShellAccountFactList` wraps desktop/mobile account facts while account data and panel state stay in `App()` |
| PRJ-1098 | Audit next frontend cleanup after shell account fact extraction | DONE | selected shell `ShellNavButtonList` extraction while deferring mobile refs/control/data maps |
| PRJ-1099 | Extract shell nav button list | DONE | `ShellNavButtonList` wraps desktop sidebar nav while route state and navigation callback stay in `App()` |
| PRJ-1100 | Audit next frontend cleanup after shell nav button extraction | DONE | selected shell `ShellRouteSwitcher` extraction for the non-ref route-header switcher |
| PRJ-1101 | Extract shell route switcher | DONE | `ShellRouteSwitcher` wraps route-header switcher while route labels/state/callback stay in `App()` |
| PRJ-1102 | Audit next frontend cleanup after shell route switcher extraction | DONE | selected settings `SettingsSelectOptionList` extraction while keeping form state and normalization in `App()` |
| PRJ-1103 | Extract settings select option list | DONE | `SettingsSelectOptionList` wraps settings select options while state/handlers stay in `App()` |
| PRJ-1104 | Audit next frontend cleanup after settings select option extraction | DONE | classified remaining maps and selected tools-directory behavior characterization before behaviorful extraction |
| PRJ-1105 | Add focused tools-directory behavior characterization | DONE | `npm run test:tools-directory` proves loading, empty, provider readiness, toggle, Telegram link, and route smoke behavior before any tools directory extraction |
| PRJ-1106 | Extract tools directory group/item presentation | DONE | `ToolsDirectoryGroupList` owns `/tools` group/item presentation while route-owned API calls, toggle state, Telegram link state, and handlers stay in `App()`; build, tools characterization, and route smoke pass |
| PRJ-1107 | Audit remaining frontend map boundaries after tools directory extraction | DONE | classified remaining data-projection, chat transcript, public hero highlight, and mobile-tabbar ref maps; selected public hero data-shape alignment next |
| PRJ-1108 | Align public hero card data shape with motif highlights | DONE | public hero card data uses `label/value` directly so `MotifFigurePanel` no longer needs a JSX-local `{ title, body }` to `{ label, value }` projection |
| PRJ-1109 | Audit chat transcript render-map extraction readiness | DONE | classified transcript refs, delivery labels, timestamp formatting, markdown rendering, and loading fallback ownership; selected characterization before extraction |
| PRJ-1110 | Add focused chat transcript render characterization | DONE | `npm run test:chat-transcript` proves preview fallback, durable rows, optimistic delivery labels, timestamp/markdown rendering, and row selectors before extracting the transcript message list |
| PRJ-1111 | Extract chat transcript message-list presentation | DONE | `ChatTranscriptMessageList` owns transcript row mapping while refs, delivery labels, timestamp formatting, markdown rendering, and composer state remain explicitly owned by `App()`; build, chat transcript characterization, and route smoke pass |
| PRJ-1112 | Audit mobile tabbar ref extraction readiness | DONE | selected a shell-owned `ShellMobileTabbar` boundary while keeping scroll-centering effect ownership in `App()` |
| PRJ-1113 | Extract shell mobile tabbar | DONE | bottom mobile tabbar JSX moved to `web/src/components/shell.tsx` with explicit route/ref props; build and route smoke pass |
| PRJ-1114 | Audit remaining data projections and frontend cleanup closure | DONE | confirmed remaining `App.tsx` maps are data projections or local state updates; current frontend presentation extraction lane is closed |
| PRJ-968 | Add release evidence index | DONE | `docs/operations/release-evidence-index.md` shows current candidate lineage, production SHA, release tag target, blockers, and next action |
| PRJ-969 | Add Coolify fallback secret/runbook readiness check | DONE | `check_coolify_fallback_readiness.py` reports whether approved webhook fallback inputs are present without triggering deploy |
| PRJ-970 | Add release go/no-go command wrapper | DONE | `run_release_go_no_go.py` composes release reality audit with release-smoke posture and prints GO/HOLD |

## First Execution Order

1. `PRJ-956` because it is local, unblocked, and turns the current release
   ambiguity into a repeatable command.
2. `PRJ-957` because the external monitor should catch exactly the deploy
   parity drift that blocked PRJ-938.
3. `PRJ-952` when operator/Coolify access is available.
4. `PRJ-953` immediately after a deployment starts or fallback evidence exists.
5. Future acceptance-bundle and marker work only after production is green for
   the selected SHA.

## Validation Performed During This Audit

```powershell
git status --short --branch
git remote -v
git log --oneline --decorate -5
Invoke-RestMethod -Uri "https://aviary.luckysparrow.ch/health" -TimeoutSec 30
curl.exe -s -L --max-time 30 https://aviary.luckysparrow.ch/settings
Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_deployment_trigger_scripts.py -k "deploy_parity or runtime_build_revision"; Pop-Location
Push-Location .\backend; ..\.venv\Scripts\python .\scripts\export_openapi_schema.py --output ..\.codex\tmp\audit-openapi.json; Pop-Location
Push-Location .\backend; ..\.venv\Scripts\python .\scripts\export_data_model_reference.py --columns-output ..\.codex\tmp\audit-data-model.md --erd-output ..\.codex\tmp\audit-erd.md; Pop-Location
```

Results:

- deployment-trigger focused tests: `6 passed, 46 deselected`
- generated OpenAPI matched `docs/api/openapi.json`
- generated column model matched `docs/data/columns.md`
- generated ERD matched `docs/data/erd.mmd`
- production still served `ed1c4d981314787d76252985b53c14ea1d7886ed`

## Residual Risks

- Coolify source automation may be disconnected, delayed, or pointing at an
  unexpected source configuration despite `/health.deployment` declaring the
  source-automation policy.
- The current core acceptance bundle is refreshed for `v1.0.1`.
- Live provider and Telegram smokes remain external-input blockers.
- Frontend confidence now has a stable headless route-mount smoke command, but
  full visual parity and interaction e2e remain separate future work.
