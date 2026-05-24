# Task

## Header
- ID: PRJ-1283
- Title: Architecture graph PR template checklist
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: QA/Test + Product Docs Agent
- Depends on: PRJ-1282
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1282
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1282
- Risk Rows: RISK-ARCH-GRAPH-1282
- Iteration: 1283
- Operation Mode: BUILDER
- Mission ID: PRJ-1283-architecture-graph-pr-template-checklist
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
- Mission objective: add graph-governance checklist prompts to the existing pull request template and map the checklist as graph evidence.
- Release objective advanced: graph-system drift prevention during review, before CI becomes the only feedback surface.
- Included slices: PR template, graph node/relation/evidence rows, generator pytest pin, generated graph artifacts, state updates.
- Explicit exclusions: hosted GitHub Actions first-run proof, commit/push, production smoke.
- Checkpoint cadence: one bounded implementation and validation checkpoint.
- Stop conditions: PR template starts duplicating CI logic or adds mandatory checks unrelated to graph/evidence changes.
- Handoff expectation: graph-relevant PRs should state registry/evidence/generated-artifact/fast-gate posture in the PR body.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, next steps | Integration and state updates | Final acceptance | Fast graph pytest, generator run, diff check | IN_PROGRESS |
| Product/Requirements | Coordinator | PR template, requirements matrix | Review checklist wording | Graph review prompts without overclaiming | Source diff review | IN_PROGRESS |
| Architecture | Coordinator | graph registries | Node/relation/evidence rows | PR template appears in graph | generator validation | IN_PROGRESS |
| Backend/API | Coordinator | graph pytest | generator pytest pins | PR checklist evidence remains visible | focused pytest | IN_PROGRESS |
| Frontend/UX | omitted | no UI changed | none | no output | not applicable | OMITTED |
| Data/Migrations | omitted | no schema changed | none | no output | not applicable | OMITTED |
| QA/Test | Coordinator | existing PR template and graph gates | checklist plus tests | Graph PR review gate | focused pytest | IN_PROGRESS |
| Security/Ops/Docs | Coordinator | PR workflow docs | PR checklist | Review-time graph discipline | inspection | IN_PROGRESS |

## Context
PRJ-1282 added CI validation for graph-relevant changes. The remaining local review gap is that the PR template did not ask authors to disclose graph registry, chain, evidence, research, generated artifact, or fast-gate posture.

## Goal
Make architecture graph updates visible during PR review and represent the PR template checklist as official graph documentation evidence.

## Success Signal
- User or operator problem: agents may rely on CI but omit graph context from review notes.
- Expected product or reliability outcome: graph-relevant PRs explicitly report whether registries, chains, evidence, research claims, generated artifacts, and fast gates were handled.
- How success will be observed: PR template has graph checklist, graph registry includes `DOC-PR-TEMPLATE`, generated artifacts include it, and fast graph pytest passes.
- Post-launch learning needed: no

## Scope
- `.github/pull_request_template.md`
- `docs/architecture/registry/nodes.csv`
- `docs/architecture/registry/relations.csv`
- `docs/architecture/registry/evidence.csv`
- `backend/tests/test_architecture_graph_generator.py`
- generated graph artifacts and source-of-truth state files

## Implementation Plan
1. Add graph/evidence checklist prompts to the existing PR template.
2. Add the PR template as a curated graph documentation node.
3. Link it to the graph workflow and CI policy.
4. Add evidence and pytest pins.
5. Regenerate inventory and graph artifacts.
6. Run the fast graph pytest gate and whitespace checks.
7. Update source-of-truth state files.

## Acceptance Criteria
- PR template includes graph/evidence checklist prompts.
- `DOC-PR-TEMPLATE` and `EVID-ARCH-PR-TEMPLATE-CHECKLIST` exist in the graph.
- Generated graph artifacts include the PR template node and evidence.
- Fast graph pytest passes.

## Deliverable For This Stage
Verified implementation and graph evidence for the PR template checklist.

## Constraints
- reuse the existing PR template instead of creating a parallel review process
- keep checklist scoped to graph/evidence responsibilities
- do not claim hosted CI proof

## Definition of Done
- [x] PR template updated.
- [x] Graph registries and generated artifacts refreshed.
- [x] Fast graph pytest passes.
- [x] Source-of-truth state updated.

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `8 passed, 1 deselected in 4.64s`
- Manual checks:
  - inventory plus graph generation PASS with `auto_nodes=5238`, `auto_relations=3935`, merged `nodes=5297`, `relations=3988`, `chains=7`, `evidence=20`, `research_sources=21`, `theory_claims=9`
  - generated graph JSON, evidence map, and node page include `DOC-PR-TEMPLATE` and `EVID-ARCH-PR-TEMPLATE-CHECKLIST`
  - PR template scan confirms `Architecture Graph / Evidence Map`, `Graph registry updated`, `Function chain updated`, and `Fast graph gate`
  - `git diff --check` -> PASS with LF/CRLF warnings only
- High-risk checks: checklist is review guidance, not runtime proof
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## Result Report

- Task summary: Added graph/evidence checklist prompts to the existing pull request template and mapped that checklist into the architecture graph.
- Files changed: `.github/pull_request_template.md`, graph registry CSVs, generated graph artifacts, generator pytest, and source-of-truth state files.
- How tested: graph generation PASS with `nodes=5297`, `relations=3988`, `evidence=20`; fast graph pytest PASS with `8 passed, 1 deselected in 4.64s`; generated artifact presence scan PASS; PR template scan PASS; `git diff --check` PASS with LF/CRLF warnings only.
- What is incomplete: hosted GitHub Actions proof remains optional supplementary evidence under `DEC-005`; PR checklist is review guidance rather than proof.
- Next steps: capture hosted Actions result after push or add new curated chains/research claims only when a concrete release-critical module or theory claim is selected.
- Decisions made: checklist complements tests/CI and does not replace them

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: CI policy exists, but PR template did not ask authors to disclose graph/evidence work.
- Gaps: hosted CI proof remains optional supplementary evidence under `DEC-005`.
- Inconsistencies: none found.
- Architecture constraints: CSV remains canonical and graph artifacts must be regenerated.

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1283 architecture graph PR template checklist
- Priority rationale: after CI policy, PR review is the next drift-prevention layer.
- Why other candidates were deferred: production smoke needs deployment/push context; new curated chains should wait for release-critical module selection.

### 3. Plan Implementation
- Files or surfaces to modify: PR template, graph registry, graph tests, generated artifacts, state files.
- Logic: review checklist plus graph proof, no new validation framework.
- Edge cases: checklist must not claim proof by itself.

### 4. Execute Implementation
- Implementation notes: Updated the existing PR template, added `DOC-PR-TEMPLATE`, `REL-GRAPH-007..008`, `EVID-ARCH-PR-TEMPLATE-CHECKLIST`, and pytest assertions.

### 5. Verify and Test
- Validation performed: graph generation, fast graph pytest, generated artifact presence scan, PR template scan, and `git diff --check`.
- Result: PASS.

### 6. Self-Review
- Simpler option considered: PR template only.
- Technical debt introduced: no
- Scalability assessment: checklist is low-cost and path-independent.
- Refinements made: Kept the checklist scoped to visibility and explicitly recorded that it does not replace tests, CI, or runtime proof.

### 7. Update Documentation and Knowledge
- Docs updated: `.github/pull_request_template.md`
- Context updated: task board, project state, active mission, next steps, system health, project memory index, delivery map, module confidence, requirements, quality scenarios, and risk register
- Learning journal updated: not applicable
