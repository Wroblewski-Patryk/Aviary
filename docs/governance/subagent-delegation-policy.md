# Subagent Delegation Policy

## Goal

Use subagents to speed up Personality/Aviary delivery without losing runtime
contract quality, ownership, or validation evidence.

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

- assign explicit file or module ownership to each subagent
- avoid overlapping write scopes across parallel workers
- do not duplicate work between main agent and subagents
- require validation expectations before work starts
- integrate returned changes with review and follow-up verification

## Output Contract

Every delegated result should report:

1. objective completed
2. files changed
3. validations run
4. residual risks
5. next suggested step
