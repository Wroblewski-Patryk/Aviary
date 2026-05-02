# Task

## Header
- ID: PRJ-897
- Title: Shared Recent Activity Localization
- Task Type: refactor
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-896
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 897
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-896 left shared recent-activity feed entries as the next smallest localization gap. The same hardcoded English array is reused by Dashboard, Memory, Reflections, and Personality.

## Goal
Localize the shared recent-activity entries through the existing UI copy structure so Polish module routes no longer inherit English activity titles or timestamps from a shared route-local constant.

## Success Signal
- User or operator problem: Polish users still see English activity rows on otherwise localized module surfaces.
- Expected product or reliability outcome: shared activity rows follow the active UI language wherever they are reused.
- How success will be observed: build passes and a Polish browser smoke confirms localized activity titles and absence of the old English activity strings.
- Post-launch learning needed: no

## Deliverable For This Stage
Implementation, verification, and source-of-truth updates for the shared recent-activity localization slice.

## Scope
- `web/src/App.tsx`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-897-shared-recent-activity-localization.md`

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not change backend activity APIs or persistence

## Implementation Plan
1. Add shared recent-activity row copy to `UI_COPY.common` for English, Polish, and German.
2. Replace the hardcoded `personalityRecentActivity` array with the localized shared copy.
3. Localize the shared Personality activity action label if it is route-owned.
4. Run the web build and a targeted Polish smoke on `/memory`, `/reflections`, `/dashboard`, and `/personality`.
5. Update task and context evidence.

## Acceptance Criteria
- Shared recent-activity rows render from the active UI language.
- Polish Memory and Reflections do not show the old English shared activity titles.
- Build and browser smoke evidence are recorded.
- No backend, DB, auth, scheduler, provider, or action-layer behavior changes.

## Definition of Done
- [x] Shared recent-activity copy is localized through the existing UI copy system.
- [x] `Push-Location .\web; npm run build; Pop-Location` passes.
- [x] Polish browser smoke across affected shared surfaces passes.

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
- Tests: `Push-Location .\web; npm run build; Pop-Location` passed.
- Manual checks: Chrome CDP Polish shared activity smoke passed across `/dashboard`, `/memory`, `/reflections`, and `/personality`; old English activity rows were absent and no horizontal overflow was detected at 390px width.
- Screenshots/logs: `.codex/artifacts/prj897-shared-recent-activity-localization/pl-shared-recent-activity-smoke.json`, `.codex/artifacts/prj897-shared-recent-activity-localization/pl-memory-shared-activity-scrolled.png`
- High-risk checks: no runtime, backend, auth, provider, scheduler, database, or action-layer changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`, `docs/governance/autonomous-engineering-loop.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: canonical localized module shell work PRJ-891 through PRJ-896
- Canonical visual target: shared recent-activity rows inside canonical Dashboard, Memory, Reflections, and Personality surfaces
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: `UI_COPY` localization
- New shared pattern introduced: no
- Design-memory entry reused: localized canonical module copy pattern
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: no change
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: `/tools` still needs a copy ownership pass for route-owned versus provider/data-owned English values.
- State checks: loading not changed | empty not changed | error not changed | success checked
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: mobile checked at 390px
- Input-mode checks: pointer not changed | keyboard not changed | touch layout checked
- Accessibility checks: no semantic regressions intended
- Parity evidence: Chrome CDP smoke screenshot in task artifact directory

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note: revert the `web/src/App.tsx` shared activity copy patch
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
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This task localizes the current static shared activity rows only. Replacing them with real persisted activity is a separate product/data task.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY` or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB -> validation -> error handling -> test. Partial implementations, mock-only paths, placeholders, fake data, and temporary fixes are forbidden.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: Polish UI user of shared module surfaces
- Existing workaround or pain: activity rows remain English inside otherwise localized screens
- Smallest useful slice: localize the shared static activity rows
- Success metric or signal: targeted Polish smoke passes
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: browse localized module surfaces with shared activity rows
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: Chrome CDP Polish shared activity smoke
- Rollback or disable path: revert frontend localization patch

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not changed
- Error state verified: not changed
- Refresh/restart behavior verified: route loaded from a fresh headless browser profile
- Regression check performed: web production build and targeted browser smoke

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: public UI copy only
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: no secrets touched
- Security tests or scans: not applicable
- Fail-closed behavior: not applicable
- Residual risk: low

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: Moved shared recent-activity rows into `UI_COPY.common.recentActivity` and localized the shared Personality activity action label.
- Files changed: `web/src/App.tsx`, `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`, `.codex/tasks/PRJ-897-shared-recent-activity-localization.md`
- How tested: web production build and Chrome CDP Polish shared activity smoke.
- What is incomplete: `/tools` still needs route-owned versus provider/data-owned copy ownership review.
- Next steps: run a narrow `/tools` ownership pass.
- Decisions made: kept the rows as static UI copy for this slice; replacing them with real persisted activity remains a separate product/data task.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `personalityRecentActivity` is a shared hardcoded English array reused across localized surfaces.
- Gaps: recent activity is static UI copy, not real persisted activity.
- Inconsistencies: localized module surfaces can still show English shared rows.
- Architecture constraints: reuse `UI_COPY`; avoid a new localization store.

### 2. Select One Priority Task
- Selected task: PRJ-897 Shared Recent Activity Localization.
- Priority rationale: it closes the shared gap explicitly left by PRJ-896 and improves several routes at once.
- Why other candidates were deferred: `/tools` ownership needs a separate audit to avoid translating provider/data-owned values incorrectly.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/App.tsx`, task/context docs.
- Logic: move shared activity rows and the route-owned action label into `UI_COPY`.
- Edge cases: keep timestamps localized as display copy without implying real live activity.

### 4. Execute Implementation
- Implementation notes: Added localized shared activity rows and `view` labels to `UI_COPY.common`; replaced the hardcoded array and Personality action label with copy references.

### 5. Verify and Test
- Validation performed: `Push-Location .\web; npm run build; Pop-Location`; Chrome CDP Polish shared activity smoke across four affected routes.
- Result: passed.

### 6. Self-Review
- Simpler option considered: duplicating Polish rows in each route, but shared `UI_COPY.common` better matches the existing reuse boundary.
- Technical debt introduced: no
- Scalability assessment: consistent with the existing UI copy localization approach.
- Refinements made: added a scrolled screenshot focused on the shared activity rows after the first screenshot landed above the target section.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-897-shared-recent-activity-localization.md`
- Context updated: `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
