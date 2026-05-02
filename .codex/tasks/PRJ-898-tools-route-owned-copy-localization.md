# Task

## Header
- ID: PRJ-898
- Title: Tools Route-Owned Copy Localization
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-897
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 898
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
After PRJ-897, `/tools` is the remaining planned localization surface with mixed English ownership. Route-owned labels should be localized, while provider/data-owned values should remain untouched.

## Goal
Localize `/tools` route-owned copy without translating provider-owned or API-owned values.

## Success Signal
- User or operator problem: Polish users see English UI chrome inside the Tools route.
- Expected product or reliability outcome: Tools route-owned UI copy follows the active UI language while raw provider values remain faithful to source data.
- How success will be observed: build passes and a Polish browser smoke confirms localized route-owned Tools strings and absence of targeted old English UI strings.
- Post-launch learning needed: no

## Deliverable For This Stage
Implementation, verification, and source-of-truth updates for `/tools` route-owned copy localization.

## Scope
- `web/src/App.tsx`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-898-tools-route-owned-copy-localization.md`

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not translate provider/API-owned values such as group titles, item labels, item descriptions, status reasons, next actions, capabilities, or source-of-truth strings

## Implementation Plan
1. Add missing route-owned Tools copy keys to `UI_COPY.tools` for English, Polish, and German.
2. Replace hardcoded Tools summary notes, directory title/count labels, status labels, provider readiness labels, Telegram link helper text, expiry copy, and toast/error copy with `copy.tools`.
3. Preserve provider/API-owned values exactly as received from the backend.
4. Run the web build and a targeted Polish `/tools` browser smoke.
5. Update task and context evidence.

## Acceptance Criteria
- Route-owned `/tools` UI text renders from `UI_COPY.tools`.
- Polish `/tools` smoke finds localized route-owned phrases and no targeted old English UI strings.
- Provider/API-owned strings remain untouched.
- Build and browser smoke evidence are recorded.

## Definition of Done
- [x] Tools route-owned copy is localized through the existing UI copy system.
- [x] `Push-Location .\web; npm run build; Pop-Location` passes.
- [x] Polish `/tools` browser smoke passes.

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
- Manual checks: Chrome CDP Polish `/tools` route-owned copy smoke passed with a mocked app API snapshot; targeted localized phrases were present, targeted old English route-owned phrases were absent, visible provider-owned values were preserved, and no horizontal overflow was detected at 390px width.
- Screenshots/logs: `.codex/artifacts/prj898-tools-route-owned-copy-localization/pl-tools-route-owned-copy-smoke.json`, `.codex/artifacts/prj898-tools-route-owned-copy-localization/pl-tools-route-owned-copy-mobile.png`
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
- Design source reference: canonical localized module shell work and PRJ-897 ownership pass
- Canonical visual target: existing `/tools` canonical directory surface
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: `UI_COPY` localization
- New shared pattern introduced: no
- Design-memory entry reused: localized canonical route-owned copy pattern
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: no change
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: provider/API-owned English values may remain by design.
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
- Rollback note: revert the `web/src/App.tsx` Tools copy patch
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
Provider/API-owned copy remains out of scope by design.

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
- User or operator affected: Polish UI user of `/tools`
- Existing workaround or pain: user must interpret English route-owned UI text inside the Tools surface
- Smallest useful slice: localize route-owned Tools copy only
- Success metric or signal: targeted Polish smoke passes
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: browse localized Tools surface
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: Chrome CDP Polish `/tools` route-owned copy smoke
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

- Task summary: Localized `/tools` route-owned UI copy and preserved provider/API-owned values.
- Files changed: `web/src/App.tsx`, `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`, `.codex/tasks/PRJ-898-tools-route-owned-copy-localization.md`
- How tested: web production build and Chrome CDP Polish `/tools` route-owned copy smoke.
- What is incomplete: provider/API-owned values may still be English by design.
- Next steps: run a fresh localized module-copy reaudit.
- Decisions made: `link_state` enum display is frontend-owned and was localized; provider-owned item fields were intentionally not translated.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `/tools` still contains hardcoded route-owned English strings.
- Gaps: provider/API-owned values remain English and need ownership separation, not blanket translation.
- Inconsistencies: other localized modules use `UI_COPY` for their route-owned body copy.
- Architecture constraints: reuse `UI_COPY`; preserve backend-owned values.

### 2. Select One Priority Task
- Selected task: PRJ-898 Tools Route-Owned Copy Localization.
- Priority rationale: it is the planned remaining localization surface after shared recent activity cleanup.
- Why other candidates were deferred: provider/data localization requires backend or data-contract decisions and is not part of this route-owned UI slice.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/App.tsx`, task/context docs.
- Logic: add missing copy keys and route-owned format helpers.
- Edge cases: do not translate backend-owned item fields or provider identifiers.

### 4. Execute Implementation
- Implementation notes: Added missing Tools copy keys, localized Tools route-owned status/link-state formatting and helper text, and removed the now-unused title-case formatter.

### 5. Verify and Test
- Validation performed: `Push-Location .\web; npm run build; Pop-Location`; Chrome CDP Polish `/tools` route-owned copy smoke.
- Result: passed.

### 6. Self-Review
- Simpler option considered: blanket-translating visible English strings, but this would corrupt provider/API-owned values.
- Technical debt introduced: no
- Scalability assessment: consistent with the existing `UI_COPY` localization approach.
- Refinements made: localized `link_state` enum display after the first smoke text sample exposed `Not Linked`.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-898-tools-route-owned-copy-localization.md`
- Context updated: `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
