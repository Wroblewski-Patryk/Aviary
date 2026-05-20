# User Collaboration Workflow

## Objective

Keep agent work aligned with the user's intent while preserving momentum,
truthfulness, and small reversible steps.

## Default Collaboration Loop

1. Restate the concrete target when the request has ambiguity.
2. Identify the active source of truth: task board, planning doc, design
   reference, production evidence, or direct user instruction.
3. Make reasonable assumptions when the risk is low and record them in the
   task or final report.
4. Stop for a user decision when assumptions would change architecture,
   product direction, data safety, deployment risk, or canonical visual intent.
5. Deliver one useful slice before expanding scope.
6. Report what changed, what was validated, what remains uncertain, and the
   next tiny task.

## Continue Intent

When the user says `pracuj dalej`, `rob dalej`, `kontynuuj`, `next`, `go`, or
similar, treat it as permission to continue through the active coordinator
mission, not as a request for a random tiny slice.

1. Read `.agents/state/active-mission.md`, `.agents/state/next-steps.md`,
   `.codex/context/TASK_BOARD.md`, and current risk/quality/module-confidence
   rows.
2. Choose exactly one mission checkpoint by priority:
   active blocker > explicit next useful pass > missing proof > known issue >
   oldest open responsibility-learning gap.
3. Refresh `.agents/state/active-mission.md` before broad implementation.
4. If the work has separable lanes, use
   `.agents/workflows/responsibility-lanes.md` before delegating.
5. If there is no safe next action, say so plainly and name the smallest
   missing decision or evidence.

## User Working Style

- Be direct and evidence-first; do not soften real blockers into optimism.
- Prefer clear hierarchy: coordinator, lanes, owners, proof, done-state.
- When context is dense, summarize the chosen path and the rejected alternatives
  briefly.
- Keep reports concise but high signal, with concrete files, checks, risks, and
  next checkpoint.
- Store durable collaboration learnings in project state or agent workflow
  files when they affect future work.

## Decision Points

Ask before continuing when:

- two approved sources of truth conflict
- user notes conflict with a canonical screenshot or previously approved
  interpretation
- the proper implementation requires architecture or design-system changes
- the available evidence is not enough to safely choose between product
  behaviors
- a shortcut would introduce placeholder, mock-only, temporary, or
  workaround-only behavior

## Evidence Habit

Every meaningful answer after implementation should make the work auditable:

- changed files or docs
- checks actually run
- browser or screenshot evidence for UI work
- smoke or rollback notes for runtime/deployment work
- explicit residual risks
- next tiny task

## Tone And Language

- Communicate with the user in the user's language.
- Keep repository artifacts in English.
- Be concise, concrete, and candid about uncertainty.
- Do not bury blockers. Name the blocker and the smallest decision or evidence
  needed to unblock it.
