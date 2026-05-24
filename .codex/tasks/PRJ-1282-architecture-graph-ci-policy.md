# Task

## Header
- ID: PRJ-1282
- Title: Architecture graph CI validation policy
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: QA/Test + Ops/Release + Product Docs Agent
- Depends on: PRJ-1281
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1282
- Operation Mode: ARCHITECT
- Mission ID: PRJ-1282-architecture-graph-ci-policy
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed through the continuation state.
- [x] `.agents/core/mission-control.md` was reviewed through the continuation state.
- [x] Missing or template-like state tables were bootstrapped from repository sources, or confirmed not needed.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task or mission improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: add a CI-backed validation policy for the architecture graph system.
- Release objective advanced: graph-system regression prevention for future feature, evidence, and research-map edits.
- Included slices: GitHub Actions workflow, graph registry rows, graph docs, testing docs, generator pytest pin, source-of-truth updates.
- Explicit exclusions: production smoke, new curated feature chains, hosted GitHub Actions result before push.
- Checkpoint cadence: one bounded implementation and validation checkpoint.
- Stop conditions: CI workflow requires secrets, deploy credentials, or broader repo-wide release workflow decisions.
- Handoff expectation: future graph edits should use local fast gate and CI fast gate; heavy gate remains manual before release-level graph confidence.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, next steps | Integration, task closure, memory updates | Parent decision and final acceptance | Fast graph pytest, generator run, diff check | IN_PROGRESS |
| Product/Requirements | Coordinator | requirements matrix | Requirement trace remains accurate | Updated REQ-ARCH row if needed | Source diff review | IN_PROGRESS |
| Architecture | Coordinator | graph-system docs and registries | graph registry nodes/relations/evidence | CI policy represented as official graph node | generator validation | IN_PROGRESS |
| Backend/API | Coordinator | backend graph tests | generator pytest | CI policy node/evidence pinned | focused pytest | IN_PROGRESS |
| Frontend/UX | omitted | no UI surface changed | none | no output | not applicable | OMITTED |
| Data/Migrations | omitted | no schema changed | none | no output | not applicable | OMITTED |
| QA/Test | Coordinator | testing docs | GitHub Actions graph workflow | automatic fast gate and manual heavy gate policy | local command proof | IN_PROGRESS |
| Security/Ops/Docs | Coordinator | testing docs, graph docs | CI workflow and docs | documented fast/heavy CI policy | YAML/file inspection and local validation | IN_PROGRESS |

### Lane Checks

- [x] `.agents/state/active-mission.md` was refreshed for continuation work.
- [x] `.agents/workflows/responsibility-lanes.md` was represented by serial lane ownership because the slice is tightly coupled.
- [x] Every important responsibility has an owner or explicit omission.
- [x] No delegated write lanes overlap.
- [x] Each delegated lane has expected output and proof.
- [x] Missing ownership/evidence/context gaps will be recorded if discovered.
- [x] Process eval is not required because no subagent split was used.

## Context
PRJ-1281 left all current curated chains verified. The next release-confidence gap was that fast/heavy graph gates were documented locally but not encoded as a CI policy.

## Goal
Add a minimal GitHub Actions workflow and graph registry evidence so architecture graph freshness and fast pytest validation are automatically checked for graph-relevant changes.

## Success Signal
- User or operator problem: future agents can forget to regenerate graph artifacts or run graph pytest.
- Expected product or reliability outcome: stale architecture graph artifacts are caught by local and CI gates.
- How success will be observed: workflow exists, graph registry validates, generated artifacts are fresh, and fast graph pytest passes.
- Post-launch learning needed: yes

## Scope
- `.github/workflows/architecture-graph.yml`
- `docs/architecture/registry/nodes.csv`
- `docs/architecture/registry/workflows.csv`
- `docs/architecture/registry/relations.csv`
- `docs/architecture/registry/evidence.csv`
- `docs/architecture/graph-system.md`
- `docs/architecture/registry/README.md`
- `docs/engineering/testing.md`
- `backend/tests/test_architecture_graph_generator.py`
- generated graph artifacts and source-of-truth state files

## Implementation Plan
1. Add a focused GitHub Actions workflow with automatic fast gate and manual heavy gate.
2. Add the CI policy as an official graph workflow node with relations and evidence.
3. Document the CI policy in graph and testing docs.
4. Pin CI policy presence in graph generator tests.
5. Regenerate inventory and graph artifacts.
6. Run fast graph pytest and related lightweight checks.
7. Update project state and ledgers.

## Acceptance Criteria
- `.github/workflows/architecture-graph.yml` exists and uses repository-native graph commands.
- `WORKFLOW-ARCH-GRAPH-CI` and `EVID-ARCH-GRAPH-CI-POLICY` are in the graph registry.
- Generated Obsidian/JSON/Mermaid/status/evidence artifacts include the CI policy.
- Fast graph pytest passes.
- State files record the residual hosted-CI first-run caveat.

## Deliverable For This Stage
Verified CI policy implementation and graph evidence update.

## Constraints
- use existing graph generator and pytest gates
- do not introduce a separate validation framework
- do not claim hosted Actions proof before the workflow runs remotely
- keep heavy all-node parity manual because it is intentionally slower

## Definition of Done
- [x] CI workflow added and documented.
- [x] Graph registries and generated artifacts are fresh.
- [x] Fast graph pytest passes.
- [x] Source-of-truth state updated.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated graph validation logic
- temporary bypasses
- claiming production or hosted CI evidence without a run

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `8 passed, 1 deselected in 2.82s`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m py_compile .\scripts\generate_architecture_inventory.py .\scripts\generate_architecture_graph.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Manual checks:
  - inventory plus graph generation PASS with `auto_nodes=5237`, `auto_relations=3935`, merged `nodes=5295`, `relations=3986`, `chains=7`, `evidence=19`, `research_sources=21`, `theory_claims=9`
  - generated graph JSON, evidence map, and node page include `WORKFLOW-ARCH-GRAPH-CI` and `EVID-ARCH-GRAPH-CI-POLICY`
  - `git diff --check` -> PASS with LF/CRLF warnings only
- Screenshots/logs: not applicable
- High-risk checks: hosted CI first run remains pending until push
- Coverage ledger updated: not applicable
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## Architecture Evidence
- Architecture source reviewed: `docs/architecture/graph-system.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: user requested full graph system completion
- Follow-up architecture doc updates: graph-system and registry README updated

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: graph CI workflow and testing docs
- Rollback note: remove `.github/workflows/architecture-graph.yml` and associated graph registry rows if the policy needs to be paused
- Observability or alerting impact: GitHub Actions check visibility for graph changes
- Staged rollout or feature flag: manual heavy gate through workflow dispatch

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Result Report

- Task summary: Added a focused GitHub Actions workflow for architecture graph validation and mapped that policy back into the graph system itself.
- Files changed: `.github/workflows/architecture-graph.yml`, graph registry CSVs, generated graph artifacts, graph/testing docs, generator pytest, and project state files.
- How tested: inventory plus graph generation PASS with `auto_nodes=5237`, `auto_relations=3935`, merged `nodes=5295`, `relations=3986`, `chains=7`, `evidence=19`, `research_sources=21`, `theory_claims=9`; fast graph pytest PASS with `8 passed, 1 deselected in 2.82s`; py_compile PASS; generated artifact presence check PASS; `git diff --check` PASS with LF/CRLF warnings only.
- What is incomplete: hosted GitHub Actions proof remains optional supplementary evidence under `DEC-005`.
- Next steps: capture hosted Actions first-run proof after push, or select production smoke/new curated chain only when release needs require it.
- Decisions made: heavy graph gate remains manual

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: graph gates existed locally but not as CI policy.
- Gaps: hosted first-run evidence cannot exist before push.
- Inconsistencies: none found.
- Architecture constraints: CSV remains canonical and graph artifacts must be regenerated.

### 1a. Bootstrap Missing Project Knowledge
- Bootstrap needed: no
- Missing or template-like files: no `.github/workflows` existed
- Sources scanned: active mission, next steps, task board, project state, graph docs, testing docs, registry CSVs
- Rows created or corrected: CI workflow graph rows
- Assumptions recorded: GitHub Actions is the intended hosted CI surface because `.github` exists and the repo already has GitHub PR metadata
- Blocking unknowns: none for local implementation
- Why it was safe to continue: workflow is scoped to graph files and uses existing commands

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1282 architecture graph CI policy
- Priority rationale: all curated chains are verified; next gap is preventing graph evidence drift.
- Why other candidates were deferred: production smoke needs deployment target; new curated chains should wait for release-critical module selection.

### 3. Plan Implementation
- Files or surfaces to modify: workflow, graph registries, graph docs, testing docs, pytest, state files.
- Logic: reuse inventory generator, graph generator, git diff freshness check, fast/heavy pytest gates.
- Edge cases: heavy gate stays manual to avoid slow default CI.

### 4. Execute Implementation
- Implementation notes: Added `.github/workflows/architecture-graph.yml`, graph node `WORKFLOW-ARCH-GRAPH-CI`, relations `REL-GRAPH-004..006`, evidence `EVID-ARCH-GRAPH-CI-POLICY`, graph/testing docs, and pytest assertions.

### 5. Verify and Test
- Validation performed: graph generation, fast graph pytest, py_compile, generated artifact presence check, and `git diff --check`.
- Result: PASS locally; hosted first-run proof pending until push.

### 6. Self-Review
- Simpler option considered: docs-only CI policy.
- Technical debt introduced: no
- Scalability assessment: workflow is path-filtered and heavy gate is manual.
- Refinements made: Kept the slow all-node page parity gate manual in CI to avoid making every graph PR pay the heavy runtime cost.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/architecture/graph-system.md`, `docs/architecture/registry/README.md`, `docs/engineering/testing.md`
- Context updated: task board, project state, active mission, next steps, system health, project memory index, delivery map, module confidence, requirements, quality scenarios, and risk register
- Learning journal updated: not applicable
