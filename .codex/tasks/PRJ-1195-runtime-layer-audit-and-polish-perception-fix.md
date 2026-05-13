# Task

## Header
- ID: PRJ-1195
- Title: Audit runtime layers and repair Polish positive perception cue
- Task Type: audit/fix
- Current Stage: release
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-1194
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-COGNITIVE-RUNTIME-001
- Requirement Rows: not applicable
- Quality Scenario Rows: QA-AI-002
- Risk Rows: RISK-AI-002
- Iteration: 1195
- Operation Mode: TESTER
- Mission ID: digital-being-layer-audit
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed.
- [x] Affected module confidence rows were identified.
- [x] Affected quality scenario and risk rows were identified.

## Context
The memory runtime flow is verified. The next question is whether the other
digital-being layers are correctly implemented and test-backed.

## Goal
Audit non-memory cognitive runtime layers and fix any small, clear defect found
within the selected slice.

## Scope
- Audit foreground and background layer status.
- Fix Polish positive affect/language cue normalization for `dziekuje`.
- Add focused regression tests.
- Update repo source-of-truth state.

## Implementation Plan
1. Read architecture, runtime, and module-confidence state.
2. Inspect foreground stage implementations and tests.
3. Record a layer-by-layer audit.
4. Patch the narrow perception language/affective cue defect.
5. Run focused validation.
6. Update docs and ledgers.

## Acceptance Criteria
- Runtime layer audit exists as a durable repo artifact.
- Polish `Dziękuję`/`dziekuje` maps to Polish and positive engagement after normalization.
- Focused tests pass.
- Remaining gaps are named without overstating readiness.

## Definition of Done
- [x] audit artifact added
- [x] focused tests pass
- [x] docs/state updated
- [x] full backend pytest or documented reason for narrower validation

## Forbidden
- Do not introduce a new cognitive subsystem.
- Do not change canonical runtime stage ordering.
- Do not claim provider/mobile readiness without proof.

## Validation Evidence
- Focused command:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_affective_contract.py tests/test_language_runtime.py tests/test_runtime_pipeline.py -k "polish_thanks or runtime_pipeline_api_source or contract_smoke_pins_stage"; Pop-Location`
  - result: `4 passed, 129 deselected`
- Full backend gate:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location`
  - result: `1093 passed`

## Result Report
- Task summary: Audited runtime layers and fixed one Polish perception cue gap.
- Files changed: perception, language utility, focused tests, audit docs/state.
- What is incomplete: native device proof and external provider activation remain separate tracked gaps.
- Next steps: move to mobile device proof or provider activation work.
