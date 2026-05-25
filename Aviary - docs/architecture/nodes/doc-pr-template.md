---
id: "DOC-PR-TEMPLATE"
name: "Pull Request Template"
type: "documentation"
status: "verified"
layer: "docs"
module: "github"
feature: "architecture_graph"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: ".github/pull_request_template.md"
related_files: [".github/workflows/architecture-graph.yml"]
tags: ["aviary", "docs", "pull_request", "architecture_graph", "evidence"]
---

# Pull Request Template

ID: `DOC-PR-TEMPLATE`

## Summary

Repository PR checklist that asks authors to report architecture graph registry chain evidence research and graph gate updates

## Links

- parent: [[workflow-arch-graph-ci|WORKFLOW-ARCH-GRAPH-CI]]
- children: none
- depends_on: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]], [[workflow-arch-graph-ci|WORKFLOW-ARCH-GRAPH-CI]]
- used_by: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]
- ui_related: none
- api_related: none
- database_related: none
- tests_related: [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]]
- docs_related: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `documents` -> [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]: PR template asks authors to disclose graph registry chain evidence research and graph gate updates
- `depends_on` -> [[workflow-arch-graph-ci|WORKFLOW-ARCH-GRAPH-CI]]: PR checklist complements the automatic graph CI gate by making graph evidence visible in review

Incoming: none

## Chains

- none

## Evidence

- `EVID-ARCH-PR-TEMPLATE-CHECKLIST` documentation verified: Pull request template now requires graph-relevant authors to report registry chain evidence research generated artifact and fast gate updates (`.github/pull_request_template.md`).

## Theory Claims

- none

## Notes

PR template now includes an Architecture Graph and Evidence Map section so graph updates are visible during review.
