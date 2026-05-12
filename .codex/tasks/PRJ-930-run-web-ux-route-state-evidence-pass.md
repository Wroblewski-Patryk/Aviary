# Task

## Header
- ID: PRJ-930
- Title: Run web UX route-state evidence pass
- Task Type: release
- Current Stage: verification
- Status: BLOCKED
- Owner: Frontend Builder | QA/Test
- Depends on: PRJ-929
- Priority: P1
- Coverage Ledger Rows: `ARCH-WEB-UX-001`
- Module Confidence Rows: not closed
- Requirement Rows: not applicable
- Quality Scenario Rows: web route-state/accessibility evidence
- Risk Rows: route-smoke validation reliability
- Iteration: 930
- Operation Mode: BUILDER
- Mission ID: `MIS-V1-ARCH-EVIDENCE-2026-05-11`
- Mission Status: BLOCKED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed.
- [x] `.agents/core/mission-control.md` was reviewed for long-running work.
- [x] Missing or template-like state tables were bootstrapped from repository
      sources, or confirmed not needed.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified or
      marked not applicable.
- [x] The task or mission improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: Collect fresh route-state evidence for `ARCH-WEB-UX-001`.
- Release objective advanced: v1 web UX confidence.
- Included slices: Browser plugin attempt, local Vite reachability, typecheck,
  Vite build, route-smoke command-pack execution, cleanup.
- Explicit exclusions: visual redesign, UI code polish, provider credentials,
  production deploy.
- Checkpoint cadence: record validation pass/fail and environment cleanup.
- Stop conditions: route-state harness fails before producing reliable evidence.
- Handoff expectation: next task repairs or replaces the browser route-state
  harness before claiming `ARCH-WEB-UX-001`.

## Context
After `PRJ-929`, `ARCH-WEB-UX-001` became the next no-external-input row. The
first task was to run the generated command pack and collect fresh proof.

## Goal
Prove the current web route-state/accessibility baseline, or record an honest
failed validation if the harness blocks proof.

## Success Signal
- User or operator problem: route smoke alone had stale confidence; fresh route
  state proof was needed before v1 closure.
- Expected product or reliability outcome: route-state proof is attached to the
  architecture radar.
- How success will be observed: `npm run smoke:routes`, typecheck, and Vite
  build pass with preserved exit code.
- Post-launch learning needed: yes

## Deliverable For This Stage
Fresh validation result for the `ARCH-WEB-UX-001` command pack.

## Scope
- `web/scripts/route-smoke.mjs`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/context/LEARNING_JOURNAL.md`
- `.agents/state/known-issues.md`
- `.agents/state/system-health.md`
- `.agents/state/next-steps.md`
- this task file

## Implementation Plan
1. Attempt Browser plugin route validation.
2. If Browser is unavailable, use the generated `ARCH-WEB-UX-001` command pack.
3. Preserve external command exit codes while validating.
4. If route smoke fails, inspect whether the failure is product UI or harness/environment.
5. Clean up any validation-owned browser or dev-server processes.
6. Record the exact blocker and next repair.

## Acceptance Criteria
- Passing case: route smoke, typecheck, and build pass with non-masked exit
  status.
- Failing case: route smoke failure is recorded as `BLOCKED` or `FAILED`, not
  counted as UX proof.
- Validation-owned local processes are stopped.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] Browser path attempted and blocker recorded.
- [x] Command-pack execution attempted with preserved exit code.
- [x] Cleanup evidence recorded.
- [ ] Route-state proof collected.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- claiming `ARCH-WEB-UX-001` as `READY` without a passing route-state proof
- hiding route-smoke failures behind `Pop-Location` exit-code masking
- leaving validation-owned browser or dev-server processes running

## Validation Evidence
- Tests:
  - Browser plugin path: blocked, `No active Codex browser pane available`
  - `Push-Location .\web; npm run smoke:routes; if ($LASTEXITCODE -eq 0) { npm exec -- tsc -b --pretty false }; if ($LASTEXITCODE -eq 0) { npm exec -- vite build }; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
    -> failed with `Timed out waiting for CDP response to Page.enable`
  - `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
    -> passed
  - `Push-Location .\web; npm exec -- vite build; Pop-Location`
    -> passed
- Manual checks:
  - direct one-off `chrome --headless=new --dump-dom http://127.0.0.1:5173/`
    against Vite returned DOM, so Chrome itself can render a local route
  - route-smoke internal CDP harness remains unreliable in this host
  - validation-owned Vite server was stopped; matching Chrome temp profile
    directory counts after cleanup were `0,0,0`
- Screenshots/logs: route-smoke stack traces recorded in task state and system health
- High-risk checks: failed smoke is not counted as route-state proof
- Coverage ledger updated: yes
- Coverage rows closed or changed: `ARCH-WEB-UX-001` remains `IMPLEMENTED_NEEDS_EVIDENCE`
- Module confidence ledger updated: not applicable
- Requirements matrix updated: not applicable
- Quality scenarios updated: not applicable
- Risk register updated: not applicable
- Reality status: blocked

## Architecture Evidence
- Architecture source reviewed: `docs/operations/project-status-dashboard.md`,
  `docs/operations/architecture-implementation-audit-2026-05-10.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: keep `ARCH-WEB-UX-001` open

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/screen-quality-checklist.md`
- Canonical visual target: current route shell
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not completed
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: not applicable
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: no
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: unknown because route-state proof is blocked
- State checks: blocked
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: not completed
- Input-mode checks: not completed
- Accessibility checks: not completed
- Parity evidence: blocked

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: command packs now preserve exit code
- Rollback note: revert route-smoke harness-only changes if a better browser path replaces them
- Observability or alerting impact: improves honesty of web validation failures
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

## Notes
Safe assumption: the product build is not currently proven broken because
typecheck and Vite build pass, and a one-off local Chrome DOM dump against Vite
returned DOM. The failing path is the committed route-state harness.

## Result Report

- Task summary: `ARCH-WEB-UX-001` validation attempted but blocked by
  route-smoke Chrome/CDP timeout.
- Files changed: route-smoke harness send-order hardening, command-pack exit
  preservation, state/context records.
- How tested: Browser attempted, route smoke attempted, typecheck and build run.
- What is incomplete: route-state/accessibility proof is not collected.
- Next steps: repair or replace the route-state browser harness, then rerun
  the `ARCH-WEB-UX-001` command pack.
- Decisions made: failed route smoke is treated as a validation blocker, not as
  web UX completion evidence.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `ARCH-WEB-UX-001` lacks fresh proof.
- Gaps: Browser plugin has no active pane; route-smoke CDP path times out.
- Inconsistencies: PowerShell command packs could mask failed native commands
  when followed by `Pop-Location`.
- Architecture constraints: no product UI changes without proof target.

### 2. Select One Priority Mission Objective
- Selected task: `ARCH-WEB-UX-001`
- Priority rationale: next no-external-input row after `PRJ-929`.
- Why other candidates were deferred: provider smoke needs credentials; doc
  maps and proactive proof are lower in dashboard order.

### 3. Plan Implementation
- Files or surfaces to modify: validation harness only if needed; context/state.
- Logic: try Browser first, then generated command pack.
- Edge cases: preserve exit code and clean validation processes.

### 4. Execute Implementation
- Implementation notes: fixed command-pack exit preservation and CDP pending
  registration ordering; attempted dump-dom fallback but did not keep it because
  it did not produce reliable route-smoke proof.

### 5. Verify and Test
- Validation performed: Browser attempt, route smoke, typecheck, Vite build,
  cleanup checks.
- Result: route smoke blocked; typecheck/build passed; Vite server and temp
  Chrome profile directories cleaned up.

### 6. Self-Review
- Simpler option considered: ignore route-smoke and count build/typecheck; rejected because route-state proof is the requirement.
- Technical debt introduced: no product debt; validation harness still needs repair.
- Scalability assessment: command packs now preserve failure status for future tasks.
- Refinements made: recorded the blocker and cleanup evidence.

### 7. Update Documentation and Knowledge
- Docs updated: task board, project state, known issues, system health, learning journal.
- Context updated: yes
- Learning journal updated: yes.
