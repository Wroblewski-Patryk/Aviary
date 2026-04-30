# Canonical Visual Implementation Workflow

Use this workflow when a project has an approved target screen, screenshot, or
mockup that implementation should match closely.

The canonical visual is not inspiration. It is a specification.

## Goal

Prevent "close enough" approximations when the task requires a polished,
high-fidelity result.

## Core Contract

- The canonical visual is a specification, not inspiration.
- Work one surface at a time.
- Do not move to the next dependent surface until the current one is judged at
  `95%` parity or higher against the active spec.
- The active spec can be:
  - the canonical screenshot alone
  - or the canonical screenshot plus explicit user-requested interpretation
    notes
- If user-requested notes conflict with each other or with a previously
  accepted interpretation, stop and ask the user to decide before continuing.

## Required Stages

### 1. Canonical Intake

- Identify the exact approved reference.
- Record the source in the task.
- Confirm whether the target is pixel-close, structurally faithful, or only
  style-inspired.

### 2. Visual Decomposition

Break the screen into:

- layout structure
- reusable components
- typography system
- decorative assets
- background assets
- surface treatments
- motion and interaction details

Do not merge all decorative work into "background styling".

### 3. Asset Strategy

For each decorative or background element, decide whether it should be:

- code-native CSS or native drawing
- SVG asset
- raster asset such as PNG or WebP

Use generated or exported image assets when the canonical design contains
texture, painterly atmosphere, organic shapes, or illustration that code will
flatten.

### 4. Gap Audit

Before implementation, compare the current UI against the canonical reference
and record missing assets, layout mismatches, hierarchy gaps, and any element
that is still only approximated.

If the user has provided explicit deviations from the screenshot, record them
as approved interpretation notes and include them in the same gap audit.

### 5. Implementation Sequencing

Recommended order:

1. asset preparation
2. structural layout parity
3. component styling parity
4. decorative and background parity
5. interaction and state parity
6. screenshot comparison pass

For flagship routes, preferred closure order is:

1. public shell frame
2. public shared navigation pieces
3. public home
4. authenticated shell frame
5. authenticated sidebar or shared navigation pieces
6. dashboard
7. chat
8. personality

Do not work broadly across multiple later surfaces while an earlier dependent
surface is still visibly drifting.

### 6. Screenshot Comparison Pass

- Capture the implemented screen in the browser.
- Compare it side by side against the canonical reference.
- List remaining mismatches explicitly.
- Do not stop at "the vibe is similar".

### 7. Quick Closure Check

After each surface slice:

1. capture the latest implementation screenshot
2. list the top 5 to 10 remaining visible mismatches
3. decide whether the current surface is at least `95%` aligned
4. only then move to the next dependent surface

If the answer is below `95%`, continue on the same surface instead of opening a
new module lane.
