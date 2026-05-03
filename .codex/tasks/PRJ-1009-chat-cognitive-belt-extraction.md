# Task

## Header
- ID: PRJ-1009
- Title: Extract chat cognitive belt presentation from App.tsx
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1008
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1009
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`PRJ-1008` selected the chat cognitive belt as the next safe presentation
extraction because it is a pure card list with one explicit goal-progress
value.

## Goal

Move chat cognitive belt card-list presentation into a typed chat component
without moving route data derivation, planning summaries, or goal-progress
calculation out of `App()`.

## Scope

- `web/src/components/chat.tsx`
- `web/src/App.tsx`
- `docs/frontend/route-component-map.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: conversation context card chrome was still embedded
  in the large chat route branch.
- Expected product or reliability outcome: chat route presentation ownership is
  more explicit while data ownership remains unchanged.
- How success will be observed: build and route smoke pass with
  `ChatCognitiveBelt` rendering the card list.
- Post-launch learning needed: no

## Deliverable For This Stage

Release-ready component extraction with validation and docs/context sync.

## Constraints
- do not move `chatCognitiveBelt` data construction out of `App()`
- do not move planning/health summary derivation
- do not change cognitive belt CSS classes or layout
- do not touch portrait/support panel composition

## Implementation Plan
1. Add `ChatCognitiveBeltItem` and `ChatCognitiveBelt` to
   `web/src/components/chat.tsx`.
2. Replace inline cognitive belt JSX in `web/src/App.tsx`.
3. Keep data construction and `chatGoalCard.progress` in `App()`.
4. Update frontend docs and context.
5. Run build, route smoke, and diff validation.

## Acceptance Criteria
- Cognitive belt card presentation renders from `ChatCognitiveBelt`.
- Data derivation and progress value remain in `App()`.
- Documentation names the new component ownership.
- Validation passes.

## Definition of Done
- [x] Component extraction completed.
- [x] Behavior/data ownership preserved in `App()`.
- [x] Docs and context updated.
- [x] Relevant validation completed.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- Manual checks:
  - confirmed `ChatCognitiveBelt` receives card data and goal progress through
    explicit props
- High-risk checks:
  - portrait/support panel and transcript shell are untouched
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
  - PRJ-1010 queued for the next extraction audit

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

- Task summary: extracted chat cognitive belt presentation into
  `ChatCognitiveBelt`.
- Files changed:
  - `web/src/components/chat.tsx`
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
  - chat portrait/support panel and transcript shell remain inline
- Next steps:
  - PRJ-1010 audit next chat extraction target
- Decisions made:
  - only presentation moved; data construction remains in `App()`

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - cognitive belt JSX remained inline
- Gaps:
  - chat topbar and support panels still need future ownership decisions
- Inconsistencies:
  - PRJ-1009 was queued but implementation was not present
- Architecture constraints:
  - preserve canonical chat layout and existing route data derivation

### 2. Select One Priority Task
- Selected task: PRJ-1009
- Priority rationale: it was the next queued implementation slice
- Why other candidates were deferred:
  - portrait/support panel requires a visual-specific audit
  - transcript shell touches loading state and refs

### 3. Plan Implementation
- Files or surfaces to modify:
  - chat component module, App usage, frontend docs, context
- Logic:
  - pass typed card data and goal progress into a presentational component
- Edge cases:
  - preserve goal progress bar rendering only for the `goal` card

### 4. Execute Implementation
- Implementation notes:
  - added `ChatCognitiveBeltItem` to keep route card data explicit

### 5. Verify and Test
- Validation performed:
  - build
  - route smoke
  - diff check
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - inline card rendering; rejected because PRJ-1008 selected extraction
- Technical debt introduced: no
- Scalability assessment:
  - adequate for current chat component decomposition
- Refinements made:
  - kept progress width as an explicit prop rather than recalculating in component

### 7. Update Documentation and Knowledge
- Docs updated:
  - frontend route/component map
  - app route cluster audit
  - v1 roadmap
- Context updated:
  - task board
  - project state
- Learning journal updated: not applicable
