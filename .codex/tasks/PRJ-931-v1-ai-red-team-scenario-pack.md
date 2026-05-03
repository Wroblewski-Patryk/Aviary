# Task

## Header
- ID: PRJ-931
- Title: V1 AI Red-Team Scenario Pack
- Task Type: research
- Current Stage: release
- Status: DONE
- Owner: Security
- Depends on: PRJ-921
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 931
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The v1 release audit identifies missing AI red-team evidence as a P1 hardening
gap. `AI_TESTING_PROTOCOL.md` and `.codex/agents/ai-red-team-agent.md` already
define required coverage, but the release lane did not yet have one concrete
scenario pack for v1.

## Goal
Create a reproducible v1 AI red-team scenario pack covering prompt injection,
tool-boundary bypass attempts, data exfiltration, unauthorized memory access,
connector misuse, malicious web content, memory corruption, and malformed
inputs.

## Scope
- `.codex/tasks/PRJ-931-v1-ai-red-team-scenario-pack.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/security/v1-ai-red-team-scenario-pack.md`
- `docs/security/v1-ai-red-team-scenarios.json`
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `docs/planning/v1-core-acceptance-bundle.md`
- `docs/engineering/testing.md`
- `docs/README.md`
- `docs/index.md`

## Implementation Plan
1. Review `AI_TESTING_PROTOCOL.md`, the AI red-team agent, secure development
   lifecycle, testing guidance, and v1 release plan.
2. Create a human-readable scenario pack with attack scope, assumptions,
   execution rules, expected fail-closed posture, and reporting template.
3. Create a machine-readable JSON scenario file using the required structured
   scenario shape.
4. Link the scenario pack from testing, release, security, and docs entrypoints.
5. Validate JSON, links, and whitespace.

## Acceptance Criteria
- Scenario pack covers prompt injection, role break, tool bypass, data
  exfiltration, unauthorized memory access, connector misuse, malicious web
  content, memory corruption, and malformed/mixed input.
- Scenarios are multi-turn where relevant and include `expected` plus
  `must_not` checks.
- The pack avoids real secrets, real private data, and instructions to perform
  harmful actions.
- Release docs distinguish scenario-pack creation from executed pass/fail
  evidence.

## Definition of Done
- [x] Human-readable scenario pack exists.
- [x] JSON scenario pack exists and parses.
- [x] Release, testing, docs, task board, and project state are synchronized.
- [x] Validation evidence is recorded.

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
- Tests: not applicable for docs/scenario-pack-only change
- Manual checks:
  - JSON scenario pack parse check passed
  - local markdown link/reference check passed
  - `git diff --check` passed
- Screenshots/logs: not applicable
- High-risk checks:
  - no real secrets or private production data included
  - pack is not marked as executed AI red-team pass/fail evidence
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `AI_TESTING_PROTOCOL.md`
  - `.codex/agents/ai-red-team-agent.md`
  - `docs/security/secure-development-lifecycle.md`
  - `docs/engineering/testing.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none.

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no runtime smoke change
- Rollback note: revert docs/context changes if superseded
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
- [x] Learning journal update was not required; no new recurring pitfall was
  confirmed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: yes
- Data classification: synthetic adversarial prompts; no real secrets
- Trust boundaries: runtime instructions, memory ownership, connector
  permissions, tool authorization, cross-user data
- Permission or ownership checks: scenario expectations require fail-closed
  handling for unauthorized access and connector misuse
- Abuse cases: prompt injection, hidden instruction extraction, data
  exfiltration, unauthorized memory access, connector misuse, malicious web
  page instructions, memory corruption
- Secret handling: no real secrets included
- Security tests or scans: scenario pack prepared; execution remains follow-up
- Fail-closed behavior: required by scenario expected outcomes
- Residual risk: scenario pack is not executed pass/fail evidence yet

## AI Testing Evidence
- `AI_TESTING_PROTOCOL.md` reviewed: yes
- Memory consistency scenarios: included
- Multi-step context scenarios: included
- Adversarial or role-break scenarios: included
- Prompt injection checks: included
- Data leakage and unauthorized access checks: included
- Result: scenario pack created; execution results remain future evidence

## Result Report
- Task summary: created the v1 AI red-team scenario pack and linked it from
  security, testing, release, and docs entrypoints.
- Files changed:
  - `.codex/tasks/PRJ-931-v1-ai-red-team-scenario-pack.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/security/v1-ai-red-team-scenario-pack.md`
  - `docs/security/v1-ai-red-team-scenarios.json`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `docs/planning/v1-core-acceptance-bundle.md`
  - `docs/engineering/testing.md`
  - `docs/README.md`
  - `docs/index.md`
- How tested:
  - JSON parse check
  - link/reference check
  - `git diff --check`
- What is incomplete:
  - scenario execution results are not captured yet
  - PRJ-932 cross-user/session isolation audit remains separate
  - PRJ-933 provider payload leakage audit remains separate
- Next steps: execute this pack or continue to `PRJ-932`.
- Decisions made: `PRJ-931` delivers reproducible scenario coverage, not a
  passing red-team report.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - AI red-team evidence was identified as missing from the v1 release bundle.
- Gaps:
  - no concrete v1 scenario pack existed.
- Inconsistencies:
  - no mismatch found; requirements existed but needed a runnable pack.
- Architecture constraints:
  - use existing AI testing protocol and red-team agent expectations.

### 2. Select One Priority Task
- Selected task: PRJ-931 V1 AI Red-Team Scenario Pack.
- Priority rationale: locally actionable P1 hardening after PRJ-921.
- Why other candidates were deferred: PRJ-930 needs production deployment
  evidence; PRJ-909 and PRJ-918 need operator inputs.

### 3. Plan Implementation
- Files or surfaces to modify: docs/context files listed in Scope.
- Logic: create human and JSON scenario pack; link to release/testing docs.
- Edge cases:
  - avoid real secrets
  - do not claim execution results
  - keep harmful prompts framed as defensive tests

### 4. Execute Implementation
- Implementation notes:
  - added scenario pack doc
  - added JSON scenario pack
  - linked release, testing, security, and docs surfaces

### 5. Verify and Test
- Validation performed:
  - JSON parse
  - local reference check
  - `git diff --check`
- Result: passed.

### 6. Self-Review
- Simpler option considered: only mention AI red-team in release plan;
  rejected because it would not make the work reproducible.
- Technical debt introduced: no
- Scalability assessment: JSON scenarios can become automated tests later.
- Refinements made:
  - separated scenario-pack creation from execution evidence
  - kept provider payload leakage and cross-user isolation as follow-up audits

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/security/v1-ai-red-team-scenario-pack.md`
  - `docs/security/v1-ai-red-team-scenarios.json`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `docs/planning/v1-core-acceptance-bundle.md`
  - `docs/engineering/testing.md`
  - `docs/README.md`
  - `docs/index.md`
- Context updated:
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
- Learning journal updated: not applicable.
