# Active Mission Packet

Last updated: 2026-05-25

Use this file as the first operational router for `pracuj dalej`, `rob dalej`,
`kontynuuj`, `next`, and similar continuation nudges. Keep it short enough that
a fresh coordinator can choose the next checkpoint without rereading the whole
repository history.

## Current Mission

- Mission ID: PRJ-1324-mystic-clean-ui-orchestration-wave-1
- Status: VERIFIED
- Selected objective: raise authenticated shell visual quality to a mystical, clean, premium baseline without behavior drift.
- Why this mission now: user requested coordinated UI improvement as the active product priority.
- Validation summary:
  - wave 1 shell/chat visual polish landed in `web/src/index.css` (CSS-only)
  - wave 2 dashboard/personality hierarchy polish landed in `web/src/index.css` (CSS-only)
  - wave 3 typography and micro-interaction polish landed in `web/src/index.css` (CSS-only)
  - wave 4 dashboard parity-finishing polish landed in `web/src/index.css` (CSS-only)
  - wave 5 evidence gate generated responsive flagship screenshot packet and proof report:
    `docs/status/ui-parity-wave5-report.json`, `docs/status/ui-parity-wave5/*.png`
  - frontend validation PASS after each wave: `npm run build`, `npm run smoke:routes` (`status=ok`, `route_count=14`)
- Residual:
  - non-blocking audit residual: mobile dashboard flow-step off-canvas geometry appears in overflow preview despite `horizontalOverflow=false`
- Next recommended checkpoint:
  - optional wave 6: refine mobile dashboard flow-step geometry so overflow preview entries become zero

Historical note:
- Residual hosted-Actions entries in older "Previous Mission" sections below are
  archival context only and are non-blocking under `DEC-005`.

## Previous Mission

- Mission ID: PRJ-1312-release-evidence-index-live-proof-sync
- Status: VERIFIED
- Selected objective: sync canonical release index with latest production evidence capture output.
- Why this mission now: PRJ-1311 generated durable artifacts, but central release index needed explicit top-level refresh for operator truth.
- Validation summary:
  - updated `docs/operations/release-evidence-index.md` `Last updated` date
  - linked latest proof summary values from `docs/status/production-release-evidence-summary-20260524T172730Z.json`
- Residual:
  - hosted architecture-graph Actions artifact proof remains optional supplementary evidence under `DEC-005`
- Next recommended checkpoint:
  - capture first hosted graph artifact packet (fast + optional heavy) and attach it to CI evidence rows

## Previous Mission

- Mission ID: PRJ-1311-single-command-production-release-evidence-capture
- Status: VERIFIED
- Selected objective: convert production evidence capture into one deterministic command.
- Why this mission now: PRJ-1310 proved artifact flow manually; this checkpoint removes operator friction and preserves repeatability.
- Validation summary:
  - added `backend/scripts/run_production_release_evidence_capture.ps1`
  - production execution PASS with release-ready output and timestamped artifacts
  - runtime ops runbook updated with canonical one-command workflow
- Residual:
  - hosted architecture-graph Actions artifact proof remains optional supplementary evidence under `DEC-005`
- Next recommended checkpoint:
  - capture first hosted graph artifact packet (fast + optional heavy) and attach it to CI evidence rows

## Previous Mission

- Mission ID: PRJ-1310-production-incident-evidence-bundle-and-release-smoke-proof
- Status: VERIFIED
- Selected objective: produce durable production release evidence artifacts from live runtime.
- Why this mission now: after policy/runbook closure, evidence artifacts were still transient unless explicitly exported and stored.
- Release objective or product milestone advanced: production proof now includes incident-evidence bundle plus machine-readable smoke output in repository status space.
- Validation summary:
  - exported incident bundle directory under `docs/status`
  - executed release smoke against `https://aviary.luckysparrow.ch` with bundle verification
  - persisted smoke JSON at `docs/status/release-smoke-prj1310.json`
- Residual:
  - hosted graph artifact proof via Actions remains optional supplementary evidence under `DEC-005`
- Next recommended checkpoint:
  - execute hosted architecture-graph workflow (fast/heavy), download artifacts, verify with local artifact validators, and attach hosted evidence packet

## Previous Mission

- Mission ID: PRJ-1309-coolify-first-deployment-policy-and-team-context
- Status: VERIFIED
- Selected objective: persist user deployment constraints (Coolify-first, no paid GitHub extensions) and team-context recovery in durable project memory.
- Why this mission now: user provided explicit VPS/Coolify constraint and requested continuation until fully aligned.
- Release objective or product milestone advanced: operator runbooks now encode the real deployment authority and first-response troubleshooting sequence.
- Validation summary:
  - decision register updated with `DEC-004`
  - deployment guide includes explicit Coolify team-switch step
  - runtime ops runbook includes Coolify control plane + no-paid-extension policy
- Residual:
  - hosted live Coolify session actions require operator environment access and are not repo-automatable without runtime credentials workflow
- Next recommended checkpoint:
  - run a live deploy smoke against the Coolify-managed public domain and attach evidence bundle if runtime revision changed

## Previous Mission

- Mission ID: PRJ-1308-local-release-gate-report-automation
- Status: VERIFIED
- Selected objective: provide one-command local release gate with durable machine-readable report.
- Why this mission now: local and CI graph gates are stable; this checkpoint creates a standard local pre-push evidence packet.
- Release objective or product milestone advanced: local release-readiness proof for architecture graph now has a deterministic report output.
- Validation summary:
  - added `backend/scripts/run_architecture_graph_local_release_gate.py`
  - generated `docs/status/architecture-graph-local-release-gate.json` with `overall_status=PASSED`
  - graph+policy+verifier+packet suite remains green
  - local curated zero-gap audit remains green (`items=[]`)
- Residual:
  - hosted artifact publication proof remains optional supplementary evidence under `DEC-005`
- Next recommended checkpoint:
  - execute hosted workflow, download artifacts, and attach hosted proof to CI policy evidence rows

## Previous Mission

- Mission ID: PRJ-1302-graph-ci-gap-artifact-proofing
- Status: VERIFIED
- Selected objective: attach durable hosted evidence by publishing curated gap-audit JSON artifacts in graph CI.
- Why this mission now: zero-gap gate is enforced locally/CI; next closure step is making hosted proof extraction trivial for release/handoff.
- Release objective or product milestone advanced: graph CI now emits reusable audit artifacts for fast and heavy modes.
- Validation summary:
  - graph query/generator fast pytest PASS: `33 passed, 1 deselected`
  - local `query_architecture_graph.py --gaps --format json --fail-on-gaps` PASS with empty `items`
  - workflow now uploads `architecture-gaps-fast` and `architecture-gaps-heavy` artifacts
- Residual:
  - hosted artifact evidence pending next push/PR run
- Next recommended checkpoint:
  - run hosted workflow and store artifact-backed proof in CI evidence rows

## Previous Mission

- Mission ID: PRJ-1301-gap-audit-cli-fail-on-gaps-hardening
- Status: VERIFIED
- Selected objective: harden gap-audit CI gate by adding native CLI `--fail-on-gaps` exit behavior.
- Why this mission now: `PRJ-1300` established zero-gap gate policy; this checkpoint removes inline workflow parsing and makes enforcement reusable for local/CI automation.
- Release objective or product milestone advanced: architecture zero-gap gate is now implemented in the query CLI contract itself.
- Validation summary:
  - graph query/generator fast pytest PASS: `33 passed, 1 deselected`
  - local `query_architecture_graph.py --gaps --format json --fail-on-gaps` PASS with empty `items`
  - workflow now calls native CLI gate directly
- Residual:
  - hosted Actions proof pending next push/PR run
- Next recommended checkpoint:
  - capture first hosted CI run with native `--fail-on-gaps` evidence

## Previous Mission

- Mission ID: PRJ-1300-architecture-gap-zero-gate-in-ci
- Status: VERIFIED
- Selected objective: enforce curated graph `--gaps` zero-state as an automatic CI gate.
- Why this mission now: `PRJ-1299` reached local zero-gap state; next step is preventing regression at merge/release boundaries.
- Release objective or product milestone advanced: architecture graph proof posture now has an automated fail gate in CI.
- Validation summary:
  - local `query_architecture_graph.py --gaps --format json` reports empty `items`
  - graph query/generator fast pytest PASS: `31 passed, 1 deselected`
  - workflow updated to fail on non-empty curated gap JSON
- Residual:
  - hosted Actions proof pending next push/PR run
- Next recommended checkpoint:
  - capture first hosted workflow run evidence and record it under `WORKFLOW-ARCH-GRAPH-CI`

## Previous Mission

- Mission ID: PRJ-1299-global-gap-audit-zero-state-closure
- Status: VERIFIED
- Selected objective: close remaining curated graph proof gaps and reach zero-gap audit state.
- Why this mission now: after `PRJ-1298` and follow-up registry/test updates, a final sequential audit was required to confirm true global gap closure.
- Release objective or product milestone advanced: architecture graph curated-node proof posture reached zero-gap state.
- Validation summary:
  - inventory generation PASS with `auto_nodes=5300`, `auto_relations=3980`
  - graph generation PASS with `nodes=5361`, `relations=4050`, `chains=11`, `evidence=65`
  - `query_architecture_graph.py --gaps --limit 20` reports `no gaps detected`
- Residual:
  - local graph and evidence posture is complete for curated nodes; production/runtime/provider smoke remains separate scope
- Next recommended checkpoint:
  - keep zero-gap posture in CI and treat new `--gaps` rows as mandatory closure tasks before feature sign-off

## Previous Mission

- Mission ID: PRJ-1298-telegram-feature-proof-gap-closure
- Status: VERIFIED
- Selected objective: close graph proof gaps for `FEAT-TELEGRAM`.
- Why this mission now: `FEAT-TELEGRAM` was the top curated medium-risk gap
  with implemented/connection-evidence posture and no direct chain/evidence.
- Release objective or product milestone advanced: verified Telegram link and
  delivery chain in the architecture graph.
- Validation summary:
  - focused Telegram proof pack PASS: `7 passed in 2.20s`
  - combined proof plus graph tests PASS: `36 passed, 1 deselected`
  - inventory plus graph generation PASS with `auto_nodes=5297`,
    `auto_relations=3978`, merged `nodes=5358`, `relations=4048`,
    `chains=10`, `evidence=54`
  - `FEAT-TELEGRAM` query reports `Gaps: none`
- Residual:
  - local link/delivery proof only; production Telegram credential/webhook
    smoke remains deployment-specific
- Next recommended checkpoint:
  - close `DOC-FRONTEND-ROUTE-MAP`, `DOC-TOOLS-PIPELINE`, `PAGE-DASHBOARD`,
    `PAGE-TOOLS`, `SERVICE-DELIVERY-ROUTER`, or test proof rows

## Previous Mission

- Mission ID: PRJ-1297-web-app-shell-direct-proof-gap-closure
- Status: VERIFIED
- Selected objective: close direct evidence gap for graph node
  `COMP-WEB-APP`.
- Why this mission now: after `PRJ-1296`, the next medium-risk audit item was
  the verified web shell component without direct evidence.
- Release objective or product milestone advanced: graph proof density for the
  frontend shell backbone used by Dashboard/Personality/Tools/Settings routes.
- Validation summary:
  - web build PASS
  - web route smoke PASS (`route_count=14`, `status=ok`)
  - inventory plus graph generation PASS with `auto_nodes=5295`,
    `auto_relations=3977`, merged `nodes=5356`, `relations=4041`,
    `chains=9`, `evidence=53`
  - graph/query pytest PASS: `28 passed, 1 deselected`
  - `COMP-WEB-APP` query reports `Gaps: none`
- Residual:
  - local shell proof only; screenshot parity and production smoke remain
    separate scopes
- Next recommended checkpoint:
  - close `FEAT-TELEGRAM` or docs/page/test/service medium-risk proof rows

## Previous Mission

- Mission ID: PRJ-1296-personality-overview-direct-proof-gap-closure
- Status: VERIFIED
- Selected objective: close direct evidence gaps for graph nodes
  `API-PERSONALITY-OVERVIEW` and `PAGE-PERSONALITY`.
- Why this mission now: after `PRJ-1295`, the Personality overview chain was
  verified, but its API/page nodes still appeared in the medium-risk gap audit
  because they lacked direct node-level evidence rows.
- Release objective or product milestone advanced: graph proof density for the
  Personality learned-state execution chain.
- First/next checkpoint: run focused API/repository and route proof, add
  evidence rows, regenerate graph artifacts, and confirm targeted nodes report
  no gaps.
- Stop conditions: this mission must not change API behavior, frontend UI,
  memory behavior, schema, auth/session behavior, or production deployment.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py::test_app_personality_overview_uses_authenticated_user tests/test_memory_repository.py::test_memory_repository_ignores_internal_rows_when_counting_unanswered_proactive_and_recent_activity tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; if ($exit -ne 0) { exit $exit }; Push-Location .\web; npm run smoke:routes; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1296 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator ran this serially because evidence rows, generated graph
    artifacts, and state updates are tightly coupled
- Implementation:
  - added direct evidence rows for `API-PERSONALITY-OVERVIEW` and
    `PAGE-PERSONALITY`
  - pinned no-gap behavior for both nodes in graph query pytest
  - regenerated inventory and graph artifacts after task/evidence edits
- Validation:
  - focused personality API/repository proof PASS: `2 passed in 3.04s`
  - web route smoke PASS: `route_count=14`, `status=ok`
  - inventory plus graph generation PASS with `auto_nodes=5294`,
    `auto_relations=3976`, merged `nodes=5355`, `relations=4040`,
    `chains=9`, `evidence=52`, `research_sources=21`, `theory_claims=9`
  - targeted node queries for both nodes report `Gaps: none`
  - personality proof plus graph/query pytest PASS:
    `29 passed, 1 deselected in 4.05s`
- Residual:
  - local API/repository and route-render proof only; production account
    memory smoke and screenshot parity remain separate scopes
- Next recommended checkpoint:
  - use the gap audit to select `FEAT-TELEGRAM`, `COMP-WEB-APP`,
    frontend route docs, tools docs, dashboard/tools page proof rows, or
    service delivery proof
- Artifacts:
  - `.codex/tasks/PRJ-1296-personality-overview-direct-proof-gap-closure.md`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1295-profile-settings-direct-proof-gap-closure
- Status: VERIFIED
- Selected objective: close direct evidence gaps for profile/settings graph
  nodes `API-APP-ME`, `MODEL-AION-PROFILE`, and `PAGE-SETTINGS`.
- Why this mission now: after `PRJ-1294`, these verified profile/settings
  nodes are among the top medium-risk graph gaps and share the existing
  verified `CHAIN-PROFILE-SETTINGS`.
- Release objective or product milestone advanced: graph proof density for the
  profile/settings execution chain.
- First/next checkpoint: run focused profile/settings proof, add evidence rows,
  regenerate graph artifacts, and confirm the targeted nodes report no gaps.
- Stop conditions: this mission must not change API behavior, schema,
  settings UI behavior, runtime preferences, auth/session behavior, or
  production deployment.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py::test_app_me_requires_authenticated_session tests/test_api_routes.py::test_app_patch_settings_updates_profile_preferences_and_display_name tests/test_api_routes.py::test_app_patch_settings_persists_proactive_opt_in_without_semantic_side_effects tests/test_schema_baseline.py::test_alembic_head_includes_ui_language_on_profile tests/test_preferences.py tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; if ($exit -ne 0) { exit $exit }; Push-Location .\web; npm run smoke:routes; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1295 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator is running this serially because profile evidence rows,
    generated graph artifacts, and state updates are tightly coupled
- Implementation:
  - added direct evidence rows for `API-APP-ME`, `MODEL-AION-PROFILE`, and
    `PAGE-SETTINGS`
  - pinned no-gap behavior for the three profile/settings nodes in graph query
    pytest
  - restored canonical `docs/` after detecting a copied/renamed
    `Aviary - docs/` vault and excluded that copy from auto-inventory scanning
- Validation:
  - focused profile/settings proof pack PASS: `9 passed in 5.25s`
  - inventory plus graph generation PASS with `auto_nodes=5292`,
    `auto_relations=3975`, merged `nodes=5353`, `relations=4039`,
    `chains=9`, `evidence=50`, `research_sources=21`,
    `theory_claims=9`
  - targeted node queries report `Gaps: none`
  - profile/settings plus graph/query pytest PASS:
    `35 passed, 1 deselected in 15.02s`
  - web route smoke PASS: `route_count=14`, `status=ok`
  - final fast graph pytest after docs restoration PASS:
    `26 passed, 1 deselected in 3.63s`
  - final `git diff --check` PASS with LF/CRLF warnings only
- Residual:
  - local profile/settings proof only; production account data smoke and
    deeper interactive settings form proof remain separate scopes; untracked
    duplicate `Aviary - docs/` remains present and is excluded from inventory
- Next recommended checkpoint:
  - use the gap audit to select `FEAT-TELEGRAM`,
    `API-PERSONALITY-OVERVIEW`, `COMP-WEB-APP`, or frontend/docs/page proof
    rows
- Artifacts:
  - `.codex/tasks/PRJ-1295-profile-settings-direct-proof-gap-closure.md`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1294-runtime-agent-stage-evidence-gap-closure
- Status: VERIFIED
- Selected objective: close direct evidence gaps for runtime agent-stage nodes:
  `AGENT-AFFECTIVE-ASSESSMENT`, `AGENT-CONTEXT`, `AGENT-MOTIVATION`,
  `AGENT-PERCEPTION`, `AGENT-PLANNING`, and `AGENT-ROLE`.
- Why this mission now: after `PRJ-1293`, these verified runtime agent nodes
  are the top repeated medium-risk graph gaps and can be closed with existing
  focused agent test suites.
- Release objective or product milestone advanced: graph proof density for the
  AION runtime stage agents.
- First/next checkpoint: run the focused agent proof pack, add evidence rows,
  regenerate graph artifacts, and confirm targeted nodes report no gaps.
- Stop conditions: this mission must not change runtime behavior, agent logic,
  AI provider behavior, prompts, action authority, or production deployment.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_perception_assessor.py tests/test_context_agent.py tests/test_planning_agent.py tests/test_role_agent.py tests/test_motivation_engine.py tests/test_affective_assessor.py tests/test_affective_contract.py tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1294 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator is running this serially because evidence rows and generated
    graph artifacts are tightly coupled
- Implementation:
  - added direct evidence rows for perception, context, planning, role,
    motivation, and affective assessment runtime agent-stage nodes
  - pinned no-gap behavior for the six agent nodes in graph query pytest
- Validation:
  - focused agent proof pack PASS: `210 passed in 0.44s`
  - inventory plus graph generation PASS with `auto_nodes=5290`,
    `auto_relations=3974`, merged `nodes=5351`, `relations=4038`,
    `chains=9`, `evidence=47`, `research_sources=21`,
    `theory_claims=9`
  - sampled targeted node queries report `Gaps: none`
  - agent proof pack plus graph/query pytest PASS:
    `235 passed, 1 deselected in 3.82s`
- Residual:
  - this proves local stage contracts only; live AI provider behavior,
    production runtime smoke, and full backend regression remain separate
    scopes
- Next recommended checkpoint:
  - use the gap audit to select the next medium-risk node: `FEAT-TELEGRAM`,
    `API-APP-ME`, `API-PERSONALITY-OVERVIEW`, or frontend/doc/profile proof
    nodes
- Artifacts:
  - `.codex/tasks/PRJ-1294-runtime-agent-stage-evidence-gap-closure.md`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1293-curated-medium-risk-proof-cleanup
- Status: VERIFIED
- Selected objective: close the next small curated medium-risk graph gaps for
  `API-TOOLS-OVERVIEW`, `DOC-PIPELINE-APP-CHAT`, and
  `TEST-WEB-ROUTE-SMOKE` without changing runtime behavior.
- Why this mission now: after `PRJ-1292`, the gap audit has no high-risk rows;
  these are the smallest medium-risk proof gaps that can be closed with local
  evidence and graph metadata.
- Release objective or product milestone advanced: graph proof density for
  tools API, app chat documentation, and web route smoke infrastructure.
- First/next checkpoint: run focused local tools and route proof, add evidence
  rows and graph-query assertions, regenerate graph artifacts, and confirm the
  targeted nodes report no gaps.
- Stop conditions: this mission must not change web runtime UI, API behavior,
  connector policy, provider credentials, or production deployment.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py::test_app_tools_overview_exposes_grouped_backend_truth tests/test_api_routes.py::test_app_tools_overview_marks_provider_backed_integrations_ready_when_configured tests/test_api_routes.py::test_app_patch_tools_preferences_updates_requested_enablement_state tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; if ($exit -ne 0) { exit $exit }; Push-Location .\web; npm run smoke:routes; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1293 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator is running this serially because graph metadata, generated
    artifacts, and state updates are tightly coupled; subagent tooling exists
    but was not explicitly requested in the user prompt
- Implementation:
  - added direct evidence rows for `API-TOOLS-OVERVIEW`,
    `DOC-PIPELINE-APP-CHAT`, and `TEST-WEB-ROUTE-SMOKE`
  - updated `TEST-WEB-ROUTE-SMOKE` self-test metadata
  - clarified `CHAIN-TOOLS-OVERVIEW` so live provider credential activation
    remains residual external proof rather than a missing local overview link
  - pinned no-gap behavior for the three nodes in graph query pytest
- Validation:
  - focused tools API pytest PASS: `3 passed in 2.23s`
  - inventory plus graph generation PASS with `auto_nodes=5288`,
    `auto_relations=3973`, merged `nodes=5349`, `relations=4037`,
    `chains=9`, `evidence=41`, `research_sources=21`,
    `theory_claims=9`
  - targeted node queries for the three PRJ-1293 nodes report `Gaps: none`
  - focused tools plus graph/query pytest PASS:
    `27 passed, 1 deselected in 7.92s`
  - web route smoke PASS: `route_count=14`, `status=ok`
- Residual:
  - live provider credential activation, Telegram delivery, and agent-stage
    evidence remain separate follow-up graph missions
- Next recommended checkpoint:
  - rerun graph gap audit and choose Telegram, runtime agent-stage evidence,
    or `API-APP-ME` evidence as a separate mission
- Artifacts:
  - `.codex/tasks/PRJ-1293-curated-medium-risk-proof-cleanup.md`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1292-service-test-prompt-evidence-gap-closure
- Status: VERIFIED
- Selected objective: close the next service/test/prompt graph evidence gaps
  for `PROMPT-OPENAI-RUNTIME`, `SERVICE-MEMORY-REPOSITORY`,
  `SERVICE-RUNTIME-ORCHESTRATOR`, `TEST-API-ROUTES`,
  `TEST-MEMORY-REPOSITORY`, `TEST-RUNTIME-PIPELINE`, and
  `TEST-SCHEMA-BASELINE`.
- Why this mission now: after `PRJ-1291`, these verified curated nodes are the
  top missing-evidence rows in the graph audit.
- Release objective or product milestone advanced: graph proof density for
  core runtime, memory, prompt, and test infrastructure nodes.
- First/next checkpoint: run focused proof pack, add evidence rows, regenerate
  graph artifacts, and confirm targeted nodes report no gaps.
- Stop conditions: this mission does not change runtime, memory, prompt, API,
  schema, or test behavior.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_openai_prompting.py tests/test_response_budget_policy.py tests/test_openai_client.py::test_openai_client_generate_reply_uses_api_chat_response_budget tests/test_runtime_pipeline.py::test_runtime_pipeline_api_source tests/test_runtime_pipeline.py::test_runtime_pipeline_contract_smoke_pins_stage_and_action_boundary_invariants tests/test_memory_repository.py::test_memory_repository_persists_structured_episode_payload tests/test_memory_repository.py::test_memory_repository_projects_recent_chat_transcript_in_chronological_order tests/test_api_routes.py::test_event_endpoint_contract_smoke_pins_public_shape_and_debug_gate tests/test_schema_baseline.py::test_schema_baseline_tracks_structured_memory_payload_column tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1292 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator is running this serially because evidence rows, generated
    artifacts, and state updates are tightly coupled
- Implementation:
  - added evidence rows for OpenAI runtime prompting, runtime orchestrator,
    memory repository, API route tests, memory repository tests, runtime
    pipeline tests, and schema baseline tests
  - pinned service/test/prompt no-gap behavior in graph query pytest
- Validation:
  - focused proof pack PASS: `13 passed in 2.90s`
  - inventory plus graph generation PASS with `auto_nodes=5286`,
    `auto_relations=3972`, merged `nodes=5347`, `relations=4036`,
    `chains=9`, `evidence=38`, `research_sources=21`,
    `theory_claims=9`
  - targeted node queries for the seven service/test/prompt nodes report
    `Gaps: none`
  - service/test/prompt plus graph/query pytest PASS:
    `36 passed, 1 deselected in 6.05s`
- Residual:
  - local focused proof only; no live OpenAI provider, full backend suite, or
    production smoke claimed
- Next recommended checkpoint:
  - rerun graph gap audit and close the next curated proof gap in priority
    order
- Artifacts:
  - `.codex/tasks/PRJ-1292-service-test-prompt-evidence-gap-closure.md`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1291-runtime-memory-doc-feature-gap-closure
- Status: VERIFIED
- Selected objective: close the next documentation and feature-level graph
  gaps by adding explicit evidence for runtime/memory docs and by threading
  foreground runtime plus memory flow feature anchors into the event ingress
  chain.
- Why this mission now: after `PRJ-1290`, the gap audit top rows are
  `DOC-MEMORY-SYSTEM`, `DOC-RUNTIME-FLOW`, `FEAT-EVENT-INGRESS`,
  `FEAT-FOREGROUND-RUNTIME`, and `FEAT-MEMORY-FLOW`.
- Release objective or product milestone advanced: runtime/memory source of
  truth traceability in the architecture graph.
- First/next checkpoint: add evidence rows, update chain anchors, regenerate
  graph artifacts, and confirm these nodes report no gaps.
- Stop conditions: this mission does not change runtime behavior, memory
  behavior, docs content, or production smoke.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1291 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator is running this serially because graph chain semantics,
    evidence rows, generated artifacts, and state updates are tightly coupled
- Implementation:
  - added `EVID-EVENT-INGRESS-FEATURE-PROOF`
  - added `EVID-DOC-RUNTIME-FLOW`
  - added `EVID-DOC-MEMORY-SYSTEM`
  - updated `CHAIN-EVENT-INGRESS` with `FEAT-EVENT-INGRESS`,
    `FEAT-FOREGROUND-RUNTIME`, and `FEAT-MEMORY-FLOW` anchors
  - pinned runtime/memory docs and feature no-gap behavior in graph query
    pytest
- Validation:
  - inventory plus graph generation PASS with `auto_nodes=5284`,
    `auto_relations=3971`, merged `nodes=5345`, `relations=4035`,
    `chains=9`, `evidence=31`, `research_sources=21`,
    `theory_claims=9`
  - targeted node queries for `DOC-MEMORY-SYSTEM`, `DOC-RUNTIME-FLOW`,
    `FEAT-EVENT-INGRESS`, `FEAT-FOREGROUND-RUNTIME`, and
    `FEAT-MEMORY-FLOW` report `Gaps: none`
  - graph/query pytest PASS: `22 passed, 1 deselected in 4.62s`
- Residual:
  - graph/doc/feature evidence only; no runtime behavior, memory behavior, or
    production smoke changed
- Next recommended checkpoint:
  - rerun graph gap audit and close the next curated proof gap in priority
    order
- Artifacts:
  - `.codex/tasks/PRJ-1291-runtime-memory-doc-feature-gap-closure.md`
  - `docs/architecture/registry/chains.csv`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1290-app-chat-event-gap-closure
- Status: VERIFIED
- Selected objective: close the next high-risk curated graph gap by adding
  explicit evidence for `API-APP-CHAT-MESSAGE` and `EVENT-APP-CHAT-TURN`,
  while clarifying that native binary upload is future scope rather than a
  missing link in the current text/serialized-attachment chain.
- Why this mission now: after `PRJ-1289`, the gap audit points at app chat
  API/event nodes with missing evidence rows and a future-scope chain note.
- Release objective or product milestone advanced: app chat execution-chain
  proof quality in the architecture graph.
- First/next checkpoint: run focused app-chat API and transcript tests, add
  node-level evidence, clear the current chain missing-link field, regenerate
  graph artifacts, and confirm app-chat API/event nodes report no gaps.
- Stop conditions: this mission does not implement native binary/media upload,
  alter chat runtime behavior, change attachment transport, or claim
  production chat smoke.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py::test_app_chat_message_runs_runtime_under_authenticated_user tests/test_api_routes.py::test_app_chat_message_localizes_runtime_timestamp_from_profile_utc_offset tests/test_api_routes.py::test_app_chat_message_exposes_bounded_pending_connector_confirmation tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; if ($exit -eq 0) { Push-Location .\web; npm run test:chat-transcript; $exit=$LASTEXITCODE; Pop-Location }; exit $exit`.

## PRJ-1290 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator is running this serially because app-chat chain scope,
    evidence rows, generated graph artifacts, and state updates are tightly
    coupled
- Implementation:
  - added `EVID-APPCHAT-API-PROOF`
  - added `EVID-APPCHAT-EVENT-PROOF`
  - clarified `CHAIN-APP-CHAT-MESSAGE` missing links as `None` for the
    verified current scope, with native binary upload kept as future scope in
    notes
  - pinned app-chat API/event no-gap behavior in graph query pytest
- Validation:
  - focused app-chat API pytest PASS: `3 passed in 3.29s`
  - web chat transcript characterization PASS with `status=ok`,
    `appSourceCount=2`, `telegramSourceCount=2`
  - inventory plus graph generation PASS with `auto_nodes=5282`,
    `auto_relations=3970`, merged `nodes=5343`, `relations=4034`,
    `chains=9`, `evidence=28`, `research_sources=21`,
    `theory_claims=9`
  - app-chat plus graph/query pytest PASS:
    `25 passed, 1 deselected in 5.78s`
  - `query_architecture_graph.py --node API-APP-CHAT-MESSAGE --show-gaps`
    and `--node EVENT-APP-CHAT-TURN --show-gaps` report `Gaps: none`
  - top curated gap audit no longer lists `API-APP-CHAT-MESSAGE` or
    `EVENT-APP-CHAT-TURN`
- Residual:
  - local API/runtime/transcript proof only; native binary/media upload and
    production chat smoke remain separate future scopes
- Next recommended checkpoint:
  - after app-chat/event closure, close documentation evidence gaps for
    `DOC-MEMORY-SYSTEM` and `DOC-RUNTIME-FLOW`
- Artifacts:
  - `.codex/tasks/PRJ-1290-app-chat-event-gap-closure.md`
  - `docs/architecture/registry/chains.csv`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1289-event-ingress-api-gap-closure
- Status: VERIFIED
- Selected objective: close the next high-risk curated graph gap by adding
  explicit API evidence for `API-EVENT-INGRESS`.
- Why this mission now: after `PRJ-1288`, the gap audit no longer lists
  `MODEL-AION-MEMORY` and the highest remaining straightforward gap is
  `API-EVENT-INGRESS` with no evidence row.
- Release objective or product milestone advanced: runtime ingress
  traceability and proof quality in the architecture graph.
- First/next checkpoint: run focused event endpoint tests, add API evidence
  and relation, regenerate graph artifacts, and confirm
  `API-EVENT-INGRESS` reports no gaps.
- Stop conditions: this mission does not change event endpoint behavior,
  runtime orchestration, debug endpoint policy, Telegram ingress, or production
  event smoke.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py::test_event_endpoint_returns_public_response_and_normalizes_event tests/test_api_routes.py::test_event_endpoint_enforces_api_boundary_for_source_and_payload_shape tests/test_api_routes.py::test_event_endpoint_contract_smoke_pins_public_shape_and_debug_gate tests/test_runtime_pipeline.py::test_runtime_pipeline_api_source tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1289 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator is running this serially because event ingress evidence,
    generated graph artifacts, and state updates are tightly coupled
- Implementation:
  - added `REL-EVENT-002`
  - added `EVID-EVENT-INGRESS-API-PROOF`
  - pinned event ingress proof in graph generator/query pytest
- Validation:
  - focused event ingress pytest PASS: `4 passed in 28.36s`
  - inventory plus graph generation PASS with `auto_nodes=5280`,
    `auto_relations=3969`, merged `nodes=5341`, `relations=4033`,
    `chains=9`, `evidence=26`, `research_sources=21`,
    `theory_claims=9`
  - event ingress plus graph/query pytest PASS:
    `24 passed, 1 deselected in 6.66s`
  - `query_architecture_graph.py --node API-EVENT-INGRESS --show-gaps`
    reports `EVID-EVENT-INGRESS-API-PROOF` and `Gaps: none`
  - top curated gap audit no longer lists `API-EVENT-INGRESS`
- Residual:
  - local API/runtime contract proof only; production event ingress smoke and
    Telegram webhook proof remain separate runtime/release scopes
- Next recommended checkpoint:
  - after event ingress gap closure, rerun gap audit and choose between
    app-chat/event future-scope gap semantics or documentation evidence gaps
- Artifacts:
  - `.codex/tasks/PRJ-1289-event-ingress-api-gap-closure.md`
  - `docs/architecture/registry/relations.csv`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1288-aion-memory-model-gap-closure
- Status: VERIFIED
- Selected objective: close the next high-risk curated gap from the graph
  audit by adding explicit evidence for `MODEL-AION-MEMORY` and refining gap
  attribution so feature-level missing links do not over-report on model nodes.
- Why this mission now: after `PRJ-1287`, the audit points at
  `MODEL-AION-MEMORY` as a verified model with no evidence row.
- Release objective or product milestone advanced: memory model traceability
  and evidence quality in the architecture graph.
- First/next checkpoint: run focused memory/model tests, add model evidence and
  relation, refine gap attribution, regenerate graph artifacts, and confirm
  `MODEL-AION-MEMORY` reports no gaps.
- Stop conditions: this mission does not change memory persistence behavior,
  database schema, retrieval policy, or production memory smoke.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_memory_repository.py::test_memory_repository_persists_structured_episode_payload tests/test_memory_repository.py::test_memory_repository_projects_recent_chat_transcript_in_chronological_order tests/test_schema_baseline.py::test_schema_baseline_tracks_structured_memory_payload_column tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1288 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator is running this serially because memory evidence, query gap
    attribution, generated artifacts, and state updates are tightly coupled
- Implementation:
  - refined `backend/scripts/query_architecture_graph.py` so chain
    `missing_links` are attributed to feature/API/UI/event/workflow nodes and
    do not over-report feature future scope on model nodes
  - added `REL-MEMORY-001`
  - added `EVID-AION-MEMORY-MODEL-PROOF`
  - pinned the memory model evidence and model-gap attribution behavior in
    graph generator/query pytest
- Validation:
  - focused memory/model pytest PASS: `3 passed in 13.37s`
  - inventory plus graph generation PASS with `auto_nodes=5278`,
    `auto_relations=3968`, merged `nodes=5339`, `relations=4031`,
    `chains=9`, `evidence=25`, `research_sources=21`,
    `theory_claims=9`
  - memory/schema plus graph/query pytest PASS:
    `22 passed, 1 deselected in 20.58s`
  - `query_architecture_graph.py --node MODEL-AION-MEMORY --show-gaps`
    reports `EVID-AION-MEMORY-MODEL-PROOF` and `Gaps: none`
  - top curated gap audit no longer lists `MODEL-AION-MEMORY`
- Residual:
  - local model/repository/schema proof only; production memory smoke remains
    a separate runtime/release scope
- Next recommended checkpoint:
  - after memory model gap closure, rerun gap audit and close the next
    high-risk service/runtime evidence gap
- Artifacts:
  - `.codex/tasks/PRJ-1288-aion-memory-model-gap-closure.md`
  - `backend/scripts/query_architecture_graph.py`
  - `docs/architecture/registry/relations.csv`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1287-data-model-graph-gap-closure
- Status: VERIFIED
- Selected objective: close the next high-risk curated gap from the graph
  audit by adding explicit chain and evidence for `FEAT-DATA-MODEL`.
- Why this mission now: after `PRJ-1286` closed the auth gap, the gap audit
  points at the data model foundation as a verified node without its own
  evidence row or chain.
- Release objective or product milestone advanced: database/model traceability
  and schema proof integrity in the architecture graph.
- First/next checkpoint: completed schema baseline tests, data model chain/
  evidence/relations, regenerated graph artifacts, and confirmed
  `FEAT-DATA-MODEL` no longer reports gaps.
- Stop conditions: this mission does not change ORM models, migrations,
  production database schema, or runtime data behavior.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_schema_baseline.py tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1287 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator ran this serially because data-model chain rows,
    evidence, generated artifacts, and state updates are tightly coupled
- Implementation:
  - added `REL-DATA-004`
  - added `CHAIN-DATA-MODEL-SCHEMA`
  - added `EVID-DATA-MODEL-SCHEMA-CHAIN`
  - pinned data model chain/evidence in graph generator pytest
- Validation:
  - schema baseline pytest PASS: `6 passed in 14.38s`
  - inventory plus graph generation PASS with `auto_nodes=5276`,
    `auto_relations=3967`, merged `nodes=5337`, `relations=4029`,
    `chains=9`, `evidence=24`, `research_sources=21`,
    `theory_claims=9`
  - schema plus graph/query pytest PASS:
    `24 passed, 1 deselected in 7.00s`
  - `query_architecture_graph.py --node FEAT-DATA-MODEL --show-gaps`
    reports `CHAIN-DATA-MODEL-SCHEMA`, `EVID-DATA-MODEL-SCHEMA-CHAIN`,
    and `Gaps: none`
  - top curated gap audit no longer lists `FEAT-DATA-MODEL`
- Residual:
  - local schema contract proof only; production database migration smoke is a
    separate deployment scope
- Next recommended checkpoint:
  - rerun gap audit and close the next high-risk memory/model/service evidence
    gap, likely `MODEL-AION-MEMORY`, `SERVICE-MEMORY-REPOSITORY`, or
    `SERVICE-RUNTIME-ORCHESTRATOR`
- Artifacts:
  - `.codex/tasks/PRJ-1287-data-model-graph-gap-closure.md`
  - `docs/architecture/registry/chains.csv`
  - `docs/architecture/registry/relations.csv`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1286-auth-api-graph-gap-closure
- Status: VERIFIED
- Selected objective: close the first high-risk curated gap from the graph
  audit by adding explicit chain, relations, and evidence for `API-APP-AUTH`.
- Why this mission now: `PRJ-1285` made missing-proof gaps visible and ranked
  `API-APP-AUTH` first; the node is verified but lacked its own evidence row
  and chain participation.
- Release objective or product milestone advanced: graph-system proof quality
  for authenticated app access.
- First/next checkpoint: completed focused auth API tests, graph chain/
  evidence/relations, regenerated graph artifacts, and confirmed
  `API-APP-AUTH` no longer appears in the top gap report.
- Stop conditions: this mission does not change auth runtime behavior,
  password/session implementation, UI login UX, or production auth smoke.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py::test_app_auth_register_sets_session_cookie_and_returns_user_snapshot tests/test_api_routes.py::test_app_me_requires_authenticated_session tests/test_api_routes.py::test_app_login_logout_and_me_roundtrip tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1286 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator ran this serially because the graph CSV rows, generated
    artifacts, focused tests, and state updates are tightly coupled
- Implementation:
  - added `REL-AUTH-001..004`
  - added `CHAIN-APP-AUTH`
  - added `EVID-AUTH-API-CHAIN-REFRESH`
  - pinned auth chain/evidence in graph generator pytest
- Validation:
  - focused auth API pytest PASS: `3 passed in 2.77s`
  - inventory plus graph generation PASS with `auto_nodes=5275`,
    `auto_relations=3967`, merged `nodes=5336`, `relations=4028`,
    `chains=8`, `evidence=23`, `research_sources=21`,
    `theory_claims=9`
  - focused auth plus graph/query pytest PASS:
    `21 passed, 1 deselected in 71.18s`
  - `query_architecture_graph.py --node API-APP-AUTH --show-gaps` reports
    `CHAIN-APP-AUTH`, `EVID-AUTH-API-CHAIN-REFRESH`, and `Gaps: none`
  - top curated gap audit no longer lists `API-APP-AUTH`
- Residual:
  - local API contract proof only; production auth smoke and security review
    remain separate scopes
- Next recommended checkpoint:
  - run the gap audit and close the next high-risk curated gap, likely
    `FEAT-DATA-MODEL`, `MODEL-AION-MEMORY`, or
    `SERVICE-MEMORY-REPOSITORY`
- Artifacts:
  - `.codex/tasks/PRJ-1286-auth-api-graph-gap-closure.md`
  - `docs/architecture/registry/chains.csv`
  - `docs/architecture/registry/relations.csv`
  - `docs/architecture/registry/evidence.csv`
  - generated graph artifacts

## Previous Mission

- Mission ID: PRJ-1285-architecture-graph-gap-audit-mode
- Status: VERIFIED
- Selected objective: extend the architecture graph query CLI with a global
  missing-proof audit mode that lists nodes with evidence, test, docs, chain,
  or research-support gaps.
- Why this mission now: `PRJ-1284` made single-node systemic analysis usable;
  the next agent-readiness gap is producing a prioritized queue of graph
  evidence holes before future work chooses a target.
- Release objective or product milestone advanced: graph-system evidence
  auditing and missing-proof detection.
- First/next checkpoint: completed `--gaps` mode, focused tests,
  docs/evidence, regenerated artifacts, and state refresh.
- Stop conditions: this mission does not fix every discovered gap, implement a
  graph UI, or treat auto-inventory rows as release-critical defects by
  default.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1285 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator ran this serially because CLI behavior, graph evidence,
    generated artifacts, and state updates are tightly coupled
- Implementation:
  - extended `backend/scripts/query_architecture_graph.py` with `--gaps` and
    `--include-auto`
  - added focused gap-audit tests to
    `backend/tests/test_architecture_graph_query.py`
  - added evidence row `EVID-ARCH-GRAPH-GAP-AUDIT`
  - documented gap-audit usage in `docs/architecture/graph-system.md`
- Validation:
  - inventory plus graph generation PASS with `auto_nodes=5274`,
    `auto_relations=3967`, merged `nodes=5335`, `relations=4024`,
    `chains=7`, `evidence=22`, `research_sources=21`,
    `theory_claims=9`
  - focused query plus fast graph pytest PASS:
    `18 passed, 1 deselected in 3.39s`
  - CLI `--gaps --limit 5 --format json` smoke PASS and excludes auto rows by
    default
  - generated evidence map, node page, and graph JSON include
    `EVID-ARCH-GRAPH-GAP-AUDIT`
- Residual:
  - audit output is a prioritization queue and does not itself close the
    reported gaps
  - auto-inventory rows are excluded by default because they are broad coverage
    rather than release-critical curated proof
- Next recommended checkpoint:
  - use the audit output to choose the next high-risk curated evidence/chain
    closure task, such as `API-APP-AUTH` or `FEAT-DATA-MODEL`
- Artifacts:
  - `.codex/tasks/PRJ-1285-architecture-graph-gap-audit-mode.md`
  - `backend/scripts/query_architecture_graph.py`
  - `backend/tests/test_architecture_graph_query.py`
  - `docs/architecture/registry/evidence.csv`
  - `docs/architecture/graph-system.md`

## Previous Mission

- Mission ID: PRJ-1284-architecture-graph-query-cli
- Status: VERIFIED
- Selected objective: add a local architecture graph query CLI so agents can
  inspect node impact, chains, evidence, research claims, and missing proof
  before answering systemic "does this work" questions.
- Why this mission now: `PRJ-1282` added CI drift prevention and `PRJ-1283`
  added PR review discipline; the next usability gap is making the graph
  quickly queryable by agents without manual CSV spelunking.
- Release objective or product milestone advanced: graph-system operational
  usefulness and agent systemic-analysis reliability.
- First/next checkpoint: completed the CLI, focused pytest coverage,
  script/test/evidence graph registry rows, regenerated artifacts, and state
  updates.
- Stop conditions: this mission did not add a web graph UI, production smoke,
  or new neuroscience claims; it only added a local query surface over the
  existing generated graph export.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1284 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator ran this serially because the CLI, graph registry rows,
    generated artifacts, tests, and source-of-truth updates are tightly coupled
- Implementation:
  - added `backend/scripts/query_architecture_graph.py`
  - added `backend/tests/test_architecture_graph_query.py`
  - added graph nodes `SCRIPT-QUERY-ARCH-GRAPH` and
    `TEST-ARCH-GRAPH-QUERY`
  - added relations `REL-GRAPH-009..012`
  - added evidence `EVID-ARCH-GRAPH-QUERY-CLI`
  - documented the local query workflow in `docs/architecture/graph-system.md`
- Validation:
  - inventory plus graph generation PASS with `auto_nodes=5267`,
    `auto_relations=3961`, merged `nodes=5328`, `relations=4018`,
    `chains=7`, `evidence=21`, `research_sources=21`,
    `theory_claims=9`
  - focused query plus fast graph pytest PASS:
    `14 passed, 1 deselected in 2.94s`
  - CLI node smoke PASS for
    `python .\scripts\query_architecture_graph.py --node WORKFLOW-ARCH-GRAPH --show-gaps`
  - CLI search smoke PASS for
    `python .\scripts\query_architecture_graph.py --search query --limit 5 --format json`
  - generated graph JSON, evidence map, and Obsidian node page include
    `SCRIPT-QUERY-ARCH-GRAPH`, `TEST-ARCH-GRAPH-QUERY`, and
    `EVID-ARCH-GRAPH-QUERY-CLI`
  - `git diff --check` PASS with LF/CRLF warnings only
- Residual:
  - local CLI is not an interactive graph UI
  - CLI reads generated JSON and does not replace canonical CSV, hosted CI,
    runtime smoke, screenshot proof, usability proof, or production proof
- Next recommended checkpoint:
  - optionally capture hosted graph CI proof when available; otherwise use the new
    CLI to identify the next release-critical node with missing proof before
    adding new graph work
- Artifacts:
  - `.codex/tasks/PRJ-1284-architecture-graph-query-cli.md`
  - `backend/scripts/query_architecture_graph.py`
  - `backend/tests/test_architecture_graph_query.py`
  - `docs/architecture/registry/nodes.csv`
  - `docs/architecture/registry/relations.csv`
  - `docs/architecture/registry/evidence.csv`
  - `docs/architecture/graph-system.md`

## Previous Mission

- Mission ID: PRJ-1283-architecture-graph-pr-template-checklist
- Status: VERIFIED
- Selected objective: add review-time architecture graph checklist prompts to
  the existing pull request template and map that checklist as graph evidence.
- Why this mission now: `PRJ-1282` added automatic CI policy; the remaining
  drift-prevention gap was making graph registry, chain, evidence, research,
  generated-artifact, and fast-gate posture visible in PR review.
- Release objective or product milestone advanced: graph-system review
  discipline and future agent handoff reliability.
- First/next checkpoint: completed PR template checklist, graph node/relation/
  evidence rows, generator pytest pin, graph regeneration, and state updates.
- Stop conditions: hosted GitHub Actions proof is optional supplementary
  evidence under `DEC-005`; checklist is review guidance and does not replace
  tests or CI.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1283 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the PR template graph checklist
    serially because review wording, graph registry rows, generated artifacts,
    and pytest pins were tightly coupled
- Implementation:
  - added `Architecture Graph / Evidence Map` section to
    `.github/pull_request_template.md`
  - added graph node `DOC-PR-TEMPLATE`
  - added graph relations `REL-GRAPH-007..008`
  - added evidence row `EVID-ARCH-PR-TEMPLATE-CHECKLIST`
  - extended generator pytest to pin the PR template node/evidence rollup
- Validation:
  - inventory plus graph generation PASS with `auto_nodes=5238`,
    `auto_relations=3935`, merged `nodes=5297`, `relations=3988`,
    `chains=7`, `evidence=20`, `research_sources=21`,
    `theory_claims=9`
  - fast graph pytest PASS: `8 passed, 1 deselected in 4.64s`
  - generated graph JSON, evidence map, and Obsidian node page include
    `DOC-PR-TEMPLATE` and `EVID-ARCH-PR-TEMPLATE-CHECKLIST`
  - PR template scan confirms Architecture Graph checklist prompts
  - `git diff --check` PASS with LF/CRLF warnings only
- Residual:
  - hosted GitHub Actions proof remains optional supplementary evidence under `DEC-005`
  - PR checklist is review guidance and not a replacement for generator,
    pytest, CI, runtime, screenshot, usability, or production proof
- Next recommended checkpoint:
  - optionally capture hosted Actions result when available; otherwise only add a new
    curated chain/research claim when a concrete release-critical module or
    theory claim is selected
- Artifacts:
  - `.codex/tasks/PRJ-1283-architecture-graph-pr-template-checklist.md`
  - `.github/pull_request_template.md`
  - `docs/architecture/registry/nodes.csv`
  - `docs/architecture/registry/relations.csv`
  - `docs/architecture/registry/evidence.csv`
  - `backend/tests/test_architecture_graph_generator.py`

## Previous Mission

- Mission ID: PRJ-1282-architecture-graph-ci-policy
- Status: VERIFIED
- Selected objective: add a CI-backed validation policy for the architecture
  graph system so graph-relevant changes run freshness and fast pytest gates
  automatically, with a manual heavy gate for release-level confidence.
- Why this mission now: `PRJ-1281` left all current curated chains verified;
  the next graph maturity gap was preventing future registry/generated-output
  drift through a durable CI policy.
- Release objective or product milestone advanced: graph-system regression
  prevention and agent workflow reliability.
- First/next checkpoint: completed GitHub Actions workflow, graph registry
  node/relation/evidence rows, graph/testing docs, generator pytest pin,
  graph regeneration, and state updates.
- Stop conditions: hosted GitHub Actions proof is optional supplementary
  evidence under `DEC-005`.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1282 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the CI policy serially because the
    workflow, graph registry rows, generated artifacts, docs, and pytest pin
    were tightly coupled
- Implementation:
  - added `.github/workflows/architecture-graph.yml`
  - added graph node `WORKFLOW-ARCH-GRAPH-CI`
  - added graph relations `REL-GRAPH-004..006`
  - added evidence row `EVID-ARCH-GRAPH-CI-POLICY`
  - documented automatic fast and manual heavy graph CI policy
  - extended generator pytest to pin CI policy node/evidence rollup
- Validation:
  - inventory plus graph generation PASS with `auto_nodes=5237`,
    `auto_relations=3935`, merged `nodes=5295`, `relations=3986`,
    `chains=7`, `evidence=19`, `research_sources=21`,
    `theory_claims=9`
  - fast graph pytest PASS: `8 passed, 1 deselected in 2.82s`
  - py_compile PASS for graph/inventory generators
  - generated graph JSON, evidence map, and Obsidian node page include
    `WORKFLOW-ARCH-GRAPH-CI` and `EVID-ARCH-GRAPH-CI-POLICY`
  - `git diff --check` PASS with LF/CRLF warnings only
- Residual:
  - hosted GitHub Actions first-run result must be collected after push
  - heavy graph gate remains manual for release-level graph confidence
- Next recommended checkpoint:
  - optionally capture hosted Actions result when available for the fast graph
    gate; choose
    production smoke evidence or a new curated chain only when release needs
    require it
- Artifacts:
  - `.codex/tasks/PRJ-1282-architecture-graph-ci-policy.md`
  - `.github/workflows/architecture-graph.yml`
  - `docs/architecture/registry/nodes.csv`
  - `docs/architecture/registry/relations.csv`
  - `docs/architecture/registry/evidence.csv`
  - `backend/tests/test_architecture_graph_generator.py`

## Previous Mission

- Mission ID: PRJ-1281-personality-overview-chain-refresh
- Status: VERIFIED
- Selected objective: promote the remaining partial Personality learned-state
  overview execution chain into fresh verified graph evidence.
- Why this mission now: `PRJ-1280` verified the Tools overview chain, leaving
  `CHAIN-PERSONALITY-OVERVIEW` as the remaining curated partial chain.
- Release objective or product milestone advanced: graph-system semantic
  curation for concrete feature chains.
- First/next checkpoint: completed Personality overview chain row, evidence row,
  generator pytest pin, graph regeneration, and state updates.
- Stop conditions: production account memory smoke and deeper screenshot parity
  remain separate evidence scopes.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1281 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified Personality overview chain refresh serially
- Implementation:
  - marked `CHAIN-PERSONALITY-OVERVIEW` verified
  - added `EVID-PERSONALITY-OVERVIEW-CHAIN-REFRESH`
  - extended generator pytest to pin the verified Personality overview chain and
    evidence rollup
- Validation:
  - backend personality API pytest PASS: `1 passed, 131 deselected in 5.26s`
  - memory repository focused pytest PASS:
    `2 passed, 71 deselected in 3.67s`
  - web build PASS
  - web route smoke PASS: `route_count=14`, `status=ok`, `/personality`
    marker `aion-personality-canvas` passed
  - inventory plus graph generation PASS with `auto_nodes=5235`,
    `auto_relations=3935`, merged `nodes=5292`, `relations=3983`,
    `chains=7`, `evidence=18`, `research_sources=21`,
    `theory_claims=9`
  - fast graph pytest PASS: `8 passed, 1 deselected in 4.85s`
  - py_compile PASS for graph/inventory generators
  - curated chains have no remaining `partial` rows
- Residual:
  - production account memory smoke and screenshot parity remain separate
    evidence scopes
- Next recommended checkpoint:
  - choose the next graph maturity step from release needs: add CI policy for
    fast/heavy graph gates, add production smoke evidence, or curate a
    currently auto-discovered module into a new chain only when it becomes
    release-critical
- Artifacts:
  - `.codex/tasks/PRJ-1281-personality-overview-chain-refresh.md`
  - `docs/architecture/registry/chains.csv`
  - `docs/architecture/registry/evidence.csv`
  - `backend/tests/test_architecture_graph_generator.py`

## Previous Mission

- Mission ID: PRJ-1280-tools-overview-chain-refresh
- Status: VERIFIED
- Selected objective: promote the stale partial Tools overview execution
  chain into fresh verified graph evidence.
- Release objective or product milestone advanced: graph-system semantic
  curation for concrete feature chains.
- First/next checkpoint: completed Tools overview chain row, evidence row,
  generator pytest pin, graph regeneration, and state updates.
- Stop conditions: live external provider credential activation remains
  deferred and is not claimed by local overview proof.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1277 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the scoped UX research mapping
    serially
- Implementation:
  - added curated node `UI-CHAT-COGNITIVE-BELT`
  - added relations from app chat, web shell rendering, and route-smoke proof
  - added reviewed sources `SRC-COWAN-2001-WM4`,
    `SRC-LUCK-VOGEL-1997-VWM`, and `SRC-LAVIE-2005-LOAD`
  - added `CLAIM-CHAT-COGNITIVE-BELT-LOAD-AWARENESS`
  - added `EVID-RESEARCH-UI-CHAT-COGNITIVE-BELT`
  - extended generator pytest to pin the claim and evidence rollups
- Validation:
  - inventory plus graph generation PASS with `auto_nodes=5227`,
    `auto_relations=3931`, merged `nodes=5284`, `relations=3979`,
    `chains=7`, `evidence=14`, `research_sources=21`,
    `theory_claims=9`
  - fast graph pytest PASS: `8 passed, 1 deselected in 45.36s`
  - heavy graph pytest PASS: `9 passed in 255.06s`
  - py_compile PASS for graph/inventory generators
- Residual:
  - research support is design rationale only; route smoke, screenshots,
    accessibility checks, and usability tests remain the behavior proof layer
- Next recommended checkpoint:
  - promote one critical auto-discovered feature chain into curated evidence,
    or add another UX theory claim only after selecting a concrete node and
    reviewed sources.
- Artifacts:
  - `.codex/tasks/PRJ-1277-chat-cognitive-belt-research-claim.md`
  - `docs/architecture/registry/nodes.csv`
  - `docs/architecture/registry/relations.csv`
  - `docs/architecture/registry/research_sources.csv`
  - `docs/architecture/registry/theory_claims.csv`
  - `docs/testing/architecture-research-map.md`

## Previous Mission

- Mission ID: PRJ-1276-fast-heavy-graph-validation-modes
- Status: VERIFIED
- Selected objective: split graph validation into documented fast and heavy
  pytest gates.
- Why this mission now: `PRJ-1275` made graph validation stronger but too slow
  for every tight local loop.
- Release objective or product milestone advanced: graph-system usability and
  validation discipline.
- First/next checkpoint: completed `slow` marker, fast/heavy docs, evidence
  update, graph regeneration, and state updates.
- Stop conditions: CI policy remains a future decision.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1276 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified validation modes serially
- Implementation:
  - registered pytest `slow` marker in `backend/pyproject.toml`
  - marked full node-page parity test as slow
  - documented fast and heavy graph validation commands in graph docs
  - updated `EVID-GRAPH-GENERATOR-PYTEST`
- Validation:
  - fast graph pytest PASS: `8 passed, 1 deselected`
  - heavy graph pytest PASS: `9 passed in 99.70s`
  - py_compile PASS for graph/inventory generators
  - final fast gate rerun after source-of-truth updates PASS:
    `8 passed, 1 deselected in 4.18s`
  - `git diff --check` PASS with CRLF normalization warnings only
  - inventory plus graph generation PASS with `auto_nodes=5226`,
    `auto_relations=3931`, merged `nodes=5282`, `relations=3976`,
    `chains=7`, `evidence=13`, `research_sources=18`,
    `theory_claims=8`
- Residual:
  - CI policy still needs a future decision
- Next recommended checkpoint:
  - select one concrete UX/UI graph node for a scoped research claim.
- Artifacts:
  - `.codex/tasks/PRJ-1276-fast-heavy-graph-validation-modes.md`
  - `backend/tests/test_architecture_graph_generator.py`
  - `backend/pyproject.toml`
  - `docs/architecture/graph-system.md`
  - `docs/architecture/registry/README.md`

- Mission ID: PRJ-1275-all-node-page-parity-pytest
- Status: VERIFIED
- Selected objective: add full generated node-page parity coverage.
- Why this mission now: key generated artifacts were checked, but stale or
  orphaned Obsidian node pages could still remain unnoticed.
- Release objective or product milestone advanced: graph-system reliability
  and complete generated node-page integrity.
- First/next checkpoint: completed full node file-set/content parity test,
  evidence update, graph regeneration, and state updates.
- Stop conditions: this check is strong but heavy; CI inclusion should be a
  conscious policy decision.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1275 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified all-node parity serially
- Implementation:
  - extended `backend/tests/test_architecture_graph_generator.py`
  - test writes all generated node pages to `tmp_path`
  - test compares generated and committed node file sets
  - test asserts committed node count matches registry node count
  - test compares generated and committed content for every node page
  - updated `EVID-GRAPH-GENERATOR-PYTEST`
- Validation:
  - focused pytest PASS: `9 passed in 108.30s`
  - inventory plus graph generation PASS with `auto_nodes=5225`,
    `auto_relations=3931`, merged `nodes=5281`, `relations=3976`,
    `chains=7`, `evidence=13`, `research_sources=18`,
    `theory_claims=8`
- Residual:
  - decide whether the heavy parity check belongs in CI or remains a
    pre-release/manual validation gate
- Next recommended checkpoint:
  - document fast versus heavy graph validation commands and add them to the
    graph-system workflow.
- Artifacts:
  - `.codex/tasks/PRJ-1275-all-node-page-parity-pytest.md`
  - `backend/tests/test_architecture_graph_generator.py`
  - `docs/architecture/registry/evidence.csv`

## Previous Mission

- Mission ID: PRJ-1274-generated-artifact-parity-pytest
- Status: VERIFIED
- Selected objective: add key generated artifact parity checks for the
  architecture graph system.
- Why this mission now: generated output freshness checks existed, but exact
  parity for key generated files was not yet tested.
- Release objective or product milestone advanced: graph-system reliability
  and practical no-diff protection for key generated artifacts.
- First/next checkpoint: completed temp-generation artifact parity test,
  evidence update, graph regeneration, and state updates.
- Stop conditions: parity for every generated node page remains optional until
  CI runtime cost is accepted.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1274 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified key artifact parity serially
- Implementation:
  - extended `backend/tests/test_architecture_graph_generator.py`
  - test writes graph artifacts to `tmp_path`
  - test compares JSON, Mermaid, relation index, chain index, status rollup,
    evidence rollup, research rollup, and selected critical node pages against
    repository files
  - updated `EVID-GRAPH-GENERATOR-PYTEST`
- Validation:
  - focused pytest PASS: `8 passed`
  - inventory plus graph generation PASS with `auto_nodes=5223`,
    `auto_relations=3930`, merged `nodes=5279`, `relations=3975`,
    `chains=7`, `evidence=13`, `research_sources=18`,
    `theory_claims=8`
- Residual:
  - parity for every generated node page remains optional CI runtime work
- Next recommended checkpoint:
  - select one concrete UX/UI graph node for a scoped research claim, or add
    all-node parity only if CI runtime cost is acceptable.
- Artifacts:
  - `.codex/tasks/PRJ-1274-generated-artifact-parity-pytest.md`
  - `backend/tests/test_architecture_graph_generator.py`
  - `docs/architecture/registry/evidence.csv`

## Previous Mission

- Mission ID: PRJ-1273-generated-graph-freshness-pytest
- Status: VERIFIED
- Selected objective: add generated-output freshness pytest checks for the
  architecture graph system.
- Why this mission now: live registry validation existed, but generated
  `architecture-graph.json` and rollups could still go stale after CSV edits.
- Release objective or product milestone advanced: graph-system reliability
  and stale-output protection.
- First/next checkpoint: completed JSON count freshness checks, critical
  rollup row checks, evidence update, graph regeneration, and state updates.
- Stop conditions: strict byte-for-byte no-diff generation remains future CI
  policy work.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1273 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the freshness pytest serially
- Implementation:
  - extended `backend/tests/test_architecture_graph_generator.py`
  - test compares generated graph JSON counts to the live registry counts
  - test checks generated evidence/research rollups include critical latest
    rows
  - updated `EVID-GRAPH-GENERATOR-PYTEST`
- Validation:
  - focused pytest PASS: `7 passed`
  - inventory plus graph generation PASS with `auto_nodes=5221`,
    `auto_relations=3929`, merged `nodes=5277`, `relations=3974`,
    `chains=7`, `evidence=13`, `research_sources=18`,
    `theory_claims=8`
- Residual:
  - strict byte-for-byte no-diff generation remains future CI/governance work
- Next recommended checkpoint:
  - choose either strict CI no-diff generation policy or a concrete UX/UI
    graph node for scoped research claims.
- Artifacts:
  - `.codex/tasks/PRJ-1273-generated-graph-freshness-pytest.md`
  - `backend/tests/test_architecture_graph_generator.py`
  - `docs/architecture/registry/evidence.csv`

## Previous Mission

- Mission ID: PRJ-1272-current-registry-validation-pytest
- Status: VERIFIED
- Selected objective: extend graph generator pytest coverage to the live
  canonical registry and temp research rollup generation.
- Why this mission now: `PRJ-1271` covered synthetic rows, but the real CSV
  registry also needs automated validation.
- Release objective or product milestone advanced: graph-system reliability
  and live-registry safety for future agent edits.
- First/next checkpoint: completed live-registry validation pytest, temp
  research rollup test, evidence update, graph regeneration, and state updates.
- Stop conditions: stale-generated-output no-diff gate can wait until CI/docs
  generation policy is selected.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1272 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the live-registry pytest serially
- Implementation:
  - extended `backend/tests/test_architecture_graph_generator.py`
  - test loads current repository registry and asserts no validation errors
  - test asserts current research layer minimum coverage
  - test writes research rollup into `tmp_path`
  - updated `EVID-GRAPH-GENERATOR-PYTEST`
- Validation:
  - focused pytest PASS: `5 passed`
  - inventory plus graph generation PASS with `auto_nodes=5218`,
    `auto_relations=3927`, merged `nodes=5274`, `relations=3972`,
    `chains=7`, `evidence=13`, `research_sources=18`,
    `theory_claims=8`
- Residual:
  - stale-generated-output no-diff gate remains future CI/governance work
- Next recommended checkpoint:
  - decide whether generated docs should be enforced in CI with a no-diff
    generation gate.
- Artifacts:
  - `.codex/tasks/PRJ-1272-current-registry-validation-pytest.md`
  - `backend/tests/test_architecture_graph_generator.py`
  - `docs/architecture/registry/evidence.csv`

## Previous Mission

- Mission ID: PRJ-1271-architecture-graph-generator-pytest
- Status: VERIFIED
- Selected objective: add focused pytest coverage for architecture graph
  generator research validation and export behavior.
- Why this mission now: the graph system had command proof but no pytest for
  the research-evidence validation rules.
- Release objective or product milestone advanced: graph-system reliability
  and automated confidence for future research-claim edits.
- First/next checkpoint: completed focused pytest, registered it as evidence,
  regenerated graph outputs, and updated state files.
- Stop conditions: broader full-registry fixture tests can wait until schema
  changes again.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1271 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the generator pytest serially
- Implementation:
  - added `backend/tests/test_architecture_graph_generator.py`
  - tests cover reviewed/mapped claim 3-source enforcement
  - tests cover graph JSON export of `research_sources` and `theory_claims`
  - added `EVID-GRAPH-GENERATOR-PYTEST`
- Validation:
  - focused pytest PASS: `3 passed`
  - inventory plus graph generation PASS with `auto_nodes=5215`,
    `auto_relations=3925`, merged `nodes=5271`, `relations=3970`,
    `chains=7`, `evidence=13`, `research_sources=18`,
    `theory_claims=8`
- Residual:
  - no full fixture-based end-to-end registry pytest yet
- Next recommended checkpoint:
  - add a generated-registry smoke pytest only if the CSV schema changes again
    or CI starts running docs validation automatically.
- Artifacts:
  - `.codex/tasks/PRJ-1271-architecture-graph-generator-pytest.md`
  - `backend/tests/test_architecture_graph_generator.py`
  - `docs/architecture/registry/evidence.csv`

## Previous Mission

- Mission ID: PRJ-1270-affect-motivation-role-research-claims
- Status: VERIFIED
- Selected objective: promote affective assessment, motivation, and role
  selection into curated graph nodes with research-backed theory claims.
- Why this mission now: `PRJ-1269` left motivation, affective state, and role
  selection as the next source-review targets.
- Release objective or product milestone advanced: graph completeness for
  runtime stages and safer research-backed interpretation of affect,
  motivation, and role metaphors.
- First/next checkpoint: completed curated node rows, runtime relations,
  reviewed sources, theory claims, generated graph outputs, and state updates.
- Stop conditions: UX-specific neuroscience claims remain future work until a
  concrete UI node and source set are selected.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1270 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the runtime-stage research expansion
    serially
- Implementation:
  - added curated graph nodes `AGENT-AFFECTIVE-ASSESSMENT`,
    `AGENT-MOTIVATION`, and `AGENT-ROLE`
  - added runtime relation rows `REL-RUNTIME-006..008`
  - added affective neuroscience, motivation/reward, and social cognition
    sources
  - added theory claims for affective signal integration, motivation
    valuation/selection, and role social posture
  - added `EVID-RESEARCH-AFFECT-MOTIVATION-ROLE`
- Validation:
  - inventory plus graph generation PASS with `auto_nodes=5205`,
    `auto_relations=3917`, merged `nodes=5261`, `relations=3962`,
    `chains=7`, `evidence=12`, `research_sources=18`,
    `theory_claims=8`
- Residual:
  - UX-specific neuroscience claims remain future source-review work
- Next recommended checkpoint:
  - select one concrete UX/UI node and review cognitive-load, attention, or
    usability sources before adding UX theory claims.
- Artifacts:
  - `.codex/tasks/PRJ-1270-affect-motivation-role-research-claims.md`
  - `docs/architecture/registry/nodes.csv`
  - `docs/architecture/registry/relations.csv`
  - `docs/architecture/registry/research_sources.csv`
  - `docs/architecture/registry/theory_claims.csv`

## Previous Mission

- Mission ID: PRJ-1269-research-claim-expansion
- Status: VERIFIED
- Selected objective: expand research-backed theory claims for perception,
  planning, and memory/reflection graph nodes.
- Why this mission now: `PRJ-1268` left the research evidence layer with only
  two seed claims, and the next continuation checkpoint was to add
  claim-specific sources where available.
- Release objective or product milestone advanced: project-system confidence,
  agent research traceability, and safer interpretation of neuroscience
  metaphors.
- First/next checkpoint: completed source expansion, added 3 theory claims,
  regenerated graph artifacts, and kept limitations explicit.
- Stop conditions: do not add motivation, affective, role, or UX claims until
  claim-specific sources are reviewed.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1269 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the research claim expansion serially
- Implementation:
  - added attention/salience sources for `AGENT-PERCEPTION`
  - added cognitive-control and predictive-processing sources for
    `AGENT-PLANNING`
  - added systems-consolidation sources for `FEAT-MEMORY-FLOW`
  - added three scoped theory claims with limitations
  - added `EVID-RESEARCH-CLAIM-EXPANSION`
- Validation:
  - inventory plus graph generation PASS with `auto_nodes=5204`,
    `auto_relations=3917`, merged `nodes=5257`, `relations=3959`,
    `chains=7`, `evidence=11`, `research_sources=11`,
    `theory_claims=5`
- Residual:
  - motivation, affective, role-selection, and UX neuroscience claims remain
    future source-review work
- Next recommended checkpoint:
  - add motivation/affective theory claims only after reviewing suitable
    affective neuroscience and motivation-control sources.
- Artifacts:
  - `.codex/tasks/PRJ-1269-research-claim-expansion.md`
  - `docs/architecture/registry/research_sources.csv`
  - `docs/architecture/registry/theory_claims.csv`
  - `docs/testing/architecture-research-map.md`

## Previous Mission

- Mission ID: PRJ-1268-research-evidence-mapping-layer
- Status: VERIFIED
- Selected objective: add neuroscience/cognitive-science research evidence
  mapping to the architecture graph system.
- Why this mission now: user asked for feature-management agents to attach
  appropriate scientific research when code expresses cognitive or
  neuroscience-inspired theories.
- Release objective or product milestone advanced: project-system confidence,
  theory traceability, and safer AI-agent interpretation of research-backed
  claims.
- First/next checkpoint: completed research source registry, theory claim
  registry, 3-source validation, generated research rollup, seed claims, and
  graph/state updates.
- Stop conditions: research support must not be treated as runtime proof or as
  evidence that the software implements a biological brain.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1268 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the research evidence layer serially
- Implementation:
  - added `docs/architecture/registry/research_sources.csv`
  - added `docs/architecture/registry/theory_claims.csv`
  - updated `backend/scripts/generate_architecture_graph.py` to validate and
    export research sources and theory claims
  - generated `docs/testing/architecture-research-map.md`
  - added node-page theory claim sections and graph JSON research payloads
  - seeded 4 reviewed neuroscience/cognitive-science sources and 2 theory
    claims
- Validation:
  - Python compile PASS for graph and inventory generators
  - inventory plus graph generation PASS with `auto_nodes=5203`,
    `auto_relations=3917`, merged `nodes=5256`, `relations=3959`,
    `chains=7`, `evidence=10`, `research_sources=4`, `theory_claims=2`
- Residual:
  - the seed research set covers only the first runtime/memory claims
  - future neuroscience-inspired features need claim-specific source review
- Next recommended checkpoint:
  - promote additional runtime, memory, reflection, motivation, and planning
    theories into `theory_claims.csv`, or mark them `needs_sources`.
- Artifacts:
  - `.codex/tasks/PRJ-1268-research-evidence-mapping-layer.md`
  - `docs/architecture/registry/research_sources.csv`
  - `docs/architecture/registry/theory_claims.csv`
  - `docs/testing/architecture-research-map.md`

## Previous Mission

- Mission ID: PRJ-1267-whole-repository-architecture-inventory
- Status: VERIFIED
- Selected objective: expand the graph foundation into a whole-repository
  auto-inventory layer.
- Why this mission now: user asked to execute everything after the graph
  foundation, and full manual inventory is not scalable or honest without an
  automated coverage layer.
- Release objective or product milestone advanced: project-system confidence,
  impact analysis breadth, and future AI-agent planning.
- First/next checkpoint: completed auto scanner, generated CSV inventory,
  merged auto rows into graph outputs, and kept curated proof separate.
- Stop conditions: auto rows must not be treated as verified user-facing
  feature proof until promoted into curated chains/evidence.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1267 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the auto-inventory layer serially
- Implementation:
  - added `backend/scripts/generate_architecture_inventory.py`
  - updated `backend/scripts/generate_architecture_graph.py`
  - generated `docs/architecture/registry/auto_nodes.csv`
  - generated `docs/architecture/registry/auto_relations.csv`
  - generated `docs/architecture/registry/auto_inventory_summary.md`
  - regenerated Obsidian nodes, relation index, graph JSON/Mermaid, status,
    and evidence rollups from merged curated + auto rows
- Validation:
  - inventory plus graph generation PASS with `auto_nodes=5197`,
    `auto_relations=3915`, merged `nodes=5249`, `relations=3954`,
    `chains=7`, `evidence=9`
- Residual:
  - auto-discovered rows are broad inventory, not release-critical proof
  - curated chains/evidence still need promotion for critical modules
- Next recommended checkpoint:
  - promote backend API route/function rows into curated chains and evidence
    first, then frontend route/component rows.
- Artifacts:
  - `.codex/tasks/PRJ-1267-whole-repository-architecture-inventory.md`
  - `backend/scripts/generate_architecture_inventory.py`
  - `docs/architecture/registry/auto_nodes.csv`
  - `docs/architecture/registry/auto_relations.csv`
  - `docs/architecture/registry/auto_inventory_summary.md`

## Previous Mission

- Mission ID: PRJ-1266-architecture-graph-evidence-system-foundation
- Status: VERIFIED
- Selected objective: create the first CSV-first Obsidian architecture graph
  evidence foundation for systemic feature analysis.
- Why this mission now: user explicitly requested a living project nervous
  system for dependencies, function chains, test/docs evidence, graph exports,
  missing links, and AI-agent workflow.
- Release objective or product milestone advanced: project-system confidence
  and future autonomous agent coordination.
- First/next checkpoint: completed registry contract, seeded graph CSVs,
  generator/validator, generated Obsidian nodes and graph exports, and source
  of truth updates.
- Stop conditions: next work should expand inventory module-by-module, not
  claim exhaustive coverage from the foundation seed.
- Parent validation gate:
  `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit`.

## PRJ-1266 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified the graph foundation serially
  - subagents were not spawned because available subagent tooling requires an
    explicit user request for delegation
- Implementation:
  - added `docs/architecture/graph-system.md`
  - added canonical CSV registries in `docs/architecture/registry/`
  - added `backend/scripts/generate_architecture_graph.py`
  - generated Obsidian node pages, relation/chain indexes, graph exports,
    status rollup, and evidence rollup
  - updated docs index, docs README, traceability matrix, task board, project
    state, requirement matrix, quality scenario, risk register, delivery map,
    system health, next steps, and module confidence
- Validation:
  - graph generator PASS with `nodes=52`, `relations=39`, `chains=7`,
    `evidence=9`
- Residual:
  - foundation seed is not exhaustive
  - typed CSV views are manual mirrors for now
  - no dedicated pytest for the generator yet
- Next recommended checkpoint:
  - expand graph coverage for backend API route/function inventory and
    frontend route/component inventory as separate focused tasks.
- Artifacts:
  - `.codex/tasks/PRJ-1266-architecture-graph-evidence-system-foundation.md`
  - `docs/architecture/graph-system.md`
  - `docs/architecture/registry/nodes.csv`
  - `docs/architecture/graphs/architecture-graph.json`
  - `docs/status/architecture-map-status.md`

## Previous Mission

- Mission ID: PRJ-1265-chat-attachments-functional-pass
- Status: VERIFIED
- Selected objective: deliver functional chat attachments without backend API
  contract changes, then verify full-route stability.
- Why this mission now: user explicitly flagged non-working chat file attach.
- Release objective or product milestone advanced: v1.2 chat usability and
  backend-aligned function mapping.
- First/next checkpoint: completed attachment picker/chips/remove flow and
  outbound text serialization of attached content.
- Stop conditions: next work should target screenshot parity deltas for
  dashboard/chat/personality.
- Parent validation gate: `npm run build`, `npm run smoke:routes`,
  `npm run test:chat-transcript`, cleanup check, and `git diff --check`.

## PRJ-1265 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented and verified a functional chat attachment pass
- Implementation:
  - added file attachment control to chat composer
  - added attachment preview chips and remove interaction
  - bounded file count and max file size
  - serialized attachment text into outgoing `/app/chat/message` payload
- Validation:
  - `npm run build` PASS
  - `npm run smoke:routes` PASS (`route_count=14`, `status=ok`)
  - `npm run test:chat-transcript` PASS (`status=ok`)
- Artifacts:
  - `.codex/tasks/PRJ-1265-chat-attachments-functional-pass.md`

## PRJ-1263 Current Evidence

- Branch: `main`.
- Lane status:
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - widened and clarified desktop dashboard guidance rail, increased hero/flow
    readability, reduced over-compression, and restored desktop recent panel
    visibility
  - preserved route structure, backend data mapping, controls, shared shell,
    and cross-route behavior
- Validation:
  - `npm run build` PASS
  - combined focused `/dashboard` screenshot/navigation/account gate PASS:
    `screenshot_count=2`, `failed_count=0`, `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no validation-owned node/Vite, 5173/4173 listener,
    Chromium, or headless browser leftovers
- Residual:
  - This is a verified Dashboard structure pass, not final pixel-perfect 1:1
    closure.
- Next recommended checkpoint:
  - Run the next Dashboard-only parity slice for exact spacing/typography/icon
    fidelity against canonical reference.
- Artifacts:
  - `.codex/tasks/PRJ-1263-dashboard-canonical-structure-pass.md`
  - `artifacts/route-smoke/prj-1263-dashboard-pass/report.json`
  - `artifacts/route-smoke/prj-1263-dashboard-pass/desktop-dashboard.png`
  - `artifacts/route-smoke/prj-1263-dashboard-pass/mobile-dashboard.png`

## Previous Mission

- Mission ID: PRJ-1260-chat-cognitive-belt-quieting
- Status: VERIFIED
- Selected objective: make Chat's top cognitive belt read as a quiet context
  strip instead of a badge-heavy control row.
- Why this mission now: after `PRJ-1259`, Pasteur identified the Chat top belt
  as the smallest canonical-backed mismatch that directly matches the user's
  request to reduce cards, badges, and control clutter.
- Release objective or product milestone advanced: v1.2 web Chat canonical
  desktop composition.
- First/next checkpoint: completed a CSS-only Chat cognitive-belt pass. The
  six context modules remain visible but use quieter material, icon-like
  accents, and less badge-heavy status treatment.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/dashboard`
  desktop/tablet/mobile screenshot gate, navigation proof, account proof,
  screenshot review, cleanup check, and `git diff --check`.

## PRJ-1259 Previous Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Epicurus and completed read-only
  - QA lane delegated to Goodall and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - Current Focus now uses a compact scenic circular focal treatment instead
    of the prior generic teal orb
  - all Dashboard data/copy/CTA, hero signals, PRJ-1258 summary band,
    mobile/tablet structure, cognitive flow, Chat, Personality, and shared
    shell were not changed
- Validation:
  - `node --check scripts/route-smoke.mjs` PASS
  - `npm run build` PASS
  - combined focused `/dashboard` screenshot/navigation/account gate PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no validation-owned node/Vite, 5173/4173 listener,
    Chromium, or headless browser leftovers; one fresh route-smoke temp
    profile from this checkpoint was removed
- Residual:
  - This is a verified Dashboard Current Focus focal pass, not a full 95%
    pixel parity claim. Exact canonical icon glyphs and richer focus content
    remain separate content/data decisions.
- Next recommended checkpoint:
  - Pick one exact remaining screenshot mismatch on one route, or make a
    content/data decision before changing canonical copy, icon glyphs,
    route-smoke fixture content, or backend-backed labels.
- Artifacts:
  - `.codex/tasks/PRJ-1259-dashboard-current-focus-focal.md`
  - `.codex/artifacts/prj1259-dashboard-current-focus-focal/report.json`
  - `.codex/artifacts/prj1259-dashboard-current-focus-focal/screenshots/`

## Previous Mission

- Mission ID: PRJ-1255-chat-desktop-persona-overlay-placement
- Status: VERIFIED
- Selected objective: place desktop Chat's Planning overlay as a lower-right
  persona-stage annotation instead of a transcript-facing lower-left label.
- Why this mission now: `PRJ-1254` left Chat overlay placement as the next
  concrete screenshot-backed mismatch from the UX parity lane, and Pascal
  confirmed it should stay a CSS-only placement slice.
- Release objective or product milestone advanced: v1.2 web Chat canonical
  desktop/tablet persona-stage composition.
- First/next checkpoint: completed a CSS-only Chat portrait overlay placement
  pass. The overlay now sits on the right/bottom side of the persona stage,
  below the channel annotation, while mobile keeps its existing placement.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/chat` desktop/tablet/mobile
  screenshot gate, `test:chat-transcript`, navigation proof, account proof,
  screenshot review, cleanup check, and `git diff --check`.

## PRJ-1255 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Pascal and completed read-only
  - QA lane delegated to Parfit and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - Chat Planning overlay now uses lower-right portrait-stage placement on
    desktop/tablet instead of the transcript-facing lower-left edge
  - mobile Chat keeps its previous overlay placement through an explicit
    `right: auto` override
  - transcript, composer, source markers, cognitive belt, backend data,
    Dashboard, and Personality were not changed
- Validation:
  - `npm run build` PASS
  - focused `/chat` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - `npm run test:chat-transcript` PASS: `status=ok`,
    `appSourceCount=2`, `telegramSourceCount=2`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no validation-owned node/Vite, 5173/4173 listener,
    Chromium, or headless browser leftovers; three fresh route-smoke temp
    profiles from this checkpoint were removed
- Residual:
  - This is a verified Chat overlay placement pass, not a full 95% pixel
    parity claim. Exact canonical icon metaphors, fixture copy, and richer
    data values remain separate content/data decisions.
- Next recommended checkpoint:
  - Pick one exact remaining screenshot mismatch on one route, or make a
    content/data decision before changing canonical copy, icon glyphs,
    route-smoke fixture content, or backend-backed labels.
- Artifacts:
  - `.codex/tasks/PRJ-1255-chat-desktop-persona-overlay-placement.md`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/report.json`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/navigation-proof.json`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/account-proof.json`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/screenshots/`

## Previous Mission

- Mission ID: PRJ-1254-personality-mobile-timeline-rail
- Status: VERIFIED
- Selected objective: make mobile Personality's Mind Layers Timeline read like
  the canonical compact layer rail instead of a tall text list.
- Why this mission now: after Chat desktop belt quieting in `PRJ-1253`, the
  next concrete implemented-screenshot mismatch was mobile Personality's
  hidden timeline track and tall text-list rhythm.
- Release objective or product milestone advanced: v1.2 web Personality
  canonical mobile first-scroll quality.
- First/next checkpoint: completed a CSS-only mobile Personality timeline pass.
  Timeline rows now show token, signal track, and value chip while preserving
  all six layers and backend-backed values.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/personality`
  desktop/tablet/mobile screenshot gate, navigation proof, account proof,
  screenshot review, cleanup check, and `git diff --check`.

## PRJ-1254 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Faraday and completed read-only
  - QA lane delegated to Poincare and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - mobile Personality timeline rows now use compact rail columns, visible
    signal tracks, smaller tokens, and value chips
  - secondary detail copy is hidden only in the mobile rail to reduce first
    scroll height
  - all six layers and values remain visible; desktop/tablet remain stable
- Validation:
  - `npm run build` PASS
  - focused `/personality` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - cleanup found no validation-owned node/Vite, 5173/4173 listener,
    Chromium, or headless browser leftovers; three fresh route-smoke temp
    profiles from this checkpoint were removed
- Residual:
  - This is a verified mobile timeline hierarchy pass, not a full 95% pixel
    parity claim. Exact canonical icon glyphs and richer data values remain
    separate content/data decisions.
- Artifacts:
  - `.codex/tasks/PRJ-1254-personality-mobile-timeline-rail.md`
  - `.codex/artifacts/prj1254-personality-mobile-timeline-rail/report.json`
  - `.codex/artifacts/prj1254-personality-mobile-timeline-rail/navigation-proof.json`
  - `.codex/artifacts/prj1254-personality-mobile-timeline-rail/account-proof.json`
  - `.codex/artifacts/prj1254-personality-mobile-timeline-rail/screenshots/`

## Previous Mission

- Mission ID: PRJ-1253-chat-desktop-cognitive-belt-quieting
- Status: VERIFIED
- Selected objective: make desktop Chat's cognitive belt flatter and visually
  secondary to the transcript/persona stage.
- Why this mission now: after `PRJ-1251` and `PRJ-1252`, Dashboard and
  Personality had fresh mobile hierarchy passes. The UX parity lane identified
  Chat's desktop cognitive belt as the next concrete flagship mismatch left by
  `PRJ-1250`.
- Release objective or product milestone advanced: v1.2 web Chat canonical
  desktop first-read quality.
- First/next checkpoint: completed a CSS-only Chat belt pass. The six context
  items are lower, flatter, less card-heavy, and still preserve all supported
  labels, values, progress, transcript source markers, and mobile rail
  behavior.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/chat` desktop/tablet/mobile
  screenshot gate, `test:chat-transcript`, navigation proof, account proof,
  `git diff --check`, screenshot review, and cleanup check.

## PRJ-1253 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Halley and completed read-only
  - QA lane delegated to Fermat and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - desktop Chat cognitive belt cards now use lower height, lighter material,
    smaller UI typography, quieter meta chips, and a tiny accent marker
  - all belt items, labels, values, progress, transcript source markers, and
    mobile rail behavior remain supported
- Validation:
  - `npm run build` PASS
  - focused `/chat` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - `npm run test:chat-transcript` first hit a CDP `Page.navigate` timeout;
    immediate rerun PASS: `status=ok`, `appSourceCount=2`,
    `telegramSourceCount=2`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no validation-owned node/Vite, 5173/4173 listener, or
    headless browser leftovers; six fresh route-smoke temp profiles from this
    checkpoint were removed
- Residual:
  - This is a verified hierarchy/density pass, not a full 95% pixel parity
    claim. Exact canonical icon metaphors and fixture-copy parity remain
    separate content/data decisions.
- Artifacts:
  - `.codex/tasks/PRJ-1253-chat-desktop-cognitive-belt-quieting.md`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/report.json`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/navigation-proof.json`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/account-proof.json`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/screenshots/`

## Previous Mission

- Mission ID: PRJ-1252-personality-mobile-callout-map-quieting
- Status: VERIFIED
- Selected objective: make mobile Personality hero callouts feel like compact
  embodied-map annotations instead of chunky cards over the figure.
- Why this mission now: after PRJ-1251, Dashboard mobile signals were quieted.
  Fresh Personality screenshots plus the UX parity lane identified mobile
  callout card weight and portrait occlusion as the next smallest high-impact
  canonical mismatch.
- Release objective or product milestone advanced: v1.2 web Personality
  canonical mobile first-read quality.
- First/next checkpoint: completed a CSS-only Personality mobile callout pass.
  Mobile callouts are smaller, lighter, and placed with more portrait
  breathing room; `Planning` no longer wraps; all supported callouts remain
  visible.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/personality`
  desktop/tablet/mobile screenshot gate, navigation proof, account proof,
  `git diff --check`, screenshot review, and cleanup check.

## PRJ-1252 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Bacon and completed read-only
  - QA lane delegated to Nash and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - mobile Personality callouts now use smaller width, padding, type, radius,
    material, and shadow so they read as annotations rather than cards
  - lower callouts sit with more figure clearance; `Planning` keeps
    `0 active goals` on one line
  - all supported callouts and backend-backed values remain visible
- Validation:
  - `npm run build` PASS
  - focused `/personality` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no Personality route-smoke, Vite/dev-server, 5173/4173
    listener, or headless browser leftovers; four fresh route-smoke temp
    profiles from this checkpoint were removed
- Residual:
  - This is a verified mobile callout hierarchy pass, not a full 95% pixel
    parity claim. Exact icon/content/copy parity remains a separate
    content/data decision.
- Artifacts:
  - `.codex/tasks/PRJ-1252-personality-mobile-callout-map-quieting.md`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/report.json`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/navigation-proof.json`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/account-proof.json`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/screenshots/`

## Previous Mission

- Mission ID: PRJ-1251-dashboard-mobile-hero-signal-quieting
- Status: VERIFIED
- Selected objective: make mobile Dashboard hero signal cards quieter and make
  count values read as numerals while preserving all supported signals and the
  PRJ-1248 flow rail.
- Why this mission now: after PRJ-1250, Chat metadata was quiet and verified.
  Fresh screenshots plus UX/QA lanes identified mobile Dashboard hero signal
  density and numeral ambiguity as the smallest high-impact UI checkpoint.
- Release objective or product milestone advanced: v1.2 web Dashboard
  canonical mobile first-read quality.
- First/next checkpoint: completed a CSS-only Dashboard signal pass. Dashboard
  signal values now use UI tabular numerals, and mobile hero signal cards keep
  label/value/detail while dropping decorative wave and third-line note noise
  from the first-read card treatment.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/dashboard`
  desktop/tablet/mobile screenshot gate, full route smoke, navigation proof,
  account proof, `git diff --check`, screenshot review, and cleanup check.

## PRJ-1251 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Locke and completed read-only
  - QA lane delegated to Turing and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - Dashboard signal values now use UI tabular numerals instead of display
    serif styling, so `1` and `0 / 0` read as clear numbers
  - mobile Dashboard signal cards are lighter, shorter, and less decorative;
    all six supported signal cards remain visible
- Validation:
  - `npm run build` PASS
  - focused `/dashboard` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no Personality route-smoke, Vite/dev-server, 5173/4173
    listener, temp route-smoke/chat-transcript profile, or headless browser
    leftovers; unrelated Vite processes from `Obiekty` were left untouched
- Residual:
  - This is a verified mobile first-read hierarchy pass, not a full
    pixel-perfect Dashboard parity claim. Exact icon/content/copy parity
    remains a separate content/data decision.
- Artifacts:
  - `.codex/tasks/PRJ-1251-dashboard-mobile-hero-signal-quieting.md`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/report.json`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/navigation-proof.json`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/account-proof.json`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/screenshots/`

## Previous Mission

- Mission ID: PRJ-1250-chat-source-marker-quieting
- Status: VERIFIED
- Selected objective: keep Chat's `App` / `Telegram` transcript source marker
  visible while reducing its visual weight so it reads as quiet metadata, not a
  competing primary accent.
- Why this mission now: PRJ-1249 added the truthful marker, and fresh Chat
  screenshots showed the teal text was useful but a little too loud in the
  dense transcript.
- Release objective or product milestone advanced: v1.2 web Chat
  communication clarity and canonical visual calm.
- First/next checkpoint: completed a CSS-only Chat metadata polish. The source
  marker now renders as a small low-contrast chip inside the existing metadata
  row, with no source mapping, backend, fixture, component-structure, or shared
  shell change.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  or backend-backed labels. Live Telegram credential smoke remains outside this
  visual slice.
- Parent validation gate: web build, chat transcript characterization, focused
  `/chat` desktop/tablet/mobile screenshot gate, full route smoke, navigation
  proof, account proof, `git diff --check`, manual screenshot review, and
  validation cleanup.

## PRJ-1250 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Sagan and completed read-only
  - QA lane delegated to Copernicus and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - `.aion-chat-source-marker` now uses a quieter chip treatment with lower
    contrast, smaller type, and light material so the source truth remains
    available without competing with speaker, time, delivery, or message
    content
- Validation:
  - `npm run build` PASS
  - `npm run test:chat-transcript` PASS: `status=ok`,
    `appSourceCount=2`, `telegramSourceCount=2`, `deliveredCount=1`
  - focused `/chat` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`
  - full route smoke PASS: `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup check found no route-smoke, Vite, or 5173/4173 listener leftovers;
    a transient chat-transcript temp profile lock warning was cleaned with
    targeted temp-directory removal; final Windows cleanup reported two stale
    `chrome-headless-shell` handles with empty command lines and `taskkill`
    reported no running task instance
- Residual:
  - This is a verified visual quieting slice, not a new channel-routing proof
    or a full canonical content/icon parity claim.
- Artifacts:
  - `.codex/tasks/PRJ-1250-chat-source-marker-quieting.md`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/report.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/route-smoke-report.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/navigation-proof.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/account-proof.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/screenshots/`

## Previous Mission

- Mission ID: PRJ-1249-channel-routing-tool-truth-and-source-marker
- Status: VERIFIED
- Selected objective: make Aviary truthful about action-owned web knowledge
  tools and visibly distinguish App/API versus Telegram transcript messages in
  first-party Chat.
- Why this mission now: the user showed a real conversation where Aviary
  denied search/browser capability despite connected action-layer tools, and
  asked that the canonical native/web communicator show whether messages are
  app-native or Telegram-backed without duplicating notifications.
- Release objective or product milestone advanced: v1.2 web/runtime
  communication continuity confidence.
- First/next checkpoint: completed a narrow runtime + web Chat slice. The
  expression guardrail now corrects false search/page-read capability denial
  when foreground awareness has tool hints, transcript projection marks
  Telegram-delivered assistant outreach as `telegram`, and the Chat transcript
  metadata row displays `App` or `Telegram`.
- Stop conditions: live Telegram credential smoke remains out of scope unless
  credentials and a live delivery target are explicitly provided. Do not
  introduce a second chat store, notification fan-out path, or connector
  provider.
- Parent validation gate: focused backend pytest, web build, chat transcript
  characterization, focused `/chat` desktop/tablet/mobile screenshot gate,
  `git diff --check`, and cleanup check.

## PRJ-1249 Current Evidence

- Branch: `main`.
- Lane status:
  - Backend/architecture explorer completed read-only and identified channel
    selection, tool-awareness, Telegram router, and focused test owners
  - Frontend/UX explorer completed read-only and identified the existing
    transcript metadata row as the minimal source-marker surface
  - coordinator implemented and validated the integrated slice
- Implementation:
  - `ExpressionAgent` now distinguishes false tool-capability denial from
    memory/time denial and returns a correction message instead of repeating an
    untrue "no search/browser" claim when `available_tool_hints` are loaded
  - app chat endpoint proof pins app-native messages to `reply.channel == api`
    with no Telegram client call
  - transcript projection now marks assistant rows as `telegram` when the
    delivered action included `send_telegram_message`, including scheduler
    outreach that was actually delivered through Telegram
  - Chat message metadata renders a compact text source marker: `App` or
    `Telegram`
- Validation:
  - focused backend pytest PASS: `7 passed`
  - `npm run build` in `web/` PASS
  - `npm run test:chat-transcript` PASS:
    `status=ok`, `appSourceCount=2`, `telegramSourceCount=2`
  - focused `/chat` screenshot gate PASS: `screenshot_count=3`,
    `failed_count=0`, `status=ok`
  - `git diff --check` PASS with LF/CRLF warnings only
  - cleanup check stopped validation-owned `chrome-headless-shell` leftovers
- Residual:
  - live Telegram credential smoke was not run because this task did not
    activate credentials or a real Telegram target
  - separate Dashboard mobile-flow work exists as PRJ-1248 in the worktree and
    was intentionally not folded into this mission
- Artifacts:
  - `.codex/tasks/PRJ-1249-channel-routing-tool-truth-and-source-marker.md`
  - `.codex/artifacts/prj1249-channel-source-marker/chat-route-report.json`
  - `.codex/artifacts/prj1249-channel-source-marker/screenshots/`

## Previous Mission

- Mission ID: PRJ-1248-dashboard-mobile-flow-rail
- Status: VERIFIED
- Selected objective: compress mobile Dashboard's cognitive-flow stack into a
  compact horizontal rail so lower dashboard data appears sooner.
- Why this mission now: after PRJ-1246, mobile Dashboard still stacked six flow
  steps vertically, making the route feel like a long report before Active
  Goals and the lower panels.
- Release objective or product milestone advanced: v1.2 web mobile Dashboard
  canonical usability.
- First/next checkpoint: completed a CSS-only mobile Dashboard flow pass. All
  flow steps remain available through horizontal scroll with a visible
  next-step peek, and Current Phase remains visible below the rail.
- Stop conditions: next checkpoint should stay screenshot-specific and avoid
  changing route-smoke fixture copy, backend-backed data, icon glyphs, or route
  behavior without a separate content/data decision.
- Parent validation gate: web build, Dashboard desktop/tablet/mobile
  screenshot gate, full route smoke, navigation proof, account proof, visual
  screenshot review, and cleanup check.

## PRJ-1248 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Erdos and completed read-only
  - QA/responsive lane delegated to James and completed read-only
  - coordinator implemented the mobile Dashboard CSS patch and final proof
- Implementation:
  - mobile Dashboard cognitive-flow steps now use a horizontal rail
  - supported flow steps remain available instead of being hidden
  - Current Phase is retained and compacted below the rail
- Validation:
  - `npm run build` PASS
  - Dashboard screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`
  - full route smoke PASS: `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup check found no validation-owned route-smoke, headless browser, or
    5173/4173 listener leftovers
- Residual:
  - This is a verified mobile flow-density pass, not full pixel-perfect parity.
    Exact canonical icon/content/copy parity is outside this CSS-only slice.
- Artifacts:
  - `.codex/tasks/PRJ-1248-dashboard-mobile-flow-rail.md`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/report.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/route-smoke-report.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/navigation-proof.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/account-proof.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/screenshots/`

## Previous Mission

## PRJ-1246 Current Evidence

- Branch: `main`.
- Summary: mobile Chat first-read compression is verified. The cognitive belt
  is a compact horizontal context rail, supported cards remain available by
  scroll, and transcript/composer content appears sooner.
- Validation: build, Chat desktop/tablet/mobile screenshot gate, full route
  smoke, navigation proof, account proof, cleanup, and `git diff --check`
  passed.

## PRJ-1245 Current Evidence

- Branch: `main`.
- Summary: flagship secondary chrome coherence is verified. Chat's cognitive
  belt cards/meta/progress are flatter, Personality's overview status, side
  panels, and rows are quieter, and Dashboard was intentionally not edited.
- Validation: build, Dashboard/Chat/Personality desktop/tablet/mobile
  screenshot gate, full route smoke, navigation proof, account proof, and
  `git diff --check` passed.

## PRJ-1244 Current Evidence

- Branch: `main`.
- Summary: Personality canonical fidelity is verified. Personality has lighter
  hero/callout material, flatter side panels, tighter timeline rows, calmer
  tablet support rhythm, and less visually dominant mobile callouts/rows.
- Validation: build, Personality desktop/tablet/mobile screenshot gate, full
  route smoke, navigation proof, account proof, and `git diff --check` passed.

## PRJ-1243 Current Evidence

- Branch: `main`.
- Summary: Chat canonical fidelity is verified. Chat hides nonessential
  route-status pills, uses a calmer conversation/persona split, reduces
  transcript/composer weight, renders assistant ordered lists as one calm plan
  surface, and suppresses solo quick-action/portrait-copy chrome.
- Validation: build, Chat desktop/tablet/mobile screenshot gate, full route
  smoke, navigation proof, account proof, and `git diff --check` passed.

## PRJ-1242 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Pasteur and completed read-only
  - QA/responsive lane delegated to McClintock and completed read-only
  - coordinator implemented the route-local Dashboard CSS patch and final proof
- Implementation:
  - desktop Dashboard hero uses a three-part metric/figure/metric composition
  - metric cards have visible connector lines toward the central scene
  - portrait crop was adjusted for the narrower central stage
  - tablet/mobile layout remains structurally unchanged
- Validation:
  - `npm run build` PASS
  - Dashboard screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`
  - full route smoke PASS: `route_count=14`, `status=ok`
  - `npm run audit:ui-navigation` PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
- Residual:
  - This is a verified geometry pass, not full pixel-perfect parity. Static
    reference icon glyphs and metric content are outside this CSS-only slice.
- Artifacts:
  - `.codex/tasks/PRJ-1242-dashboard-hero-geometry.md`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/report.json`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/route-smoke-report.json`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/account-proof.json`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/screenshots/`

## PRJ-1241 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Parfit and completed read-only
  - QA/responsive lane delegated to Aristotle and completed read-only
  - coordinator implemented the route-local Dashboard CSS patch and final proof
- Implementation:
  - Dashboard desktop first viewport gives the scenic hero more room and
    reduces overlay/card weight
  - guidance rail rows are lighter and less competitive with the hero
  - cognitive flow is more diagrammatic and less like a heavy control strip
  - lower Reflection card shows a clean visible subset instead of a clipped
    fourth row
- Validation:
  - `npm run build` PASS
  - Dashboard screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`
  - full route smoke PASS: `route_count=14`, `status=ok`
  - `npm run audit:ui-navigation` PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
- Residual:
  - This is a verified first-viewport lock, not full pixel-perfect parity.
    Remaining Dashboard work should focus on exact hero connector/metric
    geometry.
- Artifacts:
  - `.codex/tasks/PRJ-1241-dashboard-first-viewport-lock.md`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/report.json`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/route-smoke-report.json`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/account-proof.json`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/screenshots/`

## Previous Mission

## PRJ-1240 Current Evidence

- Branch: `main`.
- Lane status:
  - requested read-only implementation lane was run serially because no
    spawn-agent tool was available in the current runtime
  - coordinator integrated the CSS-only patch and final proof
- Implementation:
  - Dashboard hero stage is taller on desktop and metric overlays are narrower,
    lighter, and less competitive with the central figure scene
  - Chat persona panel keeps the v5 stage but reduces overlay/card dominance
    and slightly favors the right persona column without adding a third panel;
    the desktop persona overlay now keeps only the primary focus row visible
    to avoid collision with the portrait label stack
  - Personality callouts and side-panel rows are lighter while preserving the
    embodied-map structure and Aviary branding
- Validation:
  - `npm run build` PASS
  - focused route screenshot gate for `/dashboard`, `/chat`, `/personality`
    across desktop/tablet/mobile PASS: `screenshot_count=9`,
    `failed_count=0`
  - focused Chat overlay cleanup screenshot gate across desktop/tablet/mobile
    PASS: `screenshot_count=3`, `failed_count=0`
  - route smoke PASS: `route_count=14`, `status=ok`
  - `npm run audit:ui-navigation` PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup check found no route-smoke/Vite node leftovers and no
    `chrome-headless-shell` leftovers
- Residual:
  - This is a verified coherence checkpoint, not a 95% pixel-parity claim.
    Next work should tune exact screenshot mismatches by route, starting with
    Dashboard density or Chat transcript/persona asset fidelity.
- Artifacts:
  - `.codex/tasks/PRJ-1240-flagship-coherence-pass.md`
  - `.codex/artifacts/prj1240-flagship-coherence-pass/report.json`
  - `.codex/artifacts/prj1240-flagship-coherence-pass/account-proof.json`
  - `.codex/artifacts/prj1240-flagship-coherence-pass/screenshots/`
  - `.codex/artifacts/prj1240-chat-overlay-cleanup/report.json`
  - `.codex/artifacts/prj1240-chat-overlay-cleanup/account-proof.json`
  - `.codex/artifacts/prj1240-chat-overlay-cleanup/screenshots/`

## Previous Mission

- Mission ID: PRJ-1239-flagship-canonical-fidelity
- Status: VERIFIED_CHECKPOINT
- Selected objective: answer the user's canonical screenshot feedback by
  moving Dashboard, Chat, and Personality from style-inspired variants toward
  the approved canonical references.
- Why this mission now: the user correctly identified that the PRJ-1238
  screens still looked like different views with similar motifs, not convergent
  canonical screens.
- Release objective or product milestone advanced: v1.2 web UI canonical
  fidelity for the three flagship authenticated surfaces.
- First/next checkpoint: completed first fidelity checkpoint. Chat now starts
  directly from the canonical conversation scene, Dashboard/Personality no
  longer render the extra desktop utility header above the route scene, and
  Personality's overview header is lighter so the embodied map dominates.
- Stop conditions: next checkpoint should focus Dashboard primary-column
  height/right-rail balance before claiming 95% parity; do not rename Aviary to
  AION/Prometheus without product decision.
- Parent validation gate: web build, 3-route desktop/tablet/mobile screenshot
  gate, navigation proof, account proof, screenshot review, and cleanup check.

## PRJ-1239 Current Evidence

- Branch: `main`.
- Lane status:
  - visual parity audit lane delegated to Confucius and completed
  - implementation mapping lane delegated to Aquinas and completed
  - coordinator integrated the first canonical frame/proportion slice
- Implementation:
  - desktop Dashboard, Chat, and Personality no longer render the extra
    `ShellUtilityBar` above the route scene
  - route-stage spacing is collapsed for the three flagship routes so the
    canonical surface starts immediately after the sidebar shell
  - Chat workspace is taller and tighter, with compact cognitive belt cards,
    a closer 60/40 body split, tighter transcript/composer spacing, and smaller
    persona-stage overlays
  - Personality overview bar is demoted from a large card to a quieter header,
    giving the embodied map and side layers stronger first-viewport priority
  - Dashboard desktop first viewport hides the secondary recent-activity panel
    so the hero, flow, lower cards, and right guidance rail no longer create a
    large mid-page void
- Validation:
  - `npm run build` PASS
  - focused route screenshot gate for `/dashboard`, `/chat`, `/personality`
    across desktop/tablet/mobile PASS: `screenshot_count=9`, `failed_count=0`
  - route smoke PASS: `route_count=14`, `status=ok`
  - `npm run audit:ui-navigation` PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - Browser plugin rendered inspection was unavailable through tool discovery;
    route-smoke screenshots are the rendered proof for this checkpoint
- Residual:
  - Dashboard is improved but still needs finer canonical tuning for exact
    card proportions and reference-copy density before a strong 95% parity
    claim.
  - Product branding remains `Aviary`; canonical screenshots containing
    `AION` or `Prometheus` are treated as visual references, not rename
    approvals.
- Artifacts:
  - `.codex/tasks/PRJ-1239-flagship-canonical-fidelity.md`
  - `.codex/artifacts/prj1239-flagship-canonical-fidelity/report.json`
  - `.codex/artifacts/prj1239-flagship-canonical-fidelity/account-proof.json`
  - `.codex/artifacts/prj1239-flagship-canonical-fidelity/screenshots/`

## Previous Mission

- Mission ID: PRJ-1238-shared-shell-noise-reduction
- Status: COMPLETED
- Selected objective: execute the first implementation slice from the
  canonical UI simplification index by reducing shared-shell noise and
  recording route-noise decisions.
- Why this mission now: `PRJ-1237` established the UI index, and the user's
  current priority is less chaos across all views. The shared shell is the
  highest-leverage first slice because every authenticated route inherits it.
- Release objective or product milestone advanced: v1.2 web UI simplification
  on `main`.
- First/next checkpoint: completed. The next mission should run
  `PASS-SETTINGS-TOOLS`, starting with Settings hero chips/card grid or Tools
  summary/provider-plumbing noise.
- Stop conditions: completed for the shell slice. Future route slices must stop
  if a visible element cannot map to the canonical index, validation finds
  route/navigation/account regressions, or deploy/source branch drift makes
  release claims unsafe.
- Parent validation gate: web build, route-smoke syntax/route proof,
  navigation/account proof, representative responsive screenshots, and cleanup
  checks.

## PRJ-1238 Current Evidence

- Branch: `main`.
- Lane status:
  - UX/noise-audit lane delegated to Faraday.
  - Shell review lane delegated to Dirac.
  - Coordinator opened the PRJ-1238 task and started the shared-shell slice.
- Implementation:
  - desktop utility bar now keeps only current route context and account
    disclosure
  - fake search, Focus mode, Quick capture, and notification chrome removed
  - desktop sidebar health card no longer shows the duplicate diagnostics pill
  - mobile route header no longer repeats visible `Workspace` above the route
    title
  - `PASS-NOISE-AUDIT` queue recorded in
    `docs/ux/canonical-ui-layout-index.md`
- Validation:
  - `npm run build` PASS
  - `node --check scripts/route-smoke.mjs` PASS
  - `npm run audit:ui-navigation` PASS, `step_count=4`, `failed_count=0`
  - route smoke `route_count=14`, `status=ok`
  - account proof `step_count=1`, `failed_count=0`, `panel_visible=true`
  - screenshot gate `viewport_count=3`, `screenshot_count=42`,
    `failed_count=0`
  - Browser/IAB proof attempted but runtime bootstrap exited unexpectedly;
    route-smoke screenshots are the rendered proof for this checkpoint
  - validation cleanup stopped route-smoke-owned `chrome-headless-shell`
    processes
- Artifacts:
  - `.codex/tasks/PRJ-1238-shared-shell-noise-reduction.md`

## Previous Mission

- Mission ID: PRJ-1237-canonical-ui-layout-index
- Status: COMPLETED
- Selected objective: turn the user's simplification direction into a
  canonical UI layout index that maps visible groups to backend-supported
  functions and removes permission for unnecessary cards, badges, chips, and
  inert controls.
- Why this mission now: PRJ-1236 is green, but the user correctly identified
  that the web UI now needs a deeper simplification pass rather than more
  single-control polish.
- Release objective or product milestone advanced: v1.2 web UI simplification
  and future native UI generation readiness.
- First/next checkpoint: completed. The next mission should run
  `PASS-NOISE-AUDIT` or `PASS-SHELL` from
  `docs/ux/canonical-ui-layout-index.md`.
- Stop conditions: completed for the planning slice. Future implementation
  must stop if a route requires backend data not currently available or if a
  visual element cannot map to the canonical index.
- Parent validation gate: source inspection of architecture docs, canonical UX
  docs, route manifest, API contracts, and state docs completed for the
  planning artifact; route-local implementation gates remain for later tasks.

## PRJ-1237 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status:
  - Architecture/data mapping lane delegated to James, timed out, then closed.
  - UX/reference simplification lane delegated to Newton and integrated.
  - Coordinator completed the canonical UI layout index.
- Implementation:
  - `docs/ux/canonical-ui-layout-index.md` added with data authority, shell
    zones, component budget, route group IDs, first-read hierarchy, noise
    taxonomy, allowed group types, simplification order, implementation
    ownership map, and future acceptance gate.
- Validation:
  - canonical UX source set and recent proof paths reviewed
  - UX/reference lane report integrated
  - no production code rewrite started before the planning artifact
  - no backend contract invented beyond known app API data sources
- Artifacts:
  - `docs/ux/canonical-ui-layout-index.md`

## Previous Mission

- Mission ID: PRJ-1236-settings-auth-accessibility-polish
- Status: COMPLETED
- Selected objective: close the next small accessibility/interaction gap after
  PRJ-1235 by aligning auth modal mode controls and Settings form controls with
  their real behavior and accessible names.
- Why this mission now: PRJ-1235 is green, and the strongest remaining
  evidence-backed gap is not another visual redesign but incomplete auth modal
  tab semantics and under-named Settings controls.
- Release objective or product milestone advanced: local v1.2 web
  release-candidate confidence.
- First/next checkpoint: local PRJ-1236 auth/Settings accessibility polish is
  complete. The next checkpoint should tackle the Tools provider-plumbing
  first-read as a separate route-local slice.
- Stop conditions: completed. Do not reopen unless a new screenshot, keyboard,
  or route-smoke proof identifies a regression.
- Parent validation gate: `node --check scripts/route-smoke.mjs`,
  `npm run build`, route smoke for 14 routes, full screenshot gate for all 14
  routes across desktop/tablet/mobile with zero UI failures, navigation proof,
  account proof, manual Login/Auth and Settings screenshot review, and cleanup
  checks.

## PRJ-1236 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status:
  - A11y residual audit lane completed by Planck.
  - UX residual screenshot audit lane completed by Nietzsche.
  - Coordinator integrated the safe auth/Settings slice.
- Implementation:
  - auth mode controls now use segmented button semantics with `aria-pressed`
    instead of an incomplete tablist pattern
  - auth modal focuses the email field on open, traps Tab/Shift+Tab inside the
    dialog, closes on Escape, and attempts focus restore to the opener
  - Settings editable controls have explicit accessible names
  - Settings copy uses calmer product language: `Personalize Aviary`,
    `App language`, `Local time`, and labelled proactive state chips
  - desktop diagnostics support text is non-interactive status copy
  - mobile auth backdrop is slightly stronger so the modal remains primary
- Validation:
  - `node --check scripts/route-smoke.mjs` PASS
  - `npm run build` PASS
  - route smoke `route_count=14`, `status=ok`
  - full responsive screenshot gate `viewport_count=3`,
    `screenshot_count=42`, `failed_count=0`
  - navigation proof `step_count=4`, `failed_count=0`
  - account proof `step_count=1`, `failed_count=0`, `panel_visible=true`
  - manual review covered mobile Login, mobile Settings, desktop Settings, and
    desktop Dashboard
  - In-app Browser proof was attempted but blocked by no active Codex browser
    pane; route-smoke screenshots and static self-review are the current proof
  - cleanup check stopped validation-owned Vite preview process trees and found
    no remaining PRJ-1236 browser/dev-server leftovers
- Artifacts:
  - `.codex/artifacts/prj1236-settings-auth-accessibility-polish/`

## Previous Mission

- Mission ID: PRJ-1235-mobile-shell-first-viewport-polish
- Status: COMPLETED
- Selected objective: compact the authenticated mobile shell so every route
  keeps one header and one navigation while giving more first-viewport space to
  the actual product surface.
- Why this mission now: PRJ-1234 is green, and the clearest remaining
  cross-route improvement visible in screenshots is shared mobile chrome
  density rather than another route-local decoration pass.
- Release objective or product milestone advanced: local v1.2 web
  mobile-transfer confidence.
- First/next checkpoint: local PRJ-1235 mobile-shell polish is complete. The
  next checkpoint should either promote a v1.2 release candidate or take the
  next evidence-backed UX item, such as Settings control naming or auth-modal
  tab semantics.
- Stop conditions: completed. Do not reopen unless a new screenshot, keyboard,
  or route-smoke proof identifies a regression.
- Parent validation gate: `node --check scripts/route-smoke.mjs`,
  `npm run build`, route smoke for 14 routes, full screenshot gate for all 14
  routes across desktop/tablet/mobile with zero UI failures, navigation proof,
  account proof, manual mobile screenshot review, and cleanup checks.

## PRJ-1235 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status:
  - UX residual audit lane completed by Meitner.
  - Code/a11y residual audit lane completed by Euclid.
  - Coordinator integrated shared-shell, CSS, and script changes.
- Implementation:
  - mobile authenticated route header and route rail are more compact
  - module stat values use UI numeric typography
  - desktop sidebar support cards are quieter
  - desktop utility search/action chips no longer expose inert fake buttons
  - account triggers use disclosure semantics instead of `aria-haspopup="dialog"`
  - `npm run audit:ui-responsive:full` captures the current 14-route gate
- Validation:
  - `node --check scripts/route-smoke.mjs` PASS
  - `npm run build` PASS
  - route smoke `route_count=14`, `status=ok`
  - full responsive screenshot gate `viewport_count=3`,
    `screenshot_count=42`, `failed_count=0`
  - navigation proof `step_count=4`, `failed_count=0`
  - account proof `step_count=1`, `failed_count=0`, `panel_visible=true`
  - manual review covered mobile Dashboard, Tools, Settings, and desktop
    Dashboard
  - cleanup check stopped the validation-owned Vite preview process tree and
    found no remaining PRJ-1235 browser/dev-server leftovers
- Artifacts:
  - `.codex/artifacts/prj1235-mobile-shell-first-viewport-polish/`

## Previous Mission

- Mission ID: PRJ-1234-v12-flagship-last-mile-polish
- Status: COMPLETED
- Selected objective: close the final flagship canonical-detail pass for
  Dashboard, Chat, Personality, and shared shell so the v1.2 web app feels
  polished enough to be a credible mobile-app foundation and daily personality
  companion.
- Why this mission now: PRJ-1233 is green, but the repository still has a
  dedicated last-mile checklist for structural rhythm, crop/atmosphere, and
  final proof on the strongest reference-driven surfaces.
- Release objective or product milestone advanced: local v1.2 web UX
  release-candidate confidence.
- First/next checkpoint: local v1.2 flagship last-mile checkpoint is complete.
  Next mission should either prepare a v1.2 release candidate promotion or run
  a product-decision pass for mobile Chat/Personality parity choices that were
  intentionally not forced in this CSS slice.
- Stop conditions: canonical references conflict with accepted user notes; a
  view needs product behavior instead of CSS/semantics polish; responsive smoke
  reports overflow/clipping; a change would require backend, API, database,
  runtime, or production deployment work.
- Parent validation gate: `node --check scripts/route-smoke.mjs`,
  `npm run build`, route smoke for 14 routes, full screenshot gate for all 14
  routes across desktop/tablet/mobile with zero UI failures, navigation proof,
  account proof, manual screenshot review of touched flagship routes, and
  cleanup checks.

## PRJ-1234 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status:
  - UX gap, design-system, and QA/Test lanes completed read-only.
  - Coordinator integrated the safe CSS/accessibility slice and final gate.
- Implementation:
  - desktop utility chrome is lighter and less admin-like
  - Chat stage and portrait support panel spacing/elevation are calmer
  - Dashboard guidance hierarchy and wide-screen side-column pacing are tighter
  - mobile Personality restores learned-knowledge as a compact map callout
  - Personality side-stack hierarchy now emphasizes conscious state and quiets
    recent activity
  - route/account/disclosure accessibility semantics were improved
  - `--aion-display` now aliases the existing display font token
- Validation:
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - route smoke -> `route_count=14`, `status=ok`
  - full responsive screenshot gate -> `viewport_count=3`,
    `screenshot_count=42`, `failed_count=0`
  - navigation proof -> `step_count=4`, `failed_count=0`
  - account proof -> `step_count=1`, `failed_count=0`, `panel_visible=true`
  - `git diff --check` -> PASS with LF/CRLF warnings only
  - cleanup checks -> no `chrome-headless-shell`, no route-smoke/dev-server
    process, and no listeners on `5173` or `4173`
- Artifacts:
  - `.codex/artifacts/prj1234-flagship-last-mile-polish/route-smoke-report.json`
  - `.codex/artifacts/prj1234-flagship-last-mile-polish/screenshot-gate-report.json`
  - `.codex/artifacts/prj1234-flagship-last-mile-polish/navigation-proof-report.json`
  - `.codex/artifacts/prj1234-flagship-last-mile-polish/account-proof-report.json`
  - `.codex/artifacts/prj1234-flagship-last-mile-polish/screenshots/`

## PRJ-1234 Result

- Final verdict: DONE for the local v1.2 flagship last-mile UX checkpoint.
- Release caveat: this is a verified local web branch checkpoint, not a
  production v1.2 release. Production release requires a separate candidate
  promotion mission with deploy parity and production smoke.

## Previous Mission

- Mission ID: PRJ-1233-v12-web-beauty-polish-pass
- Status: COMPLETED
- Selected objective: continue past the verified v1.2 web foundation into a
  full visual polish pass so Home, Chat, Personality, Dashboard, and every
  authenticated module route feel simple, beautiful, coherent, and ready to
  inform the future mobile app.
- Why this mission now: the user explicitly asked the coordinator team to keep
  working until all web views are wonderful on mobile and desktop, using the
  strongest reference screens as the quality bar rather than stopping at smoke
  correctness.
- Release objective or product milestone advanced: v1.2 web visual readiness
  and mobile-transfer baseline.
- First/next checkpoint: v1.2 web beauty polish checkpoint is complete on the
  working branch. Next mission should either prepare a v1.2 release candidate
  or run a narrower taste pass only if new screenshots/user notes identify a
  specific remaining surface.
- Stop conditions: canonical images conflict with accepted user notes; a view
  needs product behavior instead of visual polish; responsive smoke reports
  overflow/clipping; a change would require route architecture or backend
  contract changes.
- Parent validation gate: `node --check scripts/route-smoke.mjs`,
  `npm run build`, route smoke, full screenshot gate for all 14 routes across
  desktop/tablet/mobile with zero UI failures, navigation proof, account
  proof, visual screenshot review, and cleanup checks.

## PRJ-1233 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status: UX spec, flagship frontend, module-surface, and QA visual gate
  lanes completed and integrated into
  `.codex/tasks/PRJ-1233-v12-web-beauty-polish-pass.md`.
- Implementation:
  - mobile Chat now reduces pre-thread cognitive cards so the transcript
    appears sooner
  - mobile Home hides duplicated hero micro-proof chips while preserving the
    scenic hero, CTAs, callouts, feature bridge, and trust closure
  - mobile Personality reduces figure-covering callouts
  - tablet/mobile Chat persona notes are quieter
  - module routes use compact mobile stat rows, bringing unique route content
    higher in the first scroll
  - Tools mobile summary/detail density is reduced
  - Automations/Integrations desktop scenic whitespace is tightened
  - all module routes are included in the route-manifest screenshot contract
- Validation:
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - route smoke -> `route_count=14`, `status=ok`
  - full responsive screenshot gate -> `viewport_count=3`,
    `screenshot_count=42`, `failed_count=0`
  - navigation proof -> `step_count=4`, `failed_count=0`
  - account proof -> `step_count=1`, `failed_count=0`
  - screenshot review covered mobile Home, Chat, Personality, Memory, Tools,
    and desktop Chat/Integrations.
- Artifacts:
  - `.codex/artifacts/prj1233-web-ui-polish-pass/route-smoke-report.json`
  - `.codex/artifacts/prj1233-web-ui-polish-pass/screenshot-gate-report.json`
  - `.codex/artifacts/prj1233-web-ui-polish-pass/navigation-proof-report.json`
  - `.codex/artifacts/prj1233-web-ui-polish-pass/account-proof-report.json`
  - `.codex/artifacts/prj1233-web-ui-polish-pass/screenshots/`

## PRJ-1233 Result

- Final verdict: DONE for the local v1.2 web beauty polish checkpoint.
- Release caveat: this is a verified local web branch checkpoint, not a
  production v1.2 release. Production release requires a separate candidate
  promotion mission with deploy parity and production smoke.

## Previous Mission

- Mission ID: PRJ-1232-v12-web-canonical-ui-system
- Status: COMPLETED
- Selected objective: build v1.2 web UI toward the canonical documentation
  references across mobile and desktop, using the web implementation as the
  foundation for the future mobile app. The work must be functional,
  polished, and free of unnecessary decorative or explanatory clutter.
- Why this mission now: v1.1.1 is released; the user explicitly requested v1.2
  frontend improvement with agent coordination, canonical images from docs,
  and all web views supervised across mobile and desktop.
- Release objective or product milestone advanced: v1.2 canonical web UI
  baseline for future native/mobile app transfer.
- First/next checkpoint: v1.2 web canonical UI checkpoints are complete on the
  working branch. Next mission should either prepare a v1.2 release candidate
  or perform a narrower visual taste pass from fresh screenshot review.
- Stop conditions: canonical references conflict; a route lacks enough spec to
  claim parity; validation cannot capture desktop/mobile screenshots; broad
  refactor risk exceeds the first batch; production v1.1.1 marker would be
  disturbed.
- Parent validation gate: per batch `npm run build`,
  `npm run audit:ui-responsive`, `npm run audit:ui-navigation`,
  route/account smoke where relevant, visual screenshot comparison against
  canonical assets, and cleanup checks for browser/dev-server leftovers.

## PRJ-1232 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status: UX spec, frontend architecture, and QA visual-gate explorer
  lanes completed and integrated into
  `.codex/tasks/PRJ-1232-v12-web-canonical-ui-system.md`.
- Foundation implementation:
  - added `web/src/route-manifest.json` as the shared route/marker source for
    web route contracts and smoke proof
  - derived `ROUTES` and route markers from the manifest in `web/src/routes.ts`
  - updated `web/scripts/route-smoke.mjs` to consume the same manifest and to
    use manifest markers for navigation/account proof
  - improved mobile Chat by replacing the narrow-screen clipped context belt
    with stacked, readable context cards
  - refined route-smoke overflow detection so contained intentional scrollers
    do not mask or misreport document-level overflow checks
  - removed transform scaling from the public landing scenic background so
    `/` and `/login` no longer report decorative out-of-viewport elements
- Validation:
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - route smoke -> `route_count=14`, `status=ok`
  - responsive screenshots -> `screenshot_count=18`, `failed_count=0`
  - mobile foundation screenshots for `/chat`, `/settings`, `/dashboard` ->
    `failed_count=0`, `overflowingElementCount=0`
  - navigation proof -> `step_count=4`, `failed_count=0`
  - account proof -> `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - public Home/Login gate -> `screenshot_count=4`, `failed_count=0`,
    `overflowingElementCount=0` across desktop/mobile `/` and `/login`
  - Shell/Dashboard batch disambiguated mobile/tablet Dashboard labels from
    public Home and tightened desktop Dashboard density; focused gate
    `screenshot_count=3`, `failed_count=0`.
  - Chat batch lightened the desktop cognitive belt; focused gate
    `screenshot_count=3`, `failed_count=0`.
  - Personality batch improved desktop/mobile hero rhythm and compact mobile
    overview status; focused gate `screenshot_count=3`, `failed_count=0`.
  - Final responsive gate covered public, flagship, and module routes:
    `screenshot_count=39`, `failed_count=0`.
- Artifacts:
  - `.codex/artifacts/prj1232-route-smoke/report.json`
  - `.codex/artifacts/prj1232-web-responsive-visual-gate/report.json`
  - `.codex/artifacts/prj1232-mobile-foundation-gate/report.json`
  - `.codex/artifacts/prj1232-navigation-proof/report.json`
  - `.codex/artifacts/prj1232-account-proof/report.json`
  - `.codex/artifacts/prj1232-public-home-gate/report.json`
  - `.codex/artifacts/prj1232-dashboard-shell-gate/report.json`
  - `.codex/artifacts/prj1232-chat-belt-gate/report.json`
  - `.codex/artifacts/prj1232-personality-hero-gate/report.json`
  - `.codex/artifacts/prj1232-final-route-smoke/report.json`
  - `.codex/artifacts/prj1232-final-responsive-gate/report.json`

## PRJ-1232 Result

- Final verdict: DONE for the v1.2 web/mobile foundation checkpoints.
- Release caveat: this is a verified web branch checkpoint, not a production
  v1.2 release. Production release requires a separate candidate promotion
  mission with deploy parity and release smoke.
- Residual non-blocking note: exact pixel-perfect parity is not claimed for
  every canonical reference; future refinements should be taste/precision
  passes, not blockers for the functional responsive web foundation.

## Previous Mission

- Mission ID: PRJ-1231-v1-production-candidate-promotion
- Status: COMPLETED
- Selected objective: turn locally verified selected-scope v1 into a real
  production-backed release fact by committing the refreshed candidate,
  publishing it to the deploy source, proving deployed revision parity, running
  production release smoke, and recording the final marker posture.
- Why this mission now: the user asked the coordinator to keep working until
  v1 is fact, and PRJ-1230 proved only local selected-scope readiness. The
  release boundary requires deploy parity and production smoke before any new
  release claim.
- Release objective or product milestone advanced: production-backed v1
  selected-scope marker for the current web-supported candidate.
- First/next checkpoint: v1 selected-scope is released as `v1.1.1`; next work
  should either monitor production or explicitly expand deferred extension
  scope.
- Stop conditions: git push is unavailable; deploy target/source branch cannot
  be confirmed; Coolify webhook/auto-deploy access is unavailable and
  production remains on an older SHA; release smoke fails; backend/web revision
  parity drifts; tag creation would point at an unproven SHA.
- Parent validation gate: completed. Local PRJ-1230 gate remained green;
  pre-push `git diff --check` passed; production release smoke with deploy
  parity passed; release reality audit returned `GO_FOR_SELECTED_SHA`;
  selected-tag go/no-go for `v1.1.1` returned `GO`.

## PRJ-1231 Release Result

- Selected SHA: `df677370f63d2688eb792f9a3a846d2cd40a564b`
- Release tag: `v1.1.1`
- Deploy source: `origin/main`
- Production URL: `https://aviary.luckysparrow.ch`
- Production proof: backend runtime revision and web shell build revision both
  match selected SHA; `release_ready=true`; no release violations; v1 final
  acceptance state `core_v1_bundle_ready`.
- Final verdict: `released`

## Previous Mission

- Mission ID: PRJ-1230-v1-selected-scope-final-readiness-refresh
- Status: COMPLETED
- Selected objective: refresh the selected-scope v1 readiness claim against the
  current workspace, coordinate lane findings, run the parent validation gate,
  and record whether v1 remains `verified`, `partially verified`, or `blocked`.
- Why this mission now: the user asked the coordinator to finish v1 using
  agents; the existing dashboard says selected-scope readiness is `11/11`, but
  the dated evidence is from 2026-05-14 and must not be silently reused for the
  current branch.
- Release objective or product milestone advanced: selected-scope v1 closure
  / web-supported release confidence.
- First/next checkpoint: selected-scope v1 local readiness is refreshed; next
  checkpoint is production candidate promotion only if a deploy target is
  selected.
- Stop conditions: a P0/P1 selected-scope blocker appears; architecture and
  implementation conflict; parent validation fails in a way that requires a
  product or deployment decision; production release parity is requested but
  target credentials/environment are unavailable.
- Parent validation gate: `git diff --check`; full backend pytest; web
  typecheck/build/responsive audit/navigation audit/route smoke; architecture
  dashboard refresh. Production release smoke is required only if this mission
  selects a new deployable release candidate.

## Source Rows

- Task board: latest completed UI slice `PRJ-1229`; next residual Dashboard
  lower-card proportions / first-viewport density.
- Planning: `docs/planning/current-v1-release-boundary.md`;
  `docs/planning/next-iteration-plan.md`.
- Delivery map: selected-scope v1 web-supported closure; native and provider
  extensions remain deferred unless scope is reactivated.
- Requirements: `REQ-UX-001`, `REQ-MOB-001`, `REQ-AI-001..003`.
- Quality scenarios: web route rendering and release readiness gates.
- Risks: deferred provider activation, proactive target sample, deploy
  automation convergence, and native mobile proof are nonblocking selected
  scope rows.
- Module confidence: `AVIARY-WEB-RESP-001`, `AVIARY-STATUS-001`,
  `AVIARY-COGNITIVE-RUNTIME-001`, `AVIARY-MEMORY-001`.
- System health: latest dated evidence from 2026-05-14 needs refresh if this
  branch becomes the active v1 closure basis.
- Architecture / UX / security / ops sources:
  `docs/operations/project-status-dashboard.md`,
  `docs/operations/v1-selected-scope-handoff-2026-05-11.md`,
  `docs/ux/screen-quality-checklist.md`, `docs/ux/design-memory.md`,
  `docs/operations/runtime-ops-runbook.md`.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Output | Validation/proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, mission control, project memory, state files | Integration, task closure, source-of-truth updates | Mission packet, task contract, final readiness decision | Parent validation gate | COMPLETED |
| Product/Requirements | Coordinator | Current v1 boundary, requirements matrix | Scope, accepted assumptions, exclusions | Selected-scope definition and deferred extension list | Requirements trace review | COMPLETED |
| Architecture | Coordinator | Project status dashboard, architecture audit | Architecture readiness posture | Alignment or mismatch note | Dashboard refresh | COMPLETED |
| Frontend/UX | UX explorer, then coordinator | UX refs, screenshots, web route files | Dashboard lower-row density refresh and route-smoke harness hardening | Web audit/screenshot proof | COMPLETED |
| Backend/API | Coordinator | Runtime confidence rows, backend tests | No backend code planned | Runtime gate status | Full backend pytest | COMPLETED |
| QA/Test | QA explorer, then coordinator | Known issues, system health, module confidence | Read-only gate report | Parent validation command set and blocker posture | Integrated into task evidence | COMPLETED |
| Security/Ops/Docs | Coordinator | Release boundary, ops runbook, security protocol | Release/ops evidence notes and state updates | Candidate versus non-candidate release posture | Smoke/deploy risk note | COMPLETED |
| Documentation/Memory | Coordinator | Task board, project state, ledgers | Active mission, PRJ-1230 task, state summaries | Durable handoff and next checkpoint | Source-of-truth diff review | COMPLETED |

## Delegation Plan

- Lanes kept local: coordination, final integration, shared state updates,
  parent validation, final `DONE`/blocked decision.
- Lanes delegated: QA/Release read-only blocker/gate report; Frontend/UX
  read-only next-slice report.
- Lanes intentionally omitted and why: Data/Migrations, Security deep review,
  and provider Ops smoke are omitted unless validation discovers a selected
  scope change; no schema, secrets, auth, permissions, or provider execution
  change is planned.
- Known overlap risks: avoid editing `.codex/context/PROJECT_STATE.md` over
  existing user governance additions; keep subagents read-only unless a later
  lane is explicitly given a disjoint write set.
- Forbidden files or surfaces: no provider credential activation, no native
  mobile proof work, no new web shell, no architecture rewrite, no temporary
  bypasses.

## Acceptance

- [x] Every important responsibility from source docs has an owner or explicit omission.
- [x] No two write lanes own the same file or shared registry.
- [x] Each lane has expected output and validation/proof.
- [x] Parent validation will run after accepted lane integration.
- [x] Missing or unclear ownership will be recorded in `.agents/state/responsibility-learning.md`.
- [x] Process quality will be evaluated in `.agents/state/agent-evals.md` when
      this mission is broad, repeated, partial, or subagent-heavy.

## Checkpoint Log

| Date | Checkpoint | Result | Evidence | Next action |
| --- | --- | --- | --- | --- |
| 2026-05-22 | Mission opened | Multi-lane coordinator mission created after user asked to finish v1 with agents. | Active mission packet; QA/Release and UX read-only lanes delegated. | Create task contract and run/record parent gate. |
| 2026-05-22 | Lane integration | QA confirmed no selected-scope blockers and UX identified Dashboard lower-row density as the smallest polish slice. | Subagent lane reports; PRJ-1230 task contract. | Patch the focused web slice and harden route-smoke fallback. |
| 2026-05-22 | Parent validation | COMPLETED: selected-scope v1 remains locally verified for this branch. | `git diff --check` PASS with LF/CRLF warnings only; backend `1105 passed`; web build/responsive/navigation/account/route smoke PASS; architecture dashboard `11/11`; screenshot review; cleanup no leftovers. | Promote only after explicit production deploy target/parity smoke. |

