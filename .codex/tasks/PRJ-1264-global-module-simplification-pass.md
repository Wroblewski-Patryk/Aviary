# Task

## Header
- ID: PRJ-1264
- Title: Global module simplification pass
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1263
- Priority: P1
- Iteration: 1264
- Operation Mode: BUILDER
- Mission ID: PRJ-1264-global-module-simplification-pass
- Mission Status: DONE

## Context
User requested one full pass that also covers non-flagship views and removes UI clutter instead of incremental cosmetic edits.

## Goal
Simplify all module routes with calmer, lighter surfaces while preserving backend-driven data visibility and route behavior.

## Scope
- `web/src/index.css`
- routes: `/chat`, `/memory`, `/reflections`, `/plans`, `/goals`, `/insights`, `/automations`, `/integrations`, `/settings`, `/tools`
- shared module visual language only (no API or route-contract changes)

## Definition of Done
- [x] `npm run build` passes.
- [x] `npm run smoke:routes` passes for all routes.
- [x] `npm run test:chat-transcript` passes.
- [x] Chat send icon direction and composer control cleanup remain intact.

## Result
Applied one global simplification layer across non-flagship modules: reduced heavy card styling, lowered border radius and shadow depth, quieted chip treatment, and unified panel surfaces into a calmer layout system. Chat cognitive belt/item refactor and mobile transcript constraints remain active from the same delivery cycle.

## Validation Evidence
- `npm run build` in `web/` -> PASS
- `npm run smoke:routes` in `web/` -> PASS (`route_count=14`, `status=ok`)
- `npm run test:chat-transcript` in `web/` -> PASS (`status=ok`)
