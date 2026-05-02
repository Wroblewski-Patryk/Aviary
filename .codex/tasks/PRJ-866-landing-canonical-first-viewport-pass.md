# Task

## Header
- ID: PRJ-866
- Title: Landing Canonical First Viewport Pass
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-865
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 866
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
Chat, Dashboard, and Personality have received focused canonical passes. The
public Landing route has an approved reference but the current first viewport
places the hero copy too close to the viewport edge and too low, while the proof
bridge appears too late to match the approved landing rhythm.

## Goal
Improve the public Landing first viewport toward
`docs/ux/assets/aion-landing-canonical-reference-v1.png` while preserving the
existing public route, auth modal flow, copy, and landing hero asset.

## Success Signal
- User or operator problem: the public entry feels less polished than the
  authenticated canonical surfaces.
- Expected product or reliability outcome: landing reads as a premium framed
  first viewport with clear CTA and visible proof bridge.
- How success will be observed: desktop/mobile screenshots and no overflow.
- Post-launch learning needed: no

## Deliverable For This Stage
Implement a small CSS-only first-viewport framing pass for the public Landing
route and verify it with build plus screenshots.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new public route structures
- do not replace image-based landing art with gradients
- preserve auth modal behavior and current localized copy

## Scope
- `web/src/index.css`
- `.codex/tasks/PRJ-866-landing-canonical-first-viewport-pass.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Move hero copy inward from the viewport edge and higher in the first viewport.
2. Tighten the proof bridge vertical overlap so the next proof layer is visible
   earlier.
3. Keep the scenic landing art and highlight cards intact.
4. Capture desktop and mobile screenshots against the canonical landing
   reference.
5. Run build and whitespace validation.

## Acceptance Criteria
- Landing hero copy no longer hugs the left viewport edge.
- Landing CTA and micro-proof row remain visible and readable on desktop.
- Feature/proof bridge begins earlier in the first desktop viewport.
- No horizontal overflow on desktop or mobile.
- Auth modal route behavior remains unchanged.

## Definition of Done
- [x] Web build passes.
- [x] `git diff --check` passes.
- [x] Desktop and mobile landing screenshots are captured.
- [x] Canonical landing reference and latest implementation are inspected with
      `view_image`.

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
- Manual checks: `git diff --check -- web/src/index.css .codex/tasks/PRJ-866-landing-canonical-first-viewport-pass.md` passed with line-ending warnings only.
- Screenshots/logs:
  - `.codex/artifacts/prj866-landing-canonical-pass/root-before-1568x1003.png`
  - `.codex/artifacts/prj866-landing-canonical-pass/login-before-1568x1003.png`
  - `.codex/artifacts/prj866-landing-canonical-pass/desktop-1568x1003-v3.png`
  - `.codex/artifacts/prj866-landing-canonical-pass/mobile-390x844-v3.png`
  - `.codex/artifacts/prj866-landing-canonical-pass/auth-modal-390x844-v3.png`
- High-risk checks: no runtime/data-contract changes in scope
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence
- Architecture source reviewed: `docs/ux/canonical-web-screen-reference-set.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-landing-canonical-reference-v1.png`
- Canonical visual target: Public Landing canonical first viewport
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: public shell and landing hero asset
- New shared pattern introduced: no
- Design-memory entry reused: canonical route translation rules
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: preserve existing landing hero art
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: the implementation intentionally keeps the approved
  no-browser-frame landing direction from the reference set notes and preserves
  localized copy rather than forcing the English reference text.
- State checks: public success; auth modal smoke
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop | mobile
- Input-mode checks: pointer
- Accessibility checks: no new interactive controls
- Parity evidence:
  - reference inspected:
    `docs/ux/assets/aion-landing-canonical-reference-v1.png`
  - implementation inspected:
    `.codex/artifacts/prj866-landing-canonical-pass/desktop-1568x1003-v3.png`
  - mobile inspected:
    `.codex/artifacts/prj866-landing-canonical-pass/mobile-390x844-v3.png`

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note: revert landing CSS changes
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
The working tree already has local commits ahead of origin and untracked
artifacts from earlier tasks. This task keeps the Landing change scoped and does
not stage or push unrelated work.

## Production-Grade Required Contract

Every task must include Goal, Scope, Implementation Plan, Acceptance Criteria,
Definition of Done, and Result Report before closure.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: first-time public landing visitor
- Existing workaround or pain: hero copy and proof rhythm do not match the
  approved landing reference closely enough.
- Smallest useful slice: CSS-only first-viewport framing pass
- Success metric or signal: screenshot parity and no overflow
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: view public landing and open auth modal
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: Playwright landing screenshot
- Rollback or disable path: revert frontend CSS changes

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: auth modal mobile screenshot captured.

## AI Testing Evidence

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: public marketing copy only
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: not applicable
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
- Task summary: improved the public landing first viewport by moving hero copy
  inward and upward, making the CTA/proof row read earlier, and adjusting the
  proof bridge overlap on desktop and mobile.
- Files changed: `web/src/index.css`,
  `.codex/tasks/PRJ-866-landing-canonical-first-viewport-pass.md`,
  `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`.
- How tested: web build, diff whitespace check, desktop/mobile landing
  screenshots, auth modal mobile smoke screenshot, canonical reference
  inspection.
- What is incomplete: no new landing asset was generated; this is a
  first-viewport framing pass over the existing canonical landing asset.
- Next steps: continue with non-frozen route polish or pause to sort local
  commits before pushing UI passes.
- Decisions made: preserved localized landing copy and no-browser-frame public
  shell direction.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: landing hero copy starts too close to the viewport edge and too low;
  proof bridge appears late.
- Gaps: first viewport does not frame CTA and proof layers as clearly as the
  canonical landing reference.
- Inconsistencies: public landing is less tightly framed than the recently
  improved canonical authenticated surfaces.
- Architecture constraints: no route or auth-flow changes.

### 2. Select One Priority Task
- Selected task: Landing canonical first-viewport pass.
- Priority rationale: Landing is the remaining frozen canonical surface after
  Chat, Dashboard, and Personality.
- Why other candidates were deferred: Tools and Settings are not frozen in the
  canonical set.

### 3. Plan Implementation
- Files or surfaces to modify: Landing CSS only.
- Logic: no runtime logic changes.
- Edge cases: desktop framing, mobile stacking, auth modal behavior.

### 4. Execute Implementation
- Implementation notes: adjusted landing overlay padding/alignment, hero copy
  width/type rhythm, feature bridge width/negative overlap, mobile bridge
  overlap, and proof/trust band spacing.

### 5. Verify and Test
- Validation performed: web build, diff whitespace check, desktop/mobile
  screenshots, auth modal smoke screenshot.
- Result: passed.

### 6. Self-Review
- Simpler option considered: only adding left padding to hero copy; rejected
  because the hero still read too low against the canonical reference.
- Technical debt introduced: none known; CSS-only route framing change.
- Refinements made: mobile bridge overlap was reduced after screenshot review
  to avoid covering the final hero note.

### 7. Update Documentation and Knowledge
- Docs updated: task evidence only; no new canonical pattern introduced.
- Context updated: `.codex/context/TASK_BOARD.md` and
  `.codex/context/PROJECT_STATE.md`.
- Learning journal updated: not needed; no recurring pitfall confirmed.
