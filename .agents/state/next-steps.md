# Next Steps

Last updated: 2026-05-31

1. `LUC-1063` known-state and architecture baseline is done:
   - task:
     `.codex/tasks/LUC-1063-known-state-evidence-collection-and-architecture-baseline.md`
   - latest result:
     refreshed canonical known-state and architecture export evidence for Aviary preparation lane
   - proof:
     backend test files `125`; backend route decorators `19`; migration files `12`; canonical `docs/graphs` export pack present
   - delegated lanes prepared:
     Lane A docs-tree canonicalization + override curation; Lane B backend API missing-link verification; Lane C web/mobile component verification; Lane D architecture export reproducibility guard
   - next smallest useful choice:
     open child issues for Lanes A-D from `.codex/tasks/LUC-1063-known-state-evidence-collection-and-architecture-baseline.md` and route owners via 11 Innovations Director

1. `LUC-1071` source-control closure sidecar for `LUC-1063` is done:
   - task:
     `.codex/tasks/LUC-1071-source-control-closure-luc-1063.md`
   - latest result:
     local dirty state is classified as one coherent `LUC-1063` docs/state/architecture-export packet with no runtime code or secret-bearing artifacts in scope
   - proof:
     `git status --short`, `git status --branch`, and cross-file `LUC-1063` traceability grep
   - next smallest useful choice:
     source-control owner can convert this packet into one scoped commit and attach SHA evidence to the protected target lane

1. `LUC-1021` source-control closure is done:
   - task:
     `.codex/tasks/LUC-1021-source-control-closure-luc-945-976-990-994.md`
   - latest result:
     one coherent dirty packet for `LUC-945`, `LUC-976`, and child lanes `LUC-990..LUC-994` was classified and closed with a single commit
   - proof:
     focused test pack PASS (2 passed in 1.11s)
   - next smallest useful choice:
     continue from parent integration lane (`LUC-976`) or unblock assignment gate for `LUC-945`

1. LUC-945 smoke guard is done:
   - task:
     .codex/tasks/LUC-945-qa-ops-public-entry-internal-health-smoke-guard-p2.md
   - latest result:
     non-prod smoke guard now verifies /health, /internal/state/inspect, /event, /event/debug, /, and frontend catch-all path
   - proof:
     focused test pack PASS (2 passed in 1.13s)
   - next smallest useful choice:
     optionally wire this guard into a wider release/non-prod wrapper command

1. LUC-945 public-entry + internal health smoke guard is blocked:
   - task:
     .codex/tasks/LUC-945-qa-ops-public-entry-internal-health-smoke-guard-p2.md
   - latest result:
     PM created delegated QA/Test + Ops/Release implementation contract for a replayable smoke guard
   - unblock owner/action:
     11 Innovations Director must assign specialist child lanes for implementation and proof
   - next smallest useful choice:
     once assigned, run the delegated smoke commands and attach evidence in the same lane packet

## NOW

1. `LUC-976` parent preparation lane remains the active integration checkpoint:
   - owner:
     Coordinator / PM (active chat)
   - status:
     in_progress
   - task:
     `.codex/tasks/LUC-976-full-takeover-audit-and-operating-baseline.md`
   - current posture:
     child preparation lanes `LUC-990..LUC-994` are completed and ready for parent closure integration
   - proof:
     `.codex/context/TASK_BOARD.md` row: `LUC-976` is `IN_PROGRESS` with child lanes recorded as completed evidence lanes
   - next smallest useful choice:
     integrate child outputs into the `LUC-976` parent packet and close/update parent status with one evidence-backed summary

2. `LUC-1063` preparation follow-up lanes are defined and awaiting routing:
   - owner:
     11 Innovations Director (routing/assignment), Coordinator / PM (packet maintenance)
   - status:
     ready_for_routing
   - task:
     `.codex/tasks/LUC-1063-known-state-evidence-collection-and-architecture-baseline.md`
   - current posture:
     preparation-only lane map A-D is explicit (docs curation, backend/API verification, web/mobile verification, export reproducibility)
   - proof:
     `.codex/context/TASK_BOARD.md` rows for `LUC-1063` and delegated lane definitions A-D in its task packet
   - next smallest useful choice:
     create/route child issues for Lanes A-D through 11 Innovations Director with owner + proof contract per lane

3. `LUC-945` delegated preparation smoke-guard lane is blocked on assignment:
   - owner:
     11 Innovations Director (unblock owner)
   - status:
     blocked
   - task:
     `.codex/tasks/LUC-945-qa-ops-public-entry-internal-health-smoke-guard-p2.md`
   - proof:
     `.codex/context/TASK_BOARD.md` row: `LUC-945` is `BLOCKED` pending assignment
   - blocker:
     11 Innovations Director assignment decision for QA/Test + Ops/Release specialist execution
   - unblock owner/action:
     11 Innovations Director -> assign QA/Test + Ops/Release specialists and authorize delegated proof execution
   - next smallest useful choice:
     keep lane blocked with named owner/action until assignment is made; do not expand into unrelated implementation lanes

## Previous Architecture Queue

1. Select the next smallest stability or architecture-alignment slice from the
   generated project status dashboard. `PRJ-933` is done and aligned the
   architecture radar with the current v1 release boundary:
   - `docs/operations/project-status-dashboard.md`
   - `docs/operations/project-status-dashboard.json`
   Current phase is `architecture complete for selected scope with deferred
   extensions`. Selected-scope readiness is `11/11` rows (`100.0%`). There is
   no selected-scope blocker in the generated radar.

2. Keep the architecture implementation audit as the source matrix behind the
   dashboard:
   - `docs/operations/architecture-implementation-map-2026-05-10.csv`
   - `docs/operations/architecture-implementation-audit-2026-05-10.md`

## NEXT

1. Preserve the selected-scope architecture radar. Do not reopen deferred
   extension rows unless their trigger is present:
   - provider credentials and expanded organizer scope for `ARCH-CONNECTORS-001`
   - expanded proactive launch scope for `ARCH-PROACTIVE-001`
   - a newly selected release candidate for `ARCH-DEPLOY-AUTO-001`
   - explicit mobile product/release scope for `ARCH-MOBILE-001`
2. Use `docs/operations/v1-selected-scope-handoff-2026-05-11.md` as the
   concise handoff for the current achieved selected-scope posture.
2. Keep full backend pytest in the validation set after backend contract or
   action-loop changes that alter skill/tool metadata.
3. Keep the full web command pack in the validation set for route-shell,
   navigation, or authenticated-shell changes:
   `tsc -> vite build -> npm run smoke:routes`.
4. Preserve native exit codes in PowerShell command packs with
   `$exit=$LASTEXITCODE; Pop-Location; exit $exit`; `PRJ-930` proved
   `Push-Location; npm ...; Pop-Location` can mask a failed smoke.
5. For Windows sandbox `PermissionError` on pytest basetemp creation, record
   the sandboxed failure and rerun the same gate outside sandbox before
   treating it as an application regression.
6. Refresh the architecture implementation map after every meaningful
   architecture/evidence slice.
7. Refresh `docs/operations/project-status-dashboard.md` and
   `docs/operations/project-status-dashboard.json` after refreshing the map.

## LATER

1. Consider broader bounded action-loop extensions only after a concrete
   evidence-backed need appears.
2. Create a mobile implementation scope decision before counting mobile toward
   architecture completion.

## Selection Rules

- Pick one bounded mission objective for each autonomous iteration; use small
  checkpoint tasks inside that mission when useful.
- Prefer tasks that reduce blocker risk, regression risk, or unclear source of
  truth.
- Do not start new feature work when a P0/P1 regression or release blocker is
  unresolved.
- Keep this file synchronized with `.codex/context/TASK_BOARD.md` and
  `docs/planning/mvp-next-commits.md`.





