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
