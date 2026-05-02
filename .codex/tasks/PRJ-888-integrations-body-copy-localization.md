# Task

## Header
- ID: PRJ-888
- Title: Integrations Body Copy Localization
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-887
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 888
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The Polish shell labels are now localized, but PRJ-887 found that the
Integrations module still contains English hardcoded body copy in cards and
section headings.

## Goal
Move static Integrations route body copy into the existing `UI_COPY.integrations`
structure so Polish localized views no longer show English shell-owned text.

## Scope
- Route:
  - `/integrations`
- Files:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-888-integrations-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - translating provider-supplied `status_reason` values from
    `/app/tools/overview`
  - other module routes
  - backend, DB, auth, provider, scheduler, or action-layer changes

## Success Signal
- User or operator problem: localized Polish Integrations view still contains
  English route-owned body copy.
- Expected product or reliability outcome: static Integrations route copy is
  owned by the existing localization structure.
- How success will be observed: build passes and a Polish Integrations smoke no
  longer finds the targeted English hardcoded phrases.
- Post-launch learning needed: no

## Deliverable For This Stage
One focused localization refactor for static Integrations route copy.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Extend `UI_COPY.integrations` for static route body strings.
2. Replace hardcoded Integrations route copy with `copy.integrations` fields.
3. Run frontend build.
4. Run a Polish Integrations smoke for targeted English phrase absence.
5. Update task board and project state.

## Acceptance Criteria
- Static Integrations stat details, headings, boundary cards, and readiness
  details use `copy.integrations`.
- English behavior remains unchanged.
- Polish smoke confirms targeted hardcoded English phrases are absent.
- `npm run build` passes.

## Definition of Done
- [x] Integrations static body copy uses `UI_COPY.integrations`.
- [x] Build passes.
- [x] Polish Integrations smoke passes.
- [x] Task board and project state are updated.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new localization system
- translating backend/provider-supplied dynamic strings in the frontend
- backend, DB, provider, scheduler, or action-layer changes

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `git diff --check -- web/src/App.tsx .codex/tasks/PRJ-888-integrations-body-copy-localization.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - Chrome CDP Polish Integrations copy smoke
  - result: passed
  - checked route-owned Polish strings, targeted English phrase absence, route
    path, and horizontal overflow
- Screenshots/logs:
  - `.codex/artifacts/prj888-integrations-body-copy-localization/pl-integrations-copy-smoke-v3.json`
  - `.codex/artifacts/prj888-integrations-body-copy-localization/pl-integrations-mobile-v3.png`
- High-risk checks:
  - no runtime, API, provider, scheduler, or data contract changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
Provider `status_reason` values remain data-owned and may still be English when
the backend returns English strings.

## Result Report
- Extended the existing `UI_COPY.integrations` structure for static route body
  text in English, Polish, and German.
- Replaced hardcoded Integrations stat details, provider-map labels, boundary
  cards, and readiness detail labels with localized copy.
- Kept provider-supplied `status_reason` strings out of scope and data-owned.
