---
id: "WORKFLOW-RESEARCH-EVIDENCE"
name: "Research Evidence Mapping Workflow"
type: "workflow"
status: "verified"
layer: "docs"
module: "architecture"
feature: "research_evidence"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "docs/architecture/graph-system.md"
related_files: ["docs/architecture/registry/research_sources.csv", "docs/architecture/registry/theory_claims.csv", "docs/testing/architecture-research-map.md"]
tags: ["aviary", "workflow", "research_evidence", "neuroscience"]
---

# Research Evidence Mapping Workflow

ID: `WORKFLOW-RESEARCH-EVIDENCE`

## Summary

Maps neuroscience and cognitive-science claims in code to reviewed research sources and explicit limitations

## Links

- parent: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]
- children: none
- depends_on: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]], [[script-generate-arch-graph|SCRIPT-GENERATE-ARCH-GRAPH]]
- used_by: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]], [[feat-memory-flow|FEAT-MEMORY-FLOW]]
- ui_related: none
- api_related: none
- database_related: none
- tests_related: [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]]
- docs_related: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `depends_on` -> [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]: Research evidence rules are documented in the graph system contract

Incoming:
- [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]] -> `parent_of`: Architecture graph workflow owns the research evidence mapping extension
- [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]] -> `verifies`: Graph generator validates research source and theory claim registry integrity

## Chains

- `CHAIN-ARCH-GRAPH-WORKFLOW` Architecture graph evidence generation chain (verified, high)

## Evidence

- `EVID-RESEARCH-WORKFLOW` documentation verified: Research evidence workflow added with source registry claim registry 3-source rule and generated research rollup (`docs/architecture/graph-system.md`).
- `EVID-RESEARCH-CLAIM-EXPANSION` documentation verified: Research evidence expanded for perception attention planning executive-control and memory consolidation claims (`docs/architecture/registry/theory_claims.csv`).
- `EVID-RESEARCH-AFFECT-MOTIVATION-ROLE` documentation verified: Research evidence expanded for affective assessment motivation valuation and role-selection social posture claims (`docs/architecture/registry/theory_claims.csv`).

## Theory Claims

- none

## Notes

Research support is now separate from runtime proof and requires 3 sources for reviewed mapped claims.
