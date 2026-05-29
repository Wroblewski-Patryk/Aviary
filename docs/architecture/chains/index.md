# Function Chains

Generated: 2026-05-30

## App chat message execution chain

- ID: `CHAIN-APP-CHAT-MESSAGE`
- feature: [[feat-app-chat|FEAT-APP-CHAT]]
- status: `verified`
- confidence: `high`
- risk: `high`
- trigger: [[ui-chat-composer|UI-CHAT-COMPOSER]]
- last verified: `2026-05-24`

Execution chain:

[[ui-chat-composer|UI-CHAT-COMPOSER]] -> [[api-app-chat-message|API-APP-CHAT-MESSAGE]] -> [[event-app-chat-turn|EVENT-APP-CHAT-TURN]] -> [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]] -> [[model-aion-memory|MODEL-AION-MEMORY]] -> [[service-delivery-router|SERVICE-DELIVERY-ROUTER]] -> [[test-chat-transcript|TEST-CHAT-TRANSCRIPT]] -> [[doc-pipeline-app-chat|DOC-PIPELINE-APP-CHAT]]

Evidence:

- implementation: PRJ-1265 and backend/app/api/routes.py
- test: npm run test:chat-transcript and backend/tests/test_api_routes.py
- behavior: PRJ-1265 smoke route_count=14 and chat transcript PASS
- connection: relations REL-APPCHAT-001..010
- documentation: DOC-PIPELINE-APP-CHAT
- missing links: None

Current chain covers text plus serialized attachment context under existing API contract; native binary upload remains future backend scope outside this verified chain.

## Chat cognitive belt context-strip chain

- ID: `CHAIN-CHAT-COGNITIVE-BELT`
- feature: [[feat-app-chat|FEAT-APP-CHAT]]
- status: `verified`
- confidence: `medium`
- risk: `medium`
- trigger: [[ui-chat-cognitive-belt|UI-CHAT-COGNITIVE-BELT]]
- last verified: `2026-05-24`

Execution chain:

[[ui-chat-cognitive-belt|UI-CHAT-COGNITIVE-BELT]] -> [[comp-web-app|COMP-WEB-APP]] -> [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]] -> [[test-chat-transcript|TEST-CHAT-TRANSCRIPT]] -> [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]]

Evidence:

- implementation: web/src/components/chat.tsx and web/src/App.tsx
- test: web/scripts/route-smoke.mjs and web/scripts/chat-transcript-characterization.mjs
- behavior: Route smoke and transcript characterization prove rendered cognitive context strip presence within authenticated chat flow
- connection: REL-APPCHAT-011..013
- documentation: DOC-FRONTEND-ROUTE-MAP
- missing links: None

Research support remains design rationale while route/transcript tests provide local UI behavior proof.

## Web shell route proof chain

- ID: `CHAIN-WEB-ROUTE-SMOKE`
- feature: [[feat-web-shell|FEAT-WEB-SHELL]]
- status: `verified`
- confidence: `high`
- risk: `medium`
- trigger: [[comp-web-app|COMP-WEB-APP]]
- last verified: `2026-05-24`

Execution chain:

[[comp-web-app|COMP-WEB-APP]] -> [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]] -> [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]]

Evidence:

- implementation: web/src/App.tsx and route manifest
- test: npm run smoke:routes
- behavior: npm run smoke:routes route_count=14 status=ok
- connection: REL-WEB-001..006
- documentation: DOC-FRONTEND-ROUTE-MAP
- missing links: None

Route smoke is the broad route proof before deeper UX screenshot gates.

## Profile settings execution chain

- ID: `CHAIN-PROFILE-SETTINGS`
- feature: [[feat-profile-settings|FEAT-PROFILE-SETTINGS]]
- status: `verified`
- confidence: `high`
- risk: `medium`
- trigger: [[page-settings|PAGE-SETTINGS]]
- last verified: `2026-05-24`

Execution chain:

[[page-settings|PAGE-SETTINGS]] -> [[comp-web-app|COMP-WEB-APP]] -> [[api-app-me|API-APP-ME]] -> [[model-aion-profile|MODEL-AION-PROFILE]] -> [[test-preferences|TEST-PREFERENCES]] -> [[doc-data-reference|DOC-DATA-REFERENCE]]

Evidence:

- implementation: web/src/App.tsx and backend/app/api/routes.py
- test: backend/tests/test_preferences.py and backend/tests/test_api_routes.py
- behavior: PRJ-1279 focused backend settings proof plus web route smoke
- connection: REL-PROFILE-001..003 and REL-WEB-005
- documentation: DOC-API-REFERENCE and DOC-DATA-REFERENCE
- missing links: None

Focused profile/settings chain refreshed with backend API/preference tests web build and route smoke proof.

## App auth session execution chain

- ID: `CHAIN-APP-AUTH`
- feature: [[feat-profile-settings|FEAT-PROFILE-SETTINGS]]
- status: `verified`
- confidence: `high`
- risk: `high`
- trigger: [[comp-web-app|COMP-WEB-APP]]
- last verified: `2026-05-24`

Execution chain:

[[comp-web-app|COMP-WEB-APP]] -> [[api-app-auth|API-APP-AUTH]] -> [[model-aion-profile|MODEL-AION-PROFILE]] -> [[test-api-routes|TEST-API-ROUTES]] -> [[doc-api-reference|DOC-API-REFERENCE]]

Evidence:

- implementation: web/src/lib/api.ts and backend/app/api/routes.py
- test: backend/tests/test_api_routes.py auth session tests
- behavior: Focused pytest for register session requirement login logout and me roundtrip
- connection: REL-AUTH-001..004
- documentation: DOC-API-REFERENCE
- missing links: None

Auth chain maps app shell authentication through API profile/session persistence tests and docs without changing auth runtime behavior.

## Data model schema proof chain

- ID: `CHAIN-DATA-MODEL-SCHEMA`
- feature: [[feat-data-model|FEAT-DATA-MODEL]]
- status: `verified`
- confidence: `high`
- risk: `high`
- trigger: [[feat-data-model|FEAT-DATA-MODEL]]
- last verified: `2026-05-24`

Execution chain:

[[feat-data-model|FEAT-DATA-MODEL]] -> [[model-aion-memory|MODEL-AION-MEMORY]] -> [[model-aion-profile|MODEL-AION-PROFILE]] -> [[test-schema-baseline|TEST-SCHEMA-BASELINE]] -> [[doc-data-reference|DOC-DATA-REFERENCE]]

Evidence:

- implementation: backend/app/memory/models.py and backend/migrations/versions
- test: backend/tests/test_schema_baseline.py
- behavior: Schema baseline pytest verifies expected tables named unique constraints payload column and Alembic head parity
- connection: REL-DATA-001..004
- documentation: DOC-DATA-REFERENCE
- missing links: None

Data model chain maps core memory/profile/auth schema ownership through schema baseline tests and data reference docs without changing schema behavior.

## Tools overview execution chain

- ID: `CHAIN-TOOLS-OVERVIEW`
- feature: [[feat-tools|FEAT-TOOLS]]
- status: `verified`
- confidence: `high`
- risk: `medium`
- trigger: [[page-tools|PAGE-TOOLS]]
- last verified: `2026-05-24`

Execution chain:

[[page-tools|PAGE-TOOLS]] -> [[api-tools-overview|API-TOOLS-OVERVIEW]] -> [[model-aion-profile|MODEL-AION-PROFILE]] -> [[test-connector-policy|TEST-CONNECTOR-POLICY]] -> [[doc-tools-pipeline|DOC-TOOLS-PIPELINE]]

Evidence:

- implementation: web/src/App.tsx and backend/app/api/routes.py
- test: backend/tests/test_connector_policy.py and backend/tests/test_api_routes.py
- behavior: PRJ-1280 and PRJ-1293 focused backend tools proof plus Tools directory characterization and route smoke
- connection: REL-TOOLS-001..003
- documentation: DOC-TOOLS-PIPELINE
- missing links: None

Focused tools overview chain refreshed with backend API/connector policy tests web build route smoke and localized Tools directory characterization; live provider credential activation remains blocked/deferred outside local overview verification.

## Telegram link and delivery chain

- ID: `CHAIN-TELEGRAM-LINK-DELIVERY`
- feature: [[feat-telegram|FEAT-TELEGRAM]]
- status: `verified`
- confidence: `high`
- risk: `medium`
- trigger: [[page-tools|PAGE-TOOLS]]
- last verified: `2026-05-24`

Execution chain:

[[page-tools|PAGE-TOOLS]] -> [[api-tools-overview|API-TOOLS-OVERVIEW]] -> [[feat-telegram|FEAT-TELEGRAM]] -> [[service-delivery-router|SERVICE-DELIVERY-ROUTER]] -> [[test-api-routes|TEST-API-ROUTES]] -> [[test-delivery-router|TEST-DELIVERY-ROUTER]] -> [[doc-tools-pipeline|DOC-TOOLS-PIPELINE]]

Evidence:

- implementation: web/src/components/tools.tsx and backend/app/api/routes.py and backend/app/integrations/delivery_router.py
- test: backend/tests/test_api_routes.py and backend/tests/test_delivery_router.py
- behavior: PRJ-1297 focused Telegram link start confirm linked identity and delivery transport proof pack
- connection: REL-TELEGRAM-001..006
- documentation: DOC-TOOLS-PIPELINE
- missing links: None

Local Telegram linking and delivery transport path is verified with focused API and delivery router tests; live operator credential activation remains deployment-specific.

## Personality learned-state overview chain

- ID: `CHAIN-PERSONALITY-OVERVIEW`
- feature: [[feat-learned-state|FEAT-LEARNED-STATE]]
- status: `verified`
- confidence: `high`
- risk: `medium`
- trigger: [[page-personality|PAGE-PERSONALITY]]
- last verified: `2026-05-24`

Execution chain:

[[page-personality|PAGE-PERSONALITY]] -> [[api-personality-overview|API-PERSONALITY-OVERVIEW]] -> [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]] -> [[model-aion-memory|MODEL-AION-MEMORY]] -> [[test-api-routes|TEST-API-ROUTES]] -> [[doc-memory-system|DOC-MEMORY-SYSTEM]]

Evidence:

- implementation: web/src/App.tsx and backend/app/api/routes.py
- test: backend/tests/test_api_routes.py and backend/tests/test_memory_repository.py
- behavior: PRJ-1281 focused personality API memory repository web build and route smoke proof
- connection: REL-PERSONALITY-001..002 and REL-WEB-003
- documentation: DOC-MEMORY-SYSTEM
- missing links: None

Focused personality overview chain refreshed with backend API test memory repository tests web build and route smoke proof.

## General event ingress runtime chain

- ID: `CHAIN-EVENT-INGRESS`
- feature: [[feat-event-ingress|FEAT-EVENT-INGRESS]]
- status: `verified`
- confidence: `high`
- risk: `high`
- trigger: [[api-event-ingress|API-EVENT-INGRESS]]
- last verified: `2026-05-24`

Execution chain:

[[feat-event-ingress|FEAT-EVENT-INGRESS]] -> [[api-event-ingress|API-EVENT-INGRESS]] -> [[event-app-chat-turn|EVENT-APP-CHAT-TURN]] -> [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]] -> [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> [[feat-memory-flow|FEAT-MEMORY-FLOW]] -> [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]] -> [[model-aion-memory|MODEL-AION-MEMORY]] -> [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]] -> [[doc-runtime-flow|DOC-RUNTIME-FLOW]]

Evidence:

- implementation: backend/app/api/routes.py and backend/app/core/runtime.py
- test: backend/tests/test_runtime_pipeline.py
- behavior: Module ledger AVIARY-COGNITIVE-RUNTIME-001 verified
- connection: REL-EVENT-001 REL-EVENT-002 and REL-RUNTIME-001..005
- documentation: DOC-RUNTIME-FLOW
- missing links: None

Canonical AION event path with feature anchors for event ingress foreground runtime and memory flow.

## Architecture graph evidence generation chain

- ID: `CHAIN-ARCH-GRAPH-WORKFLOW`
- feature: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]
- status: `verified`
- confidence: `high`
- risk: `medium`
- trigger: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- last verified: `2026-05-24`

Execution chain:

[[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]] -> [[workflow-research-evidence|WORKFLOW-RESEARCH-EVIDENCE]] -> [[workflow-arch-graph-ci|WORKFLOW-ARCH-GRAPH-CI]] -> [[script-generate-arch-graph|SCRIPT-GENERATE-ARCH-GRAPH]] -> [[script-query-arch-graph|SCRIPT-QUERY-ARCH-GRAPH]] -> [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]] -> [[test-arch-graph-query|TEST-ARCH-GRAPH-QUERY]] -> [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]

Evidence:

- implementation: backend/scripts/generate_architecture_graph.py
- test: Fast graph pytest and heavy graph pytest
- behavior: Generated nodes/json/mermaid/status/evidence/research artifacts with all-node parity
- connection: REL-GRAPH-001..012 and REL-RESEARCH-001..003
- documentation: DOC-ARCH-GRAPH-SYSTEM
- missing links: None

Core nervous-system map generation workflow is verified; future work promotes individual features into richer curated evidence.
