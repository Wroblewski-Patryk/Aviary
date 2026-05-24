# Project Memory Index

Last updated: 2026-05-24

## Project Alias

The product name is Aviary. The repository folder is still `Personality`
because the folder has not been renamed yet. Agents must treat `Aviary` and
`Personality` as the same project in this workspace.

## Purpose

This file is the mandatory full-picture protocol for agents. It prevents the
project from drifting into repeated small fixes with no clear release progress.
Every non-trivial task must connect local code changes to the current product
state, architecture intent, module confidence, and the next release objective.

## Latest Graph Evidence Additions

- `PRJ-1300` enforced curated architecture graph zero-gap posture in CI:
  `.github/workflows/architecture-graph.yml` now runs
  `query_architecture_graph.py --gaps --format json` and fails when any
  curated gap rows exist. This turns local zero-gap posture into a merge/release gate.
- `PRJ-1299` closed the curated architecture gap queue to zero:
  global `query_architecture_graph.py --gaps --limit 20` now reports
  `no gaps detected` on latest generated graph artifacts.
- `PRJ-1296` closed Personality overview direct proof gaps:
  `API-PERSONALITY-OVERVIEW` and `PAGE-PERSONALITY` now have direct evidence
  rows and query with `Gaps: none`; existing
  `CHAIN-PERSONALITY-OVERVIEW` remains the execution chain.
- `PRJ-1295` closed profile/settings direct proof gaps:
  `API-APP-ME`, `MODEL-AION-PROFILE`, and `PAGE-SETTINGS` now have direct
  evidence rows and query with `Gaps: none`; existing
  `CHAIN-PROFILE-SETTINGS` remains the execution chain.
- `PRJ-1294` closed runtime agent-stage evidence gaps:
  `AGENT-AFFECTIVE-ASSESSMENT`, `AGENT-CONTEXT`, `AGENT-MOTIVATION`,
  `AGENT-PERCEPTION`, `AGENT-PLANNING`, and `AGENT-ROLE` now have direct
  local stage-contract evidence rows and query with `Gaps: none`.
- `PRJ-1293` closed small curated medium-risk proof gaps:
  `API-TOOLS-OVERVIEW`, `DOC-PIPELINE-APP-CHAT`, and
  `TEST-WEB-ROUTE-SMOKE` now have direct evidence rows and query with
  `Gaps: none`. `CHAIN-TOOLS-OVERVIEW` no longer treats live provider
  credential activation as a missing local overview link; it remains residual
  external-provider proof.
- `PRJ-1292` closed core service/test/prompt evidence gaps:
  `PROMPT-OPENAI-RUNTIME`, `SERVICE-MEMORY-REPOSITORY`,
  `SERVICE-RUNTIME-ORCHESTRATOR`, `TEST-API-ROUTES`,
  `TEST-MEMORY-REPOSITORY`, `TEST-RUNTIME-PIPELINE`, and
  `TEST-SCHEMA-BASELINE` now query with `Gaps: none` through focused local
  proof rows.
- `PRJ-1291` closed runtime/memory documentation and feature-anchor graph
  gaps: `DOC-RUNTIME-FLOW`, `DOC-MEMORY-SYSTEM`, `FEAT-EVENT-INGRESS`,
  `FEAT-FOREGROUND-RUNTIME`, and `FEAT-MEMORY-FLOW` now query with
  `Gaps: none` through new documentation/feature evidence rows and an updated
  `CHAIN-EVENT-INGRESS`.
- `PRJ-1290` closed the App Chat API/Event curated audit gaps:
  `API-APP-CHAT-MESSAGE` now has evidence `EVID-APPCHAT-API-PROOF`,
  `EVENT-APP-CHAT-TURN` now has evidence `EVID-APPCHAT-EVENT-PROOF`, and
  `CHAIN-APP-CHAT-MESSAGE` treats native binary upload as future scope outside
  the verified current text/serialized-attachment chain. Node queries now
  report `Gaps: none` for both nodes.
- `PRJ-1289` closed the Event Ingress API curated audit gap:
  `API-EVENT-INGRESS` now has test relation `REL-EVENT-002` and evidence
  `EVID-EVENT-INGRESS-API-PROOF` backed by focused event endpoint and runtime
  API source tests. A node query now reports `Gaps: none`.
- `PRJ-1288` closed the AionMemory model curated audit gap:
  `MODEL-AION-MEMORY` now has relation `REL-MEMORY-001`, evidence
  `EVID-AION-MEMORY-MODEL-PROOF`, and query gap attribution no longer
  over-reports feature-level future-scope missing links on model nodes. A node
  query now reports `Gaps: none`.
- `PRJ-1287` closed the data model curated audit gap:
  `FEAT-DATA-MODEL` now has docs relation `REL-DATA-004`, verified chain
  `CHAIN-DATA-MODEL-SCHEMA`, and evidence
  `EVID-DATA-MODEL-SCHEMA-CHAIN` backed by schema baseline tests. A node
  query now reports `Gaps: none`.
- `PRJ-1286` closed the first high-risk curated audit gap:
  `API-APP-AUTH` now has relations `REL-AUTH-001..004`, verified chain
  `CHAIN-APP-AUTH`, and evidence `EVID-AUTH-API-CHAIN-REFRESH` backed by
  focused auth API tests. A node query now reports `Gaps: none`.
- `PRJ-1285` verified architecture graph gap audit mode:
  `query_architecture_graph.py --gaps` produces a curated missing-proof queue
  for nodes with missing evidence, chain, docs/tests, or research-support
  signals. Auto-inventory rows are excluded by default; `--include-auto` is
  available for deliberate broad inventory audits. Evidence:
  `EVID-ARCH-GRAPH-GAP-AUDIT`.
- `PRJ-1284` verified the architecture graph query CLI:
  `backend/scripts/query_architecture_graph.py` can inspect a generated graph
  node's details, incoming/outgoing impact, chains, evidence, theory claims,
  and proof gaps. It is mapped as `SCRIPT-QUERY-ARCH-GRAPH` with tests
  `TEST-ARCH-GRAPH-QUERY` and evidence `EVID-ARCH-GRAPH-QUERY-CLI`.
  The CLI reads generated JSON as a read model; CSV remains canonical.
- `PRJ-1283` verified the architecture graph PR template checklist:
  `.github/pull_request_template.md` now asks graph-relevant authors to report
  registry, chain, evidence, research, generated artifact, and fast graph gate
  posture. The checklist is mapped as `DOC-PR-TEMPLATE` with evidence
  `EVID-ARCH-PR-TEMPLATE-CHECKLIST`. This is review guidance and does not
  replace generator pytest, hosted CI, or runtime/user-journey proof.
- `PRJ-1282` verified the architecture graph CI policy:
  `.github/workflows/architecture-graph.yml` now runs inventory regeneration,
  graph regeneration, committed-artifact diff checks, and the fast graph
  pytest gate for graph-relevant PR/push changes, with manual
  `workflow_dispatch` heavy mode. The policy is mapped as
  `WORKFLOW-ARCH-GRAPH-CI` with evidence
  `EVID-ARCH-GRAPH-CI-POLICY`. Hosted Actions proof is optional supplementary
  evidence under `DEC-005`.
- `PRJ-1281` verified the Personality learned-state overview execution chain:
  `CHAIN-PERSONALITY-OVERVIEW` now has fresh proof across `/personality` route
  rendering, `/app/personality/overview`, memory repository learned-state
  backing, generated graph artifacts, and graph pytest pins. Curated
  `chains.csv` has no remaining `partial` rows.
- `PRJ-1280` verified the Tools overview execution chain:
  `CHAIN-TOOLS-OVERVIEW` now has fresh proof across `/tools` route rendering,
  `/app/tools/overview`, `/app/tools/preferences`, connector policy tests,
  localized Tools directory browser characterization, generated graph
  artifacts, and graph pytest pins. Live provider credentials remain a
  separate deferred proof scope.
- `PRJ-1279` verified the profile/settings execution chain:
  `CHAIN-PROFILE-SETTINGS` now has fresh proof across `/settings` route
  rendering, `/app/me` backend settings behavior, profile/preference tests,
  generated graph artifacts, and graph pytest pins.
- `PRJ-1278` verified the architecture graph workflow mechanics themselves:
  `WORKFLOW-ARCH-GRAPH`, `SCRIPT-GENERATE-ARCH-GRAPH`,
  `TEST-ARCH-GRAPH-GENERATOR`, `REL-GRAPH-003`, and
  `CHAIN-ARCH-GRAPH-WORKFLOW` are now verified with closure evidence. This
  does not claim full semantic curation for every feature; it closes the map
  generation workflow.
- `PRJ-1277` verified the first concrete UX/UI research-backed graph claim:
  `UI-CHAT-COGNITIVE-BELT` now links to
  `CLAIM-CHAT-COGNITIVE-BELT-LOAD-AWARENESS` with three reviewed sources for
  working memory, visual working memory, and attentional load. This is design
  rationale only; UI behavior and usability still require separate route,
  screenshot, accessibility, or usability proof.
- `PRJ-1276` verified fast and heavy graph validation modes: everyday agents
  can run `tests/test_architecture_graph_generator.py -m "not slow"` while
  release-level graph confidence can still run full all-node parity.
- `PRJ-1268` verified the research evidence mapping layer:
  `docs/architecture/registry/research_sources.csv`,
  `docs/architecture/registry/theory_claims.csv`,
  generated `docs/testing/architecture-research-map.md`, and graph generator
  validation for reviewed/mapped theory claims with at least 3 source IDs.
- `PRJ-1267` verified the whole-repository architecture inventory layer:
  generated `auto_nodes.csv` and `auto_relations.csv` are broad map coverage,
  while curated chains/evidence remain the higher-confidence proof layer.

## Required Indexes

Agents must keep these indexes current enough that another Codex session can
continue from repository files alone:

- `.codex/context/PROJECT_STATE.md`: where Aviary is now, current phase,
  validation commands, deployment shape, and known runtime reality.
- `docs/operations/project-status-dashboard.md` and
  `docs/operations/project-status-dashboard.json`: generated project radar when
  available.
- `.codex/context/TASK_BOARD.md`: canonical task queue with `NOW`, `NEXT`,
  blockers, and done evidence.
- `.agents/state/module-confidence-ledger.md`: module-by-module confidence,
  working state, evidence, and next proof or fix.
- `.agents/state/system-health.md`: latest validation, broken journeys, stale
  checks, and environment state.
- `.agents/state/known-issues.md`: real unresolved defects, not vague concerns.
- `.agents/state/next-steps.md`: next executable tasks in priority order.
- `docs/architecture/`: current architecture truth.
- `docs/modules/`, `docs/pipelines/`, and route/component maps when present:
  implementation ownership and surface maps.
- `docs/planning/`: release plan and task sequencing.
- `docs/operations/`: release, deploy, smoke, rollback, and target-environment
  evidence. Current runtime-layer audit:
  `docs/operations/aion-runtime-layer-audit-2026-05-13.md`.

If one of these files is missing, empty, stale, or still template-like, rebuild
the minimum useful version from architecture docs, context files, accepted
feedback, code, tests, and planning notes before choosing implementation work.
Every inferred row must name its source and use a cautious status.

## Current High-Signal Entries

- `PRJ-1283` added review-time graph governance to the existing PR template:
  `DOC-PR-TEMPLATE` and `EVID-ARCH-PR-TEMPLATE-CHECKLIST` now appear in
  generated graph JSON, the evidence map, and Obsidian node pages. Latest
  inventory plus graph generation passed with `auto_nodes=5238`,
  `auto_relations=3935`, merged `nodes=5297`, `relations=3988`,
  `chains=7`, `evidence=20`, `research_sources=21`, and `theory_claims=9`;
  fast graph pytest passed with `8 passed, 1 deselected in 4.64s`.

- `PRJ-1282` added durable CI policy for graph validation:
  `WORKFLOW-ARCH-GRAPH-CI` and `EVID-ARCH-GRAPH-CI-POLICY` record the
  automatic fast gate and manual heavy gate. Latest inventory plus graph
  generation passed with `auto_nodes=5237`, `auto_relations=3935`,
  merged `nodes=5295`, `relations=3986`, `chains=7`, `evidence=19`,
  `research_sources=21`, and `theory_claims=9`; fast graph pytest passed
  with `8 passed, 1 deselected in 2.82s`; generated graph JSON, evidence
  map, and node page include the CI policy.

- `PRJ-1281` promoted the remaining curated partial chain into verified
  evidence: `CHAIN-PERSONALITY-OVERVIEW` and
  `EVID-PERSONALITY-OVERVIEW-CHAIN-REFRESH` record backend personality API
  pytest `1 passed, 131 deselected in 5.26s`, memory repository focused pytest
  `2 passed, 71 deselected in 3.67s`, web build PASS, route smoke
  `route_count=14`, `status=ok`, `/personality` marker
  `aion-personality-canvas` passed, graph generation `nodes=5292`,
  `relations=3983`, `chains=7`, `evidence=18`, `research_sources=21`,
  `theory_claims=9`, and fast graph pytest
  `8 passed, 1 deselected in 4.85s`.

- `PRJ-1280` promoted the Tools overview chain into verified evidence:
  `CHAIN-TOOLS-OVERVIEW` and `EVID-TOOLS-OVERVIEW-CHAIN-REFRESH` record
  backend focused pytest `12 passed, 126 deselected in 24.09s`, web build
  PASS, localized Tools directory characterization PASS for full/toggle/
  telegram_link_start/loading/empty/error states, route smoke PASS, graph
  generation `nodes=5291`, `relations=3983`, `chains=7`, `evidence=17`,
  `research_sources=21`, `theory_claims=9`, and fast graph pytest
  `8 passed, 1 deselected in 9.99s`.

- `PRJ-1279` promoted a stale partial functional chain into verified evidence:
  `CHAIN-PROFILE-SETTINGS` and
  `EVID-PROFILE-SETTINGS-CHAIN-REFRESH` record backend focused pytest
  `10 passed, 127 deselected in 3.32s`, web build PASS, route smoke
  `route_count=14`, `status=ok`, `/settings` marker
  `aion-settings-canvas` passed, graph generation `nodes=5286`,
  `relations=3979`, `chains=7`, `evidence=16`, `research_sources=21`,
  `theory_claims=9`, and fast graph pytest
  `8 passed, 1 deselected in 3.69s`.

- `PRJ-1278` verified the graph workflow's own confidence state:
  `EVID-ARCH-GRAPH-WORKFLOW-CLOSURE` records that the generator, registry,
  generated artifacts, research mapping, and fast/heavy pytest workflow are
  operational. Latest graph generation passed with `nodes=5285`,
  `relations=3979`, `chains=7`, `evidence=15`, `research_sources=21`, and
  `theory_claims=9`; fast graph pytest passed with
  `8 passed, 1 deselected in 4.02s`; heavy graph pytest passed with
  `9 passed in 127.74s`.

- `PRJ-1277` verified scoped UX research mapping for the Chat cognitive belt:
  `docs/architecture/registry/nodes.csv`, `relations.csv`,
  `research_sources.csv`, `theory_claims.csv`, and `evidence.csv` now include
  `UI-CHAT-COGNITIVE-BELT`,
  `CLAIM-CHAT-COGNITIVE-BELT-LOAD-AWARENESS`, and
  `EVID-RESEARCH-UI-CHAT-COGNITIVE-BELT`. Latest graph generation passed with
  `nodes=5284`, `relations=3979`, `evidence=14`,
  `research_sources=21`, and `theory_claims=9`; fast graph pytest passed with
  `8 passed, 1 deselected`; heavy graph pytest passed with
  `9 passed in 255.06s`.

- `PRJ-1267` verified the whole-repository architecture inventory layer:
  `backend/scripts/generate_architecture_inventory.py` now generates
  `docs/architecture/registry/auto_nodes.csv`,
  `docs/architecture/registry/auto_relations.csv`, and
  `docs/architecture/registry/auto_inventory_summary.md`. The graph generator
  merges curated and auto rows. Latest full run passed with
  `auto_nodes=5197`, `auto_relations=3915`, merged `nodes=5249`,
  `relations=3954`, `chains=7`, and `evidence=9`. Auto rows are broad
  inventory, not release-critical proof; promote them into curated chains and
  evidence before using them for confidence claims.

- `PRJ-1266` verified the architecture graph evidence system foundation:
  `docs/architecture/graph-system.md`, CSV registries under
  `docs/architecture/registry/`, and
  `backend/scripts/generate_architecture_graph.py` now provide the first
  Obsidian-compatible node/relation/chain/evidence graph. The generator passed
  with `nodes=52`, `relations=39`, `chains=7`, and `evidence=9`. This is a
  foundation, not exhaustive whole-repo coverage; future feature work must
  update graph rows before treating behavior as officially mapped.

- `PRJ-1229` verified authenticated desktop utility bar parity: desktop
  authenticated routes now show the shared utility/search/action/account band
  above route content, reusing the existing `ShellUtilityBar` and
  `aion-utility-*` styles without adding fake browser controls or changing
  mobile/tablet headers. Web build, responsive audit, navigation audit,
  account proof, desktop Dashboard/Chat screenshot review, tablet/mobile
  guardrail review, and validation cleanup passed.

- `PRJ-1228` verified Dashboard desktop hero overlay parity: desktop
  Dashboard signal card columns now overlay the scenic figure stage instead of
  sitting as detached side columns, and desktop-only figure-note callouts are
  hidden so the metric overlay becomes the primary canonical card language.
  Web build, responsive audit, navigation audit, account proof, and
  desktop/tablet/mobile Dashboard screenshot review passed.

- `PRJ-1227` verified desktop sidebar support rhythm: authenticated desktop
  sidebar support cards now follow the navigation stack with a modest
  canonical gap instead of being pushed to the viewport bottom. This moves the
  shared shell closer to
  `docs/ux/assets/aviary-sidebar-layout-canonical-reference-v1.png` without
  changing route behavior, mobile/tablet headers, auth, APIs, backend, runtime,
  or deployment. Web build, responsive audit, navigation audit, account proof,
  and screenshot review passed.

- `PRJ-1226` verified tablet route header rhythm: authenticated tablet
  headers now align the Aviary wordmark, route identity, and account trigger in
  one compact row above the shared route rail while phone mobile headers and
  desktop sidebar remain unchanged. Route-smoke now waits for the route marker
  after `#root` attaches before saving screenshots, preventing false
  loading-state captures. Web build, responsive audit, navigation audit,
  account proof, screenshot review, and validation cleanup passed.

- `PRJ-1225` verified mobile/tablet account trigger polish: authenticated
  route headers now use a dedicated Aviary shell material trigger with
  `aria-expanded` state instead of generic outline button styling, and
  route-smoke has an optional `--account-proof` that clicks the mobile account
  trigger and verifies the panel appears. Web build, responsive audit,
  navigation audit, account proof, screenshot review, and validation cleanup
  passed.

- `PRJ-1224` verified shared shell navigation affordance: tablet/mobile route
  rails now show a subtle continuation affordance, scroll snapping, and end
  padding while desktop sidebar structure and route behavior remain unchanged.
  Web build, responsive audit, navigation audit, representative
  desktop/tablet/mobile screenshot review, and validation cleanup passed.

- `PRJ-1223` verified Dashboard Memory Growth label readability: compact chart
  labels now stay visually separated in the narrow desktop card while
  desktop/tablet/mobile Dashboard composition remains stable. Web build,
  responsive audit, focused `/dashboard` route-smoke screenshot review,
  navigation audit, and validation cleanup passed.
- `PRJ-1222` verified Tools integral status deduplication: Tools item cards now
  suppress supplemental integral pills when they duplicate the primary status
  label, so `Internal chat` shows one clear `Always on` state while capability
  details remain visible. Web build, responsive audit, focused `/tools`
  desktop/tablet/mobile route-smoke screenshot review, navigation audit, and
  validation cleanup passed.
- `PRJ-1221` verified Settings save action hierarchy: Settings `Save settings`
  now uses a route-local calm teal primary style instead of warning-like amber,
  while reset runtime data remains visually distinct. Web build, responsive
  audit, focused `/settings` desktop/tablet/mobile route-smoke screenshot
  review, navigation audit, and validation cleanup passed.
- `PRJ-1220` verified mobile Chat assistant response width: mobile assistant
  answers now use the full transcript width by hiding the decorative avatar on
  narrow screens while preserving speaker metadata. Web build, responsive
  audit, focused `/chat` desktop/tablet/mobile route-smoke screenshot review,
  navigation audit, and validation cleanup passed.
- `PRJ-1219` verified Tools summary numeric readability: summary count values
  now use unambiguous UI typography with tabular numbers, so mobile `1` no
  longer reads like the letter `I`. Web build, responsive audit, navigation
  audit, desktop/tablet/mobile Tools screenshot review, and validation cleanup
  passed.
- `PRJ-1218` verified Dashboard recent activity timestamp readability: compact
  `Recent Activity` timestamps now use calmer metadata typography in narrow
  right-rail contexts, removing awkward tablet uppercase fragmentation while
  preserving desktop/mobile Dashboard layouts. Web build, responsive audit,
  navigation audit, desktop/tablet/mobile Dashboard screenshot review, and
  validation cleanup passed.
- `PRJ-1217` verified Chat tablet transcript clearance: tablet-only CSS now
  tightens transcript/list-card/input spacing so the long assistant route-smoke
  answer clears the composer in the first viewport. Web build, responsive
  audit, navigation audit, desktop/tablet/mobile Chat screenshot review, and
  validation cleanup passed.
- `PRJ-1216` verified Chat cognitive belt readability: the Motivation card now
  renders dense motivation metrics as structured compact lines rather than one
  slash-separated string, removing desktop first-viewport truncation while
  preserving the desktop, tablet, and mobile belt layouts. Web build,
  responsive audit, navigation audit, desktop/tablet/mobile Chat screenshot
  review, and validation cleanup passed.
- `PRJ-1215` verified mobile Chat context rail readability: the horizontal
  cognitive belt keeps conversation-first rhythm while using tuned card width,
  body line clamp, scroll padding, and edge masking so the first card reads
  clearly and the next card feels like an intentional peek. Web build,
  responsive audit, navigation audit, and desktop/tablet/mobile Chat screenshot
  review passed.
- `PRJ-1214` verified Personality embodied-map polish: count-heavy callout
  values use UI typography, the Mind Layers timeline carries a compact
  `6 layers` context pill, and the mobile screenshot keeps a readable timeline
  heading instead of raw rows. Web build, responsive audit, navigation audit,
  and refreshed desktop/tablet/mobile Personality screenshot review passed.
- `PRJ-1213` verified the Settings destructive-action hierarchy: reset
  runtime data details are collapsed behind a native disclosure boundary by
  default, while confirmation and submit controls remain available after
  expansion. Web build, responsive audit, navigation audit, and refreshed
  desktop/tablet/mobile Settings screenshots passed.
- `AVIARY-COGNITIVE-RUNTIME-001` now includes `PRJ-1212`: AI reply generation
  uses a centralized, channel-aware `ResponseBudgetPolicy`. App/API chat gets
  a larger bounded generation budget than Telegram, concise remains lower
  cost, deep analysis can expand, and the prompt contract tells the model to
  complete answers cleanly instead of stopping mid-sentence, mid-list, or
  inside an unfinished code block. Telegram transport segmentation remains in
  delivery routing. Full backend pytest passed with `1105 passed`.
- `AVIARY-WEB-RESP-001` is the active web responsive confidence row for the
  mobile, tablet, and desktop web shell scope. As of `PRJ-1209`, shared shell
  navigation is `VERIFIED` with `npm run build`, `npm run audit:ui-responsive`,
  and `npm run audit:ui-navigation`. As of `PRJ-1211`, focused Chat response
  readability is also verified with expanded chat reply output budgets,
  markdown list-continuation coverage, refreshed desktop/tablet/mobile Chat
  screenshots, and the same responsive/navigation audit gates.
- `PRJ-1210` verified the Tools route as a clearer capability directory:
  readiness, next action, and user control now precede technical details while
  preserving the same API payload and controls.
- Route-local visual work should continue from concrete screenshot evidence
  rather than broad polish loops. Native app proof remains deferred by current
  scope.

## Architecture Refresh Protocol

When architecture, module boundaries, app flow, route ownership, data model,
runtime behavior, UX system, or deployment shape changes, the same mission must
refresh the relevant indexes before it can be called done.

Minimum refresh checklist:

1. Update the canonical architecture or ADR file that owns the decision.
2. Update module maps, pipeline maps, route maps, or API ownership docs when
   affected.
3. Update `.codex/context/PROJECT_STATE.md` if phase, stack, deploy shape,
   validation commands, or runtime reality changed.
4. Regenerate or update project-status dashboard artifacts when the readiness
   picture changes.
5. Update `.codex/context/TASK_BOARD.md` and `docs/planning/*` so the next
   queue reflects the new architecture.
6. Update `.agents/state/module-confidence-ledger.md` for every affected
   module.
7. Update `.agents/state/system-health.md` when validation, smoke, deploy, or
   runtime status changed.
8. Record unresolved mismatches in `.agents/state/known-issues.md`.

Architecture changes left only in chat, commit messages, or scattered planning
notes are not accepted as source of truth.

## Module Confidence Ledger Protocol

Use `.agents/state/module-confidence-ledger.md` as the fast answer to:

- Which modules exist?
- Which user journeys does each module own?
- Does it work in the real app?
- What evidence proves that?
- What is blocked, broken, stale, or unverified?
- What is the next smallest proof or fix?

Before selecting a new implementation mission, read the ledger and prefer work
in this order:

1. `BROKEN` or `FAIL` release-critical journeys.
2. `BLOCKED` release-critical journeys.
3. `IMPLEMENTED_NOT_VERIFIED` P0/P1 journeys.
4. `PARTIAL` journeys where evidence points to a real defect.
5. New features only after release-critical existing flows are stable or
   explicitly deferred.

Do not convert unknowns into features. First create a verification mission or
mission slice. Create a fix only when proof, code inspection, or a reproducible
user journey shows a real defect.

## Reality Language Rule

Agents must not report vague completion states such as "almost done", "close",
"should work", "looks good", or "probably fixed" without evidence.

Allowed completion language:

- `verified`: evidence exists and is recorded.
- `implemented, not verified`: code exists but proof is missing.
- `partially verified`: exact passing and missing scenarios are listed.
- `blocked`: exact blocker and next unblock action are listed.
- `failed`: fresh verification failed and the failure is recorded.

The user should not be the first tester of a core journey. If a task affects a
browser, mobile, API, auth, data, AI, memory, runtime behavior, or deployment
flow, the agent must run the relevant automated or manual journey proof where
local access allows it.

## Real Journey Proof

For user-facing work, validation must prove the real journey, not just that code
compiled. Examples:

- send an event through the real runtime path when event handling changed;
- verify memory, reflection, scheduler, or action side effects through the
  canonical API or worker path when those systems changed;
- navigate from the real browser shell entry point, not only direct route
  access;
- verify loading, empty, error, success, and blocked states when the action has
  those states;
- verify persistence after reload or service restart when data changes;
- verify mobile or responsive behavior when the surface is browser-facing;
- verify auth, ownership, and fail-closed behavior when data access matters.

If a journey cannot be exercised locally, record why, the residual risk, and the
next best proof. Do not mark the module as working.

## Mission-Based Task Selection

Every autonomous run must start by answering:

- Where is Aviary now?
- What is the final or current release objective?
- Which module or journey is the biggest blocker to that objective?
- What evidence do we already have?
- What mission would most increase release confidence?

Use `.agents/core/mission-control.md` to scope a multi-hour mission when one
coherent objective needs several slices. Small tasks are mission slices, not the
operating goal.

## Handoff Requirement

After substantial work, update the indexes and leave the next agent a clear
handoff:

- current objective;
- mission status;
- files and modules changed;
- evidence collected;
- module confidence changes;
- known broken or unverified journeys;
- next checkpoint or mission.

## Coordinator Memory

For broad Aviary / Personality work, also update or review:

- `.agents/state/active-mission.md` for the current coordinator mission,
  source rows, lanes, delegation plan, and parent validation gate;
- `.agents/workflows/responsibility-lanes.md` for standard lane selection and
  lane brief/report templates;
- `.agents/state/responsibility-learning.md` when a missing lane, unclear
  owner, bad split, missing evidence, or missing context should improve future
  missions.
