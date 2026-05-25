# PRJ-1332 - Shell Health Backend Map

## Header
- ID: PRJ-1332
- Title: Shell health backend map
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Coordinator + Frontend Builder
- Priority: P1
- Requirement Rows: REQ-UX-1332
- Module Confidence Rows: AVIARY-WEB-SHELL-HEALTH-001, AVIARY-WEB-RESP-001
- Mission ID: PRJ-1331-backend-capability-to-final-personality-ui
- Mission Status: CHECKPOINTED

## Context
The active mission is mapping backend capabilities into a final-feeling Aviary UI. After the first Personality slice, the next smallest truthful slice was the static desktop shell `System Health` card. Backend/API and frontend audit lanes confirmed that `/health` already exists, is already consumed by Automations, and can safely power a high-level shell health summary if the UI maps only selected fields.

## Goal
Replace the static shell health card with a localized, backend-backed summary from `/health` without exposing raw ops/debug payloads or changing backend contracts.

## Scope
- `web/src/lib/api.ts`
- `web/src/App.tsx`
- `web/src/index.css`
- Desktop shell health card and shared health fetch behavior only

## Implementation Plan
1. Use read-only lane output to identify safe `/health` fields.
2. Extend `AppHealthResponse` with only selected shell-safe fields.
3. Fetch health for every authenticated shell route instead of only Dashboard and Automations.
4. Add localized shell health copy for loading, ready, attention, and unavailable states.
5. Derive a compact shell health model from `status`, `release_readiness.ready`, scheduler/reflection health, attention pending count, violation count, and runtime revision.
6. Replace static `System Health / Optimal` UI with the derived model.
7. Add scoped CSS state tones and run web build plus route-smoke screenshot proof.

## Acceptance Criteria
- Shell health is no longer hardcoded `Optimal`.
- The shell health card uses `/health` through the existing API client and state.
- UI does not dump raw `runtime_policy`, detailed scheduler/debug payloads, or connector env requirements.
- Dashboard, Personality, and Automations screenshots pass desktop/tablet/mobile route-smoke audit.
- Account proof remains green.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
  - `Push-Location .\web; node scripts/route-smoke.mjs --screenshots ..\.codex\artifacts\prj1332-shell-health-backend-map\screenshots --report ..\.codex\artifacts\prj1332-shell-health-backend-map\report.json --screenshot-routes /dashboard,/personality,/automations --viewports desktop,tablet,mobile --account-proof; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Screenshots/logs:
  - `.codex/artifacts/prj1332-shell-health-backend-map/report.json`
  - `.codex/artifacts/prj1332-shell-health-backend-map/screenshots/desktop-dashboard.png`
  - `.codex/artifacts/prj1332-shell-health-backend-map/screenshots/desktop-personality.png`
  - `.codex/artifacts/prj1332-shell-health-backend-map/screenshots/mobile-dashboard.png`
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/canonical-ui-layout-index.md`, `docs/ux/visual-direction-brief.md`, `docs/ux/design-memory.md`
- Canonical visual target: calm authenticated shell rail with truthful system posture.
- Fidelity target: structurally_faithful
- Existing shared pattern reused: existing API health fetch state, existing sidebar health card
- New shared pattern introduced: no
- State checks: loading, ready, attention, unavailable
- Responsive checks: desktop, tablet, mobile for Dashboard, Personality, Automations
- Accessibility checks: route-smoke found `unnamedInteractiveCount=0`
- Parity evidence: 9-screenshot route-smoke gate passed.

## Architecture Evidence
- Architecture source reviewed: `/health` response builder, backend route contract, backend health tests, frontend API client, subagent Backend/API inventory.
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates: none; this is UI mapping over an existing endpoint.

## Result Report
- Task summary: Desktop shell health now uses backend health state instead of static decorative copy.
- Files changed:
  - `web/src/lib/api.ts`
  - `web/src/App.tsx`
  - `web/src/index.css`
- How tested: web build, focused route-smoke screenshot/account proof, visual screenshot review.
- What is incomplete: full backend capability coverage remains a multi-slice mission; chat empty/demo state, Goals/Insights derivation, Tools/Integrations deep capability views, and connector confirmation history remain future slices.
- Next steps: continue with chat transcript truth/empty-state cleanup or deepen Tools/Integrations capability mapping.

## Autonomous Loop Evidence
### 1. Analyze Current State
- The shell health card was static while `/health` already exposed release, scheduler, reflection, deployment, and attention posture.

### 2. Select One Priority Mission Objective
- Selected task: replace static shell health with a safe backend-backed summary.

### 3. Plan Implementation
- Use the existing `api.getHealth()` path and avoid raw ops/debug exposure.

### 4. Execute Implementation
- Extended health typing, broadened authenticated health fetch, added localized copy and derived shell health state, and updated sidebar markup/styles.

### 5. Verify and Test
- Build PASS.
- Dashboard, Personality, and Automations desktop/tablet/mobile screenshot gate PASS.

### 6. Self-Review
- No backend changes.
- No raw `runtime_policy` dump.
- No fake status data added.

### 7. Update Documentation and Knowledge
- Task artifact created.
- Active mission, task board, project state, delivery map, requirement matrix, module confidence, quality/risk/system health, and next steps updated in the same cycle.
