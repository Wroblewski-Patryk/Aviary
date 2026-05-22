# Task

## Header
- ID: PRJ-1231
- Title: V1 Production Candidate Promotion
- Task Type: release
- Current Stage: release
- Status: IN_PROGRESS
- Owner: Ops/Release
- Depends on: PRJ-1230
- Priority: P0
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-STATUS-001, AVIARY-WEB-RESP-001, AVIARY-COGNITIVE-RUNTIME-001, AVIARY-MEMORY-001
- Requirement Rows: REQ-UX-001, REQ-MOB-001, REQ-AI-001, REQ-AI-002, REQ-AI-003
- Quality Scenario Rows: release readiness, deployed revision parity, web route rendering
- Risk Rows: ARCH-DEPLOY-AUTO-001, ARCH-CONNECTORS-001, ARCH-PROACTIVE-001, ARCH-MOBILE-001
- Iteration: 1231
- Operation Mode: BUILDER
- Mission ID: PRJ-1231-v1-production-candidate-promotion
- Mission Status: IN_PROGRESS

## Context
PRJ-1230 proved local selected-scope v1 readiness on the current branch, but
the release boundary forbids a new release claim without selected SHA, deployed
revision parity, production release smoke, and marker/tag evidence.

## Goal
Turn the current selected-scope v1 candidate into a production-backed release
fact, or record the exact external blocker that prevents release.

## Constraints
- Do not move existing historical tags `v1.0.0`, `v1.0.1`, or `v1.1.0`.
- Do not claim release based only on local tests.
- Do not count deferred provider, proactive, deploy automation, or native
  extension rows as shipped.
- Do not use a temporary bypass for failing production parity.
- Preserve existing uncommitted user/governance changes unless they are
  intentionally included in the selected release candidate.

## Definition of Done
- [ ] Selected SHA and release branch are explicit.
- [ ] Local gate is green or a blocker is recorded.
- [ ] Candidate commit is pushed to the deploy source or blocked with evidence.
- [ ] Production `/health` and web meta revisions match the selected SHA.
- [ ] Production release smoke with deploy parity passes.
- [ ] Release marker/tag is created only after production proof is green.
- [ ] Source-of-truth state records SHA, tag, smoke proof, deferred scope, and residual risks.

## Forbidden
- new architecture or deployment framework
- hidden release marker movement
- manual tag creation before production parity
- treating local selected-scope readiness as production release
- claiming connector/proactive/native extension readiness without their gates

## Responsibility Lanes

| Lane | Owner | Expected output | Proof | Status |
| --- | --- | --- | --- | --- |
| Coordinator | Active chat | Candidate selection, integration, final verdict | Parent gate and state updates | IN_PROGRESS |
| QA/Test | QA explorer | Minimal gate checklist and blocker posture | Read-only report integrated | COMPLETED |
| Ops/Release | Ops explorer, then coordinator | Exact deploy/smoke/tag sequence and required access | Read-only report, then commands | IN_PROGRESS |
| Documentation/Memory | Coordinator | Release state updates | Source-of-truth diffs | PLANNED |

## Implementation Plan
1. Confirm the current branch, dirty worktree, and deploy source.
2. Create a candidate commit that includes release-relevant changes without
   reverting unrelated user work.
3. Push the candidate branch and, if appropriate, fast-forward the deploy
   source branch.
4. Run production release smoke with deploy parity against
   `https://aviary.luckysparrow.ch`.
5. Create a new release marker only after production proof is green.
6. Update source-of-truth state and result report.

## Acceptance Criteria
- Final verdict is exactly one of `released`, `blocked`, or
  `locally verified but not released`.
- If `released`, the report includes selected SHA, tag, production smoke
  result, deploy parity, and cleanup evidence.
- If `blocked`, the report names the blocking access, command, or failing gate.

## Validation Evidence
- Local gate: inherited from PRJ-1230 pending pre-push sanity.
- Production gate: pending.
- Cleanup: pending.

## Result Report
- Task summary: pending
- Selected SHA: pending
- Selected tag: pending
- Branch/source: pending
- How tested: pending
- Production proof: pending
- What is incomplete: pending
- Final verdict: pending
