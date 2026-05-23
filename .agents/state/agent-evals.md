# Agent Process Evals

Last updated: 2026-05-23

Use this ledger to improve how Codex agents work together. It evaluates the
process, not only the code.

| ID | Date | Mission/task | Coordinator score | Lane split score | Brief clarity score | Proof score | Memory score | Main failure mode | Improvement for next mission | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AEV-001 | 2026-05-22 | PRJ-1230 | 4 | 4 | 4 | 5 | 4 | The first web validation attempt exposed that the fallback browser harness proof was weaker than the Playwright path. | Keep coordinator-owned parent validation local, but require every delegated QA gate to name fallback proof assumptions and auth/async marker coverage. | closed |
| AEV-002 | 2026-05-23 | PRJ-1237 | 4 | 3 | 4 | 3 | 4 | The UX/reference lane returned useful taxonomy, but the architecture/data lane was too broad and timed out before producing an independent route-to-API report. | For future planning missions, split read-only lanes into smaller first deliverables with a hard minimum output, especially route-to-API tables before broader commentary. | open |
| AEV-003 | 2026-05-23 | PRJ-1238 | 5 | 5 | 5 | 4 | 4 | Browser/IAB bootstrap failed after the shell patch, so rendered proof relied on the existing Playwright route-smoke screenshot gate instead of in-app Browser inspection. | Keep Browser as the first rendered-inspection attempt, but record bootstrap failures and proceed with route-smoke screenshots when the Browser runtime is unavailable. | open |
| AEV-004 | 2026-05-23 | PRJ-1239 | 5 | 5 | 5 | 4 | 5 | The first validation attempt ran build and route-smoke in parallel, causing route-smoke to hit a transient missing `dist/index.html` while Vite rebuilt output. | Do not parallelize destructive/build output producers with consumers of the same `dist` directory; run build before route-smoke screenshot gates. | open |
| AEV-005 | 2026-05-23 | PRJ-1240 | 5 | 3 | 4 | 5 | 5 | The user asked for agent coordination, but this runtime did not expose a spawn-agent tool; the coordinator had to run the lane model serially. | Discover multi-agent tooling before promising delegation; if unavailable, record the serial-lane fallback in the task and responsibility-learning ledger. | open |
| AEV-006 | 2026-05-23 | PRJ-1243 | 5 | 4 | 5 | 5 | 5 | The lane input arrived as a user-supplied read-only UX parity brief rather than a separate callable subagent result, so the coordinator had to integrate it directly and keep implementation ownership local. | Keep future screenshot-fidelity briefs narrow and implementation selectors explicit; one route surface plus one validation pack worked well for this checkpoint. | open |
| AEV-007 | 2026-05-23 | PRJ-1244 | 5 | 5 | 5 | 5 | 5 | Delegated UX and QA lanes returned bounded, actionable outputs while the coordinator kept CSS implementation and final validation local. | Keep this split for future flagship UI passes: one parity lane, one QA lane, one route-local implementation slice, then screenshot proof before state updates. | open |
| AEV-008 | 2026-05-23 | PRJ-1245 | 5 | 5 | 5 | 5 | 5 | The UX lane correctly recommended not touching Dashboard, preventing a broad coherence pass from weakening the already-verified hero composition. | For future multi-surface polish, require the parity lane to identify what should remain untouched as explicitly as what should change. | open |
| AEV-009 | 2026-05-23 | PRJ-1246 | 5 | 5 | 5 | 5 | 5 | The UX and QA lanes converged on the same minimal Chat mobile checkpoint, allowing the coordinator to keep implementation narrow and validation sequential. | Keep this pattern for remaining canonical work: one screenshot mismatch, one read-only parity lane, one read-only QA lane, then coordinator-owned CSS and proof. | open |
| AEV-010 | 2026-05-23 | PRJ-1248 | 5 | 5 | 5 | 5 | 5 | The UX lane corrected the coordinator's initial Personality preference by pointing to the higher-impact mobile Dashboard flow stack, improving prioritization without broadening scope. | Let read-only parity lanes challenge the coordinator's first visual hunch, then keep the chosen checkpoint single-route and CSS-only. | open |
| AEV-011 | 2026-05-23 | PRJ-1250 | 5 | 4 | 5 | 5 | 5 | Read-only lanes gave useful but slightly different priority signals: UX identified Chat source-marker loudness while QA emphasized broader Dashboard validation posture. | When lanes disagree, record the decision basis explicitly: prefer the fresher changed surface when it has a concrete screenshot issue, then keep implementation and proof narrow. | open |
| AEV-012 | 2026-05-23 | PRJ-1251 | 5 | 5 | 5 | 5 | 5 | UX parity and coordinator screenshot review converged on Dashboard mobile signal density, while QA supplied the exact route-focused gate and known false positives. | Keep using one UX parity lane plus one QA lane for small UI polish; integrate only when both point to a bounded route-local checkpoint. | open |
| AEV-013 | 2026-05-23 | PRJ-1252 | 5 | 4 | 5 | 5 | 5 | QA correctly warned that Dashboard should remain the default if no fresher target existed, while UX supplied a concrete Personality mobile callout mismatch with selectors and screenshot rationale. | Allow QA route defaults to be overridden by a fresh screenshot-backed UX lane when the coordinator records the decision basis and keeps the implementation route-local. | open |
| AEV-014 | 2026-05-23 | PRJ-1253 | 5 | 5 | 5 | 5 | 5 | The coordinator initially selected a second Personality slice, but the UX parity lane identified a better cross-flagship balance target on Chat desktop before implementation progressed too far. | Keep delegated UX lanes early enough that they can redirect the route choice; delete stale task contracts immediately when the mission pivots. | open |
| AEV-015 | 2026-05-23 | PRJ-1254 | 5 | 4 | 5 | 5 | 5 | The UX lane returned the next Chat overlay checkpoint after the coordinator had already implemented and validated the Personality timeline rail. | When a lane returns after implementation starts, finish the already-validated narrow checkpoint if it is still valuable, but record the lane's recommendation as the next task instead of discarding it. | open |
| AEV-016 | 2026-05-23 | PRJ-1255 | 5 | 5 | 5 | 5 | 5 | UX and QA lanes converged on a narrow CSS-only overlay placement slice, and the coordinator preserved implementation locally while using screenshots to confirm desktop/tablet/mobile behavior. | Keep tiny visual slices scoped to one selector family when the canonical mismatch is placement-only; require a responsive reset check whenever desktop absolute positioning changes. | open |

## Scoring

- `0`: missing or harmful.
- `1`: present but unclear.
- `2`: usable with major gaps.
- `3`: acceptable.
- `4`: strong.
- `5`: excellent and reusable.

## Required Eval Triggers

- broad mission with subagents
- failed or partial validation
- architecture or UX direction choice
- repeated task churn
- user says work is going in circles
- coordinator discovers a missing lane, bad split, or weak proof

## Closure Rule

Close an eval row only after the next mission brief, hierarchy, lane catalog,
task template, test strategy, or project memory has been updated.
