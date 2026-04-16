# Subagent Orchestration Workflow

## Objective

Use delegation safely in a backend-first Python project with a shared runtime and shared docs.

## Steps

1. Keep the critical-path runtime change local.
2. Delegate only independent side work such as:
   - docs alignment
   - isolated tests
   - bounded ops/checklist updates
3. Assign clear ownership and explicit file scope.
4. Continue non-overlapping local work while subagents run.
5. Integrate and verify delegated output before closing the task.

## Guardrails

- no overlapping write ownership
- no duplicate implementation effort
- no waiting unless blocked on the result
- no delegation of under-specified runtime behavior
- no blind trust on delegated code without local verification
