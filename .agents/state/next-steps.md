# Next Steps

Last updated: 2026-05-25

## NOW

1. Continue from `LUC-260` full takeover audit baseline:
   - latest task:
     `.codex/tasks/LUC-260-full-takeover-audit-and-operating-baseline.md`
   - latest result:
     takeover-preparation baseline now includes known-state map, operating-model parity scan, and gap register with activation lanes
   - proof:
     source-of-truth/state scan complete; role-scope guardrails applied; missing-equivalent artifacts explicitly listed
   - next smallest useful choice:
     create specialist child issues for parity gaps (`docs/documentation-overview.md`, `docs/graphs/*` architecture-awareness exports, `docs/status/architecture-awareness-report.md`) and then fold outputs into one takeover readiness packet

1. Continue from `PRJ-1338` provider setup guidance:
   - latest task:
     `.codex/tasks/PRJ-1338-provider-setup-guidance.md`
   - latest result:
     Tools now renders backend-derived setup guides for Telegram, ClickUp, Google Calendar, and Google Drive, keeps integral tools guide-free, separates provider state from next safe action and backend execution boundary, and avoids credential/env-name leaks
   - proof:
     syntax checks PASS; `npm run build` PASS; `npm run test:tools-directory` PASS via Edge with `setupGuideCount=4`, `integralSetupGuideCount=0`, `hasSetupBoundary=true`, `leaksEnvNames=false`, and Telegram pending state proof;
     strict `/tools,/integrations` screenshot gate PASS with `screenshot_count=6`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; `/tools` desktop/tablet/mobile setup guides and no credential leaks proved; account proof PASS
   - next smallest useful choice:
     continue module metric derivation, deeper Personality state derivation, or connector confirmation history only if backend history support is added

1. Continue from `PRJ-1337` connector confirmation consent copy:
   - latest task:
     `.codex/tasks/PRJ-1337-connector-confirmation-consent-copy.md`
   - latest result:
     Chat confirmation UI now shows friendly connector labels such as `ClickUp / Update task`, keeps the backend reason visible, and Tools shows Telegram pending confirmation as a waiting-for-chat-confirmation state instead of generic no-code copy
   - proof:
     connector render/browser characterization PASS; Tools characterization PASS including `telegram_link_pending`;
     `npm run build` PASS;
     strict `/chat,/tools,/integrations` screenshot gate PASS with `screenshot_count=9`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; account proof PASS; Browser live-dev auth gate showed no console errors or framework overlay
   - next smallest useful choice:
     continue provider setup guidance, module metric derivation, deeper Personality state derivation, or connector confirmation history only if backend history support is added

1. Continue from `PRJ-1336` Integrations external-only provider map:
   - latest task:
     `.codex/tasks/PRJ-1336-integrations-external-only.md`
   - latest result:
     Integrations now shows only Telegram, ClickUp, Google Calendar, and Google Drive from `/app/tools/overview`, while Tools keeps the full 7-item catalog
   - proof:
     syntax checks PASS; `npm run build` PASS; `npm run test:tools-directory` PASS;
     strict `/integrations,/tools` screenshot gate PASS with `screenshot_count=6`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; `/integrations` contract proof `integrationProviderCount=4`; account proof PASS
   - next smallest useful choice:
     continue connector confirmation history, provider setup guidance, module metric derivation, or deeper Personality state derivation

1. Continue from `PRJ-1335` Tools contract fixture refresh:
   - latest task:
     `.codex/tasks/PRJ-1335-tools-contract-fixture-refresh.md`
   - latest result:
     Tools characterization and route-smoke now prove the backend-shaped 4-group / 7-tool `/app/tools/overview` catalog, and technical details expose safe binding metadata plus all next actions
   - proof:
     syntax checks PASS; `npm run build` PASS; `npm run test:tools-directory` PASS with `groupCount=4`, `itemCount=7`, `toggleCount=4`, `capabilityChipCount=21`, `technicalDetailsCount=7`;
     strict `/tools,/integrations` screenshot gate PASS with `screenshot_count=6`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; account proof PASS; mobile `/tools` overflow was caught and fixed before closure
   - next smallest useful choice:
     filter Integrations to true external surfaces/channels and translate backend next-action IDs into calmer product copy where appropriate

1. Continue from `PRJ-1331` backend-capability-to-final-personality-UI mission:
   - latest task:
     `.codex/tasks/PRJ-1333-chat-empty-transcript-truth.md`
   - latest result:
     empty `/app/chat/history` now renders a truthful designed first-message state instead of fake `preview-*` transcript rows
   - proof:
     `npm run build` PASS; `npm run test:chat-transcript` PASS with empty/full/send proof;
     empty-history `/chat` screenshot gate PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; account proof PASS
   - next smallest useful choice:
     deepen Tools/Integrations capability mapping, connector confirmation history, or module metric derivation

1. Continue from `PRJ-1332` shell health backend map:
   - latest task:
     `.codex/tasks/PRJ-1332-shell-health-backend-map.md`
   - latest result:
     desktop shell health now maps selected `/health` fields into localized loading/ready/attention/unavailable posture instead of static `Optimal`
   - proof:
     `npm run build` PASS; focused `/dashboard,/personality,/automations` screenshot gate PASS with
     `viewport_count=3`, `screenshot_count=9`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; account proof PASS
   - next smallest useful choice:
     clean up chat transcript truth/empty-demo state, or deepen Tools/Integrations capability mapping

1. Continue from `PRJ-1331` Personality backend map first slice:
   - task:
     `.codex/tasks/PRJ-1331-personality-backend-map-first-slice.md`
   - result:
     `/personality` now uses localized, backend-signal-aware map/status/timeline/side-panel copy and explicit loading/error/empty/success posture for `/app/personality/overview`
   - proof:
     `npm run build` PASS; focused `/personality` screenshot gate PASS with
     `viewport_count=3`, `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; account proof PASS
   - next smallest useful choice:
     continue Personality first-viewport/map fidelity after the shell health slice

1. Canonical no-paid-GitHub release baseline:
   - required gate:
     `.\backend\scripts\run_production_release_proof_cycle.ps1 -BaseUrl "https://aviary.luckysparrow.ch"`
   - required graph gate:
     `python backend/scripts/run_architecture_graph_local_release_gate.py`
   - policy:
     hosted GitHub Actions proof is optional and must not block release readiness

1. Continue from verified `PRJ-1311` single-command production release evidence capture:
   - task:
     `.codex/tasks/PRJ-1311-single-command-production-release-evidence-capture.md`
   - result:
     one command now captures bundle + smoke + summary in `docs/status`
   - proof:
     `backend/scripts/run_production_release_evidence_capture.ps1`;
     `docs/status/production-release-evidence-summary-20260524T172730Z.json`
   - next smallest useful choice:
     add this command to release handoff checklist runs and keep latest summary linked in ops status

1. Continue from verified `PRJ-1310` production incident-evidence bundle and smoke proof:
   - task:
     `.codex/tasks/PRJ-1310-production-incident-evidence-bundle-and-release-smoke-proof.md`
   - result:
     production proof artifacts now exist in `docs/status` as reusable evidence
   - proof:
     `docs/status/20260524T172450Z_incident-bundle-20260524T172450Z/*`;
     `docs/status/release-smoke-prj1310.json`
   - next smallest useful choice:
     wire this capture into a single local command wrapper for repeatable per-release evidence generation

1. Continue from verified `PRJ-1309` Coolify-first deployment policy and team-context recovery:
   - task:
     `.codex/tasks/PRJ-1309-coolify-first-deployment-policy-and-team-context.md`
   - result:
     deployment policy is now explicitly Coolify-first and no-paid-GitHub-extension
   - proof:
     `DEC-004`; `docs/architecture/28_local_windows_and_coolify_deploy.md`;
     `docs/operations/runtime-ops-runbook.md`; production smoke PASS with
     `release_ready=true`, `release_violations=[]`
   - next smallest useful choice:
     execute a live Coolify deploy for the current mainline revision and attach
     deploy evidence JSON (`trigger_coolify_deploy_webhook.py --evidence-path ...`)

1. Continue from verified `PRJ-1305` Hosted Gap Artifact Verifier Script:
   - task:
     `.codex/tasks/PRJ-1305-hosted-gap-artifact-verifier-script.md`
   - result:
     downloaded hosted gap artifacts can be validated by a dedicated script
   - proof:
     `backend/scripts/verify_architecture_gap_artifact.py`;
     `backend/tests/test_verify_architecture_gap_artifact.py`; graph suite
     PASS (`37 passed, 1 deselected`)
   - next smallest useful choice:
     run hosted workflow after push/PR, download `architecture-gaps-fast`,
     and validate with the artifact verifier helper

1. Environment fallback for hosted proof (`PRJ-1309`, optional):
   - if `gh` CLI or `GITHUB_TOKEN` is unavailable, use manual Actions trigger:
     - `https://github.com/Wroblewski-Patryk/Aviary/actions/workflows/architecture-graph.yml`
   - run `validation_mode=fast`, then optionally `validation_mode=heavy`
   - download hosted artifacts and validate with:
     - `backend/scripts/verify_architecture_gap_artifact.py`
     - `backend/scripts/build_architecture_graph_hosted_evidence_packet.py`

1. Continue from verified `PRJ-1304` Architecture Graph Hosted Proof Checklist (optional):
   - task:
     `.codex/tasks/PRJ-1304-architecture-graph-hosted-proof-checklist.md`
   - result:
     final hosted-proof flow is standardized in one operations checklist
   - proof:
     `docs/operations/architecture-graph-hosted-proof-checklist.md`
     defines preconditions, artifact capture steps, and failure handling
   - next smallest useful choice:
     run the hosted checklist after push/PR and attach artifact evidence
     to graph CI policy rows

1. Continue from verified `PRJ-1303` Graph CI Policy Regression Test:
   - task:
     `.codex/tasks/PRJ-1303-graph-ci-policy-regression-test.md`
   - result:
     graph workflow gate/artefact contract is now guarded by tests
   - proof:
     graph suite PASS (`35 passed, 1 deselected`); local
     `query_architecture_graph.py --gaps --format json --fail-on-gaps`
     returns empty `items`
   - next smallest useful choice:
     capture hosted run artifacts after push/PR and bind proof to CI policy
     evidence rows

1. Continue from verified `PRJ-1302` Graph CI Gap Artifact Proofing:
   - task:
     `.codex/tasks/PRJ-1302-graph-ci-gap-artifact-proofing.md`
   - result:
     graph CI now publishes `architecture-gaps-fast` and
     `architecture-gaps-heavy` artifacts for hosted evidence
   - proof:
     graph query/generator fast pytest PASS (`33 passed, 1 deselected`);
     local `query_architecture_graph.py --gaps --format json --fail-on-gaps`
     returns empty `items`
   - next smallest useful choice:
     execute hosted workflow via push/PR and attach artifact evidence to CI
     policy rows (`WORKFLOW-ARCH-GRAPH-CI`)

1. Continue from verified `PRJ-1301` Gap Audit CLI Fail-On-Gaps Hardening:
   - task:
     `.codex/tasks/PRJ-1301-gap-audit-cli-fail-on-gaps-hardening.md`
   - result:
     curated gap CI gate now uses native
     `query_architecture_graph.py --gaps --format json --fail-on-gaps`
     exit behavior
   - proof:
     graph query/generator fast pytest PASS (`33 passed, 1 deselected`);
     local `--fail-on-gaps` command returns empty `items` with exit code `0`
   - next smallest useful choice:
     capture first hosted GitHub Actions proof for the native fail-on-gaps
     step after push/PR and attach it to CI policy evidence

1. Continue from verified `PRJ-1299` Global Gap Audit Zero-State Closure:
   - task:
     `.codex/tasks/PRJ-1299-global-gap-audit-zero-state-closure.md`
   - result:
     curated architecture gap audit now reports `no gaps detected`
   - proof:
     inventory generation PASS (`auto_nodes=5300`, `auto_relations=3980`);
     graph generation PASS (`nodes=5361`, `relations=4050`, `chains=11`,
     `evidence=65`); `query_architecture_graph.py --gaps --limit 20`
     returns `no gaps detected`
   - next smallest useful choice:
     wire this zero-gap gate into release cadence (pre-merge/pre-release check)
     and keep closing any new gap rows immediately when they appear

1. Continue from verified `PRJ-1298` Telegram Feature Proof Gap Closure:
   - task:
     `.codex/tasks/PRJ-1298-telegram-feature-proof-gap-closure.md`
   - result:
     `FEAT-TELEGRAM` now has direct evidence, explicit relations, and a
     verified execution chain with `Gaps: none`
   - proof:
     focused Telegram proof pack PASS (`7 passed`); combined proof plus graph
     tests PASS (`36 passed, 1 deselected`); graph generation PASS
     (`nodes=5358`, `relations=4048`, `chains=10`, `evidence=54`)
   - next smallest useful choice:
     close medium-risk proof rows for `DOC-FRONTEND-ROUTE-MAP`,
     `DOC-TOOLS-PIPELINE`, `PAGE-DASHBOARD`, `PAGE-TOOLS`,
     `SERVICE-DELIVERY-ROUTER`, or test nodes from gap audit

1. Continue from verified `PRJ-1297` Web App Shell Direct Proof Gap Closure:
   - task:
     `.codex/tasks/PRJ-1297-web-app-shell-direct-proof-gap-closure.md`
   - result:
     `COMP-WEB-APP` now has direct evidence and reports `Gaps: none`
   - proof:
     web build PASS; web route smoke PASS with `route_count=14`,
     `status=ok`; graph generation PASS with `nodes=5356`,
     `relations=4041`, `chains=9`, `evidence=53`; graph/query pytest PASS
     with `28 passed, 1 deselected`
   - next smallest useful choice:
     close `FEAT-TELEGRAM`, `DOC-FRONTEND-ROUTE-MAP`,
     `DOC-TOOLS-PIPELINE`, `PAGE-DASHBOARD`, `PAGE-TOOLS`,
     `SERVICE-DELIVERY-ROUTER`, or test proof rows from the gap audit

1. Continue from verified `PRJ-1296` Personality Overview Direct Proof Gap Closure:
   - task:
     `.codex/tasks/PRJ-1296-personality-overview-direct-proof-gap-closure.md`
   - result:
     `API-PERSONALITY-OVERVIEW` and `PAGE-PERSONALITY` now have direct
     evidence rows and report `Gaps: none`
   - proof:
     focused personality API/repository proof PASS with `2 passed in 3.04s`;
     web route smoke PASS with `route_count=14`, `status=ok`; graph
     generation PASS with `auto_nodes=5294`, `auto_relations=3976`, merged
     `nodes=5355`, `relations=4040`, `chains=9`, `evidence=52`;
     personality proof plus graph/query pytest PASS with
     `29 passed, 1 deselected in 4.05s`
   - next smallest useful choice:
     close `FEAT-TELEGRAM`, `COMP-WEB-APP`, frontend route docs, tools docs,
     dashboard/tools page proof rows, or service delivery proof from the
     latest gap audit

1. Continue from verified `PRJ-1295` Profile Settings Direct Proof Gap Closure:
   - task:
     `.codex/tasks/PRJ-1295-profile-settings-direct-proof-gap-closure.md`
   - result:
     `API-APP-ME`, `MODEL-AION-PROFILE`, and `PAGE-SETTINGS` now have direct
     evidence rows and report `Gaps: none`
   - proof:
     focused profile/settings proof pack PASS with `9 passed in 5.25s`; graph
     generation PASS with `auto_nodes=5292`, `auto_relations=3975`, merged
     `nodes=5353`, `relations=4039`, `chains=9`, `evidence=50`;
     profile/settings plus graph/query pytest PASS with
     `35 passed, 1 deselected in 15.02s`; web route smoke PASS with
     `route_count=14`, `status=ok`
   - next smallest useful choice:
     close `FEAT-TELEGRAM`, `API-PERSONALITY-OVERVIEW`, `COMP-WEB-APP`, or
     frontend/docs/page proof rows from the latest gap audit

1. Continue from verified `PRJ-1294` Runtime Agent Stage Evidence Gap Closure:
   - task:
     `.codex/tasks/PRJ-1294-runtime-agent-stage-evidence-gap-closure.md`
   - result:
     six runtime agent-stage nodes now have direct evidence rows and no longer
     appear in the top graph gap queue
   - proof:
     focused agent proof pack PASS with `210 passed in 0.44s`; graph
     generation PASS with `auto_nodes=5290`, `auto_relations=3974`, merged
     `nodes=5351`, `relations=4038`, `chains=9`, `evidence=47`,
     `research_sources=21`, `theory_claims=9`; agent proof pack plus
     graph/query pytest PASS with `235 passed, 1 deselected in 3.82s`
   - next smallest useful choice:
     close `FEAT-TELEGRAM`, `API-APP-ME`, `API-PERSONALITY-OVERVIEW`, or
     frontend/doc/profile proof rows from the latest gap audit

1. Continue from verified `PRJ-1293` Curated Medium-Risk Proof Cleanup:
   - task:
     `.codex/tasks/PRJ-1293-curated-medium-risk-proof-cleanup.md`
   - result:
     `API-TOOLS-OVERVIEW`, `DOC-PIPELINE-APP-CHAT`, and
     `TEST-WEB-ROUTE-SMOKE` now have direct evidence rows and report
     `Gaps: none`
   - proof:
     focused tools API pytest PASS with `3 passed in 2.23s`; inventory plus
     graph generation PASS with `auto_nodes=5288`, `auto_relations=3973`,
     merged `nodes=5349`, `relations=4037`, `chains=9`, `evidence=41`,
     `research_sources=21`, `theory_claims=9`; focused tools plus graph/query
     pytest PASS with `27 passed, 1 deselected in 7.92s`; web route smoke PASS
     with `route_count=14`, `status=ok`
   - next smallest useful choice:
     close medium-risk graph gaps for `FEAT-TELEGRAM`, runtime agent-stage
     nodes, or `API-APP-ME`

1. Continue from verified `PRJ-1292` Service/Test/Prompt graph evidence gap closure:
   - task:
     `.codex/tasks/PRJ-1292-service-test-prompt-evidence-gap-closure.md`
   - result:
     core service/test/prompt nodes now have evidence rows and report
     `Gaps: none`
   - proof:
     focused proof pack PASS with `13 passed in 2.90s`; inventory plus graph
     generation PASS with `auto_nodes=5286`, `auto_relations=3972`, merged
     `nodes=5347`, `relations=4036`, `chains=9`, `evidence=38`,
     `research_sources=21`, `theory_claims=9`; targeted node queries for the
     seven service/test/prompt nodes report `Gaps: none`; combined
     service/test/prompt plus graph/query pytest PASS with
     `36 passed, 1 deselected in 6.05s`
   - next smallest useful choice:
     close medium-risk gaps for `FEAT-TELEGRAM`, `API-TOOLS-OVERVIEW`,
     `DOC-PIPELINE-APP-CHAT`, `TEST-WEB-ROUTE-SMOKE`, or agent nodes

1. Continue from verified `PRJ-1291` Runtime and Memory doc/feature graph gap closure:
   - task:
     `.codex/tasks/PRJ-1291-runtime-memory-doc-feature-gap-closure.md`
   - result:
     runtime/memory source-of-truth docs now have evidence rows and
     `CHAIN-EVENT-INGRESS` includes event ingress, foreground runtime, and
     memory flow feature anchors
   - proof:
     inventory plus graph generation PASS with `auto_nodes=5284`,
     `auto_relations=3971`, merged `nodes=5345`, `relations=4035`,
     `chains=9`, `evidence=31`, `research_sources=21`,
     `theory_claims=9`; targeted node queries for `DOC-MEMORY-SYSTEM`,
     `DOC-RUNTIME-FLOW`, `FEAT-EVENT-INGRESS`, `FEAT-FOREGROUND-RUNTIME`,
     and `FEAT-MEMORY-FLOW` report `Gaps: none`; graph/query pytest PASS
     with `22 passed, 1 deselected in 4.62s`
   - next smallest useful choice:
     close service/test/prompt evidence gaps for `PROMPT-OPENAI-RUNTIME`,
     `SERVICE-MEMORY-REPOSITORY`, `SERVICE-RUNTIME-ORCHESTRATOR`,
     `TEST-API-ROUTES`, or `TEST-MEMORY-REPOSITORY`

1. Continue from verified `PRJ-1290` App Chat API and Event graph gap closure:
   - task:
     `.codex/tasks/PRJ-1290-app-chat-event-gap-closure.md`
   - result:
     `API-APP-CHAT-MESSAGE` and `EVENT-APP-CHAT-TURN` now have explicit
     evidence rows, and `CHAIN-APP-CHAT-MESSAGE` no longer treats future
     native binary upload as a missing current-chain link
   - proof:
     focused app-chat API pytest PASS with `3 passed in 3.29s`; web chat
     transcript characterization PASS with `status=ok`, `appSourceCount=2`,
     `telegramSourceCount=2`; inventory plus graph generation PASS with
     `auto_nodes=5282`, `auto_relations=3970`, merged `nodes=5343`,
     `relations=4034`, `chains=9`, `evidence=28`,
     `research_sources=21`, `theory_claims=9`; app-chat plus graph/query
     pytest PASS with `25 passed, 1 deselected in 5.78s`; node queries for
     `API-APP-CHAT-MESSAGE` and `EVENT-APP-CHAT-TURN` report `Gaps: none`
   - next smallest useful choice:
     close documentation/feature graph gaps for `DOC-MEMORY-SYSTEM`,
     `DOC-RUNTIME-FLOW`, `FEAT-EVENT-INGRESS`, `FEAT-FOREGROUND-RUNTIME`, or
     `FEAT-MEMORY-FLOW`

1. Continue from verified `PRJ-1289` Event Ingress API graph gap closure:
   - task:
     `.codex/tasks/PRJ-1289-event-ingress-api-gap-closure.md`
   - result:
     `API-EVENT-INGRESS` now has explicit test relation `REL-EVENT-002` and
     evidence `EVID-EVENT-INGRESS-API-PROOF`
   - proof:
     focused event ingress pytest PASS with `4 passed in 28.36s`; inventory
     plus graph generation PASS with `auto_nodes=5280`,
     `auto_relations=3969`, merged `nodes=5341`, `relations=4033`,
     `chains=9`, `evidence=26`, `research_sources=21`,
     `theory_claims=9`; event ingress plus graph/query pytest PASS with
     `24 passed, 1 deselected in 6.66s`; node query for
     `API-EVENT-INGRESS` reports `Gaps: none`; top curated gap audit no
     longer lists `API-EVENT-INGRESS`
   - next smallest useful choice:
     close `API-APP-CHAT-MESSAGE` and `EVENT-APP-CHAT-TURN` together if the
     native binary upload future-scope gap can be explicitly deferred, or
     close `DOC-MEMORY-SYSTEM` / `DOC-RUNTIME-FLOW` as documentation evidence

1. Continue from verified `PRJ-1288` AionMemory model graph gap closure:
   - task:
     `.codex/tasks/PRJ-1288-aion-memory-model-gap-closure.md`
   - result:
     `MODEL-AION-MEMORY` now has explicit memory repository proof through
     `REL-MEMORY-001` and `EVID-AION-MEMORY-MODEL-PROOF`; query gap
     attribution no longer makes model nodes inherit unrelated feature-level
     future-scope missing links
   - proof:
     focused memory/model pytest PASS with `3 passed in 13.37s`; inventory
     plus graph generation PASS with `auto_nodes=5278`,
     `auto_relations=3968`, merged `nodes=5339`, `relations=4031`,
     `chains=9`, `evidence=25`, `research_sources=21`,
     `theory_claims=9`; memory/schema plus graph/query pytest PASS with
     `22 passed, 1 deselected in 20.58s`; node query for
     `MODEL-AION-MEMORY` reports `Gaps: none`; top curated gap audit no
     longer lists `MODEL-AION-MEMORY`
   - next smallest useful choice:
     close the next curated graph gap with a narrow evidence task, likely
     `API-EVENT-INGRESS`, `DOC-MEMORY-SYSTEM`, or `DOC-RUNTIME-FLOW`

1. Continue from verified `PRJ-1287` Data Model graph gap closure:
   - task:
     `.codex/tasks/PRJ-1287-data-model-graph-gap-closure.md`
   - result:
     `FEAT-DATA-MODEL` now has explicit docs relation `REL-DATA-004`,
     verified chain `CHAIN-DATA-MODEL-SCHEMA`, and evidence
     `EVID-DATA-MODEL-SCHEMA-CHAIN`
   - proof:
     schema baseline pytest PASS with `6 passed in 14.38s`; inventory plus
     graph generation PASS with `auto_nodes=5276`, `auto_relations=3967`,
     merged `nodes=5337`, `relations=4029`, `chains=9`, `evidence=24`,
     `research_sources=21`, `theory_claims=9`; schema plus graph/query pytest
     PASS with `24 passed, 1 deselected in 7.00s`; node query for
     `FEAT-DATA-MODEL` reports `Gaps: none`; top curated gap audit no longer
     lists `FEAT-DATA-MODEL`
   - next smallest useful choice:
     close the next high-risk memory/runtime gap from audit output, likely
     `MODEL-AION-MEMORY`, `SERVICE-MEMORY-REPOSITORY`, or
     `SERVICE-RUNTIME-ORCHESTRATOR`

1. Continue from verified `PRJ-1286` Auth API graph gap closure:
   - task:
     `.codex/tasks/PRJ-1286-auth-api-graph-gap-closure.md`
   - result:
     `API-APP-AUTH` now has explicit graph relations, a verified chain
     `CHAIN-APP-AUTH`, and evidence `EVID-AUTH-API-CHAIN-REFRESH`
   - proof:
     focused auth API pytest PASS with `3 passed in 2.77s`; inventory plus
     graph generation PASS with `auto_nodes=5275`, `auto_relations=3967`,
     merged `nodes=5336`, `relations=4028`, `chains=8`, `evidence=23`,
     `research_sources=21`, `theory_claims=9`; focused auth plus graph/query
     pytest PASS with `21 passed, 1 deselected in 71.18s`; node query for
     `API-APP-AUTH` reports `Gaps: none`; top curated gap audit no longer
     lists `API-APP-AUTH`
   - next smallest useful choice:
     close the next high-risk curated gap from audit output, likely
     `FEAT-DATA-MODEL`, `MODEL-AION-MEMORY`, or
     `SERVICE-MEMORY-REPOSITORY`, depending on release priority

1. Continue from verified `PRJ-1285` architecture graph gap audit mode:
   - task:
     `.codex/tasks/PRJ-1285-architecture-graph-gap-audit-mode.md`
   - result:
     `query_architecture_graph.py --gaps` now produces a curated
     missing-proof queue for nodes lacking evidence rows, function chains,
     docs/tests links, or resolved research support; `--include-auto` is
     available for deliberate broad inventory auditing
   - proof:
     inventory plus graph generation PASS with `auto_nodes=5274`,
     `auto_relations=3967`, merged `nodes=5335`, `relations=4024`,
     `chains=7`, `evidence=22`, `research_sources=21`, `theory_claims=9`;
     focused query plus fast graph pytest PASS with
     `18 passed, 1 deselected in 3.39s`; CLI gap JSON smoke PASS; generated
     evidence map, node page, and graph JSON include
     `EVID-ARCH-GRAPH-GAP-AUDIT`
   - next smallest useful choice:
     use the audit output to promote the first high-risk curated gap into a
     dedicated evidence/chain task, such as `API-APP-AUTH` or
     `FEAT-DATA-MODEL`, rather than adding unrelated graph machinery

1. Continue from verified `PRJ-1284` architecture graph query CLI:
   - task:
     `.codex/tasks/PRJ-1284-architecture-graph-query-cli.md`
   - result:
     agents can run `backend/scripts/query_architecture_graph.py` to inspect
     a node's details, incoming/outgoing impact, function chains, evidence,
     theory claims, and missing-proof gaps from the generated graph read model
   - proof:
     inventory plus graph generation PASS with `auto_nodes=5267`,
     `auto_relations=3961`, merged `nodes=5328`, `relations=4018`,
     `chains=7`, `evidence=21`, `research_sources=21`,
     `theory_claims=9`; focused query plus fast graph pytest PASS with
     `14 passed, 1 deselected in 2.94s`; CLI node smoke PASS for
     `WORKFLOW-ARCH-GRAPH --show-gaps`; CLI search smoke PASS with curated
     query nodes ranked before auto rows; generated graph JSON, evidence map,
     and node page include `SCRIPT-QUERY-ARCH-GRAPH`,
     `TEST-ARCH-GRAPH-QUERY`, and `EVID-ARCH-GRAPH-QUERY-CLI`;
     `git diff --check` PASS with LF/CRLF warnings only
   - next smallest useful choice:
      optionally capture hosted GitHub Actions proof when available; otherwise use
     the new CLI to select the next release-critical node with missing proof
     and promote only that chain/evidence slice

1. Continue from verified `PRJ-1283` architecture graph PR template checklist:
   - task:
     `.codex/tasks/PRJ-1283-architecture-graph-pr-template-checklist.md`
   - result:
     the existing pull request template now asks graph-relevant authors to
     report registry, chain, evidence, research, generated artifact, and fast
     graph gate posture; the checklist is represented in the architecture
     graph as `DOC-PR-TEMPLATE`
   - proof:
     inventory plus graph generation PASS with `auto_nodes=5238`,
     `auto_relations=3935`, merged `nodes=5297`, `relations=3988`,
     `chains=7`, `evidence=20`, `research_sources=21`,
     `theory_claims=9`; fast graph pytest PASS with
     `8 passed, 1 deselected in 4.64s`; generated graph JSON, evidence map,
     and node page include `DOC-PR-TEMPLATE` and
     `EVID-ARCH-PR-TEMPLATE-CHECKLIST`; PR template scan confirms graph
     checklist prompts; `git diff --check` PASS with LF/CRLF warnings only
   - next smallest useful choice:
      optionally capture hosted GitHub Actions proof when available; otherwise add
     new curated chains or research claims only when a concrete
     release-critical module or scoped theory claim is selected

1. Continue from verified `PRJ-1282` architecture graph CI policy:
   - task:
     `.codex/tasks/PRJ-1282-architecture-graph-ci-policy.md`
   - result:
     graph validation now has a focused GitHub Actions workflow with an
     automatic fast gate for graph-relevant PR/push changes and a manual
     heavy gate for release-level graph confidence; the policy is itself
     represented in the architecture graph as `WORKFLOW-ARCH-GRAPH-CI`
   - proof:
     inventory plus graph generation PASS with `auto_nodes=5237`,
     `auto_relations=3935`, merged `nodes=5295`, `relations=3986`,
     `chains=7`, `evidence=19`, `research_sources=21`,
     `theory_claims=9`; fast graph pytest PASS with
     `8 passed, 1 deselected in 2.82s`; py_compile PASS; generated graph
     JSON, evidence map, and node page include `WORKFLOW-ARCH-GRAPH-CI`
     and `EVID-ARCH-GRAPH-CI-POLICY`; `git diff --check` PASS with
     LF/CRLF warnings only
   - next smallest useful choice:
      optionally capture hosted GitHub Actions proof when available; otherwise
     choose production smoke evidence or a new curated chain only when a
     release-critical auto-discovered module needs official proof

1. Continue from verified `PRJ-1281` Personality overview chain refresh:
   - task:
     `.codex/tasks/PRJ-1281-personality-overview-chain-refresh.md`
   - result:
     `CHAIN-PERSONALITY-OVERVIEW` is now verified with backend Personality
     API, memory repository, web build, route smoke, graph generation, and
     graph pytest evidence; curated `chains.csv` has no remaining `partial`
     rows
   - proof:
     backend personality API pytest PASS with
     `1 passed, 131 deselected in 5.26s`; memory repository focused pytest
     PASS with `2 passed, 71 deselected in 3.67s`; web build PASS; web route
     smoke PASS with `route_count=14`, `status=ok`, `/personality` marker
     `aion-personality-canvas` passed; graph generation PASS with
     `auto_nodes=5235`, `auto_relations=3935`, merged `nodes=5292`,
     `relations=3983`, `chains=7`, `evidence=18`,
     `research_sources=21`, `theory_claims=9`; fast graph pytest PASS with
     `8 passed, 1 deselected in 4.85s`; py_compile PASS
   - next smallest useful choice:
     pick the next graph maturity step from release needs: CI policy for
     fast/heavy graph gates, production smoke evidence, or a new curated chain
     only when an auto-discovered module becomes release-critical

1. Continue from verified `PRJ-1280` Tools overview chain refresh:
   - task:
     `.codex/tasks/PRJ-1280-tools-overview-chain-refresh.md`
   - result:
     `CHAIN-TOOLS-OVERVIEW` is now verified with backend Tools API,
     connector policy, web build, route smoke, localized browser
     characterization, graph generation, and graph pytest evidence
   - proof:
     backend focused pytest PASS with `12 passed, 126 deselected in 24.09s`;
     web build PASS; Tools directory characterization PASS for full, toggle,
     telegram_link_start, loading, empty, and error states; web route smoke
     PASS; graph generation PASS with `auto_nodes=5234`,
     `auto_relations=3935`, merged `nodes=5291`, `relations=3983`,
     `chains=7`, `evidence=17`, `research_sources=21`,
     `theory_claims=9`; fast graph pytest PASS with
     `8 passed, 1 deselected in 9.99s`; py_compile PASS
   - next smallest useful choice:
     promote `CHAIN-PERSONALITY-OVERVIEW` if fresher curated memory/personality
     chain confidence is needed

1. Continue from verified `PRJ-1279` profile/settings chain refresh:
   - task:
     `.codex/tasks/PRJ-1279-profile-settings-chain-refresh.md`
   - result:
     `CHAIN-PROFILE-SETTINGS` is now verified with fresh backend API,
     preference utility, web build, route smoke, graph generation, and graph
     pytest evidence
   - proof:
     backend focused pytest PASS with `10 passed, 127 deselected in 3.32s`;
     web build PASS; web route smoke PASS with `route_count=14`, `status=ok`,
     `/settings` marker `aion-settings-canvas` passed; graph generation PASS
     with `auto_nodes=5229`, `auto_relations=3931`, merged `nodes=5286`,
     `relations=3979`, `chains=7`, `evidence=16`,
     `research_sources=21`, `theory_claims=9`; fast graph pytest PASS with
     `8 passed, 1 deselected in 3.69s`; py_compile PASS
   - next smallest useful choice:
     promote `CHAIN-TOOLS-OVERVIEW` or `CHAIN-PERSONALITY-OVERVIEW` if the
     next mission needs fresher curated chain confidence

1. Continue from verified `PRJ-1278` architecture graph workflow closure:
   - task:
     `.codex/tasks/PRJ-1278-architecture-graph-workflow-closure.md`
   - result:
     the graph system's own workflow, generator, test, relation, and chain
     statuses are verified with explicit closure evidence
   - proof:
     graph generation PASS with `auto_nodes=5228`, `auto_relations=3931`,
     merged `nodes=5285`, `relations=3979`, `chains=7`, `evidence=15`,
     `research_sources=21`, `theory_claims=9`; fast graph pytest PASS with
     `8 passed, 1 deselected in 4.02s`; heavy graph pytest PASS
     `9 passed in 127.74s`; py_compile PASS
   - next smallest useful choice:
     promote one stale partial feature chain, such as profile settings,
     tools overview, or personality overview, into fresh verified evidence

1. Continue from verified `PRJ-1277` Chat cognitive belt research claim:
   - task:
     `.codex/tasks/PRJ-1277-chat-cognitive-belt-research-claim.md`
   - result:
     the Chat cognitive belt is now a curated graph node with a scoped
     3-source UX theory claim about compact context, working memory, visual
     working memory, and attentional load
   - proof:
     graph generation PASS with `auto_nodes=5227`, `auto_relations=3931`,
     merged `nodes=5284`, `relations=3979`, `chains=7`, `evidence=14`,
     `research_sources=21`, `theory_claims=9`; fast graph pytest PASS with
     `8 passed, 1 deselected in 45.36s`; heavy graph pytest PASS with
     `9 passed in 255.06s`; py_compile PASS
   - next smallest useful choice:
     promote one critical auto-discovered feature chain into curated evidence,
     or add another UX theory claim only after selecting a concrete graph node
     and three reviewed sources

1. Continue from verified `PRJ-1276` fast/heavy graph validation modes:
   - task:
     `.codex/tasks/PRJ-1276-fast-heavy-graph-validation-modes.md`
   - result:
     graph generator pytest now has a fast default gate that excludes the
     slow all-node page parity check, while the full heavy gate remains
     available for release, generator, and docs-regeneration confidence
   - proof:
     fast pytest PASS with `8 passed, 1 deselected`; heavy pytest PASS with
     `9 passed in 99.70s`; inventory plus graph generation PASS with
     `auto_nodes=5226`, `auto_relations=3931`, merged `nodes=5282`,
     `relations=3976`, `chains=7`, `evidence=13`,
     `research_sources=18`, `theory_claims=8`
   - next smallest useful choice:
     select a concrete UX/UI graph node for scoped neuroscience/cognitive
     science claims, or promote one critical auto-discovered feature chain
     into curated evidence

1. Continue from verified `PRJ-1275` all node page parity pytest:
   - task:
     `.codex/tasks/PRJ-1275-all-node-page-parity-pytest.md`
   - result:
     every generated Obsidian node page is now compared against fresh temp
     generator output under pytest
   - proof:
     focused pytest PASS with `9 passed in 108.30s`; inventory plus graph
     generation PASS with `auto_nodes=5225`, `auto_relations=3931`, merged
     `nodes=5281`, `relations=3976`, `chains=7`, `evidence=13`,
     `research_sources=18`, `theory_claims=8`
   - next smallest useful choice:
     document fast versus heavy graph validation commands, then select a
     concrete UX/UI graph node for scoped research claims

1. Continue from verified `PRJ-1274` generated artifact parity pytest:
   - task:
     `.codex/tasks/PRJ-1274-generated-artifact-parity-pytest.md`
   - result:
     key generated graph artifacts are compared against fresh temp generator
     output under pytest
   - proof:
     focused pytest PASS with `8 passed`; inventory plus graph generation PASS
     with `auto_nodes=5223`, `auto_relations=3930`, merged `nodes=5279`,
     `relations=3975`, `chains=7`, `evidence=13`,
     `research_sources=18`, `theory_claims=8`
   - next smallest useful choice:
     select a concrete UX/UI graph node for scoped research claims, or expand
     artifact parity to all generated node pages only if runtime cost is
     acceptable

1. Continue from verified `PRJ-1273` generated graph freshness pytest:
   - task:
     `.codex/tasks/PRJ-1273-generated-graph-freshness-pytest.md`
   - result:
     generated `architecture-graph.json` counts and critical rollup rows are
     now checked against the live registry under pytest
   - proof:
     focused pytest PASS with `7 passed`; inventory plus graph generation PASS
     with `auto_nodes=5221`, `auto_relations=3929`, merged `nodes=5277`,
     `relations=3974`, `chains=7`, `evidence=13`,
     `research_sources=18`, `theory_claims=8`
   - next smallest useful choice:
     either choose strict CI no-diff generation policy or select a concrete
     UX/UI graph node for a scoped research claim

1. Continue from verified `PRJ-1272` current registry validation pytest:
   - task:
     `.codex/tasks/PRJ-1272-current-registry-validation-pytest.md`
   - result:
     graph generator tests now validate the live canonical CSV registry and
     temp research-rollup generation
   - proof:
     focused pytest PASS with `5 passed`; inventory plus graph generation PASS
     with `auto_nodes=5218`, `auto_relations=3927`, merged `nodes=5274`,
     `relations=3972`, `chains=7`, `evidence=13`,
     `research_sources=18`, `theory_claims=8`
   - next smallest useful choice:
     decide whether generated docs need a stale-output no-diff gate in CI, or
     select one concrete UX/UI graph node for a scoped research claim

1. Continue from verified `PRJ-1271` architecture graph generator pytest:
   - task:
     `.codex/tasks/PRJ-1271-architecture-graph-generator-pytest.md`
   - result:
     graph generator now has focused pytest coverage for research-claim
     3-source validation and graph JSON research payload export
   - proof:
     focused pytest PASS with `3 passed`; inventory plus graph generation PASS
     with `auto_nodes=5215`, `auto_relations=3925`, merged `nodes=5271`,
     `relations=3970`, `chains=7`, `evidence=13`,
     `research_sources=18`, `theory_claims=8`
   - next smallest useful choice:
     select one concrete UX/UI graph node before adding cognitive-load,
     attention, or usability neuroscience claims; add broader generator tests
     only when the registry schema changes again

1. Continue from verified `PRJ-1270` affect/motivation/role research claims:
   - task:
     `.codex/tasks/PRJ-1270-affect-motivation-role-research-claims.md`
   - result:
     affective assessment, motivation, and role selection are now curated graph
     nodes with research-backed theory claims
   - proof:
     inventory plus graph generation PASS with `auto_nodes=5205`,
     `auto_relations=3917`, merged `nodes=5261`, `relations=3962`,
     `chains=7`, `evidence=12`, `research_sources=18`, `theory_claims=8`
   - next smallest useful choice:
     select one concrete UX/UI graph node before adding cognitive-load,
     attention, or usability neuroscience claims

1. Continue from verified `PRJ-1269` research claim expansion:
   - task:
     `.codex/tasks/PRJ-1269-research-claim-expansion.md`
   - result:
     research support now covers perception/attention, planning/executive
     control, and memory/reflection consolidation claims
   - proof:
     inventory plus graph generation PASS with `auto_nodes=5204`,
     `auto_relations=3917`, merged `nodes=5257`, `relations=3959`,
     `chains=7`, `evidence=11`, `research_sources=11`, `theory_claims=5`
   - next smallest useful choice:
     review sources for motivation, affective state, role selection, and UX
     claims before adding more theory rows

1. Continue from verified `PRJ-1268` research evidence mapping layer:
   - task:
     `.codex/tasks/PRJ-1268-research-evidence-mapping-layer.md`
   - result:
     research source and theory claim registries now let agents attach
     neuroscience/cognitive-science support to concrete graph nodes with
     applicability scope and limitations
   - proof:
     inventory plus graph generation PASS with `auto_nodes=5203`,
     `auto_relations=3917`, merged `nodes=5256`, `relations=3959`,
     `chains=7`, `evidence=10`, `research_sources=4`, `theory_claims=2`
   - next smallest useful choice:
     add theory claims for runtime, reflection, motivation, planning, UX, or
     memory features only when the claim can cite at least 3 sources; otherwise
     mark it `needs_sources`

1. Continue from verified `PRJ-1267` whole-repository architecture inventory:
   - task:
     `.codex/tasks/PRJ-1267-whole-repository-architecture-inventory.md`
   - result:
     auto-discovered graph coverage now includes scanned project files, Python
     classes/functions, TypeScript/JavaScript symbols, CSS selectors, import
     relations, contains relations, test heuristics, and doc heuristics
   - proof:
     inventory plus graph generation PASS with `auto_nodes=5197`,
     `auto_relations=3915`, merged `nodes=5249`, `relations=3954`,
     `chains=7`, `evidence=9`
   - next smallest useful choice:
     promote critical auto-discovered rows into curated chain/evidence rows
     for API routes, runtime, memory, frontend routes, and tests before using
     them as release-critical proof

1. Continue from verified `PRJ-1266` architecture graph evidence foundation:
   - task:
     `.codex/tasks/PRJ-1266-architecture-graph-evidence-system-foundation.md`
   - result:
     CSV-first Obsidian-compatible graph foundation now exists with canonical
     node, relation, chain, and evidence registries plus generated node pages,
     relation/chain indexes, JSON/Mermaid graph exports, and status/evidence
     rollups
   - proof:
     `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
     PASS with `nodes=52`, `relations=39`, `chains=7`, `evidence=9`
   - next smallest useful choice:
     expand graph coverage one module at a time, starting with backend API
     route/function inventory and frontend route/component inventory; do not
     claim exhaustive graph coverage until all code/docs/tests are inventoried

1. Continue from verified `PRJ-1261`:
   - task:
     `.codex/tasks/PRJ-1261-personality-mobile-timeline-map.md`
   - result:
     mobile Personality Mind Layers Timeline now reads as a calmer layer map
     with flatter rows, stronger tokens, inline values, and quieter tracks
   - proof:
     `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS;
     combined Personality screenshot/navigation/account gate PASS with
     `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`,
     navigation `step_count=4`, account `panel_visible=true`; `git diff
     --check` PASS with LF/CRLF warning only; mobile and desktop screenshots
     reviewed; cleanup found no validation-owned leftovers and removed two
     fresh route-smoke temp profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, route-smoke fixture content, or richer Personality layer data

1. Continue from verified `PRJ-1260`:
   - task:
     `.codex/tasks/PRJ-1260-chat-cognitive-belt-quieting.md`
   - result:
     Chat top cognitive belt now reads as a calmer conversation context strip
     with lighter material, CSS-only circular icon accents, and quieter inline
     status metadata
   - proof:
     `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS;
     `npm run test:chat-transcript` PASS with `status=ok`,
     `appSourceCount=2`, `telegramSourceCount=2`; combined Chat
     screenshot/navigation/account gate PASS with `screenshot_count=3`,
     `failed_count=0`, `route_count=14`, `status=ok`, navigation
     `step_count=4`, account `panel_visible=true`; `git diff --check` PASS
     with LF/CRLF warning only; desktop/tablet/mobile screenshots reviewed;
     cleanup removed one fresh route-smoke temp profile,
     stopped four validation-owned headless browser processes, and final check
     found no validation-owned leftovers
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, route-smoke fixture content, or richer Chat plan data

1. Continue from verified `PRJ-1259`:
   - task:
     `.codex/tasks/PRJ-1259-dashboard-current-focus-focal.md`
   - result:
     Dashboard `Current Focus` now uses a compact scenic circular focal
     treatment instead of a generic teal orb placeholder
   - proof:
     `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS;
     combined Dashboard screenshot/navigation/account gate PASS with
     `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`,
     navigation `step_count=4`, `failed_count=0`, account `step_count=1`,
     `failed_count=0`, `panel_visible=true`; `git diff --check` PASS with
     LF/CRLF warning only; desktop/tablet/mobile screenshots reviewed;
     cleanup found no validation-owned leftovers and removed one fresh
     route-smoke temp profile
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, route-smoke fixture content, or richer Dashboard focus data

1. Continue from verified `PRJ-1258`:
   - task:
     `.codex/tasks/PRJ-1258-dashboard-summary-band-balance.md`
   - result:
     the lower Dashboard summary band now reads as a calmer closure band with
     more readable System Harmony rhythm, balanced layer rows, and a wide
     scenic weekly summary
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`,
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; `git diff --check` PASS with LF/CRLF warning only;
     desktop/tablet/mobile screenshots reviewed; cleanup found no
     validation-owned leftovers and removed four fresh route-smoke temp
     profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, route-smoke fixture content, or richer Dashboard summary data

1. Continue from verified `PRJ-1257`:
   - task:
     `.codex/tasks/PRJ-1257-dashboard-desktop-hero-satellite-quieting.md`
   - result:
     desktop Dashboard hero signal cards are lighter, tighter, and read more
     like connected satellites around the central figure
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`,
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; `git diff --check` PASS with LF/CRLF warning only;
     cleanup found no validation-owned leftovers and removed three fresh
     route-smoke temp profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue from verified `PRJ-1256`:
   - task:
     `.codex/tasks/PRJ-1256-personality-mobile-callout-connectors.md`
   - result:
     mobile Personality callouts now have visible connector lines and stronger
     endpoint dots tying them to the embodied figure
   - proof:
     `npm run build` PASS; Personality screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`,
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; `git diff --check` PASS with LF/CRLF warning only;
     cleanup found no validation-owned leftovers and removed eight fresh
     route-smoke temp profiles from iterative screenshot tuning
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue from verified `PRJ-1255`:
   - task:
     `.codex/tasks/PRJ-1255-chat-desktop-persona-overlay-placement.md`
   - result:
     desktop/tablet Chat now place the `Planning / Conversation continuity`
     overlay as a lower-right persona-stage annotation instead of a
     transcript-facing lower-left label
   - proof:
     `npm run build` PASS; Chat screenshot gate across desktop/tablet/mobile
     PASS with `screenshot_count=3`, `failed_count=0`, `route_count=14`,
     `status=ok`; `npm run test:chat-transcript` PASS with `status=ok`,
     `appSourceCount=2`, `telegramSourceCount=2`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`; `git diff --check` PASS with
     LF/CRLF warning only; cleanup found no validation-owned leftovers and
     removed three fresh route-smoke temp profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue Personality mobile canonical usability from `PRJ-1254`:
   - task:
     `.codex/tasks/PRJ-1254-personality-mobile-timeline-rail.md`
   - result:
     mobile Personality Mind Layers Timeline now reads as a compact token,
     signal-track, and value-chip rail while all six layers remain visible
   - proof:
     `npm run build` PASS; Personality screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`,
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; cleanup found no validation-owned leftovers and
     removed three fresh route-smoke temp profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue Chat canonical usability from `PRJ-1253`:
   - task:
     `.codex/tasks/PRJ-1253-chat-desktop-cognitive-belt-quieting.md`
   - result:
     desktop Chat cognitive belt is flatter, lower, and visually secondary to
     the transcript/persona stage while all supported labels, values,
     progress, source markers, and mobile rail behavior remain intact
   - proof:
     `npm run build` PASS; Chat screenshot gate across desktop/tablet/mobile
     PASS with `screenshot_count=3`, `failed_count=0`, `route_count=14`,
     `status=ok`; `npm run test:chat-transcript` rerun PASS with `status=ok`,
     `appSourceCount=2`, `telegramSourceCount=2`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`; cleanup found no
     validation-owned process leftovers and removed six fresh route-smoke temp
     profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue Personality mobile canonical usability from `PRJ-1252`:
   - task:
     `.codex/tasks/PRJ-1252-personality-mobile-callout-map-quieting.md`
   - result:
     mobile Personality callouts now read as compact embodied-map annotations
     rather than chunky metric cards, `Planning` stays on one line, and all
     supported backend-backed values remain visible
   - proof:
     `npm run build` PASS; Personality screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`,
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; cleanup found no Personality validation-owned
     process leftovers and removed four fresh route-smoke temp profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue Dashboard mobile canonical usability from `PRJ-1251`:
   - task:
     `.codex/tasks/PRJ-1251-dashboard-mobile-hero-signal-quieting.md`
   - result:
     mobile Dashboard hero signal cards are quieter and count values now read
     as clear UI numerals while every supported signal remains visible
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`; cleanup found no Personality
     validation-owned leftovers
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue Chat visual fidelity from `PRJ-1250`:
   - task:
     `.codex/tasks/PRJ-1250-chat-source-marker-quieting.md`
   - result:
     Chat keeps the truthful `App` / `Telegram` transcript marker while
     rendering it as quieter metadata, so the source truth no longer competes
     with speaker, time, delivery status, or message content
   - proof:
     `npm run build` PASS; `npm run test:chat-transcript` PASS with
     `appSourceCount=2`, `telegramSourceCount=2`; Chat screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`; cleanup found no route-smoke,
     Vite, or 5173/4173 listener leftovers after targeted temp-profile cleanup;
     final Windows cleanup reported two stale `chrome-headless-shell` handles
     with no running task instance
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue mobile Dashboard canonical usability from `PRJ-1248`:
   - task:
     `.codex/tasks/PRJ-1248-dashboard-mobile-flow-rail.md`
   - result:
     mobile Dashboard's cognitive-flow steps now read as a compact horizontal
     rail with a visible next-step peek, while Current Phase remains available
     and lower dashboard data appears sooner
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`; cleanup found no
     validation-owned leftovers
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, or
     route-smoke fixture content

1. Continue mobile Chat canonical usability from `PRJ-1246`:
   - task:
     `.codex/tasks/PRJ-1246-chat-mobile-first-read.md`
   - result:
     mobile Chat's cognitive belt now reads as a compact horizontal context
     rail, so the transcript and composer appear sooner while supported cards
     remain available through scroll
   - proof:
     `npm run build` PASS; Chat screenshot gate across desktop/tablet/mobile
     PASS with `screenshot_count=3`, `failed_count=0`; route smoke
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; cleanup found no validation-owned leftovers
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, or
     route-smoke fixture content

1. Continue flagship canonical coherence from `PRJ-1245`:
   - task:
     `.codex/tasks/PRJ-1245-flagship-coherence-tightening.md`
   - result:
     Chat's cognitive belt and Personality's overview/side-panel micro-surfaces
     now read flatter and less card-heavy, while Dashboard was intentionally
     left untouched
   - proof:
     `npm run build` PASS; Dashboard/Chat/Personality screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=9`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`
   - next smallest useful choice:
     make a content/data decision for exact canonical copy/icon parity, or pick
     one exact remaining screenshot mismatch on one route only

1. Continue flagship canonical parity from `PRJ-1244`:
   - task:
     `.codex/tasks/PRJ-1244-personality-canonical-fidelity.md`
   - result:
     Personality now has lighter hero/callout material, flatter side panels,
     tighter timeline rows, a calmer tablet side-support rhythm, and less
     visually dominant mobile callouts/rows
   - proof:
     `npm run build` PASS; Personality screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`
   - next smallest useful choice:
     choose one remaining exact screenshot mismatch across Dashboard, Chat, or
     Personality, or make a content/data decision before changing canonical
     icon glyphs, route-smoke fixture copy, or backend-backed labels

1. Continue Chat canonical parity from `PRJ-1243`:
   - task:
     `.codex/tasks/PRJ-1243-chat-canonical-fidelity.md`
   - result:
     Chat now hides nonessential route-status pills, uses a more balanced
     desktop conversation/persona split, calms transcript/composer density,
     renders assistant ordered lists as one calm plan surface, and suppresses
     the solo quick-action chip plus competing desktop portrait copy
   - proof:
     `npm run build` PASS; Chat screenshot gate across desktop/tablet/mobile
     PASS with `screenshot_count=3`, `failed_count=0`; route smoke
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`
   - next smallest useful choice:
     move to a separate Personality canonical fidelity checkpoint, or make a
     content/data decision before changing Chat icon glyphs, canonical card
     copy, or route-smoke transcript fixture content

1. Continue Dashboard canonical parity from `PRJ-1242`:
   - task:
     `.codex/tasks/PRJ-1242-dashboard-hero-geometry.md`
   - result:
     desktop Dashboard metrics now sit as side satellites with visible
     connector lines around the central hero
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`
   - next smallest useful choice:
     make a separate content/data decision before changing metric labels,
     values, or icon glyphs; otherwise move to one single-surface Chat or
     Personality checkpoint

1. Continue Dashboard canonical parity from `PRJ-1241`:
   - task:
     `.codex/tasks/PRJ-1241-dashboard-first-viewport-lock.md`
   - result:
     Dashboard first viewport now has a stronger scenic hero, quieter metric
     overlays/right guidance/cognitive flow, and no clipped lower Reflection
     row
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`
   - next smallest useful choice:
     tune exact Dashboard hero connector/metric geometry, or switch to one
     separate single-surface checkpoint for Chat or Personality

1. Continue flagship canonical parity from `PRJ-1240`:
   - task:
     `.codex/tasks/PRJ-1240-flagship-coherence-pass.md`
   - result:
     Dashboard, Chat, and Personality received a CSS-only coherence pass with
     stronger Dashboard scene authority, quieter Chat persona overlays, and
     calmer Personality callout/side-panel density
   - proof:
     `npm run build` PASS; focused route screenshot gate for `/dashboard`,
     `/chat`, `/personality` across desktop/tablet/mobile PASS with
     `screenshot_count=9`, `failed_count=0`; route smoke `route_count=14`,
     `status=ok`; navigation proof `step_count=4`, `failed_count=0`;
     account proof `step_count=1`, `failed_count=0`, `panel_visible=true`
   - next smallest useful choice:
     take one exact screenshot mismatch at a time: Dashboard card/copy-density
     parity first, or Chat transcript/persona asset fidelity second

1. Continue Dashboard canonical parity from `PRJ-1239`:
   - task:
     `.codex/tasks/PRJ-1239-flagship-canonical-fidelity.md`
   - result:
     Dashboard, Chat, and Personality no longer render the extra desktop
     utility header above the flagship scene; Chat is tighter against the v5
     60/40 canonical target; Personality's overview header is quieter and the
     embodied map dominates the first viewport
   - proof:
     `npm run build` PASS; focused route screenshot gate for `/dashboard`,
     `/chat`, `/personality` across desktop/tablet/mobile PASS with
     `screenshot_count=9`, `failed_count=0`; route smoke `route_count=14`,
     `status=ok`; navigation proof `failed_count=0`; account proof
     `panel_visible=true`
   - next smallest useful choice:
     tune exact Dashboard card proportions/copy density and then rerun the
     same three-route canonical comparison gate

1. Continue v1.2 UI simplification from `PRJ-1238`:
   - task:
     `.codex/tasks/PRJ-1238-shared-shell-noise-reduction.md`
   - result:
     shared shell fake utility controls and duplicate labels are removed;
     `PASS-NOISE-AUDIT` queue is recorded in
     `docs/ux/canonical-ui-layout-index.md`
   - proof:
     `npm run build` PASS; route smoke `route_count=14`, `status=ok`;
     navigation proof `failed_count=0`; account proof `panel_visible=true`;
     screenshot gate `viewport_count=3`, `screenshot_count=42`,
     `failed_count=0`
   - next smallest useful choices:
     run `PASS-SETTINGS-TOOLS`, starting with Settings hero chips/card grid
     and Tools summary/provider-plumbing noise

1. Continue v1.2 UI simplification from the canonical index:
   - task:
     `.codex/tasks/PRJ-1237-canonical-ui-layout-index.md`
   - source of truth:
     `docs/ux/canonical-ui-layout-index.md`
   - result:
     global shell zones, backend/client data authority IDs, route group IDs,
     first-read hierarchy, component budgets, noise taxonomy, allowed group
     types, implementation ownership map, and acceptance gates are defined
   - next smallest useful choices:
     run `PASS-NOISE-AUDIT` from current screenshots, then `PASS-SHELL` to
     remove duplicate global chrome and inert controls before route-specific
     simplification

1. Selected-scope v1 is released as `v1.1.1`:
   - task:
     `.codex/tasks/PRJ-1231-v1-production-candidate-promotion.md`
   - selected SHA:
     `df677370f63d2688eb792f9a3a846d2cd40a564b`
   - proof:
     production release smoke with deploy parity PASS; release reality audit
     `GO_FOR_SELECTED_SHA`; selected SHA go/no-go `GO`; selected-tag
     `v1.1.1` go/no-go `GO`; backend and web production revisions match the
     selected SHA; `release_ready=true`; `release_violations=[]`
   - next smallest useful choices:
     monitor production, prepare a concise user-facing release note, or expand
     one explicitly deferred extension scope such as provider activation,
     proactive launch, deploy automation hardening, or native proof

1. Selected-scope v1 is locally verified as of `PRJ-1230`:
   - task:
     `.codex/tasks/PRJ-1230-v1-selected-scope-final-readiness-refresh.md`
   - proof:
     backend full pytest -> `1105 passed`; web build/responsive/navigation/
     account/route smoke -> PASS; architecture dashboard refresh ->
     selected-scope readiness `11/11`; `git diff --check` -> PASS with
     LF/CRLF warnings only; desktop/tablet/mobile Dashboard screenshots
     reviewed; cleanup confirmed no validation-owned browser/server leftovers
   - release boundary:
     do not call this a new production release candidate until deploy parity
     and release smoke are run for the chosen target
   - next smallest useful choices:
     promote a production candidate with release smoke, or continue optional
     screenshot-driven route polish without changing the selected-scope v1
     readiness claim

1. Continue from the authenticated desktop utility bar checkpoint:
   - task:
     `.codex/tasks/PRJ-1229-authenticated-desktop-utility-bar-parity.md`
   - result:
     desktop authenticated routes now show the shared utility/search/action
     and account band above route content; the implementation reuses existing
     shell components and does not introduce fake browser chrome
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with
     `step_count=4`, `failed_count=0`;
     `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
     PASS with `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
     `panel_visible=true`; refreshed desktop Dashboard, desktop Chat, tablet
     Dashboard, and mobile Dashboard screenshots reviewed; cleanup confirmed
     no AION validation leftovers
   - residual:
     1:1 parity still needs Dashboard lower-card proportions, exact route
     density/copy comparison, and subsequent route-local flagship polish
   - next smallest slice:
     continue Dashboard parity from lower-card proportions and first-viewport
     density, then return to Chat/personality route-specific gaps

1. Continue from the Dashboard desktop hero overlay checkpoint:
   - task:
     `.codex/tasks/PRJ-1228-dashboard-desktop-hero-overlay-parity.md`
   - result:
     desktop Dashboard signal card columns now overlay the scenic figure stage
     instead of sitting as detached side columns; desktop-only figure-note
     callouts are hidden so the metric overlay becomes the primary canonical
     card language
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with
     `step_count=4`, `failed_count=0`;
     `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
     PASS with `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
     `panel_visible=true`; refreshed desktop, tablet, and mobile Dashboard
     screenshots reviewed; cleanup confirmed no AION validation leftovers
   - residual:
     Dashboard still needs further 1:1 parity slices for lower card
     proportions, top utility interpretation, and exact canonical density
   - next smallest slice:
     continue Dashboard parity from concrete screenshot comparison, then return
     to other flagship routes

1. Continue from the desktop sidebar support rhythm checkpoint:
   - task:
     `.codex/tasks/PRJ-1227-desktop-sidebar-support-rhythm.md`
   - result:
     authenticated desktop sidebar support cards now follow the navigation
     stack with a modest canonical gap instead of being pushed to the viewport
     bottom
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with
     `step_count=4`, `failed_count=0`;
     `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
     PASS with `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
     `panel_visible=true`; refreshed desktop Dashboard, desktop Chat, and
     tablet Dashboard screenshots reviewed; cleanup confirmed no validation
     leftovers
   - residual:
     sidebar card micro-details remain a future dedicated parity pass only if
     screenshot comparison identifies them as the next highest-value gap
   - next smallest slice:
     choose the next polish slice from concrete screenshot evidence across
     shared shell pieces, Dashboard, Chat, Tools, Settings, Home, or another
     flagship route

1. Continue from the tablet route header rhythm checkpoint:
   - task:
     `.codex/tasks/PRJ-1226-tablet-route-header-rhythm.md`
   - result:
     authenticated tablet route headers now align the Aviary wordmark, route
     identity, and account trigger in one compact row above the shared route
     rail while phone mobile headers and desktop sidebar remain unchanged
   - proof:
     `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS;
     `npm run audit:ui-responsive` PASS with `route_count=14`,
     `viewport_count=3`, `screenshot_count=18`, `failed_count=0`; `npm run
     audit:ui-navigation` PASS with `step_count=4`, `failed_count=0`;
     `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
     PASS with `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
     `panel_visible=true`; refreshed tablet Dashboard, tablet Tools, and
     mobile Dashboard screenshots reviewed; cleanup confirmed no validation
     leftovers
   - residual:
     route-local tablet polish remains future work only when a concrete route
     screenshot shows a remaining density or hierarchy issue
   - next smallest slice:
     choose the next polish slice from concrete screenshot evidence across
     shared shell pieces, Dashboard, Chat, Tools, Settings, Home, or another
     flagship route

1. Continue from the mobile/tablet account trigger checkpoint:
   - task:
     `.codex/tasks/PRJ-1225-mobile-account-trigger-polish.md`
   - result:
     repeated authenticated mobile/tablet route headers now use a dedicated
     Aviary shell material account trigger instead of generic outline button
     styling, with `aria-expanded` reflecting panel state
   - proof:
     `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS;
     `npm run audit:ui-responsive` PASS with `route_count=14`,
     `viewport_count=3`, `screenshot_count=18`, `failed_count=0`; `npm run
     audit:ui-navigation` PASS with `step_count=4`, `failed_count=0`;
     `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
     PASS with `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
     `panel_visible=true`; refreshed mobile Dashboard, mobile Settings, and
     tablet Dashboard screenshots reviewed; cleanup confirmed no validation
     leftovers
   - residual:
     deeper account panel layout/content polish remains a separate future slice
     if screenshots show it needs more hierarchy work
   - next smallest slice:
     choose the next polish slice from concrete screenshot evidence across
     shared shell pieces, Dashboard, Chat, Tools, Settings, Home, or another
     flagship route

1. Continue from the shared shell navigation affordance checkpoint:
   - task:
     `.codex/tasks/PRJ-1224-shared-shell-navigation-affordance.md`
   - result:
     shared tablet/mobile route rails now show a subtle right-edge
     continuation affordance with scroll snapping and end padding while the
     desktop sidebar remains structurally unchanged
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with
     `step_count=4`, `failed_count=0`; refreshed desktop Dashboard, tablet
     Dashboard, mobile Chat, and mobile Settings screenshots reviewed; cleanup
     confirmed no validation leftovers
   - residual:
     future route additions may need a grouped navigation model if the rail
     becomes too long for comfortable scanning
   - next smallest slice:
     choose the next polish slice from concrete screenshot evidence across
     shared shell pieces, Dashboard, Chat, Tools, Settings, Home, or another
     flagship route

1. Continue from the Dashboard Memory Growth label checkpoint:
   - task:
     `.codex/tasks/PRJ-1223-dashboard-memory-growth-labels.md`
   - result:
     Dashboard `Memory Growth` chart labels now read as separate compact labels
     instead of visually merging in the narrow desktop card
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; focused `/dashboard` route-smoke to
     `C:\tmp\prj1223-ui-responsive` PASS with `screenshot_count=3`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS; refreshed
     desktop/tablet/mobile Dashboard screenshots reviewed; cleanup confirmed no
     validation leftovers
   - residual:
     future additional memory metric categories may need a wider chart
     treatment instead of more abbreviations
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Dashboard, Chat, Tools, Settings, Home, or another flagship route

1. Continue from the Tools integral status deduplication checkpoint:
   - task:
     `.codex/tasks/PRJ-1222-tools-integral-status-deduplication.md`
   - result:
     Tools item cards now hide the supplemental integral pill when it
     duplicates the primary status label, so `Internal chat` shows one clear
     `Always on` status while details remain visible
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; focused `/tools` route-smoke to
     `C:\tmp\prj1222-ui-responsive` PASS with `screenshot_count=3`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS; refreshed
     desktop/tablet/mobile Tools screenshots reviewed; cleanup confirmed no
     validation leftovers
   - residual:
     future tool state labels should avoid duplicate visible badges when status
     and supplemental metadata carry the same text
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Dashboard, Chat, Tools, Settings, or another flagship route

1. Continue from the Settings save action hierarchy checkpoint:
   - task:
     `.codex/tasks/PRJ-1221-settings-save-action-hierarchy.md`
   - result:
     Settings `Save settings` now reads as a calm teal primary action instead
     of a warning-like amber band, while reset runtime data remains clearly
     separated as the danger boundary
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; focused `/settings` route-smoke to
     `C:\tmp\prj1221-ui-responsive` PASS with `screenshot_count=3`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS; refreshed
     desktop/tablet/mobile Settings screenshots reviewed; cleanup confirmed no
     validation leftovers
   - residual:
     future Settings secondary actions should keep destructive, warning, and
     primary color semantics distinct
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Dashboard, Chat, Tools, Settings, or another flagship route

1. Continue from the mobile Chat assistant-width checkpoint:
   - task:
     `.codex/tasks/PRJ-1220-chat-mobile-assistant-width.md`
   - result:
     mobile Chat assistant responses now use the full transcript width by
     hiding the decorative avatar column on narrow screens while preserving
     speaker metadata
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; focused `/chat` route-smoke to
     `C:\tmp\prj1220-ui-responsive` PASS with `screenshot_count=3`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS; refreshed
     desktop/tablet/mobile Chat screenshots reviewed; cleanup confirmed no
     validation leftovers
   - residual:
     richer live Chat composer states still need route-local screenshot
     coverage when selected as a concrete UX slice
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Chat, Dashboard, Tools, or another flagship route

1. Continue from the Tools summary numeric-readability checkpoint:
   - task:
     `.codex/tasks/PRJ-1219-tools-summary-numeric-readability.md`
   - result:
     Tools summary count values now use unambiguous UI numeric typography with
     tabular numbers, so mobile `1` no longer reads like the letter `I`
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile Tools
     screenshots reviewed; cleanup confirmed no validation leftovers
   - residual:
     future compact metric cards should keep count-heavy values in UI numeric
     typography rather than display-serif glyphs
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Dashboard, Chat, Tools, or another flagship route

1. Continue from the Dashboard recent-activity time-readability checkpoint:
   - task:
     `.codex/tasks/PRJ-1218-dashboard-recent-activity-time-readability.md`
   - result:
     compact Dashboard `Recent Activity` timestamps now use calmer metadata
     typography in narrow right-rail contexts, removing awkward tablet
     uppercase timestamp fragmentation
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile
     Dashboard screenshots reviewed; cleanup confirmed no validation leftovers
   - residual:
     future Dashboard card/content polish should continue from concrete
     screenshot evidence rather than route-wide typography churn
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Dashboard, Chat, or another flagship route

1. Continue from the Chat tablet transcript-clearance checkpoint:
   - task:
     `.codex/tasks/PRJ-1217-chat-tablet-transcript-clearance.md`
   - result:
     tablet Chat now has tighter transcript/card/input spacing so the long
     assistant response clears the composer in the first viewport
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile Chat
     screenshots reviewed; cleanup confirmed no validation leftovers
   - residual:
     richer Chat composer states, especially pending confirmations and
     multi-action states, still need route-local screenshot coverage when
     selected as a concrete UI gap
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence;
     avoid opening a new surface until Chat has no visible first-read defects

1. Continue from the Chat cognitive-belt readability checkpoint:
   - task:
     `.codex/tasks/PRJ-1216-chat-cognitive-belt-readability.md`
   - result:
     Chat Motivation metrics now render as four compact readable lines inside
     the existing cognitive belt instead of a slash-separated string that
     truncated on desktop
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile Chat
     screenshots reviewed; cleanup confirmed no validation leftovers
   - residual:
     mobile rail still intentionally peeks the next card, so edge text can be
     partially visible by design; richer Chat composer/state design remains
     outside this focused belt-readability slice
   - next smallest slice:
     select the next route-local UI fix only from concrete screenshot evidence
     after this checkpoint, with Chat composer/state polish as a likely
     candidate if a specific gap is visible

1. Continue from the Chat mobile context-rail checkpoint:
   - task:
     `.codex/tasks/PRJ-1215-chat-mobile-context-rail-readability.md`
   - result:
     mobile Chat keeps the horizontal cognitive context rail while making the
     first card readable and the next card an intentional peek
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile Chat
     screenshots reviewed; cleanup confirmed no validation leftovers
   - residual:
     broader Chat v5 desktop/tablet composition and richer composer state
     design remain outside this focused mobile rail slice
   - next smallest slice:
     choose the next route-local polish only from concrete screenshot evidence
     so the UI mission does not turn into unbounded churn

1. Continue from the Personality embodied-map checkpoint:
   - task:
     `.codex/tasks/PRJ-1214-personality-embodied-map-polish.md`
   - result:
     Personality count-heavy callout values now read as UI data, and the
     mobile Mind Layers timeline keeps compact visible context before the rows
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile
     Personality screenshots reviewed; cleanup confirmed no validation
     leftovers
   - residual:
     broader Chat v5 composition and deeper Personality state coverage remain
     outside this focused route-local polish
   - next smallest slice:
     continue Chat v5 composition polish, or continue Personality state
     coverage only if screenshot review identifies a concrete gap

1. Continue from the Settings danger-boundary checkpoint:
   - task:
     `.codex/tasks/PRJ-1213-settings-danger-boundary-polish.md`
   - result:
     Settings reset runtime data now uses a native disclosure boundary, so
     destructive reset details are accessible but collapsed by default and safe
     daily preferences dominate the first read
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile
     Settings screenshots reviewed
   - residual:
     reset API, auth, session, persistence, and backend behavior were outside
     this presentational safety-boundary slice
   - next smallest slice:
     continue route-local Chat v5 composition polish or Personality route
     polish while keeping responsive/navigation audits green

1. Continue from the channel-aware AI response budget checkpoint:
   - task:
     `.codex/tasks/PRJ-1212-channel-aware-ai-response-budget-policy.md`
   - result:
     `ResponseBudgetPolicy` now owns app/API chat, Telegram, concise,
     structured, and deep generation budgets; expression passes the resolved
     channel into OpenAI reply generation; and prompts instruct the model to
     finish cleanly rather than stopping mid-sentence, mid-list, or inside
     unfinished code blocks
   - proof:
     response-budget/client/prompt pack PASS with `14 passed`;
     expression/client/prompt/budget/delivery pack PASS with `53 passed`;
     runtime channel pack PASS with `3 passed, 112 deselected`; graph/API
     focused rerun PASS with `6 passed`; full backend pytest PASS with
     `1105 passed`
   - residual:
     live token-spend and latency telemetry were not added in this slice
   - next smallest slice:
     monitor real answer quality/cost, then extend `ResponseBudgetPolicy`
     only if a long-form product mode or telemetry need appears; otherwise
     continue route-local Chat v5, Personality, or Settings polish

2. Continue from the Chat response readability and desktop height checkpoint:
   - task:
     `.codex/tasks/PRJ-1211-chat-response-readability-and-height.md`
   - result:
     Chat reply generation has expanded output budgets, markdown list
     continuation stays inside numbered/bulleted items, and desktop Chat has
     a viewport-bound stage with internal transcript scrolling
   - proof:
     `tests/test_openai_client.py` PASS with `7 passed`; `npm run
     test:chat-markdown` PASS with `case_count=7`; `node --check
     scripts/route-smoke.mjs` PASS; `npm run build` PASS; `npm run
     audit:ui-responsive` PASS with `route_count=14`, `viewport_count=3`,
     `screenshot_count=18`, `failed_count=0`; `npm run audit:ui-navigation`
     PASS with `status=ok`, `step_count=4`, `failed_count=0`; refreshed
     desktop/tablet/mobile Chat screenshots reviewed
   - residual:
     broader Chat v5 route composition polish remains open; Browser preview
     without route-smoke mock auth redirects `/chat` to `/login`, so
     mock-authenticated route-smoke remains the authenticated screenshot proof
     path
   - next smallest slice:
     continue route-local Chat v5 composition polish or move to Personality or
     Settings route-local polish while keeping responsive/navigation audits
     green

3. Continue from the Tools route UX clarity checkpoint:
   - task:
     `.codex/tasks/PRJ-1210-tools-route-ux-clarity.md`
   - result:
     Tools cards now foreground readiness, availability, link state, provider
     posture, next action, and user control before technical details; single
     item groups span the directory width on desktop/tablet
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile Tools
     screenshots reviewed; cleanup confirmed no active `chrome_headless_shell`,
     no validation Node processes, and no listener on `5173`; `git diff
     --check` passed with LF/CRLF warnings only
   - residual:
     deeper Tools art direction and connector-specific states can improve when
     provider scope expands
   - next smallest slice:
     continue Settings confidence polish, Personality route-local polish, or
     broader Chat v5 composition work

4. Continue from the shared shell navigation proof checkpoint:
   - task:
     `.codex/tasks/PRJ-1209-shared-shell-navigation-proof-and-tablet.md`
   - result:
     mobile shell navigation has repeatable mock-authenticated interaction
     proof, and the tablet route switcher now uses the shared icon+label rail
     instead of older text pills
   - proof:
     `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS;
     `npm run audit:ui-responsive` PASS with `route_count=14`,
     `viewport_count=3`, `screenshot_count=18`, `failed_count=0`; `npm run
     audit:ui-navigation` PASS with `status=ok`, `step_count=4`,
     `failed_count=0`; desktop/tablet/mobile Dashboard screenshots reviewed;
     cleanup confirmed no active `chrome_headless_shell` and no listener on
     `5173`; `git diff --check` passed with LF/CRLF warnings only
   - residual:
     Browser plugin remains unavailable in this local runtime because of
     missing kernel assets, but the route-smoke Playwright proof now covers the
     interaction gap
   - next smallest slice:
     continue route-local layout passes for Personality, Settings, Tools, and
     deeper Chat v5 convergence

3. Continue from the Personality mobile nav-clearance checkpoint:
   - task:
     `.codex/tasks/PRJ-1207-personality-mobile-nav-clearance.md`
   - result:
     mobile Personality now leaves route-local clearance between the portrait
     hero and Mind Layers timeline so the fixed tabbar does not cover timeline
     rows in the audited first-read
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; refreshed mobile Personality screenshot reviewed;
     cleanup confirmed no active `chrome_headless_shell` and no listener on
     `5173`; `git diff --check` passed with LF/CRLF warnings only
   - next smallest slice:
     continue Personality content hierarchy/side-panel polish, Settings/Tools
     responsive polish, or deeper Chat v5 layout/composer/transcript
     convergence

4. Continue from the Chat mobile first-read compression checkpoint:
   - task:
     `.codex/tasks/PRJ-1206-chat-mobile-first-read-compression.md`
   - result:
     mobile Chat context cards now use a horizontal rail, so conversation and
     composer content appear sooner while context remains accessible
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; refreshed mobile Chat screenshot reviewed; cleanup
     confirmed no active `chrome_headless_shell` and no listener on `5173`;
     `git diff --check` passed with LF/CRLF warnings only
   - next smallest slice:
     continue with deeper chat v5 desktop/tablet layout, transcript, and
     composer canonical polish or move to personality route-local polish

5. Continue from the Chat brand-copy alignment checkpoint:
   - task:
     `.codex/tasks/PRJ-1205-chat-brand-copy-alignment.md`
   - result:
     chat assistant label, composer safety note, and shared sidebar quote
     signature now align with the Aviary product shell
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; refreshed desktop chat screenshot reviewed; cleanup
     confirmed no active `chrome_headless_shell` and no listener on `5173`;
     `git diff --check` passed with LF/CRLF warnings only
   - next smallest slice:
     continue with chat v5 layout/composer/transcript canonical polish or
     personality route-local polish

6. Continue from the dashboard canonical content-rhythm checkpoint:
   - task:
     `.codex/tasks/PRJ-1204-dashboard-canonical-content-rhythm.md`
   - result:
     dashboard first-read hierarchy is calmer: desktop greeting is less
     cramped, guidance rows preserve readable copy with aligned actions, and
     recent activity rows now have visual tokens
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; refreshed desktop dashboard screenshot reviewed;
     cleanup confirmed no active `chrome_headless_shell` and no listener on
     `5173`; `git diff --check` passed with LF/CRLF warnings only
   - next smallest slice:
     continue route-local web polish with chat canonical convergence or a
     deeper final dashboard tableau pass before moving to personality

7. Continue from the dashboard CTA navigation checkpoint:
   - task:
     `.codex/tasks/PRJ-1203-dashboard-cta-navigation-polish.md`
   - result:
     dashboard action controls now route to existing product surfaces rather
     than behaving like decorative buttons
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; Playwright fallback clicked 10 dashboard CTAs and
     verified `/chat`, `/goals`, `/reflections`, `/memory`, and `/insights`;
     cleanup confirmed no active `chrome_headless_shell` and no listener on
     `5173`; `git diff --check` passed with LF/CRLF warnings only
   - next smallest slice:
     continue dashboard content canonical convergence against
     `docs/ux/assets/aion-dashboard-canonical-reference-v2.png` and
     `docs/ux/assets/aviary-dashboard-hero-canonical-reference-v4.png`

8. Continue from the authenticated shared-shell polish checkpoint:
   - task:
     `.codex/tasks/PRJ-1202-authenticated-shell-mobile-polish.md`
   - result:
     logged-in mobile/tablet chrome no longer shows technical build copy in
     the first viewport, and the fixed mobile tabbar now uses calmer Aviary
     material styling with a teal active state
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; cleanup confirmed no active `chrome_headless_shell`
     and no listener on `5173`; `git diff --check` passed with LF/CRLF
     warnings only
   - next smallest slice:
     start dashboard content canonical convergence against
     `docs/ux/assets/aion-dashboard-canonical-reference-v2.png` and
     `docs/ux/assets/aviary-dashboard-hero-canonical-reference-v4.png`

9. Continue from the public Home canonical polish checkpoint:
   - task:
     `.codex/tasks/PRJ-1201-public-home-canonical-polish.md`
   - result:
     Home now reads more like a full-width canonical landing surface; the
     presentation-only tag and nested-window framing are gone, public nav uses
     real anchors, auth placeholders are localized, and the visible wordmark is
     aligned with Aviary
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; Playwright fallback browser proof verified
     CTA -> register modal, localized placeholders, nav hrefs, and
     `unnamedButtons=0`
   - next smallest slice:
     decide whether to continue public landing parity with richer proof/social
     rhythm and section depth, or move to the authenticated shell/dashboard
     canonical convergence lane

10. Continue from the active web responsive breakpoint scope:
   - task:
     `.codex/tasks/PRJ-1200-rescope-to-web-responsive-breakpoints.md`
   - result:
     current UI scope is web across mobile, tablet, and desktop breakpoints;
     native app proof is deferred unless explicitly reactivated
   - proof:
     architecture dashboard refresh returned `DEFERRED:4`, `READY:11`,
     selected-scope readiness `11/11`; `npm run build` and
     `npm run audit:ui-responsive` passed with `route_count=14`,
     `viewport_count=3`, `screenshot_count=18`, and `failed_count=0`
   - next smallest slice:
     inspect or polish the web screenshots only from explicit visual feedback;
     otherwise keep `npm run audit:ui-responsive` as the active UI gate

11. Preserve the hardened native mobile proof doctor as deferred evidence:
   - task:
     `.codex/tasks/PRJ-1199-harden-mobile-device-proof-doctor.md`
   - result:
     `npm run doctor:ui-mobile-device` now reports Android SDK env checks,
     default SDK path existence, checked tool candidates, proof readiness, and
     concrete next actions
   - current blocker:
     local native proof remains blocked because `adb`, `emulator`,
     `ANDROID_HOME`, `ANDROID_SDK_ROOT`, and the default Windows Android SDK
     path are unavailable
   - next smallest slice:
     do not pursue native proof unless native app scope is reactivated

12. Continue from the cleaned tools overview baseline:
   - task:
     `.codex/tasks/PRJ-1197-remove-tools-roadmap-placeholders.md`
   - result:
     `/app/tools/overview` no longer lists future-only Trello or Nest
     placeholder entries; active tools are limited to implemented
     runtime/API/configuration contracts
   - proof:
     focused tools-overview API pack `3 passed, 129 deselected`; web
     TypeScript project build passed; production-code placeholder scan found
     no remaining `planned_placeholder` active-path matches
   - next smallest slice:
     keep external provider activation under `ARCH-CONNECTORS-001` and only
     add future providers after their bounded runtime contracts exist

13. Keep the refreshed architecture dashboard baseline current:
   - task:
     `.codex/tasks/PRJ-1198-refresh-mobile-architecture-dashboard-truth.md`
   - result:
     generated architecture dashboard now treats `ARCH-MOBILE-001` as
     `IMPLEMENTED_NOT_VERIFIED` instead of an untouched deferred future
     scaffold
   - proof:
     audit/dashboard refresh wrote `DEFERRED:3`,
     `IMPLEMENTED_NOT_VERIFIED:1`, `READY:11`; selected-scope readiness is
     `11/12`; generator scripts compile
   - next smallest slice:
     keep `ARCH-MOBILE-001` deferred while current UI scope remains web
     breakpoints

14. Continue from the verified runtime-layer baseline:
   - task:
     `.codex/tasks/PRJ-1195-runtime-layer-audit-and-polish-perception-fix.md`
   - audit:
     `docs/operations/aion-runtime-layer-audit-2026-05-13.md`
   - proof:
     focused pack `4 passed, 129 deselected`; full backend pytest
     `1093 passed`
   - next smallest slice:
     move to native mobile device proof or external provider activation.

15. Continue from the repaired production DB baseline:
   - latest memory task:
     `.codex/tasks/PRJ-1194-topic-scoped-memory-summary-buckets.md`
   - current verified baseline:
     Coolify production runs runtime memory with `RECENT_MEMORY_LIMIT=6`,
     `SEMANTIC_MEMORY_TOP_K=5`, OpenAI `text-embedding-3-small`, and pgvector
     dimensions `1536`
   - local code baseline:
     runtime query embeddings use the configured provider path, foreground
     vector retrieval includes `episodic`, and vector-matched episodes outside
     the recent temporal window enter the context bundle; PostgreSQL semantic
     vector ranking uses native pgvector distance ordering; vector relevance
     now survives context selection even when lexical overlap is absent;
     optional `relation` vector hits can rehydrate to revalidated relation
     records and merge into runtime relation state when `relation` is enabled;
     repeated recent memory topics now consolidate into semantic
     topic-scoped `memory_topic_summary` conclusions that are injected into
     context as long-term memory summaries
   - production proof:
     post-maintenance two-turn memory scenario answered `Roki`, persisted two
     episodes, and wrote two 1536-dimensional semantic embeddings; PRJ-1189
     non-temporal semantic proof on commit `d4d2911` answered `Roki` after
     15 filler episodes and retrieved original episode `id=4`; PRJ-1192
     production commit `f369556` enabled optional `relation` vector source,
     returned `VECTOR_RELATION_HITS 1` in a controlled repository proof, and
     passed release smoke with `release_ready=true`; PRJ-1194 production
     commit `c11377c` created separate `topic:dog` and `topic:deployment`
     long-term memory buckets, injected both into context, and cleaned
     synthetic rows to zero
   - next smallest slice:
     memory quality is verified for the current release path; plan an
     ANN/vector-index migration only if retrieval volume makes query latency
     require it

7. Native app proof parking lot:
   - branch: `codex/v15-mobile-ui-deploy-commits`
   - remote: `origin/codex/v15-mobile-ui-deploy-commits`
   - GitHub PR:
     `https://github.com/Wroblewski-Patryk/Aviary/pull/1`
   - production merge commit:
     `43837bb183c8975845b99b65a03cea5ccf4903a0`
   - PR creation URL:
     `https://github.com/Wroblewski-Patryk/Aviary/pull/new/codex/v15-mobile-ui-deploy-commits`
   - promotion handoff:
     `docs/operations/v15-mobile-ui-pr-and-production-promotion-handoff-2026-05-12.md`
   - local preview is intentionally stopped after validation cleanup; restart
     it with `Push-Location .\mobile; npm run deploy:ui-mobile-local` when
     another preview proof is needed
   - production is green for the merge commit and final cleanup commit;
     release smoke passed with runtime and web shell revisions matching
     `07b3b3e5fe3bd37439dd1cafbdc7fb15c4ef3a7b`
   - local conflict posture: `git merge-tree` showed no conflict output
     against `origin/main`
   - next smallest slice: deferred unless native app scope is reactivated

8. Native app groundwork archive:
   - plan: `docs/planning/v1.5-mobile-ui-plan.md`
   - latest task: `.codex/tasks/PRJ-1182-v15-mobile-device-proof-doctor.md`
   - promotion handoff:
     `docs/operations/v15-mobile-ui-pr-and-production-promotion-handoff-2026-05-12.md`
   - handoff: `docs/operations/v15-mobile-ui-local-preview-handoff-2026-05-12.md`
   - evidence:
     `.codex/artifacts/prj1158-mobile-native-shell/mobile-shell-390x1200-v2.png`
     `.codex/artifacts/prj1159-mobile-chat-route/mobile-chat-390x1200-v2.png`,
     `.codex/artifacts/prj1160-mobile-support-routes/`,
     `.codex/artifacts/prj1161-mobile-personality-route/`,
     `.codex/artifacts/prj1162-mobile-route-rail/`,
     `.codex/artifacts/prj1163-mobile-home-route-rail/`,
     and `.codex/artifacts/prj1164-mobile-ui-audit/report.json`
   - reusable validation:
     `Push-Location .\mobile; npm run audit:ui-mobile; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
     now expects `route_count=5`, `viewport_count=2`, `screenshot_count=10`,
     `action_proof_count=3`, `state_proof_count=4`, and `failed_count=0`
   - deployed preview validation:
     `Push-Location .\mobile; npm run smoke:ui-mobile-preview; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
     now expects `preview_health.ok=true`, `route_count=5`,
     `viewport_count=2`, `screenshot_count=10`, and `failed_count=0`
   - next smallest slice: capture Expo Go/simulator proof when Android tooling
     or a device is available.
   - local preview:
     stopped after validation cleanup; use `npm run deploy:ui-mobile-local`
     to restart it on `http://127.0.0.1:8093`
   - local deploy:
     `Push-Location .\mobile; npm run deploy:ui-mobile-local`
   - git hygiene:
     generated preview/cache/log artifacts are ignored by `.gitignore`
   - native proof readiness:
     `Push-Location .\mobile; npm run doctor:ui-mobile-device; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
     currently reports `status=blocked` because `adb` and `emulator` are
     unavailable
   - pushed branch:
     `origin/codex/v15-mobile-ui-deploy-commits`
   - PR creation URL:
     `https://github.com/Wroblewski-Patryk/Aviary/pull/new/codex/v15-mobile-ui-deploy-commits`

6. Preserve the completed `v1.1` web UI responsive quality baseline:
   - plan: `docs/planning/v1.1-web-ui-responsive-plan.md`
   - handoff task: `.codex/tasks/PRJ-1157-v11-web-ui-responsive-handoff.md`
   - evidence: `.codex/artifacts/prj1150-v11-ui-responsive-audit/report.json`
   `PRJ-1151` has closed dashboard mobile first-read compression and
   `PRJ-1152` has closed personality mobile balance, and `PRJ-1153` has closed
   tools tablet readability. `PRJ-1154` has closed tools mobile density.
   `PRJ-1155` has closed settings mobile density. `PRJ-1156` has closed
   dashboard lower mobile ranking. `PRJ-1157` has closed the v1.1 web
   responsive handoff. Next smallest slice: plan `v1.5` mobile from these
   learnings or start a new narrow UI polish item from explicit feedback.

7. Keep `npm run audit:ui-responsive` in the web validation set for shell,
   route layout, navigation, and responsive UI changes.

## Previous Architecture Queue

1. Select the next smallest stability or architecture-alignment slice from the
   generated project status dashboard. `PRJ-933` is done and aligned the
   architecture radar with the current v1 release boundary:
   - `docs/operations/project-status-dashboard.md`
   - `docs/operations/project-status-dashboard.json`
   Current phase is `architecture complete for selected scope with deferred
   extensions`. Selected-scope readiness is `11/11` rows (`100.0%`). There is
   no selected-scope blocker in the generated radar.

2. Keep the architecture implementation audit as the source matrix behind the
   dashboard:
   - `docs/operations/architecture-implementation-map-2026-05-10.csv`
   - `docs/operations/architecture-implementation-audit-2026-05-10.md`

## NEXT

1. Preserve the selected-scope architecture radar. Do not reopen deferred
   extension rows unless their trigger is present:
   - provider credentials and expanded organizer scope for `ARCH-CONNECTORS-001`
   - expanded proactive launch scope for `ARCH-PROACTIVE-001`
   - a newly selected release candidate for `ARCH-DEPLOY-AUTO-001`
   - explicit mobile product/release scope for `ARCH-MOBILE-001`
2. Use `docs/operations/v1-selected-scope-handoff-2026-05-11.md` as the
   concise handoff for the current achieved selected-scope posture.
2. Keep full backend pytest in the validation set after backend contract or
   action-loop changes that alter skill/tool metadata.
3. Keep the full web command pack in the validation set for route-shell,
   navigation, or authenticated-shell changes:
   `tsc -> vite build -> npm run smoke:routes`.
4. Preserve native exit codes in PowerShell command packs with
   `$exit=$LASTEXITCODE; Pop-Location; exit $exit`; `PRJ-930` proved
   `Push-Location; npm ...; Pop-Location` can mask a failed smoke.
5. For Windows sandbox `PermissionError` on pytest basetemp creation, record
   the sandboxed failure and rerun the same gate outside sandbox before
   treating it as an application regression.
6. Refresh the architecture implementation map after every meaningful
   architecture/evidence slice.
7. Refresh `docs/operations/project-status-dashboard.md` and
   `docs/operations/project-status-dashboard.json` after refreshing the map.

## LATER

1. Consider broader bounded action-loop extensions only after a concrete
   evidence-backed need appears.
2. Create a mobile implementation scope decision before counting mobile toward
   architecture completion.

## Selection Rules

- Pick one bounded mission objective for each autonomous iteration; use small
  checkpoint tasks inside that mission when useful.
- Prefer tasks that reduce blocker risk, regression risk, or unclear source of
  truth.
- Do not start new feature work when a P0/P1 regression or release blocker is
  unresolved.
- Keep this file synchronized with `.codex/context/TASK_BOARD.md` and
  `docs/planning/mvp-next-commits.md`.

