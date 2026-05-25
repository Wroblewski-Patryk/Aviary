# Subagent Delegation Policy

## Goal

Use subagents to speed up Personality/Aviary delivery without losing runtime
contract quality, ownership, validation evidence, or one accountable parent
coordinator.

The active chat acts as coordinator. Subagents are bounded contributors. A
delegated report is evidence, not approval. The coordinator owns final
integration, validation, state updates, and `DONE`.

## When To Delegate

- independent side tasks that can run in parallel
- bounded implementation slices with clear file or module ownership
- specialized analysis that does not block the immediate next local step
- docs sync or isolated test work with concrete acceptance criteria

## When Not To Delegate

- urgent blocking tasks needed for the very next step
- tightly coupled runtime-stage changes that are hard to split safely
- tasks with unclear ownership, acceptance criteria, or validation commands
- overlapping writes to the same files or contracts

## Delegation Rules

- refresh `.agents/state/active-mission.md` for broad work before delegation
- select lanes from `.agents/workflows/responsibility-lanes.md`
- assign explicit file or module ownership to each subagent
- avoid overlapping write scopes across parallel workers
- do not duplicate work between main agent and subagents
- require validation expectations before work starts
- integrate returned changes with review and follow-up verification
- keep shared state files and final closure with the coordinator unless
  explicitly assigned

## Output Contract

Every delegated result should report:

1. objective completed
2. files changed
3. validations run
4. residual risks
5. missing responsibility noticed: yes/no
6. next suggested step

## Learning Loop

If a subagent discovers a missing lane, unclear owner, bad split, missing
evidence, or missing context, the coordinator records it in
`.agents/state/responsibility-learning.md` and updates the next similar brief,
lane registry, task template, or source-of-truth doc.
