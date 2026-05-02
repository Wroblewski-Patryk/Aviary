# Task

## Header
- ID: PRJ-896
- Title: Reflections Body Copy Localization
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-895
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 896
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-895 identified `/reflections` as the highest-impact remaining localized module-copy gap after the latest Polish route audit. The route already uses the canonical module shell pattern, but multiple route-owned body-copy strings are still hardcoded in English.

## Goal
Move route-owned `/reflections` body copy into the existing `UI_COPY.reflections` contract so the Polish Reflections surface is product-usable and no longer leaks English instructional text.

## Success Signal
- User or operator problem: Polish users see English body copy inside the Reflections module.
- Expected product or reliability outcome: Reflections reads as a localized product surface while preserving the existing canonical layout.
- How success will be observed: build passes and a Polish browser smoke finds localized Reflections phrases with targeted English route-owned phrases absent.
- Post-launch learning needed: no

## Deliverable For This Stage
Implementation, verification, and source-of-truth updates for the `/reflections` route-owned body-copy localization slice.

## Scope
- `web/src/App.tsx`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-896-reflections-body-copy-localization.md`

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- keep the slice limited to `/reflections` route-owned body copy

## Implementation Plan
1. Add missing Reflections copy keys to `UI_COPY.reflections` for English, Polish, and German.
2. Replace hardcoded `/reflections` stat, flow, prompt, status, and panel labels with `copy.reflections` references.
3. Preserve data-owned/shared recent-activity entries for a separate shared localization task.
4. Run the web build and a Polish browser smoke on `/reflections`.
5. Update task and context evidence.

## Acceptance Criteria
- `/reflections` route-owned stat details, flow labels, prompts, and panel headers read from `UI_COPY.reflections`.
- Polish `/reflections` no longer contains the targeted old English route-owned phrases.
- Build and browser smoke evidence are recorded.
- No backend, DB, auth, scheduler, provider, or action-layer behavior changes.

## Definition of Done
- [x] Reflections body copy is localized through the existing UI copy system.
- [x] `Push-Location .\web; npm run build; Pop-Location` passes.
- [x] Polish `/reflections` smoke passes with screenshot evidence.

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
- Manual checks: Chrome CDP Polish `/reflections` copy smoke passed with a mocked app API snapshot; targeted localized phrases were present, targeted old English route-owned phrases and the rough `0 wnioski` form were absent, and no horizontal overflow was detected at 390px width.
- Screenshots/logs: `.codex/artifacts/prj896-reflections-body-copy-localization/pl-reflections-copy-smoke.json`, `.codex/artifacts/prj896-reflections-body-copy-localization/pl-reflections-mobile.png`
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
- Design source reference: canonical module shell and PRJ-895 localized module-copy audit
- Canonical visual target: existing `/reflections` canonical module shell
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: `UI_COPY` localization and canonical module canvas/stat/process/side panels
- New shared pattern introduced: no
- Design-memory entry reused: localized canonical module copy pattern from PRJ-891 through PRJ-894
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: no change
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: shared recent-activity entries may remain English and are out of scope
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
- Rollback note: revert the `web/src/App.tsx` copy references and dictionary additions
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
The shared recent activity feed is intentionally left untouched because it is used across module routes and needs a separate ownership pass.

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
- User or operator affected: Polish UI user of `/reflections`
- Existing workaround or pain: user must mentally translate route-owned English explanatory text
- Smallest useful slice: localize route-owned Reflections copy only
- Success metric or signal: targeted Polish smoke passes
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: browse localized Reflections module
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: Chrome CDP Polish `/reflections` copy smoke
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

- Task summary: Localized route-owned Reflections body copy through `UI_COPY.reflections` and fixed Polish zero-form insight counts.
- Files changed: `web/src/App.tsx`, `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`, `.codex/tasks/PRJ-896-reflections-body-copy-localization.md`
- How tested: web production build and Chrome CDP Polish `/reflections` copy smoke.
- What is incomplete: shared recent-activity feed localization remains separate.
- Next steps: localize shared recent-activity entries or run `/tools` ownership pass.
- Decisions made: browser smoke used a mocked app API snapshot because local register returned HTTP 500 and the task scope was frontend copy, not auth/backend validation.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `/reflections` contains route-owned English body copy in stats, flow rows, prompt cards, and panel headers.
- Gaps: shared recent-activity entries still need separate localization ownership.
- Inconsistencies: localized module routes are now mostly clean, but Reflections lags behind the same `UI_COPY` pattern.
- Architecture constraints: reuse `UI_COPY`; avoid route-specific localization systems.

### 2. Select One Priority Task
- Selected task: PRJ-896 Reflections Body Copy Localization.
- Priority rationale: PRJ-895 identified it as the highest-impact remaining route-owned localization gap.
- Why other candidates were deferred: Memory shared activity and Tools provider/data copy require separate ownership decisions.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/App.tsx`, task/context docs.
- Logic: add copy keys and replace hardcoded route-owned strings with localized references.
- Edge cases: singular/plural visible counts should not regress; shared data-owned English should not be treated as a route-owned failure.

### 4. Execute Implementation
- Implementation notes: Added English, Polish, and German copy keys to `UI_COPY.reflections`; replaced hardcoded Reflections stat, flow, prompt, status, and panel strings; added a Polish zero-count insight suffix.

### 5. Verify and Test
- Validation performed: `Push-Location .\web; npm run build; Pop-Location`; Chrome CDP Polish `/reflections` copy smoke with screenshot.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leaving singular/plural logic as-is, but screenshot review exposed `0 wnioski`; a zero-form suffix was the smallest clear fix.
- Technical debt introduced: no
- Scalability assessment: consistent with the existing `UI_COPY` route-localization pattern.
- Refinements made: corrected Polish zero-form insight labels after visual review.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-896-reflections-body-copy-localization.md`
- Context updated: `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
