# Module Confidence Ledger

Last updated: 2026-06-03

## Project Alias

The product name is Aviary. The repository folder is `Personality`.

## Purpose

This ledger is the quick reality map for Aviary. It tracks whether each
important runtime, memory, reflection, scheduler, action, integration, API, web,
mobile, and operations journey is implemented, verified, broken, blocked, or
unknown. Keep it honest. Do not turn uncertainty into optimism.

## Status Vocabulary

- `NOT_STARTED`: no meaningful implementation exists.
- `IN_PROGRESS`: implementation is actively changing.
- `IMPLEMENTED_NOT_VERIFIED`: code exists, but current proof is missing.
- `PARTIAL`: some scenarios pass, but important scenarios are missing or stale.
- `VERIFIED`: current evidence proves the journey for the target scope.
- `BROKEN`: a reproducible defect exists.
- `BLOCKED`: verification or implementation is blocked by access, decision,
  environment, dependency, or missing input.
- `DEFERRED`: explicitly out of the current release scope.

## Confidence Rules

- `High`: fresh reproducible evidence exists for the real journey.
- `Medium`: good local proof exists, but target, edge-case, or freshness is
  incomplete.
- `Low`: evidence is missing, stale, inferred, or chat-only.

## Ledger

| ID | Module | Journey / function | Priority | Status | Confidence | Evidence | Missing proof or defect | Next smallest action | Owner | Last verified |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AVIARY-ARCH-EXPORTER-REFRESH-001 | Architecture awareness exporter | Softwarehouse architecture-awareness exporter refreshes Aviary graph/status artifacts with bounded invocation | P1 | VERIFIED | Medium | `LUC-1687`; `.codex/tasks/LUC-1687-architecture-exporter-timeout-triage-and-reproducibility-guard.md`; pre-guard canonical run timed out after `224.843s`; `C:/Personal/Projekty/Aplikacje/Paperclip_Softwarehouse/scripts/build-architecture-awareness-index.mjs` now excludes exactly its generated graph/status output files from scanner input; guarded canonical rerun passed with exit code `0` in `167.028s`; `node --check scripts/build-architecture-awareness-index.mjs` passed; `docs/graphs/architecture-health.json` generated `2026-06-03T05:49:10.369Z` with `entities=18644`, `relations=30156`, `implementation_without_tests=6528`, `implementation_without_task=701`, `verified_without_proof=0`. | Full exporter still takes about 167 seconds on the current Aviary tree; generated task-link inference still reports 701 implementation entities without task links and needs a separate proof-link/inference lane if the project wants that number reduced. | `LUC-1689` proof-link evidence is now closed; create a narrow architecture follow-up only for deeper task-link inference improvement if required. | CTO Architect | 2026-06-03 |
| AVIARY-API-CHAT-WORKFLOW-001 | Backend API routes | Core authenticated app chat API workflow for history and message endpoints | P0 | VERIFIED | High | `LUC-942`; `.codex/tasks/LUC-942-qa-verify-core-chat-api-workflow-p0.md`; `Push-Location backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "app_chat_history or app_chat_message"; Pop-Location` -> `9 passed, 123 deselected in 16.03s`. | Focused route-level proof only; full backend pack and production smoke are separate gates. | Re-run focused pack after any chat API contract or route changes. | QA/Test | 2026-05-31 |
| AVIARY-DOCS-BASELINE-SYNC-001 | Docs / Memory ledgers | Known-state baseline evidence remains synchronized across canonical state ledgers after refresh checkpoints | P1 | VERIFIED | High | `LUC-580`; `LUC-694`; `.codex/tasks/LUC-580-known-state-architecture-baseline.md`; `.codex/tasks/LUC-694-evidence-ledger-sync-after-baseline-refresh.md`; synchronized state references in task board, project state, active mission, requirements matrix, system health, risk register, regression log, and next steps. | Verification-only checkpoint; no runtime behavior was revalidated in this lane. | Keep future baseline refreshes paired with same-day ledger synchronization checkpoint. | Docs Memory Lead | 2026-05-29 |
| AVIARY-WEB-PROVIDER-SETUP-GUIDANCE-001 | Web Tools route | Provider setup, readiness, and link-confirmation guidance from `/app/tools/overview` renders as safe product UI without credential or execution leakage | P1 | VERIFIED | Medium | `PRJ-1338`; `web/src/components/tools.tsx`; `web/src/lib/tool-formatting.ts`; `web/src/App.tsx`; `web/src/index.css`; Tools directory characterization PASS via Edge with `setupGuideCount=4`, `integralSetupGuideCount=0`, `hasSetupBoundary=true`, provider setup copy present, Telegram pending state present, and `leaksEnvNames=false`; `npm run build` PASS; strict `/tools,/integrations` screenshot/account gate PASS with `route_count=14`, `status=ok`, `screenshot_count=6`, `failed_count=0`, `/tools` setup guides present on desktop/tablet/mobile, and account `panel_visible=true`. | Live credential activation and provider mutation execution remain out of scope; default Chrome CDP can time out locally, with Edge used for the passing characterization rerun. | Continue module metric derivation, deeper Personality state derivation, or backend-exposed connector history only if the backend adds durable records. | Coordinator + Frontend Builder | 2026-05-25 |
| AVIARY-WEB-CONNECTOR-CONSENT-001 | Web Chat and Tools routes | Connector confirmation and Telegram pending-link states render backend-owned consent/link posture as human-readable product UI without faking execution or history | P1 | VERIFIED | Medium | `PRJ-1337`; `web/src/components/chat.tsx`; `web/src/components/tools.tsx`; `web/src/App.tsx`; `web/src/index.css`; connector confirmation render/browser characterization PASS; Tools directory characterization PASS including `telegram_link_pending`; `npm run build` PASS; strict `/chat,/tools,/integrations` screenshot/account gate PASS with `route_count=14`, `status=ok`, `screenshot_count=9`, `failed_count=0`, `panel_visible=true`; Browser live dev check reached auth gate with no console errors or overlay. | Backend chat history still does not expose durable pending-confirmation records, so the UI must not claim historical confirmation audit. Live provider activation was not in scope. | Continue provider setup guidance or backend-exposed confirmation history if that endpoint contract is added. | Coordinator + Frontend Builder | 2026-05-25 |
| AVIARY-WEB-INTEGRATIONS-EXTERNAL-001 | Web Integrations route | Integrations maps only external provider/channel rows from `/app/tools/overview` while Tools preserves the full capability catalog | P1 | VERIFIED | Medium | `PRJ-1336`; `web/src/App.tsx`; `web/src/components/tools.tsx`; `web/src/lib/tool-formatting.ts`; `web/scripts/route-smoke.mjs`; `web/scripts/tools-directory-characterization.mjs`; `npm run build` PASS; `npm run test:tools-directory` PASS; strict `/integrations,/tools` screenshot/account gate PASS with `screenshot_count=6`, `failed_count=0`, `panel_visible=true`; route-smoke proof `integrationProviderCount=4`, titles Telegram, ClickUp, Google Calendar, Google Drive. | Provider-specific setup flows and connector confirmation history are still separate future slices; no external credentials were activated. | Continue connector confirmation history or provider setup guidance with backend-owned link/confirmation contracts. | Coordinator + Frontend Builder | 2026-05-25 |
| AVIARY-WEB-TOOLS-CONTRACT-001 | Web Tools route | Tools frontend proof fixtures match the backend-shaped 4-group/7-tool `/app/tools/overview` catalog and expose safe binding metadata in disclosures | P1 | VERIFIED | Medium | `PRJ-1335`; `web/scripts/tools-directory-characterization.mjs`; `web/scripts/route-smoke.mjs`; `web/src/components/tools.tsx`; `web/src/index.css`; `npm run build` PASS; `npm run test:tools-directory` PASS with `groupCount=4`, `itemCount=7`, `toggleCount=4`, `capabilityChipCount=21`, `technicalDetailsCount=7`, binding authority/operations/full next-action proof; strict `/tools,/integrations` screenshot/account gate PASS with `screenshot_count=6`, `failed_count=0`, `panel_visible=true`; mobile overflow caught and fixed. | Integrations still renders from the broader tool catalog instead of a true external-only provider/channel view; raw backend action IDs are truthful but not yet fully product-copy polished. | Filter Integrations to true external surfaces/channels and translate next-action IDs where appropriate. | Coordinator + Frontend Builder | 2026-05-25 |
| AVIARY-WEB-TOOLS-CAPABILITY-001 | Web Tools route | Tools cards expose safe backend capability, skill-binding, and source-count signals from `/app/tools/overview` in the primary UI | P1 | VERIFIED | Medium | `PRJ-1334`; `web/src/components/tools.tsx`; `web/src/App.tsx`; `web/src/index.css`; `web/scripts/tools-directory-characterization.mjs`; `npm run build` PASS; `npm run test:tools-directory` PASS with `capabilityChipCount=9`, full/toggle/Telegram link/loading/empty/error proof; `/tools,/integrations` screenshot gate PASS with `screenshot_count=6`, `failed_count=0`; route smoke `route_count=14`, `status=ok`; account proof `panel_visible=true`. | `PRJ-1335` closed the stale fixture/detail gap with a broader 4-group/7-tool catalog proof. | Continue external-only Integrations filtering and calmer product copy. | Coordinator + Frontend Builder | 2026-05-25 |
| AVIARY-WEB-CHAT-EMPTY-001 | Web Chat route | Empty backend chat history renders a truthful first-message state without fake preview transcript rows | P1 | VERIFIED | Medium | `PRJ-1333`; `web/src/App.tsx`; `web/src/components/chat.tsx`; `web/src/index.css`; `/app/chat/history` contract; `npm run build` PASS; `npm run test:chat-transcript` PASS with empty `rowCount=0`, `emptyStateCount=1`, `previewMetaCount=0`, full transcript and send proof; empty-history `/chat` screenshot gate PASS with `screenshot_count=3`, `failed_count=0`; route smoke `route_count=14`, `status=ok`; account proof `panel_visible=true`. | Chat confirmation history and deeper connector action audit remain separate future slices. | Continue Tools/Integrations capability mapping or connector confirmation history. | Coordinator + Frontend Builder | 2026-05-25 |
| AVIARY-WEB-SHELL-HEALTH-001 | Web shell health | Desktop sidebar health card maps safe `/health` release, scheduler, reflection, attention, and deployment summary into localized product posture | P1 | VERIFIED | Medium | `PRJ-1332`; `web/src/lib/api.ts`; `web/src/App.tsx`; `web/src/index.css`; `/health` client data; `npm run build` PASS; focused `/dashboard,/personality,/automations` screenshot gate PASS with `viewport_count=3`, `screenshot_count=9`, `failed_count=0`; route smoke `route_count=14`, `status=ok`; account proof `panel_visible=true`. | Shell health is high-level only; deeper ops/debug health remains intentionally out of shell. Future work should map richer health details only in dedicated Tools/Integrations/ops surfaces. | Continue backend-truth UI slices for chat empty/demo state, Tools/Integrations, and connector confirmation history. | Coordinator + Frontend Builder | 2026-05-25 |
| AVIARY-WEB-PERSONALITY-MAP-001 | Web Personality route | User-facing map of backend-backed identity, learned knowledge, planning, skills, activity, and state posture | P1 | VERIFIED | Medium | `PRJ-1331`; `web/src/App.tsx`; `web/src/index.css`; `/app/personality/overview` client data; `npm run build` PASS; focused `/personality` screenshot gate PASS with `viewport_count=3`, `screenshot_count=3`, `failed_count=0`; route smoke `route_count=14`, `status=ok`; account proof `panel_visible=true`. | Full final-personality coverage is not complete; remaining work includes deeper first-viewport parity, richer state proof, and adjacent backend-capability slices for shell health, module routes, Tools/Integrations, and Chat confirmation/empty states. | Continue Personality map fidelity or take the next backend-truth UI slice. | Coordinator + Frontend Builder | 2026-05-25 |
| AVIARY-ARCH-GRAPH-CI-ZEROGAP-001 | Architecture graph CI zero-gap gate | Graph CI fails when curated `--gaps` report is non-empty | P1 | VERIFIED | Medium | `PRJ-1300`; `.github/workflows/architecture-graph.yml`; `docs/architecture/graph-system.md`; `docs/engineering/testing.md`; local `query_architecture_graph.py --gaps --format json` returns empty `items`; graph fast pytest PASS with `31 passed, 1 deselected`. | Hosted Actions evidence is optional supplementary under `DEC-005`. | Keep local/production canonical gates as required baseline and capture hosted workflow evidence only when available. | Ops/Release + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-CLI-GATE-001 | Architecture graph query CLI gate contract | Query CLI supports `--fail-on-gaps` for reusable local/CI enforcement | P1 | VERIFIED | Medium | `PRJ-1301`; `backend/scripts/query_architecture_graph.py`; `backend/tests/test_architecture_graph_query.py`; graph fast pytest PASS with `33 passed, 1 deselected`; local `query_architecture_graph.py --gaps --format json --fail-on-gaps` returns empty `items` with zero exit code. | Hosted workflow execution evidence is optional supplementary under `DEC-005`. | Keep the local CLI gate as required; capture hosted CI proof only when available. | QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-CI-ARTIFACTS-001 | Architecture graph hosted proof artifacts | Graph CI publishes curated gap-audit JSON artifacts for fast/heavy runs | P1 | VERIFIED | Medium | `PRJ-1302`; `.github/workflows/architecture-graph.yml`; upload steps `architecture-gaps-fast` and `architecture-gaps-heavy`; docs updates in graph system/testing; local zero-gap CLI PASS with empty `items`; graph fast pytest PASS with `33 passed, 1 deselected`. | Hosted artifact evidence still pending until first push/PR run. | Capture first hosted artifact bundle and attach to CI policy evidence. | Ops/Release + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-CI-POLICY-TEST-001 | Architecture graph CI policy regression safety | Workflow gate/artefact contract is protected by tests | P1 | VERIFIED | Medium | `PRJ-1303`; `backend/tests/test_architecture_graph_ci_policy.py`; graph test suite PASS with `35 passed, 1 deselected`; local zero-gap CLI PASS with empty `items`. | Hosted workflow run proof is optional supplementary under `DEC-005`. | Keep policy tests in fast graph suite and update deliberately with contract changes; collect hosted run proof only when available. | QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-WEB-SHELL-001 | Architecture graph web shell direct proof | Web app shell component has direct evidence row and no query gap | P1 | VERIFIED | Medium | `PRJ-1297`; `EVID-COMP-WEB-APP-PROOF`; web build PASS; web route smoke PASS with `route_count=14`, `status=ok`; graph generation PASS with `auto_nodes=5295`, `auto_relations=3977`, merged `nodes=5356`, `relations=4041`, `chains=9`, `evidence=53`, `research_sources=21`, `theory_claims=9`; graph/query pytest PASS with `28 passed, 1 deselected in 4.02s`; `COMP-WEB-APP` query reports `Gaps: none`. | Local shell proof only; screenshot parity and production smoke remain separate scopes. | Close the next medium-risk gap from audit, starting with `FEAT-TELEGRAM` or docs/page/service/test rows. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-PERSONALITY-OVERVIEW-001 | Architecture graph Personality overview direct proof | Personality overview API and Personality route nodes have direct evidence rows | P1 | VERIFIED | Medium | `PRJ-1296`; `EVID-API-PERSONALITY-OVERVIEW-PROOF`; `EVID-PAGE-PERSONALITY-PROOF`; focused personality API/repository proof PASS with `2 passed in 3.04s`; web route smoke PASS with `route_count=14`, `status=ok`; graph generation PASS with `auto_nodes=5294`, `auto_relations=3976`, merged `nodes=5355`, `relations=4040`, `chains=9`, `evidence=52`, `research_sources=21`, `theory_claims=9`; targeted node queries report `Gaps: none`; personality proof plus graph/query pytest PASS with `29 passed, 1 deselected in 4.05s`; `LUC-1689` refreshed focused backend route proof `10 passed, 124 deselected in 6.37s`, graph no-gap proof `2 passed, 24 deselected in 0.18s`, targeted `API-PERSONALITY-OVERVIEW` and `PAGE-PERSONALITY` queries `Gaps: none`, and route smoke PASS. | Local proof only; production account memory smoke and screenshot parity remain separate scopes. Generated exporter/task-link inference still lists broad implementation entities until architecture-lane link inference is repaired. | Keep deeper exporter/task-link inference follow-up in `LUC-1687`; production memory smoke and screenshot parity remain separate scopes. | Backend/API + QA/Test | 2026-06-03 |
| AVIARY-ARCH-GRAPH-PROFILE-SETTINGS-001 | Architecture graph profile/settings direct proof | App auth/me/settings/reset API AionProfile model and Settings route nodes have direct evidence rows | P1 | VERIFIED | Medium | `PRJ-1295`; `EVID-API-APP-ME-PROOF`; `EVID-MODEL-AION-PROFILE-PROOF`; `EVID-PAGE-SETTINGS-PROOF`; focused profile/settings proof pack PASS with `9 passed in 5.25s`; graph generation PASS with `auto_nodes=5292`, `auto_relations=3975`, merged `nodes=5353`, `relations=4039`, `chains=9`, `evidence=50`, `research_sources=21`, `theory_claims=9`; targeted node queries report `Gaps: none`; profile/settings plus graph/query pytest PASS with `35 passed, 1 deselected in 15.02s`; web route smoke PASS with `route_count=14`, `status=ok`; `LUC-1688` manual evidence overlay mapped six auth/identity endpoint nodes and reran `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "app_auth or app_me or app_login_logout or app_patch_settings or app_reset_data"; Pop-Location` -> `9 passed, 125 deselected in 48.00s`. | Local proof only; production account data smoke and deeper interactive Settings form proof remain separate scopes. Generated exporter/task-link inference still lists the endpoints until architecture-lane link inference is repaired. | `LUC-1688`, `LUC-1689`, and `LUC-1690` proof-link evidence closures are complete; keep deeper exporter/task-link inference follow-up in `LUC-1687`. | Backend/API + QA/Test | 2026-06-03 |
| AVIARY-ARCH-GRAPH-AGENT-STAGE-001 | Architecture graph runtime agent-stage proof | Perception context planning role motivation and affective assessment agent nodes have direct evidence rows | P1 | VERIFIED | Medium | `PRJ-1294`; `EVID-AGENT-PERCEPTION-PROOF`; `EVID-AGENT-CONTEXT-PROOF`; `EVID-AGENT-PLANNING-PROOF`; `EVID-AGENT-ROLE-PROOF`; `EVID-AGENT-MOTIVATION-PROOF`; `EVID-AGENT-AFFECTIVE-ASSESSMENT-PROOF`; focused agent proof pack PASS with `210 passed in 0.44s`; graph generation PASS with `auto_nodes=5290`, `auto_relations=3974`, merged `nodes=5351`, `relations=4038`, `chains=9`, `evidence=47`, `research_sources=21`, `theory_claims=9`; sampled targeted node queries report `Gaps: none`; agent proof pack plus graph/query pytest PASS with `235 passed, 1 deselected in 3.82s`. | Local stage-contract proof only; live AI provider behavior, production runtime smoke, and full backend regression remain separate scopes. | Close the next medium-risk audit gap: `FEAT-TELEGRAM`, `API-APP-ME`, or `API-PERSONALITY-OVERVIEW`. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-MEDIUM-PROOF-001 | Architecture graph curated medium-risk proof | Tools overview API app-chat pipeline docs and web route smoke test nodes have direct evidence rows | P1 | VERIFIED | Medium | `PRJ-1293`; `EVID-API-TOOLS-OVERVIEW-PROOF`; `EVID-DOC-PIPELINE-APP-CHAT-PROOF`; `EVID-TEST-WEB-ROUTE-SMOKE-PROOF`; focused tools API pytest PASS with `3 passed in 2.23s`; graph generation PASS with `auto_nodes=5288`, `auto_relations=3973`, merged `nodes=5349`, `relations=4037`, `chains=9`, `evidence=41`, `research_sources=21`, `theory_claims=9`; targeted node queries report `Gaps: none`; focused tools plus graph/query pytest PASS with `27 passed, 1 deselected in 7.92s`; web route smoke PASS with `route_count=14`, `status=ok`. | Local proof only; live provider credential activation, Telegram feature graph proof, runtime agent-stage evidence, production smoke, and screenshot parity remain separate scopes. | Close the next medium-risk audit gap: `FEAT-TELEGRAM`, runtime agent-stage evidence nodes, or `API-APP-ME`. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-SERVICE-TEST-PROMPT-001 | Architecture graph service/test/prompt proof | Core runtime service memory service OpenAI prompt and primary backend test nodes have direct evidence rows | P1 | VERIFIED | Medium | `PRJ-1292`; focused proof pack PASS with `13 passed in 2.90s`; graph generation PASS with `auto_nodes=5286`, `auto_relations=3972`, merged `nodes=5347`, `relations=4036`, `chains=9`, `evidence=38`, `research_sources=21`, `theory_claims=9`; targeted node queries for `PROMPT-OPENAI-RUNTIME`, `SERVICE-MEMORY-REPOSITORY`, `SERVICE-RUNTIME-ORCHESTRATOR`, `TEST-API-ROUTES`, `TEST-MEMORY-REPOSITORY`, `TEST-RUNTIME-PIPELINE`, and `TEST-SCHEMA-BASELINE` report `Gaps: none`; combined pytest PASS with `36 passed, 1 deselected in 6.05s`. | Local focused proof only; live OpenAI provider behavior, full backend suite, and production smoke remain separate scopes. | Close medium-risk Telegram, Tools, docs, route-smoke, and agent evidence gaps next. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-RUNTIME-MEMORY-DOCS-001 | Architecture graph runtime/memory source-of-truth proof | Runtime flow docs memory docs event ingress feature foreground runtime feature and memory flow feature graph evidence | P1 | VERIFIED | Medium | `PRJ-1291`; `EVID-EVENT-INGRESS-FEATURE-PROOF`; `EVID-DOC-RUNTIME-FLOW`; `EVID-DOC-MEMORY-SYSTEM`; updated `CHAIN-EVENT-INGRESS`; graph generation PASS with `auto_nodes=5284`, `auto_relations=3971`, merged `nodes=5345`, `relations=4035`, `chains=9`, `evidence=31`, `research_sources=21`, `theory_claims=9`; targeted node queries for `DOC-MEMORY-SYSTEM`, `DOC-RUNTIME-FLOW`, `FEAT-EVENT-INGRESS`, `FEAT-FOREGROUND-RUNTIME`, and `FEAT-MEMORY-FLOW` report `Gaps: none`; graph/query pytest PASS with `22 passed, 1 deselected in 4.62s`. | Graph/doc/feature evidence only; no runtime behavior, memory behavior, or production smoke changed. | Close service/test/prompt evidence gaps next. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-APP-CHAT-EVENT-001 | Architecture graph app chat API/event proof | `API-APP-CHAT-MESSAGE` and `EVENT-APP-CHAT-TURN` evidence for authenticated web chat runtime handoff and transcript behavior | P1 | VERIFIED | Medium | `PRJ-1290`; `EVID-APPCHAT-API-PROOF`; `EVID-APPCHAT-EVENT-PROOF`; focused app-chat API pytest PASS with `3 passed in 3.29s`; web chat transcript characterization PASS with `status=ok`, `appSourceCount=2`, `telegramSourceCount=2`; graph generation PASS with `auto_nodes=5282`, `auto_relations=3970`, merged `nodes=5343`, `relations=4034`, `chains=9`, `evidence=28`, `research_sources=21`, `theory_claims=9`; app-chat plus graph/query pytest PASS with `25 passed, 1 deselected in 5.78s`; node queries for `API-APP-CHAT-MESSAGE` and `EVENT-APP-CHAT-TURN` report `Gaps: none`; `LUC-1689` refreshed focused backend route proof `10 passed, 124 deselected in 6.37s`, graph no-gap proof `2 passed, 24 deselected in 0.18s`, targeted `API-APP-CHAT-MESSAGE` and `EVENT-APP-CHAT-TURN` queries `Gaps: none`, and chat transcript characterization PASS. | Local API/runtime/transcript proof only; native binary/media upload and production chat smoke remain separate future scopes. Generated exporter/task-link inference still lists broad implementation entities until architecture-lane link inference is repaired. | Keep deeper exporter/task-link inference follow-up in `LUC-1687`; native binary/media upload and production chat smoke remain separate future scopes. | Backend/API + QA/Test | 2026-06-03 |
| AVIARY-ARCH-GRAPH-EVENT-INGRESS-001 | Architecture graph event ingress proof | `API-EVENT-INGRESS` public event response API boundary normalization debug gate and runtime API source proof | P1 | VERIFIED | Medium | `PRJ-1289`; `REL-EVENT-002`; `EVID-EVENT-INGRESS-API-PROOF`; focused event ingress pytest PASS with `4 passed in 28.36s`; graph generation PASS with `auto_nodes=5280`, `auto_relations=3969`, merged `nodes=5341`, `relations=4033`, `chains=9`, `evidence=26`, `research_sources=21`, `theory_claims=9`; event ingress plus graph/query pytest PASS with `24 passed, 1 deselected in 6.66s`; node query for `API-EVENT-INGRESS` reports `Gaps: none`. | Local API/runtime contract proof only; production event ingress smoke and Telegram webhook proof remain separate runtime/release scopes. | Close app-chat/event future-scope gaps or documentation evidence gaps next. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-MEMORY-MODEL-001 | Architecture graph AionMemory model proof | `MODEL-AION-MEMORY` model/repository evidence and query gap attribution for memory persistence proof | P1 | VERIFIED | Medium | `PRJ-1288`; `REL-MEMORY-001`; `EVID-AION-MEMORY-MODEL-PROOF`; focused memory/model pytest PASS with `3 passed in 13.37s`; graph generation PASS with `auto_nodes=5278`, `auto_relations=3968`, merged `nodes=5339`, `relations=4031`, `chains=9`, `evidence=25`, `research_sources=21`, `theory_claims=9`; memory/schema plus graph/query pytest PASS with `22 passed, 1 deselected in 20.58s`; node query for `MODEL-AION-MEMORY` reports `Gaps: none`. | Local model/repository/schema proof only; production memory smoke remains a separate runtime/release scope. | Close the next curated graph gap, likely `API-EVENT-INGRESS` or docs evidence nodes, before adding unrelated graph machinery. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-DATA-001 | Architecture graph data model proof | `FEAT-DATA-MODEL` schema chain and evidence for ORM tables migrations constraints and Alembic head parity | P1 | VERIFIED | Medium | `PRJ-1287`; `REL-DATA-004`; `CHAIN-DATA-MODEL-SCHEMA`; `EVID-DATA-MODEL-SCHEMA-CHAIN`; schema baseline pytest PASS with `6 passed in 14.38s`; graph generation PASS with `auto_nodes=5276`, `auto_relations=3967`, merged `nodes=5337`, `relations=4029`, `chains=9`, `evidence=24`, `research_sources=21`, `theory_claims=9`; schema plus graph/query pytest PASS with `24 passed, 1 deselected in 7.00s`; node query for `FEAT-DATA-MODEL` reports `Gaps: none`. | Local schema contract proof only; production database migration smoke remains a separate deployment scope. | Use gap audit to select the next high-risk memory/runtime evidence gap. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-AUTH-001 | Architecture graph auth proof | `API-APP-AUTH` graph relations chain and evidence for app register login logout session and current user boundary | P1 | VERIFIED | Medium | `PRJ-1286`; `REL-AUTH-001..004`; `CHAIN-APP-AUTH`; `EVID-AUTH-API-CHAIN-REFRESH`; focused auth API pytest PASS with `3 passed in 2.77s`; graph generation PASS with `auto_nodes=5275`, `auto_relations=3967`, merged `nodes=5336`, `relations=4028`, `chains=8`, `evidence=23`, `research_sources=21`, `theory_claims=9`; focused auth plus graph/query pytest PASS with `21 passed, 1 deselected in 71.18s`; node query for `API-APP-AUTH` reports `Gaps: none`. | Local API contract proof only; production auth smoke, password/session security review, and UI login UX proof remain separate scopes. | Use gap audit to select the next high-risk curated gap. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-GAP-AUDIT-001 | Architecture graph gap audit | Local CLI report for curated graph nodes with missing evidence rows function chains tests docs or research-support gaps | P1 | VERIFIED | Medium | `PRJ-1285`; `backend/scripts/query_architecture_graph.py --gaps`; `backend/tests/test_architecture_graph_query.py`; `EVID-ARCH-GRAPH-GAP-AUDIT`; graph generation PASS with `auto_nodes=5274`, `auto_relations=3967`, merged `nodes=5335`, `relations=4024`, `chains=7`, `evidence=22`, `research_sources=21`, `theory_claims=9`; focused query plus fast graph pytest PASS with `18 passed, 1 deselected in 3.39s`; CLI gap JSON smoke PASS; generated evidence map/node page/graph JSON include gap audit evidence. | Audit output is a queue, not a fix; curated high-risk gaps still need dedicated evidence/chain work; auto-inventory rows are excluded by default. | Use audit output to select the next high-risk curated missing-proof node, starting with `API-APP-AUTH` or `FEAT-DATA-MODEL` if release needs match. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-QUERY-001 | Architecture graph query utility | Local read-only CLI over generated graph JSON for node details impact chains evidence theory claims and missing-proof gaps | P1 | VERIFIED | Medium | `PRJ-1284`; `backend/scripts/query_architecture_graph.py`; `backend/tests/test_architecture_graph_query.py`; `SCRIPT-QUERY-ARCH-GRAPH`; `TEST-ARCH-GRAPH-QUERY`; `EVID-ARCH-GRAPH-QUERY-CLI`; graph generation PASS with `auto_nodes=5267`, `auto_relations=3961`, merged `nodes=5328`, `relations=4018`, `chains=7`, `evidence=21`, `research_sources=21`, `theory_claims=9`; focused query plus fast graph pytest PASS with `14 passed, 1 deselected in 2.94s`; CLI node smoke PASS for `WORKFLOW-ARCH-GRAPH --show-gaps`; CLI search smoke PASS with curated query nodes ranked before auto rows; generated graph JSON/evidence/node page include query CLI evidence. | Local CLI only; not an interactive graph UI, hosted CI proof, runtime smoke, screenshot proof, or replacement for canonical CSV. | Use the CLI before future systemic function checks; optionally capture hosted graph CI proof when available, or select the next release-critical missing-proof node. | Planning + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-001 | Architecture graph evidence system | CSV-first Obsidian node/relation/chain/evidence/research registry, whole-repository auto inventory, generated graph exports, fast/heavy pytest validation, scoped UX research mapping, verified graph workflow mechanics, all current curated chains verified, and graph CI policy mapped | P0 | VERIFIED | Medium | `PRJ-1266`; `PRJ-1267`; `PRJ-1268`; `PRJ-1269`; `PRJ-1270`; `PRJ-1271`; `PRJ-1272`; `PRJ-1273`; `PRJ-1274`; `PRJ-1275`; `PRJ-1276`; `PRJ-1277`; `PRJ-1278`; `PRJ-1279`; `PRJ-1280`; `PRJ-1281`; `PRJ-1282`; `.github/workflows/architecture-graph.yml`; `WORKFLOW-ARCH-GRAPH-CI`; `EVID-ARCH-GRAPH-CI-POLICY`; `docs/architecture/graph-system.md`; curated registries in `docs/architecture/registry/nodes.csv`, `relations.csv`, `chains.csv`, `evidence.csv`, `research_sources.csv`, and `theory_claims.csv`; generated whole-repository inventory in `auto_nodes.csv` and `auto_relations.csv`; `backend/scripts/generate_architecture_inventory.py`; `backend/scripts/generate_architecture_graph.py`; `backend/tests/test_architecture_graph_generator.py`; generated `docs/architecture/nodes/`, `docs/architecture/relations/index.md`, `docs/architecture/chains/index.md`, `docs/architecture/graphs/architecture-graph.json`, `docs/architecture/graphs/architecture-graph.mmd`, `docs/status/architecture-map-status.md`, `docs/testing/architecture-evidence-map.md`, `docs/testing/architecture-research-map.md`; `UI-CHAT-COGNITIVE-BELT`; `CLAIM-CHAT-COGNITIVE-BELT-LOAD-AWARENESS`; `EVID-ARCH-GRAPH-WORKFLOW-CLOSURE`; `CHAIN-PROFILE-SETTINGS`; `EVID-PROFILE-SETTINGS-CHAIN-REFRESH`; `CHAIN-TOOLS-OVERVIEW`; `EVID-TOOLS-OVERVIEW-CHAIN-REFRESH`; `CHAIN-PERSONALITY-OVERVIEW`; `EVID-PERSONALITY-OVERVIEW-CHAIN-REFRESH`; backend Personality API pytest PASS with `1 passed, 131 deselected in 5.26s`; memory repository focused pytest PASS with `2 passed, 71 deselected in 3.67s`; web build PASS; web route smoke PASS with `/personality` marker `aion-personality-canvas`; latest CI-policy graph generation PASS with `auto_nodes=5237`, `auto_relations=3935`, merged `nodes=5295`, `relations=3986`, `chains=7`, `evidence=19`, `research_sources=21`, `theory_claims=9`; fast graph pytest PASS with `8 passed, 1 deselected in 2.82s`; heavy pytest PASS from PRJ-1278 with `9 passed in 127.74s`; no remaining curated `partial` chains. | Auto-discovered rows are broad inventory, not release-critical proof; scientific sources support theory/design claims only and do not replace implementation/test/behavior/usability proof; heavy all-node parity is intentionally slower than the fast default gate; hosted GitHub Actions proof is optional supplementary evidence under `DEC-005`; production account memory smoke and screenshot parity remain separate evidence scopes. | Keep local graph gate plus production proof cycle as canonical readiness baseline; use hosted GitHub Actions proof as supplementary evidence when available. | Planning + Documentation + QA/Test | 2026-05-24 |
| AVIARY-ARCH-GRAPH-PR-001 | Architecture graph PR review policy | Existing pull request template asks graph-relevant authors to disclose registry chain evidence research generated artifact and fast gate posture | P1 | VERIFIED | Medium | `PRJ-1283`; `.github/pull_request_template.md`; `DOC-PR-TEMPLATE`; `EVID-ARCH-PR-TEMPLATE-CHECKLIST`; graph generation PASS with `auto_nodes=5238`, `auto_relations=3935`, merged `nodes=5297`, `relations=3988`, `chains=7`, `evidence=20`, `research_sources=21`, `theory_claims=9`; fast graph pytest PASS with `8 passed, 1 deselected in 4.64s`; generated graph JSON/evidence/node page include PR template checklist. | Checklist is review guidance and does not replace generator pytest, hosted CI, runtime, screenshot, usability, or production proof. | Use this checklist in graph-relevant PRs; capture hosted CI proof after push. | Planning + QA/Test | 2026-05-24 |
| AVIARY-STATUS-001 | Project status radar | Generated project status dashboard and architecture implementation map | P0 | VERIFIED | High | `PRJ-933`; `docs/operations/project-status-dashboard.md`, `docs/operations/project-status-dashboard.json`, `docs/operations/architecture-implementation-map-2026-05-10.csv`, `docs/planning/current-v1-release-boundary.md`. | Extension rows remain visible but outside selected-scope readiness. | Keep the dashboard/audit refreshed after each architecture or release-boundary change. | Planning + QA/Test | 2026-05-11 |
| AVIARY-WEB-UX-001 | Web shell route evidence | Public and authenticated route-state smoke with lightweight accessibility checks | P1 | VERIFIED | High | `PRJ-931`; `npm exec -- tsc -b --pretty false`; `npm exec -- vite build`; `npm run smoke:routes` -> `route_count=14`, `status=ok`, zero visible unnamed interactive controls. | Visual parity and responsive screenshot comparison were not in this evidence slice. | Keep the command pack in route-shell validation; collect screenshot parity only when a UX/UI polish task requires it. | Frontend Builder + QA/Test | 2026-05-11 |
| AVIARY-WEB-CRITICAL-SMOKE-001 | Web/mobile critical UI smoke coverage | Bounded critical-route screenshot smoke proof for core public/authenticated UI surfaces on desktop and mobile | P1 | VERIFIED | Medium | `LUC-944`; `.codex/tasks/LUC-944-qa-build-web-mobile-critical-ui-smoke-coverage-p1.md`; `Push-Location web; npm run build; $exit=$LASTEXITCODE; Pop-Location; exit $exit` PASS; `Push-Location web; node scripts/route-smoke.mjs --report ../.codex/artifacts/luc944-web-mobile-critical-ui-smoke/report.json --screenshots ../.codex/artifacts/luc944-web-mobile-critical-ui-smoke/screenshots --screenshot-routes /,/login,/dashboard,/chat,/personality,/tools,/integrations,/settings --viewports desktop,mobile --fail-on-ui-findings; $exit=$LASTEXITCODE; Pop-Location; exit $exit` PASS with `status=ok`, `route_count=14`, `ui_audit.screenshot_count=16`, `ui_audit.failed_count=0`. | First smoke attempt failed when run in parallel before build completion (`ENOENT ... web/dist/index.html`); sequential rerun passed. Navigation/account interaction proofs are outside this slice. | Re-run this exact pack after critical route or shell-layout changes; extend only if new route becomes release-critical. | QA/Test | 2026-05-31 |
| AVIARY-WEB-RESP-001 | Web responsive UI baseline | Web shell route rendering across desktop, tablet, and mobile web for selected public/authenticated surfaces | P1 | VERIFIED | High | `PRJ-1150`, `PRJ-1151`, `PRJ-1152`, `PRJ-1153`, `PRJ-1154`, `PRJ-1155`, `PRJ-1156`, `PRJ-1157`, `PRJ-1200`, `PRJ-1201`, `PRJ-1202`, `PRJ-1203`, `PRJ-1204`, `PRJ-1205`, `PRJ-1206`, `PRJ-1207`, `PRJ-1208`, `PRJ-1209`, `PRJ-1210`, `PRJ-1211`, `PRJ-1213`, `PRJ-1214`, `PRJ-1215`, `PRJ-1216`, `PRJ-1217`, `PRJ-1218`, `PRJ-1219`, `PRJ-1220`, `PRJ-1221`, `PRJ-1222`, `PRJ-1223`, `PRJ-1224`, `PRJ-1225`, `PRJ-1226`, `PRJ-1227`, `PRJ-1228`, `PRJ-1229`; `node --check scripts/route-smoke.mjs`; `npm run build`; `npm run audit:ui-responsive`; latest responsive audit -> `route_count=14`, `ui_audit.viewport_count=3`, `ui_audit.screenshot_count=18`, `ui_audit.status=ok`, `failed_count=0`; `npm run audit:ui-navigation` -> `status=ok`, `navigation_proof.step_count=4`, `navigation_proof.failed_count=0`; selected routes covered across desktop/tablet/mobile: `/`, `/dashboard`, `/chat`, `/personality`, `/settings`, `/tools`; public Home polish proof verified no presentation-only landing tag, no nested-window frame, real section anchors, localized auth placeholders, and zero unnamed interactive controls; authenticated shell proof verified no technical build label in the mobile/tablet first viewport and calmer Aviary material styling for the fixed mobile tabbar; dashboard CTA proof clicked 10 action controls and verified navigation to `/chat`, `/goals`, `/reflections`, `/memory`, and `/insights`; dashboard content-rhythm proof verified no artificial desktop greeting wrap, readable guidance actions, and recent-activity token rhythm; dashboard recent-activity proof verified compact right-rail timestamp readability across desktop/tablet/mobile screenshots; dashboard memory-growth proof verified compact chart labels stay visually separated across desktop/tablet/mobile screenshots; tools clarity proof verified capability cards foreground readiness, next action, and user control before technical details across desktop/tablet/mobile screenshots; tools numeric proof verified summary count values render as unambiguous UI numerals across desktop/tablet/mobile screenshots; tools status proof verified duplicate integral/status badges are suppressed when their visible labels match; chat brand-copy proof verified Aviary assistant/safety/sidebar signature copy; chat mobile first-read proof verified the cognitive belt as a horizontal rail with no document-level horizontal overflow; chat response readability proof verified a longer numbered answer with list continuation across desktop/tablet/mobile screenshots and viewport-bounded desktop Chat stage; chat cognitive-belt proof verified Motivation metrics render as compact structured lines instead of truncated slash-separated copy; chat tablet-clearance proof verified the long assistant answer clears the composer more cleanly on tablet while desktop/mobile remain stable; chat mobile assistant-width proof verified assistant answers use the full transcript width on narrow screens while tablet/desktop remain stable; settings danger-boundary proof verified reset runtime data details behind progressive disclosure while preserving reset controls across desktop/tablet/mobile screenshots; settings save-action proof verified normal persistence uses calm teal primary hierarchy while reset remains visually distinct; personality embodied-map proof verified count-heavy callouts and compact mobile timeline context across desktop/tablet/mobile screenshots; personality mobile nav-clearance proof verified the fixed tabbar no longer covers first timeline rows; shared shell proof verified lighter desktop sidebar, mobile in-header icon rail screenshots, tablet icon+label route rail, mobile route-switch clicks to Chat, Settings, Personality, and Dashboard, and PRJ-1224 route-rail affordance proof verified tablet/mobile right-edge continuation, scroll snapping, and end padding while the desktop sidebar stayed structurally stable; PRJ-1225 account-trigger proof verified the mobile/tablet header account trigger uses shell material styling, exposes `aria-expanded`, and opens the account panel through `--account-proof`; PRJ-1226 tablet-header proof verified the tablet header aligns wordmark, route identity, and account trigger in one compact row above the route rail, and route-smoke waits for route markers before screenshot capture; PRJ-1227 sidebar-support proof verified desktop support cards follow navigation with a canonical modest gap while tablet/mobile guardrails stayed stable; PRJ-1228 Dashboard hero proof verified desktop signal cards overlay the scenic figure stage while tablet/mobile guardrails stayed stable; PRJ-1229 authenticated desktop utility proof verified the shared utility/search/action/account band appears above desktop route content while tablet/mobile headers stayed stable. | Browser preview without route-smoke mock auth redirects `/chat` to `/login`; richer Chat composer state coverage remains outside this focused proof. Native app proof is outside current scope. | Continue route-local polish only from concrete screenshot evidence while preserving `audit:ui-responsive` and `audit:ui-navigation` as regression gates. | Frontend Builder + QA/Test | 2026-05-14 |
| AVIARY-MOBILE-UI-001 | Native mobile UI shell | Expo-managed v1.5 native app groundwork over shared `/app/*` contracts | P2 | DEFERRED_BY_CURRENT_SCOPE | High | `PRJ-1158..1199` evidence is preserved, including local preview, production web-supported proof, and hardened device doctor. `PRJ-1200` user rescope moved current UI target to web mobile/tablet/desktop breakpoints and regenerated `ARCH-MOBILE-001` as `DEFERRED`. | Native app proof is outside current scope; do not claim native readiness or pursue Android SDK/device proof unless native app scope is reactivated. | Keep native app evidence parked; validate current UI through `AVIARY-WEB-RESP-001`. | Frontend Builder + QA/Test | 2026-05-14 |
| AVIARY-COGNITIVE-RUNTIME-001 | Digital-being runtime layers | Event/attention -> identity -> AI-assisted perception/fallback -> affective assessment -> context -> motivation -> role/skills -> planning -> expression -> action -> memory/reflection -> debug visibility | P0 | VERIFIED | High | `PRJ-1195`; `PRJ-1196`; `PRJ-1211`; `PRJ-1212`; `docs/operations/aion-runtime-layer-audit-2026-05-13.md`; `tests/test_runtime_pipeline.py::test_runtime_pipeline_api_source`; `tests/test_runtime_pipeline.py::test_runtime_pipeline_contract_smoke_pins_stage_and_action_boundary_invariants`; `tests/test_runtime_pipeline.py::test_runtime_pipeline_uses_ai_assisted_structured_perception_before_context`; `tests/test_perception_assessor.py`; `tests/test_affective_contract.py::test_perception_agent_emits_positive_affect_for_polish_thanks`; `tests/test_language_runtime.py::test_detect_language_uses_polish_thanks_keyword_without_diacritics`; `tests/test_response_budget_policy.py`; `tests/test_openai_client.py::test_openai_client_generate_reply_uses_api_chat_response_budget`; `tests/test_openai_client.py::test_openai_client_generate_reply_uses_telegram_budget_for_telegram_turn`; focused PRJ-1196 structured-perception pack -> `2 passed, 115 deselected`; config/policy/lifespan pack -> `70 passed`; PRJ-1212 response-budget/prompt/client pack -> `14 passed`; PRJ-1212 expression/client/prompt/budget/delivery pack -> `53 passed`; PRJ-1212 runtime channel pack -> `3 passed, 112 deselected`; PRJ-1212 graph/API focused rerun -> `6 passed`; full backend pytest -> `1105 passed`; Coolify production revision `c427ab110276c98a122d6c1be3f7d9a02eeffa3c`; release smoke `release_ready=true`; `/health.runtime_policy.structured_perception_posture=ai_assisted_active`. | Native device proof and external provider activation remain separate module gaps. Live response-length/cost telemetry is not yet implemented. | Monitor response quality/cost from real use; extend `ResponseBudgetPolicy` only from evidence or explicit product modes. | Backend Builder + QA/Test | 2026-05-14 |
| AVIARY-MEMORY-001 | Runtime memory flow | Completed event -> episodic write -> later retrieval -> compressed context -> expression influence -> next episodic write | P0 | VERIFIED | High | `PRJ-1186`; `PRJ-1189`; `PRJ-1190`; `PRJ-1191`; `PRJ-1192`; `PRJ-1193`; `PRJ-1194`; runtime constants `RECENT_MEMORY_LIMIT=6`, `RECENT_MESSAGE_LIMIT=12`, `SEMANTIC_MEMORY_TOP_K=5`, `CONTEXT_TOKEN_BUDGET=2500`; `tests/test_runtime_pipeline.py::test_runtime_recalls_pet_name_from_previous_event_response`; `tests/test_runtime_pipeline.py::test_runtime_applies_concise_response_preference_on_following_turn`; `tests/test_memory_repository.py::test_memory_repository_builds_query_embedding_with_configured_openai_provider`; `tests/test_memory_repository.py::test_memory_repository_includes_vector_matched_episodic_memory_outside_recent_window`; `tests/test_memory_repository.py::test_memory_repository_similarity_fallback_scores_beyond_small_recent_candidate_window`; `tests/test_memory_repository.py::test_memory_repository_includes_vector_matched_relation_when_relation_source_enabled`; `tests/test_reflection_worker.py::test_reflection_worker_consolidates_repeated_memory_topics_into_semantic_summary`; `tests/test_context_agent.py::test_context_summary_includes_long_term_memory_topic_summary_from_conclusions`; `tests/test_runtime_pipeline.py::test_runtime_pipeline_merges_vector_matched_relations_into_debug_state`; `tests/test_context_agent.py::test_context_summary_keeps_vector_retrieved_memory_without_lexical_overlap`; targeted memory/API suite -> `151 passed`; PRJ-1192 relation memory pack -> `4 passed`; PRJ-1192 runtime relation debug pack -> `2 passed`; PRJ-1192 Coolify compose pack -> `12 passed`; PRJ-1192 full backend pytest -> `1086 passed`; PRJ-1193 reflection/context/repository pack -> `177 passed`; PRJ-1193 full backend pytest -> `1088 passed`; PRJ-1194 focused topic-scope pack -> `4 passed`; PRJ-1194 broader memory/runtime pack -> `293 passed`; PRJ-1194 full backend pytest -> `1091 passed`; production Coolify commit `d4d2911be77d1966803d85e052c94175f0da8e18` answered `Roki` after 15 filler episodes and `memory_flow` retrieved original episode `id=4`; production Coolify commit `27324e6b8746d13d80c92e83f8c423887dc558db` wrote/recalled `Roki` and controlled pgvector repository proof ranked `old-relevant|1.0` before 250 newer noise vectors; production Coolify commit `2b6bf01b795a3d0b5a3ca055db39702f0c847b01` replied `Your dog's name is Roki.`; production Coolify commit `f36955646c0271ee1d5bfa30be81c024f260e6e9` reported `semantic_embedding_source_kinds=episodic,semantic,affective,relation`, `retrieval_lifecycle_relation_source_state=optional_family_enabled`, controlled relation-vector proof returned `RELATION_COUNT 1`, `VECTOR_RELATION_HITS 1`, `retrieval_source=vector`, `retrieval_similarity=1.0`, cleaned synthetic rows with `CLEANUP 1 1`, and release smoke returned `release_ready=true`; production Coolify commit `8d0e36e0bcd59d91bf6f0ed0d976875f979c8b3b` release smoke returned `release_ready=true` and controlled topic-summary proof returned `SUMMARY_KIND memory_topic_summary`, `SEMANTIC_EMBEDDINGS 1`, `CONTEXT_HAS_LONG_TERM True`, `CONTEXT_HAS_ROKI True`, cleanup `0 0 0`; production Coolify commit `c11377c00a935d5e49ab13a7364c0d87405436c0` release smoke returned `release_ready=true` and controlled topic-bucket proof returned `SUMMARY_BUCKETS topic:deployment topic:dog`, `TOPIC_SUMMARY_COUNT 2`, `SEMANTIC_EMBEDDINGS 3`, `CONTEXT_HAS_LONG_TERM True`, `CONTEXT_HAS_ROKI True`, `CONTEXT_HAS_DEPLOYMENT True`, cleanup `0 0 0 0`; `/health.memory_retrieval.retrieval_depth_policy` aligned to 6/5; `memory_flow` runtime log includes write status, retrieval counts, retrieved IDs, duration, and context token estimate. | ANN/index policies remain future scale-triggered work; no current latency evidence requires them. | Move to non-memory work unless production retrieval volume makes ANN/index migration necessary. | Backend Builder + QA/Test | 2026-05-13 |
| AVIARY-BLOCKER-001 | External providers | Provider credential activation smoke for connector readiness | P1 | DEFERRED | Medium | `PRJ-933`; `PRJ-1197`; `docs/planning/current-v1-release-boundary.md` keeps organizer activation outside the achieved core/web-supported marker; `/app/tools/overview` now excludes future-only Trello/Nest placeholders and focused tools-overview test passed. | External credentials/input needed before an expanded organizer launch claim; future provider candidates need bounded runtime contracts before appearing in the active tools catalog. | Run provider activation smoke only when credentials exist and organizer scope expands. | Ops/Release + QA/Test | 2026-05-14 |

## Recent Evidence Notes

- `PRJ-1263` completes a verified Dashboard canonical structure pass for
  `AVIARY-WEB-RESP-001`: desktop Dashboard now uses less compressed flagship
  proportions with a wider guidance rail, clearer hero/flow rhythm, and
  restored desktop recent-activity visibility while route contracts, behavior,
  and backend data mapping remain unchanged. Evidence: `npm run build` passed;
  focused `/dashboard` screenshot/navigation/account gate returned `status=ok`,
  `route_count=14`, `ui_audit.screenshot_count=2`,
  `ui_audit.failed_count=0`, `navigation_proof.failed_count=0`,
  `account_proof.failed_count=0`; artifacts at
  `artifacts/route-smoke/prj-1263-dashboard-pass/desktop-dashboard.png` and
  `artifacts/route-smoke/prj-1263-dashboard-pass/mobile-dashboard.png`.

- `PRJ-1262` completes a verified Personality full-surface pass for
  `AVIARY-WEB-RESP-001`: `/personality` now presents a calmer, more coherent
  hierarchy across desktop/mobile through overview bar structure tuning, hero
  material balancing, lighter callout and role-card weight, tighter timeline
  readability, and quieter side-panel surfaces while route contracts and
  backend data mapping remain unchanged. Evidence: `node --check
  web/scripts/route-smoke.mjs` passed; `npm run build` passed; focused
  `/personality` screenshot/navigation/account gate returned `status=ok`,
  `route_count=14`, `ui_audit.screenshot_count=2`, `ui_audit.failed_count=0`,
  `navigation_proof.failed_count=0`, `account_proof.failed_count=0`;
  `git diff --check` passed with LF/CRLF warning only; screenshot artifacts at
  `artifacts/route-smoke/prj-1262/desktop-personality.png` and
  `artifacts/route-smoke/prj-1262/mobile-personality.png`.

- `PRJ-1261` completes a verified Personality mobile timeline map pass for
  `AVIARY-WEB-RESP-001`: mobile Mind Layers Timeline now uses flatter rows,
  stronger layer tokens, inline values, and calmer tracks while preserving all
  six layers and values, hero figure, callouts, connector lines, side panels,
  shared shell, Dashboard, Chat, backend data, route labels, and layer order.
  Evidence: `node --check scripts/route-smoke.mjs` passed; `npm run build`
  passed; combined focused `/personality` screenshot/navigation/account gate
  returned `screenshot_count=3`, `failed_count=0`, `route_count=14`,
  `status=ok`, navigation `step_count=4`, account `panel_visible=true`;
  `git diff --check` passed with LF/CRLF warning only; mobile and desktop
  screenshots were reviewed; cleanup found no validation-owned node/Vite,
  5173/4173 listener, Chromium, or headless browser leftovers and removed two
  fresh route-smoke temp profiles.

- `PRJ-1260` completes a verified Chat cognitive-belt quieting pass for
  `AVIARY-WEB-RESP-001`: the top Chat context strip now uses lighter material,
  CSS-only circular icon accents, and quieter inline status values while all
  six context modules, transcript behavior, source markers, composer, mode
  rail, portrait stage, Dashboard, Personality, shared shell, backend data, and
  fixture copy remain unchanged. Evidence: `node --check
  scripts/route-smoke.mjs` passed; `npm run build` passed; `npm run
  test:chat-transcript` passed with `status=ok`, `appSourceCount=2`,
  `telegramSourceCount=2`; combined focused `/chat` screenshot/navigation/account
  gate returned `screenshot_count=3`, `failed_count=0`, `route_count=14`,
  `status=ok`, navigation `step_count=4`, account `panel_visible=true`;
  `git diff --check` passed with LF/CRLF warning only; desktop/tablet/mobile
  screenshots were reviewed; cleanup removed one fresh
  route-smoke temp profile, stopped four validation-owned
  `chrome-headless-shell` processes, and final check found no validation-owned
  node/Vite, 5173/4173 listener, Chromium, or headless browser leftovers.

- `PRJ-1259` completes a verified Dashboard Current Focus focal polish pass for
  `AVIARY-WEB-RESP-001`: the lower-grid `Current Focus` card now uses a compact
  scenic circular focal treatment instead of a generic orb while current focus
  copy, CTA behavior, Dashboard hero, PRJ-1258 summary band, mobile/tablet
  behavior, Chat, Personality, shared shell, and backend data remain unchanged.
  Evidence: `node --check scripts/route-smoke.mjs` passed; `npm run build`
  passed; combined focused `/dashboard` screenshot/navigation/account gate
  returned `screenshot_count=3`, `failed_count=0`, `route_count=14`,
  `status=ok`, navigation `step_count=4`, account `panel_visible=true`;
  `git diff --check` passed with LF/CRLF warning only; desktop/tablet/mobile
  screenshots were reviewed; cleanup found no validation-owned node/Vite,
  5173/4173 listener, Chromium, or headless browser leftovers and removed one
  fresh route-smoke temp profile.

- `PRJ-1258` completes a verified Dashboard summary closure-band balance pass
  for `AVIARY-WEB-RESP-001`: the lower Dashboard summary band now has a calmer
  System Harmony rhythm, balanced layer rows, and a wide scenic weekly summary
  while Dashboard hero satellites, data/copy, mobile/tablet behavior, Chat,
  Personality, shared shell, and backend data remain unchanged. Evidence:
  `npm run build` passed; focused `/dashboard` screenshot gate returned
  `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`;
  navigation proof returned `step_count=4`, `failed_count=0`; account proof
  returned `step_count=1`, `failed_count=0`, `panel_visible=true`;
  `git diff --check` passed with LF/CRLF warning only; desktop/tablet/mobile
  screenshots were reviewed; cleanup found no validation-owned node/Vite,
  5173/4173 listener, Chromium, or headless browser leftovers and removed four
  fresh route-smoke temp profiles.

- `PRJ-1257` completes a verified Dashboard desktop hero signal satellite pass
  for `AVIARY-WEB-RESP-001`: desktop Dashboard hero signals are lighter,
  tighter, and more connected to the central figure while all six supported
  values, mobile/tablet behavior, cognitive flow, Chat, Personality, shared
  shell, and backend data remain unchanged. Evidence: `npm run build` passed;
  focused `/dashboard` screenshot gate returned `screenshot_count=3`,
  `failed_count=0`, `route_count=14`, `status=ok`; navigation proof returned
  `step_count=4`, `failed_count=0`; account proof returned `step_count=1`,
  `failed_count=0`, `panel_visible=true`; `git diff --check` passed with
  LF/CRLF warning only; cleanup found no validation-owned node/Vite,
  5173/4173 listener, Chromium, or headless browser leftovers and removed
  three fresh route-smoke temp profiles.

- `PRJ-1256` completes a verified Personality mobile callout connector pass
  for `AVIARY-WEB-RESP-001`: mobile callouts now have visible connector lines
  and stronger endpoint dots tying them to the embodied figure, while all
  callouts, values, artwork, role-card visibility, and the compact timeline
  rail remain unchanged. Evidence: `npm run build` passed; focused
  `/personality` screenshot gate returned `screenshot_count=3`,
  `failed_count=0`, `route_count=14`, `status=ok`; navigation proof returned
  `step_count=4`, `failed_count=0`; account proof returned `step_count=1`,
  `failed_count=0`, `panel_visible=true`; `git diff --check` passed with
  LF/CRLF warning only; cleanup found no validation-owned node/Vite,
  5173/4173 listener, Chromium, or headless browser leftovers and removed
  eight fresh route-smoke temp profiles from iterative screenshot tuning.

- `PRJ-1255` completes a verified Chat desktop/tablet persona-stage overlay
  placement pass for `AVIARY-WEB-RESP-001`: the Planning overlay now reads as
  a lower-right portrait-stage annotation instead of a transcript-facing
  lower-left label, while mobile placement, transcript, composer, source
  markers, cognitive belt, and backend data remain unchanged. Evidence:
  `npm run build` passed; focused `/chat` screenshot gate returned
  `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`;
  `npm run test:chat-transcript` returned `status=ok`, `appSourceCount=2`,
  `telegramSourceCount=2`; navigation proof returned `step_count=4`,
  `failed_count=0`; account proof returned `step_count=1`, `failed_count=0`,
  `panel_visible=true`; `git diff --check` passed with LF/CRLF warning only;
  cleanup found no validation-owned node/Vite, 5173/4173 listener, Chromium,
  or headless browser leftovers and removed three fresh route-smoke temp
  profiles from this checkpoint.

- `PRJ-1254` completes a verified Personality mobile timeline rail pass for
  `AVIARY-WEB-RESP-001`: mobile Mind Layers Timeline now uses compact token,
  signal-track, and value-chip rows instead of a tall text list while all six
  layers and values remain visible. Evidence: `npm run build` passed; focused
  `/personality` screenshot gate returned `screenshot_count=3`,
  `failed_count=0`, `route_count=14`, `status=ok`; navigation proof returned
  `step_count=4`, `failed_count=0`; account proof returned `step_count=1`,
  `failed_count=0`, `panel_visible=true`; cleanup found no validation-owned
  node/Vite, 5173/4173 listener, Chromium, or headless browser leftovers and
  removed three fresh route-smoke temp profiles from this checkpoint.

- `PRJ-1253` completes a verified Chat desktop cognitive-belt hierarchy pass
  for `AVIARY-WEB-RESP-001`: desktop Chat belt cards are lower, flatter, and
  visually secondary to the transcript/persona stage while all supported
  labels, values, progress, source markers, and mobile rail behavior remain
  intact. Evidence: `npm run build` passed; focused `/chat` screenshot gate
  returned `screenshot_count=3`, `failed_count=0`, `route_count=14`,
  `status=ok`; `npm run test:chat-transcript` rerun returned `status=ok`,
  `appSourceCount=2`, `telegramSourceCount=2`; navigation proof returned
  `step_count=4`, `failed_count=0`; account proof returned `step_count=1`,
  `failed_count=0`, `panel_visible=true`; `git diff --check` passed with
  LF/CRLF warning only; cleanup found no validation-owned node/Vite,
  5173/4173 listener, or headless browser leftovers and removed six fresh
  route-smoke temp profiles from this checkpoint.

- `PRJ-1252` completes a verified Personality mobile callout hierarchy pass
  for `AVIARY-WEB-RESP-001`: mobile callouts now read as compact
  embodied-map annotations instead of chunky cards over the figure, `Planning`
  stays on one line, and all supported backend-backed values remain visible.
  Evidence: `npm run build` passed; focused `/personality` screenshot gate
  returned `screenshot_count=3`, `failed_count=0`, `route_count=14`,
  `status=ok`; navigation proof returned `step_count=4`, `failed_count=0`;
  account proof returned `step_count=1`, `failed_count=0`,
  `panel_visible=true`; `git diff --check` passed with LF/CRLF warning only;
  cleanup found no Personality route-smoke, Vite/dev-server, 5173/4173
  listener, or headless browser leftovers and removed four fresh route-smoke
  temp profiles from this checkpoint.

- `PRJ-1251` completes a verified Dashboard mobile hero signal hierarchy pass
  for `AVIARY-WEB-RESP-001`: Dashboard signal values now use UI tabular
  numerals, mobile hero signal cards are quieter and shorter, and all six
  supported signal cards remain visible. Evidence: `npm run build` passed;
  focused `/dashboard` screenshot gate returned `screenshot_count=3`,
  `failed_count=0`, `route_count=14`, `status=ok`; navigation proof returned
  `step_count=4`, `failed_count=0`; account proof returned `step_count=1`,
  `failed_count=0`, `panel_visible=true`; `git diff --check` passed with
  LF/CRLF warning only; cleanup found no Personality route-smoke, Vite/dev
  server, 5173/4173 listener, temp route-smoke/chat-transcript profile, or
  headless browser leftovers.

- `PRJ-1250` completes a verified Chat source-marker visual quieting slice for
  `AVIARY-WEB-RESP-001`: the already-approved `App` / `Telegram` source truth
  remains visible but now reads as a small quiet metadata chip instead of a
  competing accent. Evidence: `npm run build` passed; `npm run
  test:chat-transcript` returned `status=ok`, `appSourceCount=2`,
  `telegramSourceCount=2`; focused `/chat` screenshot gate returned
  `screenshot_count=3`, `failed_count=0`; full route smoke returned
  `route_count=14`, `status=ok`; navigation proof returned `step_count=4`,
  `failed_count=0`; account proof returned `step_count=1`, `failed_count=0`,
  `panel_visible=true`; `git diff --check` passed with LF/CRLF warning only;
  cleanup found no route-smoke, Vite, or 5173/4173 listener leftovers after
  targeted temp-profile cleanup; final Windows cleanup reported two stale
  `chrome-headless-shell` handles with empty command lines and no running task
  instance.

- `PRJ-1249` completes a verified channel-routing/tool-truth slice for
  `AVIARY-COGNITIVE-RUNTIME-001` and `AVIARY-WEB-RESP-001`: expression now
  corrects false denial of action-owned search/page-read capability when
  foreground awareness has `available_tool_hints`, app-native chat remains
  `reply.channel == api` with no Telegram client call, Telegram-delivered
  assistant transcript rows project as `telegram`, and Chat message metadata
  displays `App` or `Telegram`. Evidence: focused backend pytest returned
  `7 passed`; `npm run build` passed; `npm run test:chat-transcript` returned
  `status=ok`, `appSourceCount=2`, `telegramSourceCount=2`; focused `/chat`
  screenshot gate returned `screenshot_count=3`, `failed_count=0`,
  `status=ok`; `git diff --check` passed with LF/CRLF warnings only; cleanup
  stopped validation-owned `chrome-headless-shell` leftovers. Live Telegram
  credential smoke remains outside this slice.

- `PRJ-1248` completes a verified mobile Dashboard flow-density pass for
  `AVIARY-WEB-RESP-001`: the cognitive-flow steps now read as a compact
  horizontal rail with a visible next-step peek, all supported steps remain
  available through horizontal scroll, and lower dashboard data appears sooner.
  Evidence: `npm run build` PASS; Dashboard screenshot gate across
  desktop/tablet/mobile returned `screenshot_count=3`, `failed_count=0`; full
  route smoke returned `route_count=14`, `status=ok`; navigation proof
  returned `step_count=4`, `failed_count=0`; account proof returned
  `step_count=1`, `failed_count=0`, `panel_visible=true`; `git diff --check`
  passed with LF/CRLF warning only; cleanup found no validation-owned
  route-smoke, headless browser, or 5173/4173 listener leftovers.

- `PRJ-1246` completes a verified mobile Chat first-read pass for
  `AVIARY-WEB-RESP-001`: the cognitive belt now reads as a compact horizontal
  context rail on mobile, the transcript and composer appear sooner, and all
  supported context cards remain available through horizontal scroll. Evidence:
  `npm run build` PASS; Chat screenshot gate across desktop/tablet/mobile
  returned `screenshot_count=3`, `failed_count=0`; full route smoke returned
  `route_count=14`, `status=ok`; navigation proof returned `step_count=4`,
  `failed_count=0`; account proof returned `step_count=1`, `failed_count=0`,
  `panel_visible=true`; `git diff --check` passed with LF/CRLF warning only;
  cleanup found no validation-owned route-smoke, headless browser, or 5173/4173
  listener leftovers.

- `PRJ-1245` completes a verified flagship secondary chrome coherence pass for
  `AVIARY-WEB-RESP-001`: Chat's cognitive belt cards/meta/progress now read
  flatter, and Personality's overview status, side panels, and rows are quieter
  while Dashboard is intentionally unchanged. Evidence: `npm run build` PASS;
  Dashboard/Chat/Personality screenshot gate across desktop/tablet/mobile
  returned `screenshot_count=9`, `failed_count=0`; full route smoke returned
  `route_count=14`, `status=ok`; navigation proof returned `step_count=4`,
  `failed_count=0`; account proof returned `step_count=1`, `failed_count=0`,
  `panel_visible=true`; `git diff --check` passed with LF/CRLF warning only.

- `PRJ-1244` completes a verified Personality canonical fidelity pass for
  `AVIARY-WEB-RESP-001`: Personality now has lighter hero/callout material,
  flatter side panels, tighter timeline rows, a calmer tablet side-support
  rhythm, and less visually dominant mobile callouts/rows while preserving
  backend-backed values. Evidence: `npm run build` PASS; Personality screenshot
  gate across desktop/tablet/mobile returned `screenshot_count=3`,
  `failed_count=0`; full route smoke returned `route_count=14`, `status=ok`;
  navigation proof returned `step_count=4`, `failed_count=0`; account proof
  returned `step_count=1`, `failed_count=0`, `panel_visible=true`; `git diff
  --check` passed with LF/CRLF warning only.

- `PRJ-1243` completes a verified Chat canonical fidelity pass for
  `AVIARY-WEB-RESP-001`: Chat now hides nonessential route-status pills, uses a
  more balanced desktop conversation/persona split, calms transcript/composer
  density, renders assistant ordered lists as one calm plan surface, suppresses
  the solo quick-action chip, and removes the desktop portrait copy that
  competed with persona-stage overlays.
  Evidence: `npm run build` PASS; Chat screenshot gate across
  desktop/tablet/mobile returned `screenshot_count=3`, `failed_count=0`; full
  route smoke returned `route_count=14`, `status=ok`; navigation proof returned
  `step_count=4`, `failed_count=0`; account proof returned `step_count=1`,
  `failed_count=0`, `panel_visible=true`; `git diff --check` passed with
  LF/CRLF warning only.

- `PRJ-1242` completes a verified Dashboard hero geometry pass for
  `AVIARY-WEB-RESP-001`: desktop Dashboard metrics now sit as side satellites
  around the central hero with visible connector lines, while existing
  backend-backed metric values and tablet/mobile simplification are preserved.
  Evidence: `npm run build` PASS; Dashboard screenshot gate across
  desktop/tablet/mobile returned `screenshot_count=3`, `failed_count=0`; full
  route smoke returned `route_count=14`, `status=ok`; navigation proof returned
  `step_count=4`, `failed_count=0`; account proof returned `step_count=1`,
  `failed_count=0`, `panel_visible=true`; `git diff --check` passed with
  LF/CRLF warning only.

- `PRJ-1241` completes a verified Dashboard first-viewport lock for
  `AVIARY-WEB-RESP-001`: the desktop Dashboard hero now has stronger first-read
  authority, metric overlays and right guidance are quieter, cognitive flow
  reads more like a light bridge, and the lower Reflection card no longer shows
  a clipped row. No new components, fake data, backend contracts, shell changes,
  or branding rename were introduced. Evidence: `npm run build` PASS;
  Dashboard screenshot gate across desktop/tablet/mobile returned
  `screenshot_count=3`, `failed_count=0`; full route smoke returned
  `route_count=14`, `status=ok`; navigation proof returned `step_count=4`,
  `failed_count=0`; account proof returned `step_count=1`, `failed_count=0`,
  `panel_visible=true`; `git diff --check` passed with LF/CRLF warning only.
  This is a verified first-viewport lock, not full pixel-perfect parity.

- `PRJ-1240` completes a verified coherence checkpoint for
  `AVIARY-WEB-RESP-001`: Dashboard, Chat, and Personality received a CSS-only
  proportion/material pass with no new components, fake data, backend
  contracts, or branding rename. Dashboard gives the scenic hero stronger
  first-read authority and quieter metric overlays; Chat reduces persona-stage
  overlay dominance while preserving the canonical two-column body;
  Personality keeps the embodied map with calmer callouts and side-panel
  density. Evidence: `npm run build` PASS; focused screenshot gate for
  `/dashboard`, `/chat`, `/personality` across desktop/tablet/mobile returned
  `screenshot_count=9`, `failed_count=0`; route smoke returned
  `route_count=14`, `status=ok`; navigation proof returned `step_count=4`,
  `failed_count=0`; account proof returned `step_count=1`, `failed_count=0`,
  `panel_visible=true`; `git diff --check` passed with LF/CRLF warning only.
  This is not a 95% pixel-parity claim.

- `PRJ-1239` completes the first flagship canonical-fidelity checkpoint for
  `AVIARY-WEB-RESP-001`: Dashboard, Chat, and Personality no longer render the
  extra desktop utility header above the route-owned flagship scene; Chat is
  tighter against the v5 canonical target with compact belt cards, taller
  workspace, closer 60/40 transcript/persona split, and smaller persona
  overlays; Personality's overview card is demoted into a quiet header so the
  embodied map and side layer panels dominate; Dashboard's secondary desktop
  recent-activity panel is hidden from the first viewport to remove the large
  mid-page void before the summary band. Evidence: `npm run build` PASS;
  focused screenshot gate for `/dashboard`, `/chat`, `/personality` across
  desktop/tablet/mobile returned `screenshot_count=9`, `failed_count=0`; route
  smoke returned `route_count=14`, `status=ok`; navigation proof returned
  `step_count=4`, `failed_count=0`; account proof returned `step_count=1`,
  `failed_count=0`, `panel_visible=true`. Dashboard, Chat, and Personality
  still need exact card-proportion/copy-density parity before claiming 95%.

- `PRJ-1236` completes a local auth and Settings accessibility polish
  checkpoint for `AVIARY-WEB-RESP-001`: auth modal mode controls now use
  segmented button semantics with `aria-pressed` instead of an incomplete
  tablist; the auth modal focuses the email field, traps Tab/Shift+Tab, closes
  on Escape, and attempts focus restore; Settings controls have explicit
  accessible names; Settings copy is less implementation-oriented; desktop
  diagnostics support text is non-interactive status copy; and mobile auth
  backdrop focus is stronger. Evidence: `node --check scripts/route-smoke.mjs`
  PASS; `npm run build` PASS; route smoke `route_count=14`, `status=ok`; full
  responsive screenshot gate `viewport_count=3`, `screenshot_count=42`,
  `failed_count=0`; navigation proof `status=ok`, `step_count=4`,
  `failed_count=0`; account proof `status=ok`, `step_count=1`,
  `failed_count=0`, `panel_visible=true`; screenshot review covered mobile
  Login, mobile Settings, desktop Settings, and desktop Dashboard. Browser live
  proof was blocked by no active Codex browser pane. Production v1.2 release is
  not claimed from this local branch proof.

- `PRJ-1235` completes a local v1.2 mobile-shell first-viewport polish
  checkpoint for `AVIARY-WEB-RESP-001`: authenticated mobile route headers and
  route rails are more compact while preserving one header, one account trigger,
  and one navigation surface; module summary values use unambiguous UI numeric
  typography; desktop sidebar support cards are quieter; inert desktop utility
  buttons became non-button status chips; account triggers now use
  disclosure-aligned semantics instead of `aria-haspopup="dialog"`; and
  `npm run audit:ui-responsive:full` captures the current 14-route
  desktop/tablet/mobile screenshot gate. Evidence: `node --check
  scripts/route-smoke.mjs` PASS; `npm run build` PASS; route smoke
  `route_count=14`, `status=ok`; full responsive screenshot gate
  `viewport_count=3`, `screenshot_count=42`, `failed_count=0`; navigation
  proof `status=ok`, `step_count=4`, `failed_count=0`; account proof
  `status=ok`, `step_count=1`, `failed_count=0`, `panel_visible=true`;
  screenshot review covered mobile Dashboard, Tools, Settings, and desktop
  Dashboard. Production v1.2 release is not claimed from this local branch
  proof.

- `PRJ-1234` completes the local v1.2 flagship last-mile UX checkpoint for
  `AVIARY-WEB-RESP-001`: coordinated UX gap, design-system, and QA gate lanes
  were integrated into a scoped web polish slice. Desktop utility chrome is
  lighter; Chat stage/portrait support spacing is calmer; Dashboard guidance
  and wide-screen side-column pacing were tightened; mobile Personality
  restores `learned knowledge` as a compact embodied-map callout; Personality
  side-stack hierarchy now emphasizes conscious state while quieting recent
  activity; route/account/disclosure accessibility semantics were improved.
  Evidence: `node --check scripts/route-smoke.mjs` PASS; `npm run build`
  PASS; route smoke `route_count=14`, `status=ok`; full responsive screenshot
  gate `viewport_count=3`, `screenshot_count=42`, `failed_count=0`;
  navigation proof `status=ok`, `step_count=4`, `failed_count=0`; account
  proof `status=ok`, `step_count=1`, `failed_count=0`, `panel_visible=true`;
  `git diff --check` passed with LF/CRLF warnings only; cleanup found no
  validation-owned browser/dev-server leftovers. Production v1.2 release is
  not claimed from this local branch proof.

- `PRJ-1233` completes the v1.2 web beauty polish checkpoint for
  `AVIARY-WEB-RESP-001`: Home, Chat, Personality, Dashboard-adjacent module
  surfaces, Tools, Automations, and Integrations were refined from read-only
  UX/flagship/module/QA lane evidence. Mobile Chat now starts conversation
  sooner by reducing pre-thread cognitive cards; mobile Home removes duplicate
  hero proof chips; mobile Personality reduces figure-covering callouts;
  module routes use compact mobile stat rows; Tools mobile density is reduced;
  Automations/Integrations desktop scenic whitespace is tightened; all module
  routes are now part of the screenshot manifest contract. Evidence:
  `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS; route
  smoke `route_count=14`, `status=ok`; full responsive screenshot gate
  `viewport_count=3`, `screenshot_count=42`, `failed_count=0`; navigation
  proof `status=ok`, `step_count=4`, `failed_count=0`; account proof
  `status=ok`, `step_count=1`, `failed_count=0`; visual review covered mobile
  Home, Chat, Personality, Memory, Tools, and desktop Chat/Integrations.
  Production v1.2 release is not claimed from this local branch proof.

- `PRJ-1232` starts the v1.2 canonical web UI baseline for future mobile app
  transfer. The first verified foundation slice added a shared
  `web/src/route-manifest.json`, derived web route constants from it, updated
  route-smoke navigation/account proof to consume the same markers, and
  improved mobile Chat by stacking context cards on narrow screens instead of
  opening with a clipped horizontal belt. Evidence: `node --check
  scripts/route-smoke.mjs` PASS; `npm run build` PASS; route smoke
  `route_count=14`, `status=ok`; responsive screenshot gate
  `screenshot_count=18`, `failed_count=0`; mobile foundation gate for
  `/chat`, `/settings`, `/dashboard` `screenshot_count=3`, `failed_count=0`,
  `overflowingElementCount=0`; navigation proof `step_count=4`,
  `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
  `panel_visible=true`; public Home/Login gate `screenshot_count=4`,
  `failed_count=0`, `overflowingElementCount=0` across desktop/mobile `/` and
  `/login`. Full v1.2 UI parity was not claimed from this foundation slice
  alone.

- `PRJ-1232` finalizes the v1.2 web/mobile foundation checkpoint set for
  `AVIARY-WEB-RESP-001`: Dashboard mobile/tablet labels no longer confuse
  authenticated Dashboard with public Home; desktop Dashboard density, Chat
  cognitive belt, Personality hero rhythm, and module-route consistency were
  completed as bounded frontend checkpoints. Evidence: Dashboard shell gate
  `screenshot_count=3`, `failed_count=0`; Chat belt gate
  `screenshot_count=3`, `failed_count=0`; Personality hero gate
  `screenshot_count=3`, `failed_count=0`; final route smoke `route_count=14`,
  `status=ok`; final responsive gate `screenshot_count=39`,
  `failed_count=0`; navigation proof `status=ok`, `step_count=4`,
  `failed_count=0`; account proof `status=ok`, `step_count=1`,
  `failed_count=0`, `panel_visible=true`. Production v1.2 release is not
  claimed from this branch proof.

- `PRJ-1231` promotes selected-scope v1 to production-backed release marker
  `v1.1.1` for SHA `df677370f63d2688eb792f9a3a846d2cd40a564b`: candidate was
  pushed to `origin/main`; production release smoke with deploy parity passed;
  release reality audit returned `GO_FOR_SELECTED_SHA`; selected SHA go/no-go
  and selected-tag go/no-go returned `GO`; production backend runtime revision
  and web shell build revision match the selected SHA; `release_ready=true`,
  `release_violations=[]`, and v1 final acceptance remains
  `core_v1_bundle_ready`.

- `PRJ-1230` refreshes selected-scope v1 confidence for
  `AVIARY-STATUS-001`, `AVIARY-WEB-RESP-001`,
  `AVIARY-COGNITIVE-RUNTIME-001`, and `AVIARY-MEMORY-001`: backend full
  pytest passed with `1105 passed`; web build, responsive audit, navigation
  proof, account proof, and route smoke passed with `route_count=14`,
  `viewport_count=3`, `screenshot_count=18`, `failed_count=0`, and
  `account_proof.status=ok`; architecture dashboard refresh preserved
  selected-scope readiness at `11/11`; `git diff --check` passed with
  LF/CRLF warnings only; desktop/tablet/mobile Dashboard screenshots were
  reviewed; validation cleanup found no `chrome-headless-shell` and no
  listener on `5173`. Deferred provider, proactive, deploy automation, and
  native extension rows remain outside selected-scope v1.

- `AVIARY-WEB-RESP-001` also includes `PRJ-1229`: authenticated desktop
  utility bar parity passed `npm run build`, `npm run audit:ui-responsive`
  (`route_count=14`, `viewport_count=3`, `screenshot_count=18`,
  `failed_count=0`), `npm run audit:ui-navigation` (`step_count=4`,
  `failed_count=0`), `node scripts/route-smoke.mjs --account-proof --report
  .codex/artifacts/prj1225-account-proof/report.json`
  (`account_proof.status=ok`, `step_count=1`, `failed_count=0`,
  `panel_visible=true`), desktop Dashboard/Chat screenshot review,
  tablet/mobile Dashboard guardrail review, and validation cleanup with no
  AION leftovers. Desktop authenticated routes now show the shared
  utility/search/action/account band above route content.

- `AVIARY-WEB-RESP-001` also includes `PRJ-1228`: Dashboard desktop hero
  overlay parity passed `npm run build`, `npm run audit:ui-responsive`
  (`route_count=14`, `viewport_count=3`, `screenshot_count=18`,
  `failed_count=0`), `npm run audit:ui-navigation` (`step_count=4`,
  `failed_count=0`), `node scripts/route-smoke.mjs --account-proof --report
  .codex/artifacts/prj1225-account-proof/report.json`
  (`account_proof.status=ok`, `step_count=1`, `failed_count=0`,
  `panel_visible=true`), and desktop/tablet/mobile Dashboard screenshot
  review, and validation cleanup with no AION leftovers. Desktop signal cards
  now overlay the scenic figure stage and desktop-only figure-note callouts no
  longer compete with the canonical metric overlay language.

- `AVIARY-WEB-RESP-001` also includes `PRJ-1227`: desktop sidebar support
  rhythm passed `npm run build`, `npm run audit:ui-responsive`
  (`route_count=14`, `viewport_count=3`, `screenshot_count=18`,
  `failed_count=0`), `npm run audit:ui-navigation` (`step_count=4`,
  `failed_count=0`), `node scripts/route-smoke.mjs --account-proof --report
  .codex/artifacts/prj1225-account-proof/report.json`
  (`account_proof.status=ok`, `step_count=1`, `failed_count=0`,
  `panel_visible=true`), representative screenshot review, and validation
  cleanup with no leftovers. Desktop support cards now follow the nav stack
  with a canonical modest gap instead of being pushed to the viewport bottom.

- `AVIARY-WEB-RESP-001` also includes `PRJ-1226`: tablet route header rhythm
  passed `node --check scripts/route-smoke.mjs`, `npm run build`, `npm run
  audit:ui-responsive` (`route_count=14`, `viewport_count=3`,
  `screenshot_count=18`, `failed_count=0`), `npm run audit:ui-navigation`
  (`step_count=4`, `failed_count=0`), `node scripts/route-smoke.mjs
  --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
  (`account_proof.status=ok`, `step_count=1`, `failed_count=0`,
  `panel_visible=true`), representative screenshot review, and validation
  cleanup with no leftovers. Tablet headers now align wordmark, route identity,
  and account trigger in one compact row above the shared route rail.

- `AVIARY-WEB-RESP-001` also includes `PRJ-1225`: mobile/tablet account
  trigger polish passed `node --check scripts/route-smoke.mjs`, `npm run
  build`, `npm run audit:ui-responsive` (`route_count=14`,
  `viewport_count=3`, `screenshot_count=18`, `failed_count=0`), `npm run
  audit:ui-navigation` (`step_count=4`, `failed_count=0`), `node
  scripts/route-smoke.mjs --account-proof --report
  .codex/artifacts/prj1225-account-proof/report.json`
  (`account_proof.status=ok`, `step_count=1`, `failed_count=0`,
  `panel_visible=true`), representative screenshot review, and validation
  cleanup with no leftovers.

- `AVIARY-WEB-RESP-001` also includes `PRJ-1224`: shared shell navigation
  affordance passed `npm run build`, `npm run audit:ui-responsive`
  (`route_count=14`, `viewport_count=3`, `screenshot_count=18`,
  `failed_count=0`), `npm run audit:ui-navigation` (`step_count=4`,
  `failed_count=0`), representative desktop/tablet/mobile screenshot review,
  and validation cleanup with no leftovers. Tablet/mobile route rails now
  communicate horizontal continuation while desktop sidebar structure remains
  stable.

- `AVIARY-WEB-RESP-001` also includes `PRJ-1223`: Dashboard Memory Growth
  label polish passed `npm run build`, `npm run audit:ui-responsive`
  (`route_count=14`, `viewport_count=3`, `screenshot_count=18`,
  `failed_count=0`), focused `/dashboard` route-smoke
  (`screenshot_count=3`, `failed_count=0`), `npm run audit:ui-navigation`,
  desktop/tablet/mobile Dashboard screenshot review, and validation cleanup with no
  browser/server leftovers.

- `AVIARY-WEB-RESP-001` also includes `PRJ-1237`: canonical UI layout index
  planning proof verified `docs/ux/canonical-ui-layout-index.md` as the
  source-of-truth for simplifying future web/native UI passes. The artifact
  maps backend/client data authority, one shared shell, route group IDs,
  first-read hierarchy, component budgets, noise taxonomy, allowed group types,
  pass order, ownership map, and acceptance gates. This is planning evidence,
  not a rendered-route implementation proof; the next smallest action is
  `PASS-NOISE-AUDIT` followed by `PASS-SHELL` with screenshots and route-smoke
  proof.

- `AVIARY-WEB-RESP-001` also includes `PRJ-1238`: shared-shell noise reduction
  removed fake utility search, Focus mode, Quick capture, notification chrome,
  duplicate sidebar diagnostics, and visible mobile `Workspace` labels while
  preserving route context, account access, one desktop sidebar, one mobile
  header, and one route rail. Evidence: `npm run build` PASS, `node --check
  scripts/route-smoke.mjs` PASS, `npm run audit:ui-navigation` PASS
  (`step_count=4`, `failed_count=0`), route smoke `route_count=14`,
  `status=ok`, account proof `step_count=1`, `failed_count=0`,
  `panel_visible=true`, screenshot gate `viewport_count=3`,
  `screenshot_count=42`, `failed_count=0`.

## LUC-1690 Evidence Overlay

- 2026-06-03: `LUC-1690` added a Backend/API preparation evidence overlay for Tools and Integrations without behavior or provider mutation.
- Affected rows:
  - `AVIARY-ARCH-GRAPH-MEDIUM-PROOF-001`
  - `AVIARY-WEB-TOOLS-CAPABILITY-001`
  - `AVIARY-WEB-TOOLS-CONTRACT-001`
  - `AVIARY-WEB-INTEGRATIONS-EXTERNAL-001`
  - `AVIARY-WEB-CONNECTOR-CONSENT-001`
  - `AVIARY-WEB-PROVIDER-SETUP-GUIDANCE-001`
- Fresh proof:
  - backend route cluster: `19 passed, 115 deselected`
  - connector confirmation render characterization: PASS for pending/submitting/success/error states
- Residual:
  - generated task-link report still needs exporter/task-link inference repair under `LUC-1687`
  - current Tools directory browser characterization was blocked by local Chrome/CDP runner failure/timeout, so prior Tools browser evidence remains historical rather than refreshed in this heartbeat
  - live provider credential activation remains deferred/external

## Maintenance Rules

- Update this file when a feature ships, a bug is fixed, a regression appears,
  architecture changes, validation proves a journey, or a module is deferred.
- Prefer verification missions before fix missions when the only problem is
  missing evidence.
- Mark a journey `VERIFIED` only when evidence is current and reproducible.
- Mark a journey `BROKEN` when a real user journey fails, even if related tests
  pass.
- Link evidence to test names, commands, screenshots, smoke notes, commits, or
  task IDs. Chat-only evidence is not enough.
