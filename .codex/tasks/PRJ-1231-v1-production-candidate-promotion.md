# Task

## Header
- ID: PRJ-1231
- Title: V1 Production Candidate Promotion
- Task Type: release
- Current Stage: release
- Status: DONE
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
- Mission Status: COMPLETED

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
- [x] Selected SHA and release branch are explicit.
- [x] Local gate is green or a blocker is recorded.
- [x] Candidate commit is pushed to the deploy source or blocked with evidence.
- [x] Production `/health` and web meta revisions match the selected SHA.
- [x] Production release smoke with deploy parity passes.
- [x] Release marker/tag is created only after production proof is green.
- [x] Source-of-truth state records SHA, tag, smoke proof, deferred scope, and residual risks.

## Forbidden
- new architecture or deployment framework
- hidden release marker movement
- manual tag creation before production parity
- treating local selected-scope readiness as production release
- claiming connector/proactive/native extension readiness without their gates

## Responsibility Lanes

| Lane | Owner | Expected output | Proof | Status |
| --- | --- | --- | --- | --- |
| Coordinator | Active chat | Candidate selection, integration, final verdict | Parent gate and state updates | COMPLETED |
| QA/Test | QA explorer | Minimal gate checklist and blocker posture | Read-only report integrated | COMPLETED |
| Ops/Release | Ops explorer, then coordinator | Exact deploy/smoke/tag sequence and required access | Read-only report, then commands | COMPLETED |
| Documentation/Memory | Coordinator | Release state updates | Source-of-truth diffs | COMPLETED |

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
- Local gate: PRJ-1230 backend full pytest `1105 passed`; web build, responsive audit, navigation proof, account proof, and route smoke PASS; architecture dashboard `11/11`; pre-push `git diff --check` PASS with LF/CRLF warnings only.
- Production gate: `run_release_smoke.ps1 -BaseUrl https://aviary.luckysparrow.ch -WaitForDeployParity` PASS; `audit_release_reality.py --selected-sha df677370f63d2688eb792f9a3a846d2cd40a564b` -> `GO_FOR_SELECTED_SHA`; `run_release_go_no_go.py --selected-sha ... --enforce-local-head-parity` -> `GO`; selected tag `v1.1.1` go/no-go -> `GO`.
- Cleanup: no validation-owned browser/server leftovers from PRJ-1230; PRJ-1231 production smoke used no local browser/dev server.

## Result Report
- Task summary: packaged the PRJ-1230 selected-scope candidate, pushed it to `main`, waited for production deploy parity, ran production release smoke, created annotated tag `v1.1.1`, and verified selected-tag go/no-go.
- Selected SHA: `df677370f63d2688eb792f9a3a846d2cd40a564b`
- Selected tag: `v1.1.1`
- Branch/source: `codex/uxui-polish-batch` and `origin/main` both pushed to `df677370f63d2688eb792f9a3a846d2cd40a564b`; Coolify production reports source automation.
- How tested: PRJ-1230 local gate; PRJ-1231 `git fetch origin --tags`, `git diff --check`, production release smoke with deploy parity, release reality audit, release go/no-go, selected-tag go/no-go.
- Production proof: `https://aviary.luckysparrow.ch` health OK; backend runtime revision and web shell build revision both `df677370f63d2688eb792f9a3a846d2cd40a564b`; `release_ready=true`; `release_violations=[]`; v1 final acceptance `core_v1_bundle_ready`.
- What is incomplete: provider activation, proactive launch expansion, deploy automation hardening, and native mobile proof remain deferred extension rows outside selected-scope v1.
- Final verdict: released
