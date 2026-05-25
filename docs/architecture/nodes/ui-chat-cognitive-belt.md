---
id: "UI-CHAT-COGNITIVE-BELT"
name: "Chat Cognitive Belt"
type: "ui_element"
status: "verified"
layer: "frontend"
module: "web"
feature: "app_chat"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "web/src/components/chat.tsx"
related_files: ["web/src/App.tsx", "web/src/index.css", "web/scripts/route-smoke.mjs"]
tags: ["aviary", "ui", "chat", "cognitive_belt", "research_mapped"]
---

# Chat Cognitive Belt

ID: `UI-CHAT-COGNITIVE-BELT`

## Summary

Compact chat context strip that surfaces selected runtime cues near the transcript without owning runtime behavior

## Links

- parent: [[feat-app-chat|FEAT-APP-CHAT]]
- children: none
- depends_on: [[comp-web-app|COMP-WEB-APP]], [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- used_by: [[feat-app-chat|FEAT-APP-CHAT]]
- ui_related: [[ui-chat-composer|UI-CHAT-COMPOSER]]
- api_related: none
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]], [[test-chat-transcript|TEST-CHAT-TRANSCRIPT]]
- docs_related: [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]]
- agent_related: none

## Relations

Outgoing: none

Incoming:
- [[feat-app-chat|FEAT-APP-CHAT]] -> `parent_of`: App chat owns the cognitive belt context strip
- [[comp-web-app|COMP-WEB-APP]] -> `renders`: Web shell renders the chat cognitive belt through the chat component
- [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]] -> `verifies`: Route smoke covers authenticated chat route rendering where the belt is present

## Chains

- `CHAIN-CHAT-COGNITIVE-BELT` Chat cognitive belt context-strip chain (verified, medium)

## Evidence

- `EVID-RESEARCH-UI-CHAT-COGNITIVE-BELT` research verified: Chat cognitive belt now has a reviewed 3-source UX theory claim tied to working memory visual working memory and attentional load (`docs/architecture/registry/theory_claims.csv`).

## Theory Claims

### CLAIM-CHAT-COGNITIVE-BELT-LOAD-AWARENESS

The Chat cognitive belt can be interpreted as an engineered visual context strip that keeps a small set of salient runtime cues visible while avoiding excessive working-memory and attentional load.

- status: `reviewed`
- confidence: `medium`
- code expression: `runtime cues -> compact cognitive belt -> transcript and composer context`
- applicability: Applies to the UI rationale for compact grouping, secondary visual hierarchy, and limiting always-visible cognitive-status cues near the chat transcript.
- limitations: Working-memory and load-theory sources support the design rationale indirectly; they do not prove usability, accessibility, route behavior, or that the app models human cognition.
- sources: [SRC-COWAN-2001-WM4](https://pubmed.ncbi.nlm.nih.gov/11515286/), [SRC-LUCK-VOGEL-1997-VWM](https://www.nature.com/articles/36846), [SRC-LAVIE-2005-LOAD](https://pubmed.ncbi.nlm.nih.gov/15668100/)


## Notes

Scoped research mapping for a cognitive context strip; neuroscience support is design rationale and not behavior proof.
