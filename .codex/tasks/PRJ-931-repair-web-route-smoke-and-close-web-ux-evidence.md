# Task

## Header
- ID: PRJ-931
- Title: Repair web route smoke and close web UX evidence
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder | QA/Test
- Depends on: PRJ-930
- Priority: P1
- Coverage Ledger Rows: `ARCH-WEB-UX-001`
- Module Confidence Rows: `AVIARY-WEB-UX-001`
- Requirement Rows: not applicable
- Quality Scenario Rows: web route-state/accessibility evidence
- Risk Rows: route-smoke validation reliability
- Iteration: 931
- Operation Mode: BUILDER
- Mission ID: `MIS-V1-ARCH-EVIDENCE-2026-05-11`
- Mission Status: VERIFIED

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
- Mission objective: Repair the blocked `ARCH-WEB-UX-001` route-state proof.
- Release objective advanced: v1 web UX evidence confidence.
- Included slices: route-smoke harness repair, visible-control accessibility
  check, chat composer accessible name fix, audit/dashboard refresh, state sync.
- Explicit exclusions: visual redesign, provider activation, production deploy.
- Checkpoint cadence: validate command pack, refresh dashboard, then update state.
- Stop conditions: route smoke still fails, build fails, or a product route
  regression is discovered.
- Handoff expectation: future route-shell work can use the updated command pack
  without masked failures or stale `dist` order.

## Context
`PRJ-930` proved that the old route-state evidence path was blocked by
Chrome/CDP timeouts and by command-pack ordering that could test stale `dist`.

## Goal
Make `ARCH-WEB-UX-001` evidence reproducible and close the row as `READY`.

## Success Signal
- User or operator problem: web UX route-state evidence was blocked by a flaky
  browser harness.
- Expected product or reliability outcome: route-state proof runs against the
  freshly built app and verifies basic accessibility state.
- How success will be observed: `tsc`, `vite build`, and `smoke:routes` pass;
  architecture readiness becomes `10/14`.
- Post-launch learning needed: no

## Deliverable For This Stage
Updated route smoke, regenerated audit/dashboard artifacts, and state/context
updates showing `ARCH-WEB-UX-001` as `READY`.

## Scope
- `web/scripts/route-smoke.mjs`
- `web/src/components/chat.tsx`
- `backend/scripts/audit_architecture_implementation_map.py`
- generated audit/dashboard artifacts
- `.codex/context/*`
- `.agents/state/*`
- this task file

## Implementation Plan
1. Replace fragile Chrome/CDP route proof with Playwright-backed route smoke
   when local Playwright is available, keeping dump-DOM fallback.
2. Add route-state checks for marker presence, non-empty body text, no framework
   overlay, and zero visible unnamed interactive controls.
3. Add an accessible name to the chat composer textarea.
4. Fix the generated `ARCH-WEB-UX-001` command pack ordering to run
   `tsc -> Vite build -> route smoke`.
5. Regenerate audit/dashboard and update source-of-truth state.

## Acceptance Criteria
- `ARCH-WEB-UX-001` command pack passes.
- Route smoke reports `14` routes and status `ok`.
- Every route reports marker found, no framework overlay, non-empty body text,
  and `unnamedInteractiveCount=0`.
- Dashboard selected-scope readiness is `10/14`.
- Validation-owned processes and temp route-smoke profiles are cleaned up.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new product behavior
- do not implement workaround UI paths
- do not duplicate route smoke ownership
- keep the action/provider boundary untouched

## Definition of Done
- [x] Route smoke proof passes.
- [x] Web typecheck and production build pass before route smoke.
- [x] Audit/dashboard refreshed.
- [x] Source-of-truth state updated.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- claiming visual pixel polish
- provider activation
- production deploy changes
- lowering the route-state/a11y evidence bar to make the test pass

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm exec -- tsc -b --pretty false; if ($LASTEXITCODE -eq 0) { npm exec -- vite build }; if ($LASTEXITCODE -eq 0) { npm run smoke:routes }; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
    -> passed; route smoke `status=ok`, `route_count=14`, all routes
    `unnamedInteractiveCount=0`
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\audit_architecture_implementation_map.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_project_status_dashboard.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
    -> `rows=15`; `buckets=DEFERRED:1,IMPLEMENTED_NEEDS_EVIDENCE:3,READY:10,V1_BLOCKER:1`; selected-scope readiness `10/14`
- Manual checks:
  - no listener remained on local Vite port `5173`
  - no Chrome process with `aion-route-smoke`, `aion-connector-confirmation`,
    or `aion-dump-test` profile remained
  - temporary `aion-route-smoke-*` profile directory count after cleanup: `0`
- Screenshots/logs: route-smoke JSON output in command evidence
- High-risk checks: `ARCH-CONNECTORS-001` remains a V1 external blocker
- Coverage ledger updated: yes
- Coverage rows closed or changed: `ARCH-WEB-UX-001` -> `READY`
- Module confidence ledger updated: yes
- Module confidence rows closed or changed: `AVIARY-WEB-UX-001`
- Requirements matrix updated: not applicable
- Quality scenarios updated: not applicable
- Risk register updated: not applicable
- Reality status: verified

## Architecture Evidence
- Architecture source reviewed: project dashboard, architecture audit, current focus, known issues.
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: audit/dashboard regenerated

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: current route shell and `docs/ux/screen-quality-checklist.md`
- Canonical visual target: current web shell routes
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: route smoke and shared chat composer
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: route-state/a11y smoke only
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: visual parity not assessed in this slice
- State checks: loading route shell | empty mocked data | blocked provider state | success render
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: no framework overlay found
- Responsive checks: route smoke viewport `1366x900`
- Input-mode checks: visible interactive controls have accessible names
- Accessibility checks: zero visible unnamed interactive controls on all 14 routes
- Parity evidence: route-state evidence only

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: `ARCH-WEB-UX-001` command pack now builds before smoke
- Rollback note: revert `web/scripts/route-smoke.mjs` and chat textarea aria-label
- Observability or alerting impact: improves web evidence reliability
- Staged rollout or feature flag: not applicable

## Result Report

- Task summary: Repaired route smoke and closed `ARCH-WEB-UX-001`.
- Files changed: web route smoke, chat composer textarea, audit/dashboard
  generator state, task/context/state docs.
- How tested: web typecheck, Vite build, route smoke, audit/dashboard regeneration.
- What is incomplete: provider activation, doc-map refresh, proactive target
  sample, deploy automation sample, and mobile scope remain separate rows.
- Next steps: if provider credentials are unavailable, work `ARCH-DOC-MAPS-001`.
- Decisions made: route smoke must build fresh `dist` before checking route
  markers, and Playwright is preferred when available.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `ARCH-WEB-UX-001` was blocked by route-smoke CDP timeout and stale-dist command order.
- Gaps: route smoke did not verify visible unnamed interactive controls.
- Inconsistencies: command pack order ran smoke before build.
- Architecture constraints: no UI redesign or product behavior change.

### 2. Select One Priority Mission Objective
- Selected task: repair `ARCH-WEB-UX-001`.
- Priority rationale: highest no-external-input gap after `PRJ-929`.
- Why other candidates were deferred: providers require credentials; doc maps
  should follow this evidence slice.

### 3. Plan Implementation
- Files or surfaces to modify: route smoke harness, chat textarea accessibility,
  generated audit/dashboard.
- Logic: use Playwright when available; verify route marker, text, overlay, and
  accessible visible controls.
- Edge cases: hidden responsive controls should not count as visible a11y failures.

### 4. Execute Implementation
- Implementation notes: added Playwright-backed smoke path, dump-DOM fallback,
  visible-control name check, and chat textarea `aria-label`.

### 5. Verify and Test
- Validation performed: web command pack and audit/dashboard regeneration.
- Result: passed.

### 6. Self-Review
- Simpler option considered: mark build/typecheck enough; rejected because route-state proof was required.
- Technical debt introduced: no
- Scalability assessment: route smoke now checks route identity and lightweight accessibility state across all routes.
- Refinements made: fixed command order to build before smoke.

### 7. Update Documentation and Knowledge
- Docs updated: task board, project state, current focus, next steps, known issues, regression log, system health.
- Context updated: yes
- Learning journal updated: existing PRJ-930 lessons remain valid.
