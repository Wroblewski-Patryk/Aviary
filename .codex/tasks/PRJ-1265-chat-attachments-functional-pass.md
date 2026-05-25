# Task

## Header
- ID: PRJ-1265
- Title: Chat attachments functional pass
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1264
- Priority: P1
- Iteration: 1265
- Operation Mode: TESTER
- Mission ID: PRJ-1265-chat-attachments-functional-pass
- Mission Status: DONE

## Context
User reported that file attachment in chat did not work and requested full UX/UI continuation instead of cosmetic-only iterations.

## Goal
Deliver a functional attachment flow in web chat while preserving current backend contract (`/app/chat/message` text payload).

## Scope
- `web/src/App.tsx`
- `web/src/components/chat.tsx`
- `web/src/components/app-icons.tsx`
- `web/src/index.css`

## Definition of Done
- [x] User can add files in chat composer.
- [x] User sees attached files list and can remove each file before send.
- [x] Attachment content is included in outbound message text payload.
- [x] Build and route smoke remain green.

## Result
Implemented working attachment UX in chat composer: file picker (multi), attachment chips with remove action, bounded attachment count/size, and content serialization into message text before submit so the current backend contract can process the context without API changes.

## Validation Evidence
- `npm run build` in `web/` -> PASS
- `npm run test:chat-transcript` in `web/` -> PASS
- `npm run smoke:routes` in `web/` -> PASS (`route_count=14`, `status=ok`)
