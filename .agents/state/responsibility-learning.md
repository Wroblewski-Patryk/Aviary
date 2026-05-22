# Responsibility Learning

Last updated: 2026-05-22

Use this ledger when coordinator/subagent work exposes a missing lane, unclear
owner, bad split, missing evidence, or missing context. Gaps here must change
the next similar mission brief, lane registry, docs, or task plan.

| ID | Date | Mission/task | Gap type | Missing or unclear responsibility | Evidence/source | Next briefing change | Stored follow-up | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RLG-001 | 2026-05-22 | PRJ-1230 | missing_evidence | The validation lane assumed route-smoke fallback could prove authenticated SPA routes, but the non-Playwright fallback only dumped initial DOM and could miss async/authenticated route markers. | `web/scripts/route-smoke.mjs`; PRJ-1230 web gate first failed before CDP fallback hardening. | Future web validation briefs must assign explicit ownership for both Playwright and fallback browser harnesses, including auth state and post-navigation marker waits. | `web/scripts/route-smoke.mjs`; `.codex/tasks/PRJ-1230-v1-selected-scope-final-readiness-refresh.md` | closed |

## Gap Types

- `missing_lane`: a needed responsibility was not assigned to any agent.
- `unclear_owner`: multiple lanes assumed someone else owned the work.
- `bad_split`: delegated lanes overlapped or could not be integrated cleanly.
- `missing_evidence`: a lane delivered output without proof needed for acceptance.
- `missing_context`: a lane lacked source-of-truth context needed to act.

## Closure Rule

Close a row only after the next mission brief, task template, lane registry,
source-of-truth doc, or state file has been updated so the same gap is less
likely to repeat.
