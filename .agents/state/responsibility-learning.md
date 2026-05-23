# Responsibility Learning

Last updated: 2026-05-23

Use this ledger when coordinator/subagent work exposes a missing lane, unclear
owner, bad split, missing evidence, or missing context. Gaps here must change
the next similar mission brief, lane registry, docs, or task plan.

| ID | Date | Mission/task | Gap type | Missing or unclear responsibility | Evidence/source | Next briefing change | Stored follow-up | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RLG-001 | 2026-05-22 | PRJ-1230 | missing_evidence | The validation lane assumed route-smoke fallback could prove authenticated SPA routes, but the non-Playwright fallback only dumped initial DOM and could miss async/authenticated route markers. | `web/scripts/route-smoke.mjs`; PRJ-1230 web gate first failed before CDP fallback hardening. | Future web validation briefs must assign explicit ownership for both Playwright and fallback browser harnesses, including auth state and post-navigation marker waits. | `web/scripts/route-smoke.mjs`; `.codex/tasks/PRJ-1230-v1-selected-scope-final-readiness-refresh.md` | closed |
| RLG-002 | 2026-05-23 | PRJ-1237 | missing_evidence | The architecture/data read-only lane timed out during a planning mission, so the coordinator could not integrate an independent route-data report before closure. | Subagent James wait timed out and was closed; PRJ-1237 stayed limited to known app API contracts and current route/client data sources. | Future broad UI simplification briefs should ask architecture/data agents for a smaller first deliverable: route-to-API table only, then optional risk notes, so a timeout does not block critical planning evidence. | `.codex/tasks/PRJ-1237-canonical-ui-layout-index.md`; `docs/ux/canonical-ui-layout-index.md` | open |
| RLG-003 | 2026-05-23 | PRJ-1240 | missing_context | The user requested agent coordination and provided a read-only implementation-lane brief, but the current runtime exposed no spawn-agent tool after discovery. | `tool_search` for multi-agent/spawn-agent returned no tools; coordinator ran the lane model serially and recorded the limitation. | Future continuation briefs should explicitly say when subagent runtime is unavailable and proceed with serial lanes rather than implying hidden delegation. | `.codex/tasks/PRJ-1240-flagship-coherence-pass.md` | open |

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
