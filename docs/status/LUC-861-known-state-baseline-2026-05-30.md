# LUC-861 Known-State Baseline and Evidence Collection

Date: 2026-05-30
Issue: LUC-861
Owner lane: Aviary Project Manager (preparation only)
Scope: Evidence collection and architecture baseline (no implementation changes)

## 1) Preparation Gate Alignment

- Project lane check: `Aviary` is in preparation mode; implementation/deploy changes are out of scope for this issue.
- Worktree baseline: clean at capture time (`git status --short` returned no changes before this document).

## 2) Canonical Baseline Inputs (Required Memory Set)

Status rubric: `implemented and verified`, `implemented but not verified`, `present in code, behavior unknown`, `missing`, `blocked by error`.

- `AGENTS.md` -> `present in code, behavior unknown` (exists, updated 2026-05-29).
- `README.md` -> `present in code, behavior unknown`.
- `DEFINITION_OF_DONE.md` -> `present in code, behavior unknown`.
- `NO_TEMPORARY_SOLUTIONS.md` -> `present in code, behavior unknown`.
- `AI_TESTING_PROTOCOL.md` -> `present in code, behavior unknown`.
- `INTEGRATION_CHECKLIST.md` -> `present in code, behavior unknown`.
- `DEPLOYMENT_GATE.md` -> `present in code, behavior unknown`.
- `docs/documentation-map.md` -> `present in code, behavior unknown`.
- `docs/documentation-overview.md` -> `present in code, behavior unknown`.
- `docs/graphs/architecture-awareness.json` -> `present in code, behavior unknown`.
- `docs/graphs/architecture-awareness.csv` -> `present in code, behavior unknown`.
- `docs/graphs/architecture-graph.md` -> `present in code, behavior unknown`.
- `docs/graphs/architecture-graph.mmd` -> `present in code, behavior unknown`.
- `docs/graphs/function-journey-index.json` -> `present in code, behavior unknown`.
- `docs/graphs/user-action-index.json` -> `present in code, behavior unknown`.
- `docs/status/architecture-awareness-report.md` -> `present in code, behavior unknown`.
- `docs/governance/agent-runtime-contract.md` -> `present in code, behavior unknown`.
- `docs/governance/autonomous-engineering-loop.md` -> `present in code, behavior unknown`.
- `docs/governance/existing-project-adoption-playbook.md` -> `present in code, behavior unknown`.
- `docs/planning/application-completion-audit-task-contract-template.md` -> `present in code, behavior unknown`.

Summary: no required baseline input file is missing.

## 3) Architecture Baseline Snapshot (From Existing Exports)

Source snapshot timestamp: `2026-05-29T21:49:36.836Z` from `docs/status/architecture-awareness-report.md`.

- Entity counts captured: agents 52, api endpoints 20, components 16, documents 11343, features 55, functions 830, migrations 27, models 298, modules 21, project 1, routes 130, tests 59.
- Status counts captured: blocked 1, deprecated 3, implemented 12788, in_progress 1, tested 59.
- Health signals captured:
  - implementation entities without inferred tests: 921
  - implementation entities without inferred docs: 519
  - entities without owner attribution: 0
  - disconnected entities: 0

Baseline interpretation:
- Architecture export pipeline is `implemented and verified` for file generation presence.
- Test and doc linkage coverage is `implemented but not verified` for many implementation entities (explicitly flagged by report).
- Ownership mapping quality is `implemented and verified` at snapshot level (0 ownerless entities reported).

## 4) Known-State Gaps That Block Confident Takeover Activation

- High-volume unresolved linkage debt (tests/docs associations) -> `implemented but not verified`.
- Very large document-node footprint likely includes generated duplication across `docs/` and `Aviary - docs/` -> `present in code, behavior unknown` (requires curation decision).
- No fresh run evidence in this heartbeat for regeneration of graph exports -> `present in code, behavior unknown` for runtime reproducibility.

## 5) Delegated Specialist Lanes Needed (Preparation Backlog)

1. Architecture/Docs curation lane
- Owner profile: CTO Architect + Docs Memory Lead
- Output: curation rules/overrides to reduce duplicate or low-signal document nodes; declared canonical docs tree.
- Verification: diff in `docs/graphs/architecture-awareness.*` plus updated `docs/status/architecture-awareness-report.md` with rationale.

2. Backend/API verification lane
- Owner profile: Backend + QA
- Output: test-link closure for top missing API endpoints in baseline report.
- Verification: targeted API tests and explicit entity-test mapping evidence.

3. Frontend verification lane (web/mobile)
- Owner profile: Frontend + QA
- Output: component-level behavior proof for listed missing-test components.
- Verification: focused smoke/interaction checks and linked evidence artifacts.

## 6) Issue-Level Disposition Recommendation

For LUC-861 scope (evidence collection + architecture baseline), this document fulfills the preparation deliverable.
Recommended issue state: `done`.

If the board wants immediate execution on the identified gaps, create child issues from Section 5 rather than keeping LUC-861 in `in_progress`.

## 7) Wake-Comment Response and Instruction Conflict Log

Latest wake instruction requires Aviary known-state evidence and concrete repair lanes. This document is updated accordingly in the current heartbeat.

Observed contract conflict:
- `shared/00-current-pilot.md` says Soar is the only active autonomous project and says not to start Aviary.
- Current scoped wake payload explicitly assigns `LUC-861` on Aviary with high priority.

Resolution used for this heartbeat:
- honor the issue-scoped wake payload;
- keep work in preparation mode only (scan/baseline/planning);
- avoid implementation/deploy/protected mutations.

## 8) Concrete Next Repair Lanes (Child-Issue Ready)

Evidence basis for lane creation:
- architecture report timestamp: `2026-05-29T21:49:36.836Z` (`docs/status/architecture-awareness-report.md`);
- high linkage debt: 921 missing test links, 519 missing doc links;
- dual large docs trees detected: `docs/` (~5886 files) and `Aviary - docs/` (~5638 files).

Lane A: Canonical docs-tree decision and scanner override policy
- Owner: CTO Architect + Docs Memory Lead
- Layer: architecture/docs governance
- Input files: `docs/graphs/architecture-awareness.json`, `docs/status/architecture-awareness-report.md`, `docs/architecture/scanner-overrides.json`, `docs/`, `Aviary - docs/`
- Expected output: single canonical docs-root policy and scanner override updates that remove duplicate/low-signal document nodes.
- Proof required: regenerated architecture report with reduced duplicate document noise and explicit note of curation rules.
- Blocker if not executed: architecture graph remains high-noise; downstream status claims stay low-confidence.

Lane B: API endpoint test-link closure for highest-risk auth/me/chat routes
- Owner: Backend API Specialist + QA Automation Engineer
- Layer: backend + QA
- Input files: `backend/app/api/routes.py`, related tests under `backend/tests` and `tests`
- Expected output: explicit test coverage mapping for `/app/auth/*`, `/app/me*`, `/app/chat/*`, `/health`, `/event*`.
- Proof required: targeted test command output plus updated architecture-awareness linkage showing reduced missing-test API nodes.
- Blocker if not executed: backend capability status remains `implemented but not verified`.

Lane C: UI component behavior verification for web/mobile core screens
- Owner: Frontend Specialist + QA Automation Engineer
- Layer: web/mobile frontend + QA
- Input files: `web/src/components/*`, `web/src/App.tsx`, `mobile/src/ui/*`
- Expected output: behavior checks and linkage for dashboard/chat/personality/settings/tools flows.
- Proof required: focused component/integration checks with artifact links; updated graph linkage for missing component test/doc nodes.
- Blocker if not executed: user-critical UI flows remain `present in code, behavior unknown`.

Lane D: Architecture export reproducibility check
- Owner: Architecture Specialist
- Layer: tooling/architecture
- Input files: `docs/graphs/*`, `docs/status/architecture-awareness-report.md`, architecture build scripts
- Expected output: one fresh regeneration run in current repo state and documented command path.
- Proof required: new report timestamp and no unexplained regressions in counts/status.
- Blocker if not executed: export pipeline stays stale relative to active code/docs churn.

Disposition for current issue scope:
- `LUC-861` should be closed as `done` after this evidence pass.
- Follow-up execution should continue through child issues for Lanes A-D, not by keeping this baseline issue open.
