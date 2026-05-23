# Next Steps

Last updated: 2026-05-23

## NOW

1. Continue from verified `PRJ-1259`:
   - task:
     `.codex/tasks/PRJ-1259-dashboard-current-focus-focal.md`
   - result:
     Dashboard `Current Focus` now uses a compact scenic circular focal
     treatment instead of a generic teal orb placeholder
   - proof:
     `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS;
     combined Dashboard screenshot/navigation/account gate PASS with
     `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`,
     navigation `step_count=4`, `failed_count=0`, account `step_count=1`,
     `failed_count=0`, `panel_visible=true`; `git diff --check` PASS with
     LF/CRLF warning only; desktop/tablet/mobile screenshots reviewed;
     cleanup found no validation-owned leftovers and removed one fresh
     route-smoke temp profile
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, route-smoke fixture content, or richer Dashboard focus data

1. Continue from verified `PRJ-1258`:
   - task:
     `.codex/tasks/PRJ-1258-dashboard-summary-band-balance.md`
   - result:
     the lower Dashboard summary band now reads as a calmer closure band with
     more readable System Harmony rhythm, balanced layer rows, and a wide
     scenic weekly summary
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`,
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; `git diff --check` PASS with LF/CRLF warning only;
     desktop/tablet/mobile screenshots reviewed; cleanup found no
     validation-owned leftovers and removed four fresh route-smoke temp
     profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, route-smoke fixture content, or richer Dashboard summary data

1. Continue from verified `PRJ-1257`:
   - task:
     `.codex/tasks/PRJ-1257-dashboard-desktop-hero-satellite-quieting.md`
   - result:
     desktop Dashboard hero signal cards are lighter, tighter, and read more
     like connected satellites around the central figure
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`,
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; `git diff --check` PASS with LF/CRLF warning only;
     cleanup found no validation-owned leftovers and removed three fresh
     route-smoke temp profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue from verified `PRJ-1256`:
   - task:
     `.codex/tasks/PRJ-1256-personality-mobile-callout-connectors.md`
   - result:
     mobile Personality callouts now have visible connector lines and stronger
     endpoint dots tying them to the embodied figure
   - proof:
     `npm run build` PASS; Personality screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`,
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; `git diff --check` PASS with LF/CRLF warning only;
     cleanup found no validation-owned leftovers and removed eight fresh
     route-smoke temp profiles from iterative screenshot tuning
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue from verified `PRJ-1255`:
   - task:
     `.codex/tasks/PRJ-1255-chat-desktop-persona-overlay-placement.md`
   - result:
     desktop/tablet Chat now place the `Planning / Conversation continuity`
     overlay as a lower-right persona-stage annotation instead of a
     transcript-facing lower-left label
   - proof:
     `npm run build` PASS; Chat screenshot gate across desktop/tablet/mobile
     PASS with `screenshot_count=3`, `failed_count=0`, `route_count=14`,
     `status=ok`; `npm run test:chat-transcript` PASS with `status=ok`,
     `appSourceCount=2`, `telegramSourceCount=2`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`; `git diff --check` PASS with
     LF/CRLF warning only; cleanup found no validation-owned leftovers and
     removed three fresh route-smoke temp profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue Personality mobile canonical usability from `PRJ-1254`:
   - task:
     `.codex/tasks/PRJ-1254-personality-mobile-timeline-rail.md`
   - result:
     mobile Personality Mind Layers Timeline now reads as a compact token,
     signal-track, and value-chip rail while all six layers remain visible
   - proof:
     `npm run build` PASS; Personality screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`,
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; cleanup found no validation-owned leftovers and
     removed three fresh route-smoke temp profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue Chat canonical usability from `PRJ-1253`:
   - task:
     `.codex/tasks/PRJ-1253-chat-desktop-cognitive-belt-quieting.md`
   - result:
     desktop Chat cognitive belt is flatter, lower, and visually secondary to
     the transcript/persona stage while all supported labels, values,
     progress, source markers, and mobile rail behavior remain intact
   - proof:
     `npm run build` PASS; Chat screenshot gate across desktop/tablet/mobile
     PASS with `screenshot_count=3`, `failed_count=0`, `route_count=14`,
     `status=ok`; `npm run test:chat-transcript` rerun PASS with `status=ok`,
     `appSourceCount=2`, `telegramSourceCount=2`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`; cleanup found no
     validation-owned process leftovers and removed six fresh route-smoke temp
     profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue Personality mobile canonical usability from `PRJ-1252`:
   - task:
     `.codex/tasks/PRJ-1252-personality-mobile-callout-map-quieting.md`
   - result:
     mobile Personality callouts now read as compact embodied-map annotations
     rather than chunky metric cards, `Planning` stays on one line, and all
     supported backend-backed values remain visible
   - proof:
     `npm run build` PASS; Personality screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`,
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; cleanup found no Personality validation-owned
     process leftovers and removed four fresh route-smoke temp profiles
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue Dashboard mobile canonical usability from `PRJ-1251`:
   - task:
     `.codex/tasks/PRJ-1251-dashboard-mobile-hero-signal-quieting.md`
   - result:
     mobile Dashboard hero signal cards are quieter and count values now read
     as clear UI numerals while every supported signal remains visible
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`; cleanup found no Personality
     validation-owned leftovers
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue Chat visual fidelity from `PRJ-1250`:
   - task:
     `.codex/tasks/PRJ-1250-chat-source-marker-quieting.md`
   - result:
     Chat keeps the truthful `App` / `Telegram` transcript marker while
     rendering it as quieter metadata, so the source truth no longer competes
     with speaker, time, delivery status, or message content
   - proof:
     `npm run build` PASS; `npm run test:chat-transcript` PASS with
     `appSourceCount=2`, `telegramSourceCount=2`; Chat screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`; cleanup found no route-smoke,
     Vite, or 5173/4173 listener leftovers after targeted temp-profile cleanup;
     final Windows cleanup reported two stale `chrome-headless-shell` handles
     with no running task instance
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, source
     labels, or route-smoke fixture content

1. Continue mobile Dashboard canonical usability from `PRJ-1248`:
   - task:
     `.codex/tasks/PRJ-1248-dashboard-mobile-flow-rail.md`
   - result:
     mobile Dashboard's cognitive-flow steps now read as a compact horizontal
     rail with a visible next-step peek, while Current Phase remains available
     and lower dashboard data appears sooner
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`; cleanup found no
     validation-owned leftovers
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, or
     route-smoke fixture content

1. Continue mobile Chat canonical usability from `PRJ-1246`:
   - task:
     `.codex/tasks/PRJ-1246-chat-mobile-first-read.md`
   - result:
     mobile Chat's cognitive belt now reads as a compact horizontal context
     rail, so the transcript and composer appear sooner while supported cards
     remain available through scroll
   - proof:
     `npm run build` PASS; Chat screenshot gate across desktop/tablet/mobile
     PASS with `screenshot_count=3`, `failed_count=0`; route smoke
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`; cleanup found no validation-owned leftovers
   - next smallest useful choice:
     pick one exact remaining screenshot mismatch on one route only, or make a
     content/data decision before changing canonical copy, icon glyphs, or
     route-smoke fixture content

1. Continue flagship canonical coherence from `PRJ-1245`:
   - task:
     `.codex/tasks/PRJ-1245-flagship-coherence-tightening.md`
   - result:
     Chat's cognitive belt and Personality's overview/side-panel micro-surfaces
     now read flatter and less card-heavy, while Dashboard was intentionally
     left untouched
   - proof:
     `npm run build` PASS; Dashboard/Chat/Personality screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=9`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`
   - next smallest useful choice:
     make a content/data decision for exact canonical copy/icon parity, or pick
     one exact remaining screenshot mismatch on one route only

1. Continue flagship canonical parity from `PRJ-1244`:
   - task:
     `.codex/tasks/PRJ-1244-personality-canonical-fidelity.md`
   - result:
     Personality now has lighter hero/callout material, flatter side panels,
     tighter timeline rows, a calmer tablet side-support rhythm, and less
     visually dominant mobile callouts/rows
   - proof:
     `npm run build` PASS; Personality screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`
   - next smallest useful choice:
     choose one remaining exact screenshot mismatch across Dashboard, Chat, or
     Personality, or make a content/data decision before changing canonical
     icon glyphs, route-smoke fixture copy, or backend-backed labels

1. Continue Chat canonical parity from `PRJ-1243`:
   - task:
     `.codex/tasks/PRJ-1243-chat-canonical-fidelity.md`
   - result:
     Chat now hides nonessential route-status pills, uses a more balanced
     desktop conversation/persona split, calms transcript/composer density,
     renders assistant ordered lists as one calm plan surface, and suppresses
     the solo quick-action chip plus competing desktop portrait copy
   - proof:
     `npm run build` PASS; Chat screenshot gate across desktop/tablet/mobile
     PASS with `screenshot_count=3`, `failed_count=0`; route smoke
     `route_count=14`, `status=ok`; navigation proof `step_count=4`,
     `failed_count=0`; account proof `step_count=1`, `failed_count=0`,
     `panel_visible=true`
   - next smallest useful choice:
     move to a separate Personality canonical fidelity checkpoint, or make a
     content/data decision before changing Chat icon glyphs, canonical card
     copy, or route-smoke transcript fixture content

1. Continue Dashboard canonical parity from `PRJ-1242`:
   - task:
     `.codex/tasks/PRJ-1242-dashboard-hero-geometry.md`
   - result:
     desktop Dashboard metrics now sit as side satellites with visible
     connector lines around the central hero
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`
   - next smallest useful choice:
     make a separate content/data decision before changing metric labels,
     values, or icon glyphs; otherwise move to one single-surface Chat or
     Personality checkpoint

1. Continue Dashboard canonical parity from `PRJ-1241`:
   - task:
     `.codex/tasks/PRJ-1241-dashboard-first-viewport-lock.md`
   - result:
     Dashboard first viewport now has a stronger scenic hero, quieter metric
     overlays/right guidance/cognitive flow, and no clipped lower Reflection
     row
   - proof:
     `npm run build` PASS; Dashboard screenshot gate across
     desktop/tablet/mobile PASS with `screenshot_count=3`, `failed_count=0`;
     route smoke `route_count=14`, `status=ok`; navigation proof
     `step_count=4`, `failed_count=0`; account proof `step_count=1`,
     `failed_count=0`, `panel_visible=true`
   - next smallest useful choice:
     tune exact Dashboard hero connector/metric geometry, or switch to one
     separate single-surface checkpoint for Chat or Personality

1. Continue flagship canonical parity from `PRJ-1240`:
   - task:
     `.codex/tasks/PRJ-1240-flagship-coherence-pass.md`
   - result:
     Dashboard, Chat, and Personality received a CSS-only coherence pass with
     stronger Dashboard scene authority, quieter Chat persona overlays, and
     calmer Personality callout/side-panel density
   - proof:
     `npm run build` PASS; focused route screenshot gate for `/dashboard`,
     `/chat`, `/personality` across desktop/tablet/mobile PASS with
     `screenshot_count=9`, `failed_count=0`; route smoke `route_count=14`,
     `status=ok`; navigation proof `step_count=4`, `failed_count=0`;
     account proof `step_count=1`, `failed_count=0`, `panel_visible=true`
   - next smallest useful choice:
     take one exact screenshot mismatch at a time: Dashboard card/copy-density
     parity first, or Chat transcript/persona asset fidelity second

1. Continue Dashboard canonical parity from `PRJ-1239`:
   - task:
     `.codex/tasks/PRJ-1239-flagship-canonical-fidelity.md`
   - result:
     Dashboard, Chat, and Personality no longer render the extra desktop
     utility header above the flagship scene; Chat is tighter against the v5
     60/40 canonical target; Personality's overview header is quieter and the
     embodied map dominates the first viewport
   - proof:
     `npm run build` PASS; focused route screenshot gate for `/dashboard`,
     `/chat`, `/personality` across desktop/tablet/mobile PASS with
     `screenshot_count=9`, `failed_count=0`; route smoke `route_count=14`,
     `status=ok`; navigation proof `failed_count=0`; account proof
     `panel_visible=true`
   - next smallest useful choice:
     tune exact Dashboard card proportions/copy density and then rerun the
     same three-route canonical comparison gate

1. Continue v1.2 UI simplification from `PRJ-1238`:
   - task:
     `.codex/tasks/PRJ-1238-shared-shell-noise-reduction.md`
   - result:
     shared shell fake utility controls and duplicate labels are removed;
     `PASS-NOISE-AUDIT` queue is recorded in
     `docs/ux/canonical-ui-layout-index.md`
   - proof:
     `npm run build` PASS; route smoke `route_count=14`, `status=ok`;
     navigation proof `failed_count=0`; account proof `panel_visible=true`;
     screenshot gate `viewport_count=3`, `screenshot_count=42`,
     `failed_count=0`
   - next smallest useful choices:
     run `PASS-SETTINGS-TOOLS`, starting with Settings hero chips/card grid
     and Tools summary/provider-plumbing noise

1. Continue v1.2 UI simplification from the canonical index:
   - task:
     `.codex/tasks/PRJ-1237-canonical-ui-layout-index.md`
   - source of truth:
     `docs/ux/canonical-ui-layout-index.md`
   - result:
     global shell zones, backend/client data authority IDs, route group IDs,
     first-read hierarchy, component budgets, noise taxonomy, allowed group
     types, implementation ownership map, and acceptance gates are defined
   - next smallest useful choices:
     run `PASS-NOISE-AUDIT` from current screenshots, then `PASS-SHELL` to
     remove duplicate global chrome and inert controls before route-specific
     simplification

1. Selected-scope v1 is released as `v1.1.1`:
   - task:
     `.codex/tasks/PRJ-1231-v1-production-candidate-promotion.md`
   - selected SHA:
     `df677370f63d2688eb792f9a3a846d2cd40a564b`
   - proof:
     production release smoke with deploy parity PASS; release reality audit
     `GO_FOR_SELECTED_SHA`; selected SHA go/no-go `GO`; selected-tag
     `v1.1.1` go/no-go `GO`; backend and web production revisions match the
     selected SHA; `release_ready=true`; `release_violations=[]`
   - next smallest useful choices:
     monitor production, prepare a concise user-facing release note, or expand
     one explicitly deferred extension scope such as provider activation,
     proactive launch, deploy automation hardening, or native proof

1. Selected-scope v1 is locally verified as of `PRJ-1230`:
   - task:
     `.codex/tasks/PRJ-1230-v1-selected-scope-final-readiness-refresh.md`
   - proof:
     backend full pytest -> `1105 passed`; web build/responsive/navigation/
     account/route smoke -> PASS; architecture dashboard refresh ->
     selected-scope readiness `11/11`; `git diff --check` -> PASS with
     LF/CRLF warnings only; desktop/tablet/mobile Dashboard screenshots
     reviewed; cleanup confirmed no validation-owned browser/server leftovers
   - release boundary:
     do not call this a new production release candidate until deploy parity
     and release smoke are run for the chosen target
   - next smallest useful choices:
     promote a production candidate with release smoke, or continue optional
     screenshot-driven route polish without changing the selected-scope v1
     readiness claim

1. Continue from the authenticated desktop utility bar checkpoint:
   - task:
     `.codex/tasks/PRJ-1229-authenticated-desktop-utility-bar-parity.md`
   - result:
     desktop authenticated routes now show the shared utility/search/action
     and account band above route content; the implementation reuses existing
     shell components and does not introduce fake browser chrome
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with
     `step_count=4`, `failed_count=0`;
     `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
     PASS with `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
     `panel_visible=true`; refreshed desktop Dashboard, desktop Chat, tablet
     Dashboard, and mobile Dashboard screenshots reviewed; cleanup confirmed
     no AION validation leftovers
   - residual:
     1:1 parity still needs Dashboard lower-card proportions, exact route
     density/copy comparison, and subsequent route-local flagship polish
   - next smallest slice:
     continue Dashboard parity from lower-card proportions and first-viewport
     density, then return to Chat/personality route-specific gaps

1. Continue from the Dashboard desktop hero overlay checkpoint:
   - task:
     `.codex/tasks/PRJ-1228-dashboard-desktop-hero-overlay-parity.md`
   - result:
     desktop Dashboard signal card columns now overlay the scenic figure stage
     instead of sitting as detached side columns; desktop-only figure-note
     callouts are hidden so the metric overlay becomes the primary canonical
     card language
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with
     `step_count=4`, `failed_count=0`;
     `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
     PASS with `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
     `panel_visible=true`; refreshed desktop, tablet, and mobile Dashboard
     screenshots reviewed; cleanup confirmed no AION validation leftovers
   - residual:
     Dashboard still needs further 1:1 parity slices for lower card
     proportions, top utility interpretation, and exact canonical density
   - next smallest slice:
     continue Dashboard parity from concrete screenshot comparison, then return
     to other flagship routes

1. Continue from the desktop sidebar support rhythm checkpoint:
   - task:
     `.codex/tasks/PRJ-1227-desktop-sidebar-support-rhythm.md`
   - result:
     authenticated desktop sidebar support cards now follow the navigation
     stack with a modest canonical gap instead of being pushed to the viewport
     bottom
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with
     `step_count=4`, `failed_count=0`;
     `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
     PASS with `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
     `panel_visible=true`; refreshed desktop Dashboard, desktop Chat, and
     tablet Dashboard screenshots reviewed; cleanup confirmed no validation
     leftovers
   - residual:
     sidebar card micro-details remain a future dedicated parity pass only if
     screenshot comparison identifies them as the next highest-value gap
   - next smallest slice:
     choose the next polish slice from concrete screenshot evidence across
     shared shell pieces, Dashboard, Chat, Tools, Settings, Home, or another
     flagship route

1. Continue from the tablet route header rhythm checkpoint:
   - task:
     `.codex/tasks/PRJ-1226-tablet-route-header-rhythm.md`
   - result:
     authenticated tablet route headers now align the Aviary wordmark, route
     identity, and account trigger in one compact row above the shared route
     rail while phone mobile headers and desktop sidebar remain unchanged
   - proof:
     `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS;
     `npm run audit:ui-responsive` PASS with `route_count=14`,
     `viewport_count=3`, `screenshot_count=18`, `failed_count=0`; `npm run
     audit:ui-navigation` PASS with `step_count=4`, `failed_count=0`;
     `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
     PASS with `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
     `panel_visible=true`; refreshed tablet Dashboard, tablet Tools, and
     mobile Dashboard screenshots reviewed; cleanup confirmed no validation
     leftovers
   - residual:
     route-local tablet polish remains future work only when a concrete route
     screenshot shows a remaining density or hierarchy issue
   - next smallest slice:
     choose the next polish slice from concrete screenshot evidence across
     shared shell pieces, Dashboard, Chat, Tools, Settings, Home, or another
     flagship route

1. Continue from the mobile/tablet account trigger checkpoint:
   - task:
     `.codex/tasks/PRJ-1225-mobile-account-trigger-polish.md`
   - result:
     repeated authenticated mobile/tablet route headers now use a dedicated
     Aviary shell material account trigger instead of generic outline button
     styling, with `aria-expanded` reflecting panel state
   - proof:
     `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS;
     `npm run audit:ui-responsive` PASS with `route_count=14`,
     `viewport_count=3`, `screenshot_count=18`, `failed_count=0`; `npm run
     audit:ui-navigation` PASS with `step_count=4`, `failed_count=0`;
     `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
     PASS with `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
     `panel_visible=true`; refreshed mobile Dashboard, mobile Settings, and
     tablet Dashboard screenshots reviewed; cleanup confirmed no validation
     leftovers
   - residual:
     deeper account panel layout/content polish remains a separate future slice
     if screenshots show it needs more hierarchy work
   - next smallest slice:
     choose the next polish slice from concrete screenshot evidence across
     shared shell pieces, Dashboard, Chat, Tools, Settings, Home, or another
     flagship route

1. Continue from the shared shell navigation affordance checkpoint:
   - task:
     `.codex/tasks/PRJ-1224-shared-shell-navigation-affordance.md`
   - result:
     shared tablet/mobile route rails now show a subtle right-edge
     continuation affordance with scroll snapping and end padding while the
     desktop sidebar remains structurally unchanged
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with
     `step_count=4`, `failed_count=0`; refreshed desktop Dashboard, tablet
     Dashboard, mobile Chat, and mobile Settings screenshots reviewed; cleanup
     confirmed no validation leftovers
   - residual:
     future route additions may need a grouped navigation model if the rail
     becomes too long for comfortable scanning
   - next smallest slice:
     choose the next polish slice from concrete screenshot evidence across
     shared shell pieces, Dashboard, Chat, Tools, Settings, Home, or another
     flagship route

1. Continue from the Dashboard Memory Growth label checkpoint:
   - task:
     `.codex/tasks/PRJ-1223-dashboard-memory-growth-labels.md`
   - result:
     Dashboard `Memory Growth` chart labels now read as separate compact labels
     instead of visually merging in the narrow desktop card
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; focused `/dashboard` route-smoke to
     `C:\tmp\prj1223-ui-responsive` PASS with `screenshot_count=3`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS; refreshed
     desktop/tablet/mobile Dashboard screenshots reviewed; cleanup confirmed no
     validation leftovers
   - residual:
     future additional memory metric categories may need a wider chart
     treatment instead of more abbreviations
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Dashboard, Chat, Tools, Settings, Home, or another flagship route

1. Continue from the Tools integral status deduplication checkpoint:
   - task:
     `.codex/tasks/PRJ-1222-tools-integral-status-deduplication.md`
   - result:
     Tools item cards now hide the supplemental integral pill when it
     duplicates the primary status label, so `Internal chat` shows one clear
     `Always on` status while details remain visible
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; focused `/tools` route-smoke to
     `C:\tmp\prj1222-ui-responsive` PASS with `screenshot_count=3`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS; refreshed
     desktop/tablet/mobile Tools screenshots reviewed; cleanup confirmed no
     validation leftovers
   - residual:
     future tool state labels should avoid duplicate visible badges when status
     and supplemental metadata carry the same text
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Dashboard, Chat, Tools, Settings, or another flagship route

1. Continue from the Settings save action hierarchy checkpoint:
   - task:
     `.codex/tasks/PRJ-1221-settings-save-action-hierarchy.md`
   - result:
     Settings `Save settings` now reads as a calm teal primary action instead
     of a warning-like amber band, while reset runtime data remains clearly
     separated as the danger boundary
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; focused `/settings` route-smoke to
     `C:\tmp\prj1221-ui-responsive` PASS with `screenshot_count=3`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS; refreshed
     desktop/tablet/mobile Settings screenshots reviewed; cleanup confirmed no
     validation leftovers
   - residual:
     future Settings secondary actions should keep destructive, warning, and
     primary color semantics distinct
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Dashboard, Chat, Tools, Settings, or another flagship route

1. Continue from the mobile Chat assistant-width checkpoint:
   - task:
     `.codex/tasks/PRJ-1220-chat-mobile-assistant-width.md`
   - result:
     mobile Chat assistant responses now use the full transcript width by
     hiding the decorative avatar column on narrow screens while preserving
     speaker metadata
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; focused `/chat` route-smoke to
     `C:\tmp\prj1220-ui-responsive` PASS with `screenshot_count=3`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS; refreshed
     desktop/tablet/mobile Chat screenshots reviewed; cleanup confirmed no
     validation leftovers
   - residual:
     richer live Chat composer states still need route-local screenshot
     coverage when selected as a concrete UX slice
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Chat, Dashboard, Tools, or another flagship route

1. Continue from the Tools summary numeric-readability checkpoint:
   - task:
     `.codex/tasks/PRJ-1219-tools-summary-numeric-readability.md`
   - result:
     Tools summary count values now use unambiguous UI numeric typography with
     tabular numbers, so mobile `1` no longer reads like the letter `I`
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile Tools
     screenshots reviewed; cleanup confirmed no validation leftovers
   - residual:
     future compact metric cards should keep count-heavy values in UI numeric
     typography rather than display-serif glyphs
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Dashboard, Chat, Tools, or another flagship route

1. Continue from the Dashboard recent-activity time-readability checkpoint:
   - task:
     `.codex/tasks/PRJ-1218-dashboard-recent-activity-time-readability.md`
   - result:
     compact Dashboard `Recent Activity` timestamps now use calmer metadata
     typography in narrow right-rail contexts, removing awkward tablet
     uppercase timestamp fragmentation
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile
     Dashboard screenshots reviewed; cleanup confirmed no validation leftovers
   - residual:
     future Dashboard card/content polish should continue from concrete
     screenshot evidence rather than route-wide typography churn
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence across
     Dashboard, Chat, or another flagship route

1. Continue from the Chat tablet transcript-clearance checkpoint:
   - task:
     `.codex/tasks/PRJ-1217-chat-tablet-transcript-clearance.md`
   - result:
     tablet Chat now has tighter transcript/card/input spacing so the long
     assistant response clears the composer in the first viewport
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile Chat
     screenshots reviewed; cleanup confirmed no validation leftovers
   - residual:
     richer Chat composer states, especially pending confirmations and
     multi-action states, still need route-local screenshot coverage when
     selected as a concrete UI gap
   - next smallest slice:
     choose the next polish slice only from concrete screenshot evidence;
     avoid opening a new surface until Chat has no visible first-read defects

1. Continue from the Chat cognitive-belt readability checkpoint:
   - task:
     `.codex/tasks/PRJ-1216-chat-cognitive-belt-readability.md`
   - result:
     Chat Motivation metrics now render as four compact readable lines inside
     the existing cognitive belt instead of a slash-separated string that
     truncated on desktop
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile Chat
     screenshots reviewed; cleanup confirmed no validation leftovers
   - residual:
     mobile rail still intentionally peeks the next card, so edge text can be
     partially visible by design; richer Chat composer/state design remains
     outside this focused belt-readability slice
   - next smallest slice:
     select the next route-local UI fix only from concrete screenshot evidence
     after this checkpoint, with Chat composer/state polish as a likely
     candidate if a specific gap is visible

1. Continue from the Chat mobile context-rail checkpoint:
   - task:
     `.codex/tasks/PRJ-1215-chat-mobile-context-rail-readability.md`
   - result:
     mobile Chat keeps the horizontal cognitive context rail while making the
     first card readable and the next card an intentional peek
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile Chat
     screenshots reviewed; cleanup confirmed no validation leftovers
   - residual:
     broader Chat v5 desktop/tablet composition and richer composer state
     design remain outside this focused mobile rail slice
   - next smallest slice:
     choose the next route-local polish only from concrete screenshot evidence
     so the UI mission does not turn into unbounded churn

1. Continue from the Personality embodied-map checkpoint:
   - task:
     `.codex/tasks/PRJ-1214-personality-embodied-map-polish.md`
   - result:
     Personality count-heavy callout values now read as UI data, and the
     mobile Mind Layers timeline keeps compact visible context before the rows
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile
     Personality screenshots reviewed; cleanup confirmed no validation
     leftovers
   - residual:
     broader Chat v5 composition and deeper Personality state coverage remain
     outside this focused route-local polish
   - next smallest slice:
     continue Chat v5 composition polish, or continue Personality state
     coverage only if screenshot review identifies a concrete gap

1. Continue from the Settings danger-boundary checkpoint:
   - task:
     `.codex/tasks/PRJ-1213-settings-danger-boundary-polish.md`
   - result:
     Settings reset runtime data now uses a native disclosure boundary, so
     destructive reset details are accessible but collapsed by default and safe
     daily preferences dominate the first read
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile
     Settings screenshots reviewed
   - residual:
     reset API, auth, session, persistence, and backend behavior were outside
     this presentational safety-boundary slice
   - next smallest slice:
     continue route-local Chat v5 composition polish or Personality route
     polish while keeping responsive/navigation audits green

1. Continue from the channel-aware AI response budget checkpoint:
   - task:
     `.codex/tasks/PRJ-1212-channel-aware-ai-response-budget-policy.md`
   - result:
     `ResponseBudgetPolicy` now owns app/API chat, Telegram, concise,
     structured, and deep generation budgets; expression passes the resolved
     channel into OpenAI reply generation; and prompts instruct the model to
     finish cleanly rather than stopping mid-sentence, mid-list, or inside
     unfinished code blocks
   - proof:
     response-budget/client/prompt pack PASS with `14 passed`;
     expression/client/prompt/budget/delivery pack PASS with `53 passed`;
     runtime channel pack PASS with `3 passed, 112 deselected`; graph/API
     focused rerun PASS with `6 passed`; full backend pytest PASS with
     `1105 passed`
   - residual:
     live token-spend and latency telemetry were not added in this slice
   - next smallest slice:
     monitor real answer quality/cost, then extend `ResponseBudgetPolicy`
     only if a long-form product mode or telemetry need appears; otherwise
     continue route-local Chat v5, Personality, or Settings polish

2. Continue from the Chat response readability and desktop height checkpoint:
   - task:
     `.codex/tasks/PRJ-1211-chat-response-readability-and-height.md`
   - result:
     Chat reply generation has expanded output budgets, markdown list
     continuation stays inside numbered/bulleted items, and desktop Chat has
     a viewport-bound stage with internal transcript scrolling
   - proof:
     `tests/test_openai_client.py` PASS with `7 passed`; `npm run
     test:chat-markdown` PASS with `case_count=7`; `node --check
     scripts/route-smoke.mjs` PASS; `npm run build` PASS; `npm run
     audit:ui-responsive` PASS with `route_count=14`, `viewport_count=3`,
     `screenshot_count=18`, `failed_count=0`; `npm run audit:ui-navigation`
     PASS with `status=ok`, `step_count=4`, `failed_count=0`; refreshed
     desktop/tablet/mobile Chat screenshots reviewed
   - residual:
     broader Chat v5 route composition polish remains open; Browser preview
     without route-smoke mock auth redirects `/chat` to `/login`, so
     mock-authenticated route-smoke remains the authenticated screenshot proof
     path
   - next smallest slice:
     continue route-local Chat v5 composition polish or move to Personality or
     Settings route-local polish while keeping responsive/navigation audits
     green

3. Continue from the Tools route UX clarity checkpoint:
   - task:
     `.codex/tasks/PRJ-1210-tools-route-ux-clarity.md`
   - result:
     Tools cards now foreground readiness, availability, link state, provider
     posture, next action, and user control before technical details; single
     item groups span the directory width on desktop/tablet
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; `npm run audit:ui-navigation` PASS with `status=ok`,
     `step_count=4`, `failed_count=0`; refreshed desktop/tablet/mobile Tools
     screenshots reviewed; cleanup confirmed no active `chrome_headless_shell`,
     no validation Node processes, and no listener on `5173`; `git diff
     --check` passed with LF/CRLF warnings only
   - residual:
     deeper Tools art direction and connector-specific states can improve when
     provider scope expands
   - next smallest slice:
     continue Settings confidence polish, Personality route-local polish, or
     broader Chat v5 composition work

4. Continue from the shared shell navigation proof checkpoint:
   - task:
     `.codex/tasks/PRJ-1209-shared-shell-navigation-proof-and-tablet.md`
   - result:
     mobile shell navigation has repeatable mock-authenticated interaction
     proof, and the tablet route switcher now uses the shared icon+label rail
     instead of older text pills
   - proof:
     `node --check scripts/route-smoke.mjs` PASS; `npm run build` PASS;
     `npm run audit:ui-responsive` PASS with `route_count=14`,
     `viewport_count=3`, `screenshot_count=18`, `failed_count=0`; `npm run
     audit:ui-navigation` PASS with `status=ok`, `step_count=4`,
     `failed_count=0`; desktop/tablet/mobile Dashboard screenshots reviewed;
     cleanup confirmed no active `chrome_headless_shell` and no listener on
     `5173`; `git diff --check` passed with LF/CRLF warnings only
   - residual:
     Browser plugin remains unavailable in this local runtime because of
     missing kernel assets, but the route-smoke Playwright proof now covers the
     interaction gap
   - next smallest slice:
     continue route-local layout passes for Personality, Settings, Tools, and
     deeper Chat v5 convergence

3. Continue from the Personality mobile nav-clearance checkpoint:
   - task:
     `.codex/tasks/PRJ-1207-personality-mobile-nav-clearance.md`
   - result:
     mobile Personality now leaves route-local clearance between the portrait
     hero and Mind Layers timeline so the fixed tabbar does not cover timeline
     rows in the audited first-read
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; refreshed mobile Personality screenshot reviewed;
     cleanup confirmed no active `chrome_headless_shell` and no listener on
     `5173`; `git diff --check` passed with LF/CRLF warnings only
   - next smallest slice:
     continue Personality content hierarchy/side-panel polish, Settings/Tools
     responsive polish, or deeper Chat v5 layout/composer/transcript
     convergence

4. Continue from the Chat mobile first-read compression checkpoint:
   - task:
     `.codex/tasks/PRJ-1206-chat-mobile-first-read-compression.md`
   - result:
     mobile Chat context cards now use a horizontal rail, so conversation and
     composer content appear sooner while context remains accessible
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; refreshed mobile Chat screenshot reviewed; cleanup
     confirmed no active `chrome_headless_shell` and no listener on `5173`;
     `git diff --check` passed with LF/CRLF warnings only
   - next smallest slice:
     continue with deeper chat v5 desktop/tablet layout, transcript, and
     composer canonical polish or move to personality route-local polish

5. Continue from the Chat brand-copy alignment checkpoint:
   - task:
     `.codex/tasks/PRJ-1205-chat-brand-copy-alignment.md`
   - result:
     chat assistant label, composer safety note, and shared sidebar quote
     signature now align with the Aviary product shell
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; refreshed desktop chat screenshot reviewed; cleanup
     confirmed no active `chrome_headless_shell` and no listener on `5173`;
     `git diff --check` passed with LF/CRLF warnings only
   - next smallest slice:
     continue with chat v5 layout/composer/transcript canonical polish or
     personality route-local polish

6. Continue from the dashboard canonical content-rhythm checkpoint:
   - task:
     `.codex/tasks/PRJ-1204-dashboard-canonical-content-rhythm.md`
   - result:
     dashboard first-read hierarchy is calmer: desktop greeting is less
     cramped, guidance rows preserve readable copy with aligned actions, and
     recent activity rows now have visual tokens
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; refreshed desktop dashboard screenshot reviewed;
     cleanup confirmed no active `chrome_headless_shell` and no listener on
     `5173`; `git diff --check` passed with LF/CRLF warnings only
   - next smallest slice:
     continue route-local web polish with chat canonical convergence or a
     deeper final dashboard tableau pass before moving to personality

7. Continue from the dashboard CTA navigation checkpoint:
   - task:
     `.codex/tasks/PRJ-1203-dashboard-cta-navigation-polish.md`
   - result:
     dashboard action controls now route to existing product surfaces rather
     than behaving like decorative buttons
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; Playwright fallback clicked 10 dashboard CTAs and
     verified `/chat`, `/goals`, `/reflections`, `/memory`, and `/insights`;
     cleanup confirmed no active `chrome_headless_shell` and no listener on
     `5173`; `git diff --check` passed with LF/CRLF warnings only
   - next smallest slice:
     continue dashboard content canonical convergence against
     `docs/ux/assets/aion-dashboard-canonical-reference-v2.png` and
     `docs/ux/assets/aviary-dashboard-hero-canonical-reference-v4.png`

8. Continue from the authenticated shared-shell polish checkpoint:
   - task:
     `.codex/tasks/PRJ-1202-authenticated-shell-mobile-polish.md`
   - result:
     logged-in mobile/tablet chrome no longer shows technical build copy in
     the first viewport, and the fixed mobile tabbar now uses calmer Aviary
     material styling with a teal active state
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; cleanup confirmed no active `chrome_headless_shell`
     and no listener on `5173`; `git diff --check` passed with LF/CRLF
     warnings only
   - next smallest slice:
     start dashboard content canonical convergence against
     `docs/ux/assets/aion-dashboard-canonical-reference-v2.png` and
     `docs/ux/assets/aviary-dashboard-hero-canonical-reference-v4.png`

9. Continue from the public Home canonical polish checkpoint:
   - task:
     `.codex/tasks/PRJ-1201-public-home-canonical-polish.md`
   - result:
     Home now reads more like a full-width canonical landing surface; the
     presentation-only tag and nested-window framing are gone, public nav uses
     real anchors, auth placeholders are localized, and the visible wordmark is
     aligned with Aviary
   - proof:
     `npm run build` PASS; `npm run audit:ui-responsive` PASS with
     `route_count=14`, `viewport_count=3`, `screenshot_count=18`,
     `failed_count=0`; Playwright fallback browser proof verified
     CTA -> register modal, localized placeholders, nav hrefs, and
     `unnamedButtons=0`
   - next smallest slice:
     decide whether to continue public landing parity with richer proof/social
     rhythm and section depth, or move to the authenticated shell/dashboard
     canonical convergence lane

10. Continue from the active web responsive breakpoint scope:
   - task:
     `.codex/tasks/PRJ-1200-rescope-to-web-responsive-breakpoints.md`
   - result:
     current UI scope is web across mobile, tablet, and desktop breakpoints;
     native app proof is deferred unless explicitly reactivated
   - proof:
     architecture dashboard refresh returned `DEFERRED:4`, `READY:11`,
     selected-scope readiness `11/11`; `npm run build` and
     `npm run audit:ui-responsive` passed with `route_count=14`,
     `viewport_count=3`, `screenshot_count=18`, and `failed_count=0`
   - next smallest slice:
     inspect or polish the web screenshots only from explicit visual feedback;
     otherwise keep `npm run audit:ui-responsive` as the active UI gate

11. Preserve the hardened native mobile proof doctor as deferred evidence:
   - task:
     `.codex/tasks/PRJ-1199-harden-mobile-device-proof-doctor.md`
   - result:
     `npm run doctor:ui-mobile-device` now reports Android SDK env checks,
     default SDK path existence, checked tool candidates, proof readiness, and
     concrete next actions
   - current blocker:
     local native proof remains blocked because `adb`, `emulator`,
     `ANDROID_HOME`, `ANDROID_SDK_ROOT`, and the default Windows Android SDK
     path are unavailable
   - next smallest slice:
     do not pursue native proof unless native app scope is reactivated

12. Continue from the cleaned tools overview baseline:
   - task:
     `.codex/tasks/PRJ-1197-remove-tools-roadmap-placeholders.md`
   - result:
     `/app/tools/overview` no longer lists future-only Trello or Nest
     placeholder entries; active tools are limited to implemented
     runtime/API/configuration contracts
   - proof:
     focused tools-overview API pack `3 passed, 129 deselected`; web
     TypeScript project build passed; production-code placeholder scan found
     no remaining `planned_placeholder` active-path matches
   - next smallest slice:
     keep external provider activation under `ARCH-CONNECTORS-001` and only
     add future providers after their bounded runtime contracts exist

13. Keep the refreshed architecture dashboard baseline current:
   - task:
     `.codex/tasks/PRJ-1198-refresh-mobile-architecture-dashboard-truth.md`
   - result:
     generated architecture dashboard now treats `ARCH-MOBILE-001` as
     `IMPLEMENTED_NOT_VERIFIED` instead of an untouched deferred future
     scaffold
   - proof:
     audit/dashboard refresh wrote `DEFERRED:3`,
     `IMPLEMENTED_NOT_VERIFIED:1`, `READY:11`; selected-scope readiness is
     `11/12`; generator scripts compile
   - next smallest slice:
     keep `ARCH-MOBILE-001` deferred while current UI scope remains web
     breakpoints

14. Continue from the verified runtime-layer baseline:
   - task:
     `.codex/tasks/PRJ-1195-runtime-layer-audit-and-polish-perception-fix.md`
   - audit:
     `docs/operations/aion-runtime-layer-audit-2026-05-13.md`
   - proof:
     focused pack `4 passed, 129 deselected`; full backend pytest
     `1093 passed`
   - next smallest slice:
     move to native mobile device proof or external provider activation.

15. Continue from the repaired production DB baseline:
   - latest memory task:
     `.codex/tasks/PRJ-1194-topic-scoped-memory-summary-buckets.md`
   - current verified baseline:
     Coolify production runs runtime memory with `RECENT_MEMORY_LIMIT=6`,
     `SEMANTIC_MEMORY_TOP_K=5`, OpenAI `text-embedding-3-small`, and pgvector
     dimensions `1536`
   - local code baseline:
     runtime query embeddings use the configured provider path, foreground
     vector retrieval includes `episodic`, and vector-matched episodes outside
     the recent temporal window enter the context bundle; PostgreSQL semantic
     vector ranking uses native pgvector distance ordering; vector relevance
     now survives context selection even when lexical overlap is absent;
     optional `relation` vector hits can rehydrate to revalidated relation
     records and merge into runtime relation state when `relation` is enabled;
     repeated recent memory topics now consolidate into semantic
     topic-scoped `memory_topic_summary` conclusions that are injected into
     context as long-term memory summaries
   - production proof:
     post-maintenance two-turn memory scenario answered `Roki`, persisted two
     episodes, and wrote two 1536-dimensional semantic embeddings; PRJ-1189
     non-temporal semantic proof on commit `d4d2911` answered `Roki` after
     15 filler episodes and retrieved original episode `id=4`; PRJ-1192
     production commit `f369556` enabled optional `relation` vector source,
     returned `VECTOR_RELATION_HITS 1` in a controlled repository proof, and
     passed release smoke with `release_ready=true`; PRJ-1194 production
     commit `c11377c` created separate `topic:dog` and `topic:deployment`
     long-term memory buckets, injected both into context, and cleaned
     synthetic rows to zero
   - next smallest slice:
     memory quality is verified for the current release path; plan an
     ANN/vector-index migration only if retrieval volume makes query latency
     require it

7. Native app proof parking lot:
   - branch: `codex/v15-mobile-ui-deploy-commits`
   - remote: `origin/codex/v15-mobile-ui-deploy-commits`
   - GitHub PR:
     `https://github.com/Wroblewski-Patryk/Aviary/pull/1`
   - production merge commit:
     `43837bb183c8975845b99b65a03cea5ccf4903a0`
   - PR creation URL:
     `https://github.com/Wroblewski-Patryk/Aviary/pull/new/codex/v15-mobile-ui-deploy-commits`
   - promotion handoff:
     `docs/operations/v15-mobile-ui-pr-and-production-promotion-handoff-2026-05-12.md`
   - local preview is intentionally stopped after validation cleanup; restart
     it with `Push-Location .\mobile; npm run deploy:ui-mobile-local` when
     another preview proof is needed
   - production is green for the merge commit and final cleanup commit;
     release smoke passed with runtime and web shell revisions matching
     `07b3b3e5fe3bd37439dd1cafbdc7fb15c4ef3a7b`
   - local conflict posture: `git merge-tree` showed no conflict output
     against `origin/main`
   - next smallest slice: deferred unless native app scope is reactivated

8. Native app groundwork archive:
   - plan: `docs/planning/v1.5-mobile-ui-plan.md`
   - latest task: `.codex/tasks/PRJ-1182-v15-mobile-device-proof-doctor.md`
   - promotion handoff:
     `docs/operations/v15-mobile-ui-pr-and-production-promotion-handoff-2026-05-12.md`
   - handoff: `docs/operations/v15-mobile-ui-local-preview-handoff-2026-05-12.md`
   - evidence:
     `.codex/artifacts/prj1158-mobile-native-shell/mobile-shell-390x1200-v2.png`
     `.codex/artifacts/prj1159-mobile-chat-route/mobile-chat-390x1200-v2.png`,
     `.codex/artifacts/prj1160-mobile-support-routes/`,
     `.codex/artifacts/prj1161-mobile-personality-route/`,
     `.codex/artifacts/prj1162-mobile-route-rail/`,
     `.codex/artifacts/prj1163-mobile-home-route-rail/`,
     and `.codex/artifacts/prj1164-mobile-ui-audit/report.json`
   - reusable validation:
     `Push-Location .\mobile; npm run audit:ui-mobile; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
     now expects `route_count=5`, `viewport_count=2`, `screenshot_count=10`,
     `action_proof_count=3`, `state_proof_count=4`, and `failed_count=0`
   - deployed preview validation:
     `Push-Location .\mobile; npm run smoke:ui-mobile-preview; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
     now expects `preview_health.ok=true`, `route_count=5`,
     `viewport_count=2`, `screenshot_count=10`, and `failed_count=0`
   - next smallest slice: capture Expo Go/simulator proof when Android tooling
     or a device is available.
   - local preview:
     stopped after validation cleanup; use `npm run deploy:ui-mobile-local`
     to restart it on `http://127.0.0.1:8093`
   - local deploy:
     `Push-Location .\mobile; npm run deploy:ui-mobile-local`
   - git hygiene:
     generated preview/cache/log artifacts are ignored by `.gitignore`
   - native proof readiness:
     `Push-Location .\mobile; npm run doctor:ui-mobile-device; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
     currently reports `status=blocked` because `adb` and `emulator` are
     unavailable
   - pushed branch:
     `origin/codex/v15-mobile-ui-deploy-commits`
   - PR creation URL:
     `https://github.com/Wroblewski-Patryk/Aviary/pull/new/codex/v15-mobile-ui-deploy-commits`

6. Preserve the completed `v1.1` web UI responsive quality baseline:
   - plan: `docs/planning/v1.1-web-ui-responsive-plan.md`
   - handoff task: `.codex/tasks/PRJ-1157-v11-web-ui-responsive-handoff.md`
   - evidence: `.codex/artifacts/prj1150-v11-ui-responsive-audit/report.json`
   `PRJ-1151` has closed dashboard mobile first-read compression and
   `PRJ-1152` has closed personality mobile balance, and `PRJ-1153` has closed
   tools tablet readability. `PRJ-1154` has closed tools mobile density.
   `PRJ-1155` has closed settings mobile density. `PRJ-1156` has closed
   dashboard lower mobile ranking. `PRJ-1157` has closed the v1.1 web
   responsive handoff. Next smallest slice: plan `v1.5` mobile from these
   learnings or start a new narrow UI polish item from explicit feedback.

7. Keep `npm run audit:ui-responsive` in the web validation set for shell,
   route layout, navigation, and responsive UI changes.

## Previous Architecture Queue

1. Select the next smallest stability or architecture-alignment slice from the
   generated project status dashboard. `PRJ-933` is done and aligned the
   architecture radar with the current v1 release boundary:
   - `docs/operations/project-status-dashboard.md`
   - `docs/operations/project-status-dashboard.json`
   Current phase is `architecture complete for selected scope with deferred
   extensions`. Selected-scope readiness is `11/11` rows (`100.0%`). There is
   no selected-scope blocker in the generated radar.

2. Keep the architecture implementation audit as the source matrix behind the
   dashboard:
   - `docs/operations/architecture-implementation-map-2026-05-10.csv`
   - `docs/operations/architecture-implementation-audit-2026-05-10.md`

## NEXT

1. Preserve the selected-scope architecture radar. Do not reopen deferred
   extension rows unless their trigger is present:
   - provider credentials and expanded organizer scope for `ARCH-CONNECTORS-001`
   - expanded proactive launch scope for `ARCH-PROACTIVE-001`
   - a newly selected release candidate for `ARCH-DEPLOY-AUTO-001`
   - explicit mobile product/release scope for `ARCH-MOBILE-001`
2. Use `docs/operations/v1-selected-scope-handoff-2026-05-11.md` as the
   concise handoff for the current achieved selected-scope posture.
2. Keep full backend pytest in the validation set after backend contract or
   action-loop changes that alter skill/tool metadata.
3. Keep the full web command pack in the validation set for route-shell,
   navigation, or authenticated-shell changes:
   `tsc -> vite build -> npm run smoke:routes`.
4. Preserve native exit codes in PowerShell command packs with
   `$exit=$LASTEXITCODE; Pop-Location; exit $exit`; `PRJ-930` proved
   `Push-Location; npm ...; Pop-Location` can mask a failed smoke.
5. For Windows sandbox `PermissionError` on pytest basetemp creation, record
   the sandboxed failure and rerun the same gate outside sandbox before
   treating it as an application regression.
6. Refresh the architecture implementation map after every meaningful
   architecture/evidence slice.
7. Refresh `docs/operations/project-status-dashboard.md` and
   `docs/operations/project-status-dashboard.json` after refreshing the map.

## LATER

1. Consider broader bounded action-loop extensions only after a concrete
   evidence-backed need appears.
2. Create a mobile implementation scope decision before counting mobile toward
   architecture completion.

## Selection Rules

- Pick one bounded mission objective for each autonomous iteration; use small
  checkpoint tasks inside that mission when useful.
- Prefer tasks that reduce blocker risk, regression risk, or unclear source of
  truth.
- Do not start new feature work when a P0/P1 regression or release blocker is
  unresolved.
- Keep this file synchronized with `.codex/context/TASK_BOARD.md` and
  `docs/planning/mvp-next-commits.md`.
