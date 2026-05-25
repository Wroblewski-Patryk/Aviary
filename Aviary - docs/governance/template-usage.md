# Repository Bootstrap Usage

This repository uses local, manual bootstrap artifacts.

## Flow

1. Start from this repository bootstrap package.
2. Rename the folder.
3. Do not copy this repository's `.git` directory into the generated app.
4. Open the new project in Codex.
5. Tailor docs, plans, context, and deployment contract through guided setup.
6. Use `docs/governance/app-creation-playbook.md` and
   `.codex/templates/app-blueprint-template.md` to turn the app idea into
   product docs, architecture docs, project state, and one first vertical
   slice.
7. Confirm the initial architecture and visual-system contracts before broad
   implementation begins.
8. If the repository has multiple major modules, activate the `docs/modules/`
   starter docs and keep them aligned with architecture.
9. When the project reaches a release-readiness, handoff, incident-review, or
   stalled-queue moment, copy
   `docs/governance/function-coverage-ledger-template.csv` into
   `docs/operations/` as a dated function coverage matrix and use
   `docs/governance/function-coverage-ledger-standard.md` to classify the next
   smallest evidence, fix, blocker, or scope-decision tasks.
10. Adapt `docs/documentation-map.md` and `docs/maps/*` so agents know where
    current truth, active work, and historical proof live.
11. Keep historical task records, evidence, audits, release packets, and raw
    artifacts in `history/`, not in current canonical docs.
12. For ideas or product concepts, use
    `docs/planning/idea-to-function-chain-playbook.md` and
    `docs/planning/idea-ledger.csv` before implementation.
13. For larger slices, group connected chains under
    `docs/planning/work-package-index.csv` and `docs/planning/work-packages/`.
14. Use `docs/product/capability-map.md` and
    `docs/architecture/capability-to-implementation-map.csv` so product
    capabilities remain connected to code, tests, and evidence.
15. Record durable product, architecture, UX, security, and operations
    decisions in `docs/decisions/decision-register.csv`.
16. For multi-layer features, adapt `docs/pipelines/pipeline-registry.md` and
    `docs/pipelines/pipeline-template.md` so flows are visible across UI, API,
    services, data, side effects, tests, and docs.
17. For larger projects, activate
    `docs/architecture/architecture-evidence-graph-system.md`, graph
    registries, dependency relations, and function chains before broad
    autonomous work.
18. Define environment, service topology, runtime config, data ownership,
    release train, quality scenarios, and automation command safety before
    production-facing work.
19. For long-running autonomous builds, adapt
    `docs/operations/project-control-system.md` so agents can distinguish
    implemented-and-verified work from evidence gaps, local gaps, external
    blockers, future expansion, and historical evidence.
20. For agent-heavy projects, adapt
    `docs/governance/agent-runtime-contract.md` before broad implementation so
    agents know the real runtime flow, side-effect layer, and forbidden
    shortcuts.
21. If the project has multi-stage agent cognition, adapt
    `docs/architecture/agent-system-primitives.md` so processors, roles,
    planning, expression, action, memory, and reflection stay separate.
22. If agents wake on schedules, assignments, mentions, or resumable sessions,
    adapt `docs/operations/persistent-agent-runtime-playbook.md` so heartbeat
    status, logs, budgets, and recovery are explicit.
23. When agents can call MCP tools, workflow commands, provider actions, or
    other side-effectful routes, adapt
    `docs/operations/approval-aware-agent-command-flow.md` before enabling
    write-mode execution.
24. When agents write durable memory into an external service, adapt
    `docs/operations/external-operational-memory-agent-playbook.md` and require
    a startup handshake plus scoped credentials.
25. When the project uses local -> stage -> production promotion, adapt
    `docs/operations/deployment-template-local-stage-production.md` before the
    first release instead of relying on chat-only deploy notes.

## Existing Repository Adoption

For an established project, use
`docs/governance/existing-project-adoption-playbook.md` instead of treating the
template as a clean-room bootstrap. Preserve current project truth, install the
minimum agent context first, and turn mismatches into tracked tasks.

Run `docs/governance/agent-readiness-checklist.md` before allowing autonomous
implementation loops.

## Why Manual Mode

- Fast setup for early-stage projects
- Full flexibility per project without template-update tooling
- Easy human review of every initial decision

## Guardrails

- Keep the repository docs as the canonical baseline.
- Treat `docs/architecture/` as the approved app architecture baseline.
- Start broad app creation from an app blueprint, not from ad hoc code
  scaffolding.
- Use `docs/governance/user-feedback-loop.md` to keep user notes, corrections,
  preferences, and priority changes from being lost between iterations.
- Use `.agents/workflows/documentation-governance.md` to keep architecture,
  planning, modules, and operations docs from drifting apart.
- Use `docs/governance/agent-readiness-checklist.md` after bootstrap or
  adoption, before broad agent execution.
- If the project has a reusable UI layer, document its shared style rules in
  `docs/ux/` early.
- For UI-heavy products, fill `docs/ux/visual-direction-brief.md` before broad
  frontend expansion and use the UX starter docs during review.
- Do not skip the bootstrap checklist.
- Keep changes small and auditable in each new repo.
- Keep template Git history separate from app Git history.
- Keep subagent rules aligned with
  `docs/governance/subagent-delegation-policy.md`.
- Keep repository layout aligned with
  `docs/governance/repository-structure-policy.md`.
- Treat the function coverage ledger as optional until the project has enough
  module surface area that ad-hoc "test everything" loops stop being useful.
- Treat `docs/planning/application-completion-audit-task-contract-template.md`
  as the default structure for broad "what remains?" audits instead of letting
  agents produce chat-only app-completion summaries.
