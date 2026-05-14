# Task

## Header
- ID: PRJ-1214
- Title: Personality embodied map polish
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1213
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: not applicable
- Quality Scenario Rows: QA-UX-001
- Risk Rows: RISK-UI-001
- Iteration: 1214
- Operation Mode: BUILDER
- Mission ID: MISSION-WEB-PERSONALITY-1214
- Mission Status: DONE

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed through current continuation context.
- [x] `.agents/core/mission-control.md` was reviewed through the startup protocol.
- [x] Missing or template-like state tables were bootstrapped from repository sources, or confirmed not needed.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified or marked not applicable.
- [x] The task or mission improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: make the Personality embodied map and timeline feel more deliberate across desktop, tablet, and mobile.
- Release objective advanced: web-first responsive product shell quality.
- Included slices: Personality hero callout readability, timeline context hierarchy, responsive audit, screenshot review, state updates.
- Explicit exclusions: backend/API changes, personality payload changes, new image generation, route contract changes, production deployment.
- Checkpoint cadence: after implementation, after validation, before handoff.
- Stop conditions: build fails, route audit fails, mobile document overflow appears, or callouts obscure the figure more than before.
- Handoff expectation: Personality route polish is verified or exact blockers are recorded.

## Context
Personality already uses the canonical embodied figure and route-local layout. The remaining visible gap is polish: the mobile timeline loses its heading, numeric callout values use display typography that can read ambiguously, and the hero/timeline transition can feel less intentional than Dashboard/Tools/Settings.

## Goal
Refine the Personality embodied map and timeline so the route reads as a premium, coherent map of identity, planning, memory, and expression across all breakpoints.

## Success Signal
- User or operator problem: Personality should feel like a designed cognition map, not a decorative figure followed by raw rows.
- Expected product or reliability outcome: the route remains responsive and verified while improving hierarchy and repeated-use readability.
- How success will be observed: build and audits pass, refreshed Personality screenshots show clearer callout numerals and a visible mobile timeline context.
- Post-launch learning needed: yes

## Deliverable For This Stage
Implemented Personality embodied map polish with validation evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- keep repository artifacts in English

## Scope
- `web/src/index.css`
- source-of-truth state/docs updates after validation

## Implementation Plan
1. Improve Personality callout title readability where values contain counts.
2. Keep the mobile timeline heading visible in compact form instead of hiding context completely.
3. Tune timeline/card spacing so mobile remains readable without growing noisy.
4. Run `npm run build`, `npm run audit:ui-responsive`, and `npm run audit:ui-navigation`.
5. Review refreshed Personality screenshots.
6. Update source-of-truth state files.

## Acceptance Criteria
- Personality mobile screenshot shows a clear timeline context heading before the rows.
- Count-heavy callout titles read as UI values rather than ambiguous display text.
- Desktop/tablet/mobile Personality screenshots remain visually calm and non-overlapping.
- `npm run build` passes.
- `npm run audit:ui-responsive` passes.
- `npm run audit:ui-navigation` passes.
- Cleanup confirms no validation server/headless browser leftovers.

## Definition of Done
- [x] Implementation is merged into the local workspace.
- [x] `npm run build` passes for `web`.
- [x] `npm run audit:ui-responsive` passes for `web`.
- [x] `npm run audit:ui-navigation` passes for `web`.
- [x] Refreshed Personality screenshots are reviewed.
- [x] Source-of-truth state files are updated.

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

## Result Report

- Task summary: Personality count-heavy hero callouts now use clearer UI
  typography, and the mobile Mind Layers timeline keeps a compact visible
  context heading before the rows.
- Files changed: `web/src/index.css`, source-of-truth task/state/docs files.
- How tested: `npm run build`; `npm run audit:ui-responsive` with
  `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
  `failed_count=0`; `npm run audit:ui-navigation` with `status=ok`,
  `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile
  Personality screenshots reviewed; cleanup found no validation leftovers.
- What is incomplete: broader Chat v5 composition and deeper Personality
  content/state design remain future route-local slices.
- Next steps: continue Chat v5 composition polish or deeper Personality
  state coverage while preserving responsive/navigation audits.
- Decisions made: keep this as CSS-only route-local polish; no new components,
  data contracts, image assets, or runtime behavior were introduced.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: mobile Personality hides the timeline heading, and count-heavy callout values can read ambiguously in display type.
- Gaps: the hero-to-timeline transition is less intentional than the current canonical quality bar.
- Inconsistencies: other polished routes now expose detail progressively or with clearer hierarchy; Personality still loses context in the compact mobile proof.
- Architecture constraints: no data, API, route contract, or runtime behavior changes.

### 1a. Bootstrap Missing Project Knowledge
- Bootstrap needed: no
- Missing or template-like files: none
- Sources scanned: next steps, task board, visual direction brief, screen quality checklist, current Personality screenshots.
- Rows created or corrected: not applicable
- Assumptions recorded: safe assumption that compact visible timeline context improves readability without changing behavior.
- Blocking unknowns: none
- Why it was safe to continue: this is a presentational route-local polish slice.

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1214 Personality embodied map polish.
- Priority rationale: Personality is a flagship route and the next named candidate after Settings/Chat polish.
- Why other candidates were deferred: broader Chat v5 composition is larger; this slice is narrower and visually high leverage.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/index.css`.
- Logic: CSS-only refinement of typography, mobile timeline heading visibility, and spacing.
- Edge cases: avoid increasing mobile first-read noise, avoid hiding figure content, preserve responsive audit invariants.

### 4. Execute Implementation
- Implementation notes: added UI-type treatment for count-heavy callout
  values, added a small timeline layer count pill, and restored the mobile
  timeline heading with a compact grid layout.

### 5. Verify and Test
- Validation performed: `npm run build`; `npm run audit:ui-responsive`;
  `npm run audit:ui-navigation`; refreshed Personality screenshots reviewed at
  desktop, tablet, and mobile breakpoints; validation cleanup checked.
- Result: PASS.

### 6. Self-Review
- Simpler option considered: leaving the mobile heading hidden, but screenshot
  review showed the timeline then read as a raw list under the illustration.
- Technical debt introduced: none known; CSS stays route-local.
- Scalability assessment: the count/value typography rule can be reused for
  future callout data in the same route.
- Refinements made: after the first screenshot review, the mobile timeline
  header was changed from flex to grid so the label no longer wrapped
  vertically.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/ux/design-memory.md`.
- Context updated: task board, project state, current focus, next steps,
  system health, module confidence ledger, and project memory index.
- Learning journal updated: not applicable.
