# Task

## Header
- ID: PRJ-1290
- Title: App chat API and event graph gap closure
- Task Type: documentation
- Current Stage: verification
- Status: DONE
- Owner: Active chat coordinator
- Depends on: PRJ-1289
- Priority: P1
- Module Confidence Rows: AVIARY-ARCH-GRAPH-APP-CHAT-EVENT-001
- Requirement Rows: REQ-ARCH-1290
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1290
- Risk Rows: RISK-ARCH-GRAPH-1290
- Iteration: 1290
- Operation Mode: TESTER
- Mission ID: PRJ-1290-app-chat-event-gap-closure
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed.
- [x] `.agents/core/mission-control.md` was reviewed for long-running work.
- [x] Missing or template-like state tables were bootstrapped from repository sources, or confirmed not needed.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task or mission improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: remove `API-APP-CHAT-MESSAGE` and `EVENT-APP-CHAT-TURN` from the curated missing-proof queue.
- Release objective advanced: app-chat execution-chain traceability and proof quality.
- Included slices: focused app-chat API tests, chat transcript characterization, evidence rows, current-chain scope clarification, generated artifacts, state updates.
- Explicit exclusions: native binary/media upload implementation, attachment transport changes, production chat smoke.
- Checkpoint cadence: one focused closure checkpoint.
- Stop conditions: stop if app-chat API tests, transcript characterization, graph generation, or no-gap query proof fails.
- Handoff expectation: next agent can query app-chat API/event nodes and see evidence plus no current gaps.

## Context
`query_architecture_graph.py --gaps` reports `API-APP-CHAT-MESSAGE` and `EVENT-APP-CHAT-TURN` because the nodes lack direct evidence rows and the chain still stores future native binary upload as `missing_links`.

## Goal
Add node-level evidence and make the chain scope truthful: current app chat covers text plus serialized attachment context; native binary upload is future scope, not a missing connection in this chain.

## Success Signal
- User or operator problem: agents need systemic app-chat confidence without confusing future upload scope with current brokenness.
- Expected product or reliability outcome: app-chat API/event nodes have evidence and no graph query gaps.
- How success will be observed: `API-APP-CHAT-MESSAGE --show-gaps` and `EVENT-APP-CHAT-TURN --show-gaps` report `Gaps: none`.
- Post-launch learning needed: no.

## Deliverable For This Stage
Implemented graph evidence rows, chain scope clarification, regenerated artifacts, validation proof, and state updates.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] focused app-chat API tests pass
- [x] chat transcript characterization passes
- [x] app-chat API/event nodes have evidence rows
- [x] current app-chat chain has no missing links for the verified scope
- [x] graph generation and fast graph/query tests pass
- [x] node queries report `Gaps: none`
- [x] source-of-truth state is updated

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests:
  - focused app-chat API pytest PASS: `3 passed in 3.29s`
  - web chat transcript characterization PASS with `status=ok`, `appSourceCount=2`, `telegramSourceCount=2`
  - inventory plus graph generation PASS with `auto_nodes=5282`, `auto_relations=3970`, merged `nodes=5343`, `relations=4034`, `chains=9`, `evidence=28`, `research_sources=21`, `theory_claims=9`
  - app-chat plus graph/query pytest PASS: `25 passed, 1 deselected in 5.78s`
- Manual checks:
  - `query_architecture_graph.py --node API-APP-CHAT-MESSAGE --show-gaps` reports `EVID-APPCHAT-API-PROOF` and `Gaps: none`
  - `query_architecture_graph.py --node EVENT-APP-CHAT-TURN --show-gaps` reports `EVID-APPCHAT-EVENT-PROOF` and `Gaps: none`
  - top curated gap audit no longer lists `API-APP-CHAT-MESSAGE` or `EVENT-APP-CHAT-TURN`
- Screenshots/logs: not applicable
- High-risk checks: no runtime or upload behavior changed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable
- Module confidence ledger updated: yes
- Module confidence rows closed or changed: AVIARY-ARCH-GRAPH-APP-CHAT-EVENT-001
- Requirements matrix updated: yes
- Requirement rows closed or changed: REQ-ARCH-1290
- Quality scenarios updated: yes
- Quality scenario rows closed or changed: QA-MAINT-ARCH-GRAPH-1290
- Risk register updated: yes
- Risk rows closed or changed: RISK-ARCH-GRAPH-1290
- Reality status: verified

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/pipelines/app-chat.md`; `docs/architecture/registry/`; `backend/tests/test_api_routes.py`; `web/scripts/chat-transcript-characterization.mjs`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: generated graph artifacts and state ledgers

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no runtime behavior changed
- Rollback note: revert registry/evidence/test/state rows if proof mapping is incorrect
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist (mandatory)
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

## Result Report
- Task summary: Added node-level evidence for app chat API and app chat event nodes, and clarified that native binary upload is future scope outside the current verified chain.
- Files changed: `docs/architecture/registry/chains.csv`; `docs/architecture/registry/evidence.csv`; `backend/tests/test_architecture_graph_generator.py`; `backend/tests/test_architecture_graph_query.py`; generated graph artifacts and state ledgers.
- How tested: focused app-chat API pytest, chat transcript characterization, graph regeneration, graph generator/query pytest, node query smoke, global gap audit smoke.
- What is incomplete: native binary/media upload and production chat smoke remain separate future scopes.
- Next steps: close remaining documentation/feature gaps, especially `DOC-MEMORY-SYSTEM`, `DOC-RUNTIME-FLOW`, `FEAT-EVENT-INGRESS`, `FEAT-FOREGROUND-RUNTIME`, and `FEAT-MEMORY-FLOW`.
