# Task

## Header
- ID: PRJ-901
- Title: Real Recent Activity Surface
- Task Type: feature
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-900
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 901
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-897 localized the shared recent-activity fallback rows, but Dashboard,
Memory, Reflections, and Personality still render static demo activity even
when the backend has persisted episodic memory for the authenticated user.
The existing `/app/personality/overview` contract already gathers
authenticated user state and is the shared frontend data source for these
canonical surfaces.

## Goal
Expose a small, sanitized recent activity list from existing persisted memory
through `/app/personality/overview`, then have the web shell prefer that real
activity over localized fallback rows.

## Scope
- `backend/app/api/routes.py`
- `backend/tests/test_api_routes.py`
- `web/src/App.tsx`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: canonical surfaces stop showing demo-only recent
  activity when real persisted memory exists.
- Expected product or reliability outcome: UI activity rows reflect the
  authenticated user's real memory records without exposing raw payload data.
- How success will be observed: API test verifies sanitized overview activity;
  web build verifies the frontend projection compiles.
- Post-launch learning needed: no

## Deliverable For This Stage
Implemented and verified the real recent-activity vertical slice.

## Constraints
- Reuse the existing memory repository and `/app/personality/overview` route.
- Do not create a new activity service, route family, or persistence model.
- Do not expose raw memory payloads in the overview activity list.
- Preserve localized static rows as a fallback when no real records exist.

## Implementation Plan
1. Add a private API projection helper that sanitizes recent memory records to
   stable `event_id`, `title`, `timestamp`, `source`, and `importance` fields.
2. Include `recent_activity` in the existing authenticated overview snapshot.
3. Extend the API route test to seed user-owned memory and assert the overview
   returns real, sanitized activity.
4. Add a defensive frontend projection helper that reads `overview.recent_activity`
   and falls back to `UI_COPY.common.recentActivity`.
5. Update context docs after validation.

## Acceptance Criteria
- `/app/personality/overview` includes user-scoped `recent_activity` rows when
  memory exists.
- Recent activity rows do not include raw `payload`.
- Dashboard, Memory, Reflections, and Personality consume the same derived
  activity list.
- Empty or malformed backend activity safely falls back to localized copy rows.
- Relevant backend and frontend validations pass.

## Definition of Done
- [x] Backend overview activity projection implemented.
- [x] Frontend recent activity uses real overview data first.
- [x] API route test covers authenticated real activity.
- [x] Web build passes.
- [x] Task board and project state updated.

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
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k personality_overview; Pop-Location`
  - result: passed, `1 passed, 118 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location`
  - result: passed, `1019 passed`
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
- Manual checks: code review confirmed shared activity consumers now use the same derived list.
- Screenshots/logs: not required for this backend-backed data slice
- High-risk checks: API test asserts user scoping and payload exclusion
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence
- Architecture source reviewed: AGENTS.md, autonomous engineering loop,
  existing app API route and memory repository contracts.
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: not required

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: current canonical shared app shell and recent
  activity panels.
- Canonical visual target: preserve current canonical surfaces while replacing
  demo data with real persisted activity.
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: shared recent activity rows
- New shared pattern introduced: no
- Design-memory entry reused: shared canonical shell/activity treatment
- Design-memory update required: no
- Visual gap audit completed: not applicable
- State checks: success and fallback
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: unchanged layout
- Input-mode checks: not applicable
- Accessibility checks: semantic row rendering unchanged
- Parity evidence: existing panel structure preserved

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not required
- Rollback note: remove the `recent_activity` projection and frontend helper
  usage to restore localized fallback-only rows.
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
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
- Assumption: persisted episodic memory summaries are already user-owned and
  safe to summarize as activity titles; raw payloads stay out of the overview
  activity list.

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: authenticated AION web user
- Existing workaround or pain: static rows make canonical surfaces feel less
  useful after localization polish.
- Smallest useful slice: reuse overview data source for recent activity only.
- Success metric or signal: real memory summary appears in recent activity
  panels when available.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: authenticated shell overview rendering
- SLI: overview request success
- SLO: existing app API posture
- Error budget posture: not applicable
- Health/readiness check: unchanged
- Logs, dashboard, or alert route: unchanged
- Smoke command or manual smoke: backend route test and web build
- Rollback or disable path: remove overview activity field consumption
- `INTEGRATION_CHECKLIST.md` reviewed: yes
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: unchanged
- Error state verified: unchanged
- Refresh/restart behavior verified: unchanged
- Regression check performed: backend route test and web build

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: yes
- Data classification: authenticated user memory summary metadata
- Trust boundaries: API exposes only current authenticated user's memory rows
- Permission or ownership checks: `_require_app_auth` plus user-scoped memory
  repository query
- Abuse cases: raw payload leakage from memory records
- Secret handling: none
- Security tests or scans: payload exclusion assertion passed in API route test
- Fail-closed behavior: unauthenticated overview remains protected
- Residual risk: persisted summaries may contain user-provided content by design

## Result Report
- Task summary: `/app/personality/overview` now includes a user-scoped,
  sanitized `recent_activity` list, and shared web panels prefer that real
  activity over localized fallback rows.
- Files changed:
  - `backend/app/api/routes.py`
  - `backend/tests/test_api_routes.py`
  - `web/src/App.tsx`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k personality_overview; Pop-Location`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location`
  - `Push-Location .\web; npm run build; Pop-Location`
- What is incomplete: no runtime DB migration or new route was needed.
- Next steps: continue with the next smallest product-usability slice, likely
  replacing remaining route-local static summaries with backend-backed state
  where an approved contract exists.
- Decisions made: expose summaries and metadata only; keep raw memory payloads
  out of overview activity.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: recent activity panels consume localized fallback rows only.
- Gaps: overview does not expose sanitized recent persisted activity.
- Inconsistencies: chat history uses real memory transcript, but sibling
  surfaces do not show real recent activity.
- Architecture constraints: reuse memory repository and authenticated overview.

### 2. Select One Priority Task
- Selected task: expose and consume real recent activity.
- Priority rationale: direct product usability improvement after localization.
- Why other candidates were deferred: broader canonical visual polish is larger
  than one reversible iteration.

### 3. Plan Implementation
- Files or surfaces to modify: backend overview route/test and frontend shared
  recent activity derivation.
- Logic: sanitize existing memory rows, derive UI rows defensively, preserve
  fallback copy.
- Edge cases: missing title, missing timestamp, malformed activity arrays, raw
  payload leakage.

### 4. Execute Implementation
- Implementation notes: added `_recent_activity_snapshot`, included it in
  `_build_learned_state_snapshot`, extended the authenticated overview test,
  and added `recentActivityRows` in the web shell.

### 5. Verify and Test
- Validation performed: targeted backend route test, full backend test suite,
  and production web build.
- Result: passed.

### 6. Self-Review
- Simpler option considered: frontend-only fallback changes; rejected because
  it would not make data real.
- Technical debt introduced: no
- Scalability assessment: sufficient for the declared overview/list slice; a
  richer activity timeline can later get its own approved contract if needed.
- Refinements made: projection excludes raw payload and clamps importance.

### 7. Update Documentation and Knowledge
- Docs updated: task board and project state.
- Context updated: yes
- Learning journal updated: not applicable
