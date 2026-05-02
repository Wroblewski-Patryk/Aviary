# Task

## Header
- ID: PRJ-905
- Title: V1 Candidate Validation Gate
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-904
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 905
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-904 audited the current commit scope. The next release step requires a
fresh validation gate against the current candidate head before publishing.

## Goal
Run and record the local v1 candidate validation gate for the current release
candidate.

## Scope
- `docs/planning/v1-candidate-validation-gate.md`
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-905-v1-candidate-validation-gate.md`
- generated validation artifact under `.codex/artifacts/...` remains evidence
  output and is not committed by default

## Success Signal
- User or operator problem: release owner needs proof that the current
  candidate is locally green before publishing.
- Expected product or reliability outcome: publish work starts from a validated
  candidate instead of from stale evidence.
- How success will be observed: backend tests, web build, behavior validation,
  and diff hygiene all pass for the candidate head.
- Post-launch learning needed: no

## Deliverable For This Stage
Validation record for the current candidate.

## Constraints
- run the required gates before publish
- do not push from this task
- do not commit generated artifact output unless separately approved
- keep production parity as a later PRJ-907 requirement

## Implementation Plan
1. Run full backend tests.
2. Run web production build.
3. Run behavior validation with PRJ-905 artifact path.
4. Run `git diff --check`.
5. Document results and sync context.

## Acceptance Criteria
- Full backend gate passes.
- Web build passes.
- Behavior validation passes.
- Diff hygiene passes.
- Candidate is marked ready for PRJ-906 publish.

## Definition of Done
- [x] Full backend tests passed.
- [x] Web production build passed.
- [x] Behavior validation passed.
- [x] Diff hygiene passed.
- [x] Validation record and context were updated.

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
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location`
  - result: passed, `1019 passed`
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\run_behavior_validation.py --gate-mode operator --artifact-path ..\.codex\artifacts\prj905-v1-candidate-validation\behavior-validation-report.json; Pop-Location`
  - result: passed, `19 passed, 209 deselected`
- Manual checks:
  - `git diff --check`
  - result: passed
- Screenshots/logs: not applicable.
- High-risk checks: untracked `artifacts/behavior_validation/prj843-report.json`
  remains excluded from the candidate.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-commit-scope-audit.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: no deploy occurred; rollback belongs to PRJ-911.
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

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

- Task summary: validated the current v1 candidate locally.
- Files changed:
  - `docs/planning/v1-candidate-validation-gate.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-905-v1-candidate-validation-gate.md`
- How tested: backend tests, web build, behavior validation, diff check.
- What is incomplete: publish, production smoke, incident bundle, rollback
  drill, privacy/debug posture, AI red-team evidence.
- Next steps: start `PRJ-906` Publish V1 Candidate.
- Decisions made: keep generated artifact output out of source commits.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: candidate needed fresh local validation after PRJ-904.
- Gaps: production truth still missing.
- Inconsistencies: none found.
- Architecture constraints: production parity remains a separate gate.

### 2. Select One Priority Task
- Selected task: PRJ-905 V1 Candidate Validation Gate.
- Priority rationale: publish must not happen before local green gates.
- Why other candidates were deferred: PRJ-906 and PRJ-907 depend on this gate.

### 3. Plan Implementation
- Files or surfaces to modify: validation record and context.
- Logic: run gates, record exact commands and results.
- Edge cases: generated evidence remains local.

### 4. Execute Implementation
- Implementation notes: ran backend and web gates, then behavior validation.

### 5. Verify and Test
- Validation performed: full backend, web build, behavior validation,
  `git diff --check`.
- Result: all passed.

### 6. Self-Review
- Simpler option considered: rely on PRJ-901/902 evidence, rejected because
  candidate HEAD changed.
- Technical debt introduced: no
- Scalability assessment: validation record can be repeated for later
  candidates.
- Refinements made: candidate status separates local validation from production
  truth.

### 7. Update Documentation and Knowledge
- Docs updated: yes
- Context updated: yes
- Learning journal updated: not applicable.
