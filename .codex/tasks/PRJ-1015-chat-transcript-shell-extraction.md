# Task

## Header
- ID: PRJ-1015
- Title: Extract chat transcript shell from App.tsx
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1014
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1015
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`PRJ-1014` selected a thin transcript shell extraction. Message mapping,
message refs, delivery-state calculation, timestamp formatting, markdown
rendering, and route data helpers must remain in `App()`.

## Goal

Move chat thread-column and transcript-container presentation into a typed,
forward-ref component while preserving behavior ownership in `App()`.

## Scope

- `web/src/components/chat.tsx`
- `web/src/App.tsx`
- `docs/frontend/route-component-map.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: transcript container chrome remained inline with
  behavior-sensitive message mapping.
- Expected product or reliability outcome: shell presentation ownership is
  explicit while refs and mapping behavior stay in the route owner.
- How success will be observed: build and route smoke pass with
  `ChatTranscriptShell`.
- Post-launch learning needed: no

## Deliverable For This Stage

Release-ready component extraction with validation and docs/context sync.

## Constraints
- do not move `visibleTranscriptItems.map(...)`
- do not move message row refs
- do not move delivery-state calculation, timestamp formatting, or markdown rendering
- do not move route data helpers

## Implementation Plan
1. Add `ChatTranscriptShell` as a forward-ref component in
   `web/src/components/chat.tsx`.
2. Replace the inline thread-column/transcript container in `web/src/App.tsx`.
3. Pass loading fallback, transcript rows, and composer as explicit nodes.
4. Update frontend docs and context.
5. Run build, route smoke, and diff validation.

## Acceptance Criteria
- Thread-column and transcript-container presentation render from
  `ChatTranscriptShell`.
- Transcript container ref remains owned by `App()` through `forwardRef`.
- Message mapping and behavior-sensitive transcript calculations remain in
  `App()`.
- Validation passes.

## Definition of Done
- [x] Component extraction completed.
- [x] Behavior ownership preserved in `App()`.
- [x] Docs and context updated.
- [x] Relevant validation completed.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- Manual checks:
  - confirmed `ChatTranscriptShell` receives explicit loading, transcript, and
    composer nodes
- High-risk checks:
  - transcript mapping, message refs, delivery labels, timestamp formatting,
    and markdown rendering remain in `App()`
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
  - PRJ-1016 queued for chat data-helper extraction audit

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

- Task summary: extracted chat transcript shell presentation into
  `ChatTranscriptShell`.
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
  - chat route data-helper extraction remains deferred
- Next steps:
  - PRJ-1016 audit chat route data-helper extraction
- Decisions made:
  - `ChatTranscriptShell` forwards the transcript container ref instead of
    owning scroll behavior

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - transcript shell markup remained inline
- Gaps:
  - route data helpers still need future ownership decisions
- Inconsistencies:
  - PRJ-1015 was queued but implementation was not present
- Architecture constraints:
  - transcript behavior stays in `App()`

### 2. Select One Priority Task
- Selected task: PRJ-1015
- Priority rationale: it was the next queued implementation slice
- Why other candidates were deferred:
  - data-helper extraction is broader and should be audited separately

### 3. Plan Implementation
- Files or surfaces to modify:
  - chat component module, App usage, frontend docs, context
- Logic:
  - forward the transcript container ref and pass rows/composer as nodes
- Edge cases:
  - loading fallback must remain conditional in `App()`

### 4. Execute Implementation
- Implementation notes:
  - `ChatTranscriptShell` owns only layout classes and node placement

### 5. Verify and Test
- Validation performed:
  - build
  - route smoke
  - diff check
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - keep shell inline; rejected because PRJ-1014 selected extraction
- Technical debt introduced: no
- Scalability assessment:
  - adequate for current decomposition
- Refinements made:
  - composer is passed explicitly to avoid coupling shell to composer state

### 7. Update Documentation and Knowledge
- Docs updated:
  - frontend route/component map
  - app route cluster audit
  - v1 roadmap
- Context updated:
  - task board
  - project state
- Learning journal updated: not applicable
