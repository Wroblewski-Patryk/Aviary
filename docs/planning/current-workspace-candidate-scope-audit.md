# Current Workspace Candidate Scope Audit

Date: 2026-05-04
Task: `PRJ-1123`
Status: READY_FOR_EXPLICIT_COMMIT_DECISION

## Purpose

This audit freezes the current workspace packaging view before any commit,
push, Coolify deploy recovery, or release smoke. It does not create a release
candidate by itself. It prevents two common release mistakes:

- deploying a SHA that does not include the intended local work
- committing generated local evidence artifacts by accident

## Current Git Posture

| Check | Result |
| --- | --- |
| Branch | `main` |
| Relation to `origin/main` | ahead by 86 commits |
| Tracked modified files | 22 |
| Tracked diff size | 5298 insertions, 847 deletions |
| New task records | 83 untracked `.codex/tasks/PRJ-1042..PRJ-1122` files before this audit |
| New web characterization scripts | 2 untracked source/test scripts |
| Local generated artifact roots | `.codex/tmp/`, `artifacts/` |

## Include In Candidate Commit

Include these tracked modifications:

- `.codex/context/LEARNING_JOURNAL.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/context/TASK_BOARD.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/operations/release-evidence-index.md`
- `docs/planning/current-v1-release-boundary.md`
- `docs/planning/v1-deployment-trigger-slo-evidence.md`
- `docs/planning/v1-final-go-no-go-review.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `docs/planning/v1-release-notes-and-operator-handoff.md`
- `web/package.json`
- `web/src/App.tsx`
- `web/src/components/chat.tsx`
- `web/src/components/dashboard.tsx`
- `web/src/components/personality.tsx`
- `web/src/components/public-shell.tsx`
- `web/src/components/settings.tsx`
- `web/src/components/shared.tsx`
- `web/src/components/shell.tsx`
- `web/src/components/tools.tsx`

Include these new source/test scripts:

- `web/scripts/chat-transcript-characterization.mjs`
- `web/scripts/tools-directory-characterization.mjs`

Include the new task records from the completed frontend cleanup, release truth,
deploy preflight, validation, and candidate-scope audit lane:

- `.codex/tasks/PRJ-1042-next-cleanup-after-dashboard-progress-audit.md`
- `.codex/tasks/PRJ-1043-insights-shared-shell-alignment.md`
- `.codex/tasks/PRJ-1044-next-cleanup-after-insights-shell-audit.md`
- `.codex/tasks/PRJ-1045-integrations-side-panel-alignment.md`
- `.codex/tasks/PRJ-1046-next-cleanup-after-integrations-side-panel-audit.md`
- `.codex/tasks/PRJ-1047-automations-flow-row-alignment.md`
- `.codex/tasks/PRJ-1048-next-cleanup-after-automations-flow-row-audit.md`
- `.codex/tasks/PRJ-1049-automations-health-row-alignment.md`
- `.codex/tasks/PRJ-1050-next-cleanup-after-automations-health-row-audit.md`
- `.codex/tasks/PRJ-1051-insights-guidance-row-alignment.md`
- `.codex/tasks/PRJ-1052-next-cleanup-after-insights-guidance-row-audit.md`
- `.codex/tasks/PRJ-1053-remove-unused-module-route-side-row.md`
- `.codex/tasks/PRJ-1054-next-cleanup-after-route-side-row-removal-audit.md`
- `.codex/tasks/PRJ-1055-route-note-card-list-extraction.md`
- `.codex/tasks/PRJ-1056-next-cleanup-after-route-note-card-list-audit.md`
- `.codex/tasks/PRJ-1057-route-stat-card-list-extraction.md`
- `.codex/tasks/PRJ-1058-next-cleanup-after-route-stat-card-list-audit.md`
- `.codex/tasks/PRJ-1059-personality-timeline-row-list-extraction.md`
- `.codex/tasks/PRJ-1060-next-cleanup-after-personality-timeline-row-list-audit.md`
- `.codex/tasks/PRJ-1061-remove-stale-route-stat-card-import.md`
- `.codex/tasks/PRJ-1062-next-cleanup-after-route-stat-card-import-audit.md`
- `.codex/tasks/PRJ-1063-personality-signal-row-list-extraction.md`
- `.codex/tasks/PRJ-1064-next-cleanup-after-personality-signal-row-list-audit.md`
- `.codex/tasks/PRJ-1065-dashboard-signal-column-extraction.md`
- `.codex/tasks/PRJ-1066-next-cleanup-after-dashboard-signal-column-audit.md`
- `.codex/tasks/PRJ-1067-public-trust-pill-list-extraction.md`
- `.codex/tasks/PRJ-1068-next-cleanup-after-public-trust-pill-list-audit.md`
- `.codex/tasks/PRJ-1069-public-feature-card-list-extraction.md`
- `.codex/tasks/PRJ-1070-next-cleanup-after-public-feature-card-list-audit.md`
- `.codex/tasks/PRJ-1071-public-trust-band-extraction.md`
- `.codex/tasks/PRJ-1072-next-cleanup-after-public-trust-band-audit.md`
- `.codex/tasks/PRJ-1073-dashboard-reflection-list-extraction.md`
- `.codex/tasks/PRJ-1074-next-cleanup-after-dashboard-reflection-list-audit.md`
- `.codex/tasks/PRJ-1075-dashboard-memory-bar-chart-extraction.md`
- `.codex/tasks/PRJ-1076-next-cleanup-after-dashboard-memory-bar-chart-audit.md`
- `.codex/tasks/PRJ-1077-dashboard-guidance-list-extraction.md`
- `.codex/tasks/PRJ-1078-next-cleanup-after-dashboard-guidance-list-audit.md`
- `.codex/tasks/PRJ-1079-dashboard-recent-activity-list-extraction.md`
- `.codex/tasks/PRJ-1080-next-cleanup-after-dashboard-recent-activity-list-audit.md`
- `.codex/tasks/PRJ-1081-dashboard-balance-grid-extraction.md`
- `.codex/tasks/PRJ-1082-next-cleanup-after-dashboard-balance-grid-audit.md`
- `.codex/tasks/PRJ-1083-dashboard-cognitive-flow-track-extraction.md`
- `.codex/tasks/PRJ-1084-next-cleanup-after-dashboard-cognitive-flow-track-audit.md`
- `.codex/tasks/PRJ-1085-dashboard-figure-note-list-extraction.md`
- `.codex/tasks/PRJ-1086-next-cleanup-after-dashboard-figure-note-list-audit.md`
- `.codex/tasks/PRJ-1087-personality-activity-row-list-extraction.md`
- `.codex/tasks/PRJ-1088-next-cleanup-after-personality-activity-row-list-audit.md`
- `.codex/tasks/PRJ-1089-settings-status-pill-list-extraction.md`
- `.codex/tasks/PRJ-1090-next-cleanup-after-settings-status-pill-list-audit.md`
- `.codex/tasks/PRJ-1091-tools-summary-card-list-extraction.md`
- `.codex/tasks/PRJ-1092-next-cleanup-after-tools-summary-card-list-audit.md`
- `.codex/tasks/PRJ-1093-personality-preview-callout-list-extraction.md`
- `.codex/tasks/PRJ-1094-next-cleanup-after-personality-preview-callout-list-audit.md`
- `.codex/tasks/PRJ-1095-public-nav-link-list-extraction.md`
- `.codex/tasks/PRJ-1096-next-cleanup-after-public-nav-link-list-audit.md`
- `.codex/tasks/PRJ-1097-shell-account-fact-list-extraction.md`
- `.codex/tasks/PRJ-1098-next-cleanup-after-shell-account-fact-list-audit.md`
- `.codex/tasks/PRJ-1099-shell-nav-button-list-extraction.md`
- `.codex/tasks/PRJ-1100-next-cleanup-after-shell-nav-button-list-audit.md`
- `.codex/tasks/PRJ-1101-shell-route-switcher-extraction.md`
- `.codex/tasks/PRJ-1102-next-cleanup-after-shell-route-switcher-audit.md`
- `.codex/tasks/PRJ-1103-settings-select-option-list-extraction.md`
- `.codex/tasks/PRJ-1104-next-cleanup-after-settings-select-option-list-audit.md`
- `.codex/tasks/PRJ-1105-tools-directory-behavior-characterization.md`
- `.codex/tasks/PRJ-1106-tools-directory-group-item-presentation-extraction.md`
- `.codex/tasks/PRJ-1107-remaining-frontend-map-boundary-audit.md`
- `.codex/tasks/PRJ-1108-public-hero-card-data-shape-alignment.md`
- `.codex/tasks/PRJ-1109-chat-transcript-render-map-readiness-audit.md`
- `.codex/tasks/PRJ-1110-chat-transcript-render-characterization.md`
- `.codex/tasks/PRJ-1111-chat-transcript-message-list-extraction.md`
- `.codex/tasks/PRJ-1112-mobile-tabbar-ref-extraction-readiness-audit.md`
- `.codex/tasks/PRJ-1113-shell-mobile-tabbar-extraction.md`
- `.codex/tasks/PRJ-1114-frontend-data-projection-closure-audit.md`
- `.codex/tasks/PRJ-1115-local-release-readiness-evidence-refresh.md`
- `.codex/tasks/PRJ-1116-release-review-stale-snapshot-clarification.md`
- `.codex/tasks/PRJ-1117-current-v1-release-boundary-refresh.md`
- `.codex/tasks/PRJ-1118-release-notes-current-handoff-refresh.md`
- `.codex/tasks/PRJ-1119-v1-release-execution-plan-current-status-refresh.md`
- `.codex/tasks/PRJ-1120-final-go-no-go-historical-blocker-wording.md`
- `.codex/tasks/PRJ-1121-coolify-deploy-parity-operator-preflight.md`
- `.codex/tasks/PRJ-1122-current-workspace-candidate-validation-refresh.md`
- `.codex/tasks/PRJ-1123-current-workspace-candidate-scope-audit.md`

## Exclude Unless Separately Approved

Do not include these generated/local evidence roots by default:

- `.codex/tmp/`
- `artifacts/`

Observed examples include local smoke databases, backend logs, generated audit
JSON/Markdown, release go/no-go JSON outputs, AI red-team reports, and behavior
validation artifacts. They can be referenced by committed task/docs summaries,
but should not be swept into the candidate commit without an explicit artifact
retention decision.

## Validation Evidence

PRJ-1122 is the current local validation baseline:

- backend pytest:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location`
  -> `1045 passed`
- web build:
  `Push-Location .\web; npm run build; Pop-Location` -> passed
- tools directory characterization:
  `Push-Location .\web; npm run test:tools-directory; Pop-Location` ->
  `status=ok`
- chat transcript characterization:
  `Push-Location .\web; npm run test:chat-transcript; Pop-Location` ->
  `status=ok`
- route smoke:
  `Push-Location .\web; npm run smoke:routes; Pop-Location` ->
  `status=ok`, `route_count=14`
- diff hygiene:
  `git diff --check` -> passed

## Commit Readiness

This workspace is ready for an explicit commit decision, not for deployment
yet.

Before PRJ-952 can move:

1. stage only the included scope above
2. keep `.codex/tmp/` and `artifacts/` excluded unless separately approved
3. commit the selected scope
4. push the candidate SHA
5. recover Coolify source automation or run the approved operator fallback for
   the selected SHA
6. run production release smoke with deploy parity

The resulting pushed SHA, not the current dirty workspace, becomes the deploy
candidate.
