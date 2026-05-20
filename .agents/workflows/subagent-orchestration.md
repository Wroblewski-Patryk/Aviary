# Subagent Orchestration Workflow

## Objective

Standardize safe delegation and parallelization behavior for agent work while
keeping one accountable coordinator for the parent mission.

The active chat is the coordinator. Subagents are bounded contributors. Their
reports are evidence, not approval. The coordinator owns integration, final
validation, state updates, and task closure.

## Steps

1. Identify the critical-path task that must stay local and anchor it in
   `.codex/context/TASK_BOARD.md` or `.agents/state/active-mission.md`.
2. Review `.agents/workflows/responsibility-lanes.md`.
3. Identify independent lanes that can be delegated.
4. Confirm the user or operator instruction explicitly allows subagents.
5. Assign clear ownership, file scope, expected output, and validation proof to
   each subagent.
6. Continue local non-overlapping work while subagents run.
7. Integrate and verify subagent outputs.
8. Record missing lane or ownership learnings in
   `.agents/state/responsibility-learning.md`.

## Guardrails

- no overlapping write ownership
- no duplicate implementation effort
- no blocking wait loops without reason
- no delegation of unclear or under-specified tasks
- no delegation without validation expectations
- no drift between delegated work status and `.codex/context/TASK_BOARD.md`
- no subagent spawn just because a task is broad; use subagents only when
  explicitly requested and when the work can run in parallel
- no final `DONE` based only on subagent confidence

## Delegation Decision Matrix

| Situation | Main agent owns | Subagent can own |
| --- | --- | --- |
| Next action is blocked by the answer | Blocking analysis | Nothing yet |
| Several independent code areas are known | Integration plan | One bounded write area |
| Documentation needs sync while code changes continue | Code path | Docs-only update |
| Tests can run while implementation continues | Implementation | Targeted verification |
| Unknown codebase needs mapping | Immediate task framing | Read-only exploration |

## Ownership Rules

- Write scopes must be disjoint.
- Shared files such as `AGENTS.md`, task board, project state, and central
  route registries should usually stay with the main agent unless explicitly
  assigned.
- A subagent should not change task status to `DONE`; the main agent closes the
  task after integration and verification.
- If a subagent discovers that its scope overlaps another active edit, it should
  stop and report the conflict.

## Delegation Handoff Contract

Every delegated task should define:

- objective
- responsibility lane
- owned files or modules
- constraints or non-goals
- required validations
- expected output summary
- whether missing responsibilities should be reported

Every delegated result should report:

1. objective completed
2. files changed
3. validations run
4. residual risks
5. missing responsibility noticed: yes/no
6. next suggested step

## Integration Checklist

Before closing the parent task:

- review subagent diffs or findings
- resolve conflicts with current local changes
- run the parent task's required validation
- update task board and project state once, from the main thread
- close or explicitly leave open any subagent follow-up
- update `.agents/state/responsibility-learning.md` when a gap in ownership,
  context, proof, or lane design was discovered
