# Task

## Header
- ID: PRJ-1017
- Title: Extract chat route display-model helpers from App.tsx
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1016
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1017
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`PRJ-1016` selected a focused chat route display-model helper extraction. Chat
API calls, chat state, transcript behavior, send behavior, and route rendering
must remain in `App()`.

## Goal

Move pure chat route display projections into `web/src/lib/chat-route-model.ts`
without hiding route/API/state ownership.

## Scope

- `web/src/lib/chat-route-model.ts`
- `web/src/App.tsx`
- `docs/frontend/route-component-map.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: chat display projections were inline inside the
  large route owner.
- Expected product or reliability outcome: display-model ownership is explicit
  while route behavior remains in `App()`.
- How success will be observed: build and route smoke pass after `App()` uses
  `buildChatRouteModel`.
- Post-launch learning needed: no

## Deliverable For This Stage

Release-ready helper extraction with validation and docs/context sync.

## Constraints
- do not move chat API calls or route state
- do not move send behavior or transcript reconciliation
- do not move route rendering
- preserve existing fallback strings and display values

## Implementation Plan
1. Add `web/src/lib/chat-route-model.ts`.
2. Move quick action, current focus, linked-channel fallback, intent card,
   motivation metrics, goal card, and related-memory projections into
   `buildChatRouteModel`.
3. Replace inline chat display-model construction in `web/src/App.tsx`.
4. Update frontend docs and context.
5. Run build, route smoke, and diff validation.

## Acceptance Criteria
- `App()` imports and uses `buildChatRouteModel`.
- `chat-route-model.ts` owns only pure display projections.
- Chat API/state/transcript/send behavior remain in `App()`.
- Validation passes.

## Definition of Done
- [x] Helper extraction completed.
- [x] Behavior ownership preserved in `App()`.
- [x] Docs and context updated.
- [x] Relevant validation completed.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- Manual checks:
  - confirmed helper accepts explicit summary inputs and fallback labels
- High-risk checks:
  - chat API calls, state, send handler, transcript mapping, and route rendering
    remain in `App()`
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - PRJ-1018 queued for post-chat cleanup audit

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

- Task summary: extracted chat route display projections into
  `buildChatRouteModel`.
- Files changed:
  - `web/src/lib/chat-route-model.ts`
  - `web/src/App.tsx`
  - `docs/frontend/route-component-map.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- What is incomplete:
  - final post-chat route cleanup audit remains next
- Next steps:
  - PRJ-1018 audit remaining `App.tsx` route-local frontend architecture gaps
- Decisions made:
  - helper receives explicit `Record<string, unknown>` summary inputs rather
    than importing API state or UI copy

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - chat display projections were inline in `App()`
- Gaps:
  - remaining `App.tsx` route gaps need a fresh post-chat audit
- Inconsistencies:
  - PRJ-1017 was queued but helper module was not present
- Architecture constraints:
  - API/state ownership stays in `App()`

### 2. Select One Priority Task
- Selected task: PRJ-1017
- Priority rationale: it was the next queued implementation slice
- Why other candidates were deferred:
  - broader route wrapper extraction should wait for post-chat audit

### 3. Plan Implementation
- Files or surfaces to modify:
  - chat helper module, App usage, frontend docs, context
- Logic:
  - move pure projections behind explicit summary inputs
- Edge cases:
  - preserve no-data channel fallback and active goal/task count fallbacks

### 4. Execute Implementation
- Implementation notes:
  - added typed display-model structures and `buildChatRouteModel`

### 5. Verify and Test
- Validation performed:
  - build
  - route smoke
  - diff check
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - keep projections inline; rejected because chat components now have a clear
    display-model boundary
- Technical debt introduced: no
- Scalability assessment:
  - adequate for current route decomposition
- Refinements made:
  - helper does not import API client or route state

### 7. Update Documentation and Knowledge
- Docs updated:
  - frontend route/component map
  - app route cluster audit
  - v1 roadmap
- Context updated:
  - task board
  - project state
- Learning journal updated: not applicable
