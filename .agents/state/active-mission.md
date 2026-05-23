# Active Mission Packet

Last updated: 2026-05-23

Use this file as the first operational router for `pracuj dalej`, `rob dalej`,
`kontynuuj`, `next`, and similar continuation nudges. Keep it short enough that
a fresh coordinator can choose the next checkpoint without rereading the whole
repository history.

## Current Mission

- Mission ID: PRJ-1259-dashboard-current-focus-focal
- Status: VERIFIED
- Selected objective: make Dashboard `Current Focus` read as a polished focal
  module instead of a placeholder orb card.
- Why this mission now: after `PRJ-1258`, Epicurus identified `Current Focus`
  as the smallest fresh screenshot-backed Dashboard mismatch that could be
  improved without content, icon, backend, hero, or summary-band changes.
- Release objective or product milestone advanced: v1.2 web Dashboard
  canonical lower-grid composition.
- First/next checkpoint: completed a CSS-only Dashboard Current Focus focal
  pass. The generic orb is now a compact scenic focal treatment while all data,
  copy, CTA behavior, and surrounding Dashboard surfaces remain unchanged.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/dashboard`
  desktop/tablet/mobile screenshot gate, navigation proof, account proof,
  screenshot review, cleanup check, and `git diff --check`.

## PRJ-1259 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Epicurus and completed read-only
  - QA lane delegated to Goodall and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - Current Focus now uses a compact scenic circular focal treatment instead
    of the prior generic teal orb
  - all Dashboard data/copy/CTA, hero signals, PRJ-1258 summary band,
    mobile/tablet structure, cognitive flow, Chat, Personality, and shared
    shell were not changed
- Validation:
  - `node --check scripts/route-smoke.mjs` PASS
  - `npm run build` PASS
  - combined focused `/dashboard` screenshot/navigation/account gate PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no validation-owned node/Vite, 5173/4173 listener,
    Chromium, or headless browser leftovers; one fresh route-smoke temp
    profile from this checkpoint was removed
- Residual:
  - This is a verified Dashboard Current Focus focal pass, not a full 95%
    pixel parity claim. Exact canonical icon glyphs and richer focus content
    remain separate content/data decisions.
- Next recommended checkpoint:
  - Pick one exact remaining screenshot mismatch on one route, or make a
    content/data decision before changing canonical copy, icon glyphs,
    route-smoke fixture content, or backend-backed labels.
- Artifacts:
  - `.codex/tasks/PRJ-1259-dashboard-current-focus-focal.md`
  - `.codex/artifacts/prj1259-dashboard-current-focus-focal/report.json`
  - `.codex/artifacts/prj1259-dashboard-current-focus-focal/screenshots/`

## Previous Mission

- Mission ID: PRJ-1258-dashboard-summary-band-balance
- Status: VERIFIED
- Selected objective: make the lower Dashboard summary band read as a calmer
  canonical closure surface instead of a cramped card cluster.
- Why this mission now: after `PRJ-1257`, Kant identified the lower Dashboard
  summary band as the smallest fresh screenshot-backed mismatch that could be
  improved without content, icon, backend, or hero changes.
- Release objective or product milestone advanced: v1.2 web Dashboard
  canonical desktop closure-band composition.
- First/next checkpoint: completed a CSS-only Dashboard summary-band pass.
  System Harmony is wider and calmer, Balance across layers remains readable,
  and Weekly summary stays scenic while preserving all data and route behavior.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/dashboard`
  desktop/tablet/mobile screenshot gate, navigation proof, account proof,
  screenshot review, cleanup check, and `git diff --check`.

## PRJ-1258 Previous Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Kant and completed read-only
  - QA lane delegated to Meitner and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - lower Dashboard summary closure grid now gives System Harmony more
    breathing room and keeps Balance and Weekly summary in a calmer rhythm
  - all Dashboard data/copy, hero signals, mobile/tablet structure, cognitive
    flow, Chat, Personality, and shared shell were not changed
- Validation:
  - `npm run build` PASS
  - focused `/dashboard` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no validation-owned node/Vite, 5173/4173 listener,
    Chromium, or headless browser leftovers; four fresh route-smoke temp
    profiles from this checkpoint were removed
- Residual:
  - This is a verified Dashboard summary-band balance pass, not a full 95%
    pixel parity claim. Exact canonical icon glyphs and richer summary content
    remain separate content/data decisions.
- Next recommended checkpoint:
  - Pick one exact remaining screenshot mismatch on one route, or make a
    content/data decision before changing canonical copy, icon glyphs,
    route-smoke fixture content, or backend-backed labels.
- Artifacts:
  - `.codex/tasks/PRJ-1258-dashboard-summary-band-balance.md`
  - `.codex/artifacts/prj1258-dashboard-summary-band-balance/report.json`
  - `.codex/artifacts/prj1258-dashboard-summary-band-balance/navigation-proof.json`
  - `.codex/artifacts/prj1258-dashboard-summary-band-balance/account-proof.json`
  - `.codex/artifacts/prj1258-dashboard-summary-band-balance/screenshots/`

## Previous Mission

- Mission ID: PRJ-1255-chat-desktop-persona-overlay-placement
- Status: VERIFIED
- Selected objective: place desktop Chat's Planning overlay as a lower-right
  persona-stage annotation instead of a transcript-facing lower-left label.
- Why this mission now: `PRJ-1254` left Chat overlay placement as the next
  concrete screenshot-backed mismatch from the UX parity lane, and Pascal
  confirmed it should stay a CSS-only placement slice.
- Release objective or product milestone advanced: v1.2 web Chat canonical
  desktop/tablet persona-stage composition.
- First/next checkpoint: completed a CSS-only Chat portrait overlay placement
  pass. The overlay now sits on the right/bottom side of the persona stage,
  below the channel annotation, while mobile keeps its existing placement.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/chat` desktop/tablet/mobile
  screenshot gate, `test:chat-transcript`, navigation proof, account proof,
  screenshot review, cleanup check, and `git diff --check`.

## PRJ-1255 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Pascal and completed read-only
  - QA lane delegated to Parfit and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - Chat Planning overlay now uses lower-right portrait-stage placement on
    desktop/tablet instead of the transcript-facing lower-left edge
  - mobile Chat keeps its previous overlay placement through an explicit
    `right: auto` override
  - transcript, composer, source markers, cognitive belt, backend data,
    Dashboard, and Personality were not changed
- Validation:
  - `npm run build` PASS
  - focused `/chat` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - `npm run test:chat-transcript` PASS: `status=ok`,
    `appSourceCount=2`, `telegramSourceCount=2`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no validation-owned node/Vite, 5173/4173 listener,
    Chromium, or headless browser leftovers; three fresh route-smoke temp
    profiles from this checkpoint were removed
- Residual:
  - This is a verified Chat overlay placement pass, not a full 95% pixel
    parity claim. Exact canonical icon metaphors, fixture copy, and richer
    data values remain separate content/data decisions.
- Next recommended checkpoint:
  - Pick one exact remaining screenshot mismatch on one route, or make a
    content/data decision before changing canonical copy, icon glyphs,
    route-smoke fixture content, or backend-backed labels.
- Artifacts:
  - `.codex/tasks/PRJ-1255-chat-desktop-persona-overlay-placement.md`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/report.json`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/navigation-proof.json`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/account-proof.json`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/screenshots/`

## Previous Mission

- Mission ID: PRJ-1254-personality-mobile-timeline-rail
- Status: VERIFIED
- Selected objective: make mobile Personality's Mind Layers Timeline read like
  the canonical compact layer rail instead of a tall text list.
- Why this mission now: after Chat desktop belt quieting in `PRJ-1253`, the
  next concrete implemented-screenshot mismatch was mobile Personality's
  hidden timeline track and tall text-list rhythm.
- Release objective or product milestone advanced: v1.2 web Personality
  canonical mobile first-scroll quality.
- First/next checkpoint: completed a CSS-only mobile Personality timeline pass.
  Timeline rows now show token, signal track, and value chip while preserving
  all six layers and backend-backed values.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/personality`
  desktop/tablet/mobile screenshot gate, navigation proof, account proof,
  screenshot review, cleanup check, and `git diff --check`.

## PRJ-1254 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Faraday and completed read-only
  - QA lane delegated to Poincare and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - mobile Personality timeline rows now use compact rail columns, visible
    signal tracks, smaller tokens, and value chips
  - secondary detail copy is hidden only in the mobile rail to reduce first
    scroll height
  - all six layers and values remain visible; desktop/tablet remain stable
- Validation:
  - `npm run build` PASS
  - focused `/personality` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - cleanup found no validation-owned node/Vite, 5173/4173 listener,
    Chromium, or headless browser leftovers; three fresh route-smoke temp
    profiles from this checkpoint were removed
- Residual:
  - This is a verified mobile timeline hierarchy pass, not a full 95% pixel
    parity claim. Exact canonical icon glyphs and richer data values remain
    separate content/data decisions.
- Artifacts:
  - `.codex/tasks/PRJ-1254-personality-mobile-timeline-rail.md`
  - `.codex/artifacts/prj1254-personality-mobile-timeline-rail/report.json`
  - `.codex/artifacts/prj1254-personality-mobile-timeline-rail/navigation-proof.json`
  - `.codex/artifacts/prj1254-personality-mobile-timeline-rail/account-proof.json`
  - `.codex/artifacts/prj1254-personality-mobile-timeline-rail/screenshots/`

## Previous Mission

- Mission ID: PRJ-1253-chat-desktop-cognitive-belt-quieting
- Status: VERIFIED
- Selected objective: make desktop Chat's cognitive belt flatter and visually
  secondary to the transcript/persona stage.
- Why this mission now: after `PRJ-1251` and `PRJ-1252`, Dashboard and
  Personality had fresh mobile hierarchy passes. The UX parity lane identified
  Chat's desktop cognitive belt as the next concrete flagship mismatch left by
  `PRJ-1250`.
- Release objective or product milestone advanced: v1.2 web Chat canonical
  desktop first-read quality.
- First/next checkpoint: completed a CSS-only Chat belt pass. The six context
  items are lower, flatter, less card-heavy, and still preserve all supported
  labels, values, progress, transcript source markers, and mobile rail
  behavior.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/chat` desktop/tablet/mobile
  screenshot gate, `test:chat-transcript`, navigation proof, account proof,
  `git diff --check`, screenshot review, and cleanup check.

## PRJ-1253 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Halley and completed read-only
  - QA lane delegated to Fermat and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - desktop Chat cognitive belt cards now use lower height, lighter material,
    smaller UI typography, quieter meta chips, and a tiny accent marker
  - all belt items, labels, values, progress, transcript source markers, and
    mobile rail behavior remain supported
- Validation:
  - `npm run build` PASS
  - focused `/chat` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - `npm run test:chat-transcript` first hit a CDP `Page.navigate` timeout;
    immediate rerun PASS: `status=ok`, `appSourceCount=2`,
    `telegramSourceCount=2`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no validation-owned node/Vite, 5173/4173 listener, or
    headless browser leftovers; six fresh route-smoke temp profiles from this
    checkpoint were removed
- Residual:
  - This is a verified hierarchy/density pass, not a full 95% pixel parity
    claim. Exact canonical icon metaphors and fixture-copy parity remain
    separate content/data decisions.
- Artifacts:
  - `.codex/tasks/PRJ-1253-chat-desktop-cognitive-belt-quieting.md`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/report.json`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/navigation-proof.json`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/account-proof.json`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/screenshots/`

## Previous Mission

- Mission ID: PRJ-1252-personality-mobile-callout-map-quieting
- Status: VERIFIED
- Selected objective: make mobile Personality hero callouts feel like compact
  embodied-map annotations instead of chunky cards over the figure.
- Why this mission now: after PRJ-1251, Dashboard mobile signals were quieted.
  Fresh Personality screenshots plus the UX parity lane identified mobile
  callout card weight and portrait occlusion as the next smallest high-impact
  canonical mismatch.
- Release objective or product milestone advanced: v1.2 web Personality
  canonical mobile first-read quality.
- First/next checkpoint: completed a CSS-only Personality mobile callout pass.
  Mobile callouts are smaller, lighter, and placed with more portrait
  breathing room; `Planning` no longer wraps; all supported callouts remain
  visible.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  route-smoke fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/personality`
  desktop/tablet/mobile screenshot gate, navigation proof, account proof,
  `git diff --check`, screenshot review, and cleanup check.

## PRJ-1252 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Bacon and completed read-only
  - QA lane delegated to Nash and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - mobile Personality callouts now use smaller width, padding, type, radius,
    material, and shadow so they read as annotations rather than cards
  - lower callouts sit with more figure clearance; `Planning` keeps
    `0 active goals` on one line
  - all supported callouts and backend-backed values remain visible
- Validation:
  - `npm run build` PASS
  - focused `/personality` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no Personality route-smoke, Vite/dev-server, 5173/4173
    listener, or headless browser leftovers; four fresh route-smoke temp
    profiles from this checkpoint were removed
- Residual:
  - This is a verified mobile callout hierarchy pass, not a full 95% pixel
    parity claim. Exact icon/content/copy parity remains a separate
    content/data decision.
- Artifacts:
  - `.codex/tasks/PRJ-1252-personality-mobile-callout-map-quieting.md`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/report.json`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/navigation-proof.json`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/account-proof.json`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/screenshots/`

## Previous Mission

- Mission ID: PRJ-1251-dashboard-mobile-hero-signal-quieting
- Status: VERIFIED
- Selected objective: make mobile Dashboard hero signal cards quieter and make
  count values read as numerals while preserving all supported signals and the
  PRJ-1248 flow rail.
- Why this mission now: after PRJ-1250, Chat metadata was quiet and verified.
  Fresh screenshots plus UX/QA lanes identified mobile Dashboard hero signal
  density and numeral ambiguity as the smallest high-impact UI checkpoint.
- Release objective or product milestone advanced: v1.2 web Dashboard
  canonical mobile first-read quality.
- First/next checkpoint: completed a CSS-only Dashboard signal pass. Dashboard
  signal values now use UI tabular numerals, and mobile hero signal cards keep
  label/value/detail while dropping decorative wave and third-line note noise
  from the first-read card treatment.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  fixture content, or backend-backed labels.
- Parent validation gate: web build, focused `/dashboard`
  desktop/tablet/mobile screenshot gate, full route smoke, navigation proof,
  account proof, `git diff --check`, screenshot review, and cleanup check.

## PRJ-1251 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Locke and completed read-only
  - QA lane delegated to Turing and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - Dashboard signal values now use UI tabular numerals instead of display
    serif styling, so `1` and `0 / 0` read as clear numbers
  - mobile Dashboard signal cards are lighter, shorter, and less decorative;
    all six supported signal cards remain visible
- Validation:
  - `npm run build` PASS
  - focused `/dashboard` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup found no Personality route-smoke, Vite/dev-server, 5173/4173
    listener, temp route-smoke/chat-transcript profile, or headless browser
    leftovers; unrelated Vite processes from `Obiekty` were left untouched
- Residual:
  - This is a verified mobile first-read hierarchy pass, not a full
    pixel-perfect Dashboard parity claim. Exact icon/content/copy parity
    remains a separate content/data decision.
- Artifacts:
  - `.codex/tasks/PRJ-1251-dashboard-mobile-hero-signal-quieting.md`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/report.json`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/navigation-proof.json`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/account-proof.json`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/screenshots/`

## Previous Mission

- Mission ID: PRJ-1250-chat-source-marker-quieting
- Status: VERIFIED
- Selected objective: keep Chat's `App` / `Telegram` transcript source marker
  visible while reducing its visual weight so it reads as quiet metadata, not a
  competing primary accent.
- Why this mission now: PRJ-1249 added the truthful marker, and fresh Chat
  screenshots showed the teal text was useful but a little too loud in the
  dense transcript.
- Release objective or product milestone advanced: v1.2 web Chat
  communication clarity and canonical visual calm.
- First/next checkpoint: completed a CSS-only Chat metadata polish. The source
  marker now renders as a small low-contrast chip inside the existing metadata
  row, with no source mapping, backend, fixture, component-structure, or shared
  shell change.
- Stop conditions: next work should pick one exact route/screenshot mismatch
  or make a content/data decision before changing canonical copy, icon glyphs,
  or backend-backed labels. Live Telegram credential smoke remains outside this
  visual slice.
- Parent validation gate: web build, chat transcript characterization, focused
  `/chat` desktop/tablet/mobile screenshot gate, full route smoke, navigation
  proof, account proof, `git diff --check`, manual screenshot review, and
  validation cleanup.

## PRJ-1250 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Sagan and completed read-only
  - QA lane delegated to Copernicus and completed read-only
  - coordinator implemented the route-local CSS patch and final proof
- Implementation:
  - `.aion-chat-source-marker` now uses a quieter chip treatment with lower
    contrast, smaller type, and light material so the source truth remains
    available without competing with speaker, time, delivery, or message
    content
- Validation:
  - `npm run build` PASS
  - `npm run test:chat-transcript` PASS: `status=ok`,
    `appSourceCount=2`, `telegramSourceCount=2`, `deliveredCount=1`
  - focused `/chat` screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`
  - full route smoke PASS: `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup check found no route-smoke, Vite, or 5173/4173 listener leftovers;
    a transient chat-transcript temp profile lock warning was cleaned with
    targeted temp-directory removal; final Windows cleanup reported two stale
    `chrome-headless-shell` handles with empty command lines and `taskkill`
    reported no running task instance
- Residual:
  - This is a verified visual quieting slice, not a new channel-routing proof
    or a full canonical content/icon parity claim.
- Artifacts:
  - `.codex/tasks/PRJ-1250-chat-source-marker-quieting.md`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/report.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/route-smoke-report.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/navigation-proof.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/account-proof.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/screenshots/`

## Previous Mission

- Mission ID: PRJ-1249-channel-routing-tool-truth-and-source-marker
- Status: VERIFIED
- Selected objective: make Aviary truthful about action-owned web knowledge
  tools and visibly distinguish App/API versus Telegram transcript messages in
  first-party Chat.
- Why this mission now: the user showed a real conversation where Aviary
  denied search/browser capability despite connected action-layer tools, and
  asked that the canonical native/web communicator show whether messages are
  app-native or Telegram-backed without duplicating notifications.
- Release objective or product milestone advanced: v1.2 web/runtime
  communication continuity confidence.
- First/next checkpoint: completed a narrow runtime + web Chat slice. The
  expression guardrail now corrects false search/page-read capability denial
  when foreground awareness has tool hints, transcript projection marks
  Telegram-delivered assistant outreach as `telegram`, and the Chat transcript
  metadata row displays `App` or `Telegram`.
- Stop conditions: live Telegram credential smoke remains out of scope unless
  credentials and a live delivery target are explicitly provided. Do not
  introduce a second chat store, notification fan-out path, or connector
  provider.
- Parent validation gate: focused backend pytest, web build, chat transcript
  characterization, focused `/chat` desktop/tablet/mobile screenshot gate,
  `git diff --check`, and cleanup check.

## PRJ-1249 Current Evidence

- Branch: `main`.
- Lane status:
  - Backend/architecture explorer completed read-only and identified channel
    selection, tool-awareness, Telegram router, and focused test owners
  - Frontend/UX explorer completed read-only and identified the existing
    transcript metadata row as the minimal source-marker surface
  - coordinator implemented and validated the integrated slice
- Implementation:
  - `ExpressionAgent` now distinguishes false tool-capability denial from
    memory/time denial and returns a correction message instead of repeating an
    untrue "no search/browser" claim when `available_tool_hints` are loaded
  - app chat endpoint proof pins app-native messages to `reply.channel == api`
    with no Telegram client call
  - transcript projection now marks assistant rows as `telegram` when the
    delivered action included `send_telegram_message`, including scheduler
    outreach that was actually delivered through Telegram
  - Chat message metadata renders a compact text source marker: `App` or
    `Telegram`
- Validation:
  - focused backend pytest PASS: `7 passed`
  - `npm run build` in `web/` PASS
  - `npm run test:chat-transcript` PASS:
    `status=ok`, `appSourceCount=2`, `telegramSourceCount=2`
  - focused `/chat` screenshot gate PASS: `screenshot_count=3`,
    `failed_count=0`, `status=ok`
  - `git diff --check` PASS with LF/CRLF warnings only
  - cleanup check stopped validation-owned `chrome-headless-shell` leftovers
- Residual:
  - live Telegram credential smoke was not run because this task did not
    activate credentials or a real Telegram target
  - separate Dashboard mobile-flow work exists as PRJ-1248 in the worktree and
    was intentionally not folded into this mission
- Artifacts:
  - `.codex/tasks/PRJ-1249-channel-routing-tool-truth-and-source-marker.md`
  - `.codex/artifacts/prj1249-channel-source-marker/chat-route-report.json`
  - `.codex/artifacts/prj1249-channel-source-marker/screenshots/`

## Previous Mission

- Mission ID: PRJ-1248-dashboard-mobile-flow-rail
- Status: VERIFIED
- Selected objective: compress mobile Dashboard's cognitive-flow stack into a
  compact horizontal rail so lower dashboard data appears sooner.
- Why this mission now: after PRJ-1246, mobile Dashboard still stacked six flow
  steps vertically, making the route feel like a long report before Active
  Goals and the lower panels.
- Release objective or product milestone advanced: v1.2 web mobile Dashboard
  canonical usability.
- First/next checkpoint: completed a CSS-only mobile Dashboard flow pass. All
  flow steps remain available through horizontal scroll with a visible
  next-step peek, and Current Phase remains visible below the rail.
- Stop conditions: next checkpoint should stay screenshot-specific and avoid
  changing route-smoke fixture copy, backend-backed data, icon glyphs, or route
  behavior without a separate content/data decision.
- Parent validation gate: web build, Dashboard desktop/tablet/mobile
  screenshot gate, full route smoke, navigation proof, account proof, visual
  screenshot review, and cleanup check.

## PRJ-1248 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Erdos and completed read-only
  - QA/responsive lane delegated to James and completed read-only
  - coordinator implemented the mobile Dashboard CSS patch and final proof
- Implementation:
  - mobile Dashboard cognitive-flow steps now use a horizontal rail
  - supported flow steps remain available instead of being hidden
  - Current Phase is retained and compacted below the rail
- Validation:
  - `npm run build` PASS
  - Dashboard screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`
  - full route smoke PASS: `route_count=14`, `status=ok`
  - navigation proof PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup check found no validation-owned route-smoke, headless browser, or
    5173/4173 listener leftovers
- Residual:
  - This is a verified mobile flow-density pass, not full pixel-perfect parity.
    Exact canonical icon/content/copy parity is outside this CSS-only slice.
- Artifacts:
  - `.codex/tasks/PRJ-1248-dashboard-mobile-flow-rail.md`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/report.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/route-smoke-report.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/navigation-proof.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/account-proof.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/screenshots/`

## Previous Mission

## PRJ-1246 Current Evidence

- Branch: `main`.
- Summary: mobile Chat first-read compression is verified. The cognitive belt
  is a compact horizontal context rail, supported cards remain available by
  scroll, and transcript/composer content appears sooner.
- Validation: build, Chat desktop/tablet/mobile screenshot gate, full route
  smoke, navigation proof, account proof, cleanup, and `git diff --check`
  passed.

## PRJ-1245 Current Evidence

- Branch: `main`.
- Summary: flagship secondary chrome coherence is verified. Chat's cognitive
  belt cards/meta/progress are flatter, Personality's overview status, side
  panels, and rows are quieter, and Dashboard was intentionally not edited.
- Validation: build, Dashboard/Chat/Personality desktop/tablet/mobile
  screenshot gate, full route smoke, navigation proof, account proof, and
  `git diff --check` passed.

## PRJ-1244 Current Evidence

- Branch: `main`.
- Summary: Personality canonical fidelity is verified. Personality has lighter
  hero/callout material, flatter side panels, tighter timeline rows, calmer
  tablet support rhythm, and less visually dominant mobile callouts/rows.
- Validation: build, Personality desktop/tablet/mobile screenshot gate, full
  route smoke, navigation proof, account proof, and `git diff --check` passed.

## PRJ-1243 Current Evidence

- Branch: `main`.
- Summary: Chat canonical fidelity is verified. Chat hides nonessential
  route-status pills, uses a calmer conversation/persona split, reduces
  transcript/composer weight, renders assistant ordered lists as one calm plan
  surface, and suppresses solo quick-action/portrait-copy chrome.
- Validation: build, Chat desktop/tablet/mobile screenshot gate, full route
  smoke, navigation proof, account proof, and `git diff --check` passed.

## PRJ-1242 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Pasteur and completed read-only
  - QA/responsive lane delegated to McClintock and completed read-only
  - coordinator implemented the route-local Dashboard CSS patch and final proof
- Implementation:
  - desktop Dashboard hero uses a three-part metric/figure/metric composition
  - metric cards have visible connector lines toward the central scene
  - portrait crop was adjusted for the narrower central stage
  - tablet/mobile layout remains structurally unchanged
- Validation:
  - `npm run build` PASS
  - Dashboard screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`
  - full route smoke PASS: `route_count=14`, `status=ok`
  - `npm run audit:ui-navigation` PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
- Residual:
  - This is a verified geometry pass, not full pixel-perfect parity. Static
    reference icon glyphs and metric content are outside this CSS-only slice.
- Artifacts:
  - `.codex/tasks/PRJ-1242-dashboard-hero-geometry.md`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/report.json`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/route-smoke-report.json`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/account-proof.json`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/screenshots/`

## PRJ-1241 Current Evidence

- Branch: `main`.
- Lane status:
  - UX parity lane delegated to Parfit and completed read-only
  - QA/responsive lane delegated to Aristotle and completed read-only
  - coordinator implemented the route-local Dashboard CSS patch and final proof
- Implementation:
  - Dashboard desktop first viewport gives the scenic hero more room and
    reduces overlay/card weight
  - guidance rail rows are lighter and less competitive with the hero
  - cognitive flow is more diagrammatic and less like a heavy control strip
  - lower Reflection card shows a clean visible subset instead of a clipped
    fourth row
- Validation:
  - `npm run build` PASS
  - Dashboard screenshot gate across desktop/tablet/mobile PASS:
    `screenshot_count=3`, `failed_count=0`
  - full route smoke PASS: `route_count=14`, `status=ok`
  - `npm run audit:ui-navigation` PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
- Residual:
  - This is a verified first-viewport lock, not full pixel-perfect parity.
    Remaining Dashboard work should focus on exact hero connector/metric
    geometry.
- Artifacts:
  - `.codex/tasks/PRJ-1241-dashboard-first-viewport-lock.md`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/report.json`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/route-smoke-report.json`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/account-proof.json`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/screenshots/`

## Previous Mission

## PRJ-1240 Current Evidence

- Branch: `main`.
- Lane status:
  - requested read-only implementation lane was run serially because no
    spawn-agent tool was available in the current runtime
  - coordinator integrated the CSS-only patch and final proof
- Implementation:
  - Dashboard hero stage is taller on desktop and metric overlays are narrower,
    lighter, and less competitive with the central figure scene
  - Chat persona panel keeps the v5 stage but reduces overlay/card dominance
    and slightly favors the right persona column without adding a third panel;
    the desktop persona overlay now keeps only the primary focus row visible
    to avoid collision with the portrait label stack
  - Personality callouts and side-panel rows are lighter while preserving the
    embodied-map structure and Aviary branding
- Validation:
  - `npm run build` PASS
  - focused route screenshot gate for `/dashboard`, `/chat`, `/personality`
    across desktop/tablet/mobile PASS: `screenshot_count=9`,
    `failed_count=0`
  - focused Chat overlay cleanup screenshot gate across desktop/tablet/mobile
    PASS: `screenshot_count=3`, `failed_count=0`
  - route smoke PASS: `route_count=14`, `status=ok`
  - `npm run audit:ui-navigation` PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - `git diff --check` PASS with LF/CRLF warning only
  - cleanup check found no route-smoke/Vite node leftovers and no
    `chrome-headless-shell` leftovers
- Residual:
  - This is a verified coherence checkpoint, not a 95% pixel-parity claim.
    Next work should tune exact screenshot mismatches by route, starting with
    Dashboard density or Chat transcript/persona asset fidelity.
- Artifacts:
  - `.codex/tasks/PRJ-1240-flagship-coherence-pass.md`
  - `.codex/artifacts/prj1240-flagship-coherence-pass/report.json`
  - `.codex/artifacts/prj1240-flagship-coherence-pass/account-proof.json`
  - `.codex/artifacts/prj1240-flagship-coherence-pass/screenshots/`
  - `.codex/artifacts/prj1240-chat-overlay-cleanup/report.json`
  - `.codex/artifacts/prj1240-chat-overlay-cleanup/account-proof.json`
  - `.codex/artifacts/prj1240-chat-overlay-cleanup/screenshots/`

## Previous Mission

- Mission ID: PRJ-1239-flagship-canonical-fidelity
- Status: VERIFIED_CHECKPOINT
- Selected objective: answer the user's canonical screenshot feedback by
  moving Dashboard, Chat, and Personality from style-inspired variants toward
  the approved canonical references.
- Why this mission now: the user correctly identified that the PRJ-1238
  screens still looked like different views with similar motifs, not convergent
  canonical screens.
- Release objective or product milestone advanced: v1.2 web UI canonical
  fidelity for the three flagship authenticated surfaces.
- First/next checkpoint: completed first fidelity checkpoint. Chat now starts
  directly from the canonical conversation scene, Dashboard/Personality no
  longer render the extra desktop utility header above the route scene, and
  Personality's overview header is lighter so the embodied map dominates.
- Stop conditions: next checkpoint should focus Dashboard primary-column
  height/right-rail balance before claiming 95% parity; do not rename Aviary to
  AION/Prometheus without product decision.
- Parent validation gate: web build, 3-route desktop/tablet/mobile screenshot
  gate, navigation proof, account proof, screenshot review, and cleanup check.

## PRJ-1239 Current Evidence

- Branch: `main`.
- Lane status:
  - visual parity audit lane delegated to Confucius and completed
  - implementation mapping lane delegated to Aquinas and completed
  - coordinator integrated the first canonical frame/proportion slice
- Implementation:
  - desktop Dashboard, Chat, and Personality no longer render the extra
    `ShellUtilityBar` above the route scene
  - route-stage spacing is collapsed for the three flagship routes so the
    canonical surface starts immediately after the sidebar shell
  - Chat workspace is taller and tighter, with compact cognitive belt cards,
    a closer 60/40 body split, tighter transcript/composer spacing, and smaller
    persona-stage overlays
  - Personality overview bar is demoted from a large card to a quieter header,
    giving the embodied map and side layers stronger first-viewport priority
  - Dashboard desktop first viewport hides the secondary recent-activity panel
    so the hero, flow, lower cards, and right guidance rail no longer create a
    large mid-page void
- Validation:
  - `npm run build` PASS
  - focused route screenshot gate for `/dashboard`, `/chat`, `/personality`
    across desktop/tablet/mobile PASS: `screenshot_count=9`, `failed_count=0`
  - route smoke PASS: `route_count=14`, `status=ok`
  - `npm run audit:ui-navigation` PASS: `step_count=4`, `failed_count=0`
  - account proof PASS: `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - Browser plugin rendered inspection was unavailable through tool discovery;
    route-smoke screenshots are the rendered proof for this checkpoint
- Residual:
  - Dashboard is improved but still needs finer canonical tuning for exact
    card proportions and reference-copy density before a strong 95% parity
    claim.
  - Product branding remains `Aviary`; canonical screenshots containing
    `AION` or `Prometheus` are treated as visual references, not rename
    approvals.
- Artifacts:
  - `.codex/tasks/PRJ-1239-flagship-canonical-fidelity.md`
  - `.codex/artifacts/prj1239-flagship-canonical-fidelity/report.json`
  - `.codex/artifacts/prj1239-flagship-canonical-fidelity/account-proof.json`
  - `.codex/artifacts/prj1239-flagship-canonical-fidelity/screenshots/`

## Previous Mission

- Mission ID: PRJ-1238-shared-shell-noise-reduction
- Status: COMPLETED
- Selected objective: execute the first implementation slice from the
  canonical UI simplification index by reducing shared-shell noise and
  recording route-noise decisions.
- Why this mission now: `PRJ-1237` established the UI index, and the user's
  current priority is less chaos across all views. The shared shell is the
  highest-leverage first slice because every authenticated route inherits it.
- Release objective or product milestone advanced: v1.2 web UI simplification
  on `main`.
- First/next checkpoint: completed. The next mission should run
  `PASS-SETTINGS-TOOLS`, starting with Settings hero chips/card grid or Tools
  summary/provider-plumbing noise.
- Stop conditions: completed for the shell slice. Future route slices must stop
  if a visible element cannot map to the canonical index, validation finds
  route/navigation/account regressions, or deploy/source branch drift makes
  release claims unsafe.
- Parent validation gate: web build, route-smoke syntax/route proof,
  navigation/account proof, representative responsive screenshots, and cleanup
  checks.

## PRJ-1238 Current Evidence

- Branch: `main`.
- Lane status:
  - UX/noise-audit lane delegated to Faraday.
  - Shell review lane delegated to Dirac.
  - Coordinator opened the PRJ-1238 task and started the shared-shell slice.
- Implementation:
  - desktop utility bar now keeps only current route context and account
    disclosure
  - fake search, Focus mode, Quick capture, and notification chrome removed
  - desktop sidebar health card no longer shows the duplicate diagnostics pill
  - mobile route header no longer repeats visible `Workspace` above the route
    title
  - `PASS-NOISE-AUDIT` queue recorded in
    `docs/ux/canonical-ui-layout-index.md`
- Validation:
  - `npm run build` PASS
  - `node --check scripts/route-smoke.mjs` PASS
  - `npm run audit:ui-navigation` PASS, `step_count=4`, `failed_count=0`
  - route smoke `route_count=14`, `status=ok`
  - account proof `step_count=1`, `failed_count=0`, `panel_visible=true`
  - screenshot gate `viewport_count=3`, `screenshot_count=42`,
    `failed_count=0`
  - Browser/IAB proof attempted but runtime bootstrap exited unexpectedly;
    route-smoke screenshots are the rendered proof for this checkpoint
  - validation cleanup stopped route-smoke-owned `chrome-headless-shell`
    processes
- Artifacts:
  - `.codex/tasks/PRJ-1238-shared-shell-noise-reduction.md`

## Previous Mission

- Mission ID: PRJ-1237-canonical-ui-layout-index
- Status: COMPLETED
- Selected objective: turn the user's simplification direction into a
  canonical UI layout index that maps visible groups to backend-supported
  functions and removes permission for unnecessary cards, badges, chips, and
  inert controls.
- Why this mission now: PRJ-1236 is green, but the user correctly identified
  that the web UI now needs a deeper simplification pass rather than more
  single-control polish.
- Release objective or product milestone advanced: v1.2 web UI simplification
  and future native UI generation readiness.
- First/next checkpoint: completed. The next mission should run
  `PASS-NOISE-AUDIT` or `PASS-SHELL` from
  `docs/ux/canonical-ui-layout-index.md`.
- Stop conditions: completed for the planning slice. Future implementation
  must stop if a route requires backend data not currently available or if a
  visual element cannot map to the canonical index.
- Parent validation gate: source inspection of architecture docs, canonical UX
  docs, route manifest, API contracts, and state docs completed for the
  planning artifact; route-local implementation gates remain for later tasks.

## PRJ-1237 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status:
  - Architecture/data mapping lane delegated to James, timed out, then closed.
  - UX/reference simplification lane delegated to Newton and integrated.
  - Coordinator completed the canonical UI layout index.
- Implementation:
  - `docs/ux/canonical-ui-layout-index.md` added with data authority, shell
    zones, component budget, route group IDs, first-read hierarchy, noise
    taxonomy, allowed group types, simplification order, implementation
    ownership map, and future acceptance gate.
- Validation:
  - canonical UX source set and recent proof paths reviewed
  - UX/reference lane report integrated
  - no production code rewrite started before the planning artifact
  - no backend contract invented beyond known app API data sources
- Artifacts:
  - `docs/ux/canonical-ui-layout-index.md`

## Previous Mission

- Mission ID: PRJ-1236-settings-auth-accessibility-polish
- Status: COMPLETED
- Selected objective: close the next small accessibility/interaction gap after
  PRJ-1235 by aligning auth modal mode controls and Settings form controls with
  their real behavior and accessible names.
- Why this mission now: PRJ-1235 is green, and the strongest remaining
  evidence-backed gap is not another visual redesign but incomplete auth modal
  tab semantics and under-named Settings controls.
- Release objective or product milestone advanced: local v1.2 web
  release-candidate confidence.
- First/next checkpoint: local PRJ-1236 auth/Settings accessibility polish is
  complete. The next checkpoint should tackle the Tools provider-plumbing
  first-read as a separate route-local slice.
- Stop conditions: completed. Do not reopen unless a new screenshot, keyboard,
  or route-smoke proof identifies a regression.
- Parent validation gate: `node --check scripts/route-smoke.mjs`,
  `npm run build`, route smoke for 14 routes, full screenshot gate for all 14
  routes across desktop/tablet/mobile with zero UI failures, navigation proof,
  account proof, manual Login/Auth and Settings screenshot review, and cleanup
  checks.

## PRJ-1236 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status:
  - A11y residual audit lane completed by Planck.
  - UX residual screenshot audit lane completed by Nietzsche.
  - Coordinator integrated the safe auth/Settings slice.
- Implementation:
  - auth mode controls now use segmented button semantics with `aria-pressed`
    instead of an incomplete tablist pattern
  - auth modal focuses the email field on open, traps Tab/Shift+Tab inside the
    dialog, closes on Escape, and attempts focus restore to the opener
  - Settings editable controls have explicit accessible names
  - Settings copy uses calmer product language: `Personalize Aviary`,
    `App language`, `Local time`, and labelled proactive state chips
  - desktop diagnostics support text is non-interactive status copy
  - mobile auth backdrop is slightly stronger so the modal remains primary
- Validation:
  - `node --check scripts/route-smoke.mjs` PASS
  - `npm run build` PASS
  - route smoke `route_count=14`, `status=ok`
  - full responsive screenshot gate `viewport_count=3`,
    `screenshot_count=42`, `failed_count=0`
  - navigation proof `step_count=4`, `failed_count=0`
  - account proof `step_count=1`, `failed_count=0`, `panel_visible=true`
  - manual review covered mobile Login, mobile Settings, desktop Settings, and
    desktop Dashboard
  - In-app Browser proof was attempted but blocked by no active Codex browser
    pane; route-smoke screenshots and static self-review are the current proof
  - cleanup check stopped validation-owned Vite preview process trees and found
    no remaining PRJ-1236 browser/dev-server leftovers
- Artifacts:
  - `.codex/artifacts/prj1236-settings-auth-accessibility-polish/`

## Previous Mission

- Mission ID: PRJ-1235-mobile-shell-first-viewport-polish
- Status: COMPLETED
- Selected objective: compact the authenticated mobile shell so every route
  keeps one header and one navigation while giving more first-viewport space to
  the actual product surface.
- Why this mission now: PRJ-1234 is green, and the clearest remaining
  cross-route improvement visible in screenshots is shared mobile chrome
  density rather than another route-local decoration pass.
- Release objective or product milestone advanced: local v1.2 web
  mobile-transfer confidence.
- First/next checkpoint: local PRJ-1235 mobile-shell polish is complete. The
  next checkpoint should either promote a v1.2 release candidate or take the
  next evidence-backed UX item, such as Settings control naming or auth-modal
  tab semantics.
- Stop conditions: completed. Do not reopen unless a new screenshot, keyboard,
  or route-smoke proof identifies a regression.
- Parent validation gate: `node --check scripts/route-smoke.mjs`,
  `npm run build`, route smoke for 14 routes, full screenshot gate for all 14
  routes across desktop/tablet/mobile with zero UI failures, navigation proof,
  account proof, manual mobile screenshot review, and cleanup checks.

## PRJ-1235 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status:
  - UX residual audit lane completed by Meitner.
  - Code/a11y residual audit lane completed by Euclid.
  - Coordinator integrated shared-shell, CSS, and script changes.
- Implementation:
  - mobile authenticated route header and route rail are more compact
  - module stat values use UI numeric typography
  - desktop sidebar support cards are quieter
  - desktop utility search/action chips no longer expose inert fake buttons
  - account triggers use disclosure semantics instead of `aria-haspopup="dialog"`
  - `npm run audit:ui-responsive:full` captures the current 14-route gate
- Validation:
  - `node --check scripts/route-smoke.mjs` PASS
  - `npm run build` PASS
  - route smoke `route_count=14`, `status=ok`
  - full responsive screenshot gate `viewport_count=3`,
    `screenshot_count=42`, `failed_count=0`
  - navigation proof `step_count=4`, `failed_count=0`
  - account proof `step_count=1`, `failed_count=0`, `panel_visible=true`
  - manual review covered mobile Dashboard, Tools, Settings, and desktop
    Dashboard
  - cleanup check stopped the validation-owned Vite preview process tree and
    found no remaining PRJ-1235 browser/dev-server leftovers
- Artifacts:
  - `.codex/artifacts/prj1235-mobile-shell-first-viewport-polish/`

## Previous Mission

- Mission ID: PRJ-1234-v12-flagship-last-mile-polish
- Status: COMPLETED
- Selected objective: close the final flagship canonical-detail pass for
  Dashboard, Chat, Personality, and shared shell so the v1.2 web app feels
  polished enough to be a credible mobile-app foundation and daily personality
  companion.
- Why this mission now: PRJ-1233 is green, but the repository still has a
  dedicated last-mile checklist for structural rhythm, crop/atmosphere, and
  final proof on the strongest reference-driven surfaces.
- Release objective or product milestone advanced: local v1.2 web UX
  release-candidate confidence.
- First/next checkpoint: local v1.2 flagship last-mile checkpoint is complete.
  Next mission should either prepare a v1.2 release candidate promotion or run
  a product-decision pass for mobile Chat/Personality parity choices that were
  intentionally not forced in this CSS slice.
- Stop conditions: canonical references conflict with accepted user notes; a
  view needs product behavior instead of CSS/semantics polish; responsive smoke
  reports overflow/clipping; a change would require backend, API, database,
  runtime, or production deployment work.
- Parent validation gate: `node --check scripts/route-smoke.mjs`,
  `npm run build`, route smoke for 14 routes, full screenshot gate for all 14
  routes across desktop/tablet/mobile with zero UI failures, navigation proof,
  account proof, manual screenshot review of touched flagship routes, and
  cleanup checks.

## PRJ-1234 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status:
  - UX gap, design-system, and QA/Test lanes completed read-only.
  - Coordinator integrated the safe CSS/accessibility slice and final gate.
- Implementation:
  - desktop utility chrome is lighter and less admin-like
  - Chat stage and portrait support panel spacing/elevation are calmer
  - Dashboard guidance hierarchy and wide-screen side-column pacing are tighter
  - mobile Personality restores learned-knowledge as a compact map callout
  - Personality side-stack hierarchy now emphasizes conscious state and quiets
    recent activity
  - route/account/disclosure accessibility semantics were improved
  - `--aion-display` now aliases the existing display font token
- Validation:
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - route smoke -> `route_count=14`, `status=ok`
  - full responsive screenshot gate -> `viewport_count=3`,
    `screenshot_count=42`, `failed_count=0`
  - navigation proof -> `step_count=4`, `failed_count=0`
  - account proof -> `step_count=1`, `failed_count=0`, `panel_visible=true`
  - `git diff --check` -> PASS with LF/CRLF warnings only
  - cleanup checks -> no `chrome-headless-shell`, no route-smoke/dev-server
    process, and no listeners on `5173` or `4173`
- Artifacts:
  - `.codex/artifacts/prj1234-flagship-last-mile-polish/route-smoke-report.json`
  - `.codex/artifacts/prj1234-flagship-last-mile-polish/screenshot-gate-report.json`
  - `.codex/artifacts/prj1234-flagship-last-mile-polish/navigation-proof-report.json`
  - `.codex/artifacts/prj1234-flagship-last-mile-polish/account-proof-report.json`
  - `.codex/artifacts/prj1234-flagship-last-mile-polish/screenshots/`

## PRJ-1234 Result

- Final verdict: DONE for the local v1.2 flagship last-mile UX checkpoint.
- Release caveat: this is a verified local web branch checkpoint, not a
  production v1.2 release. Production release requires a separate candidate
  promotion mission with deploy parity and production smoke.

## Previous Mission

- Mission ID: PRJ-1233-v12-web-beauty-polish-pass
- Status: COMPLETED
- Selected objective: continue past the verified v1.2 web foundation into a
  full visual polish pass so Home, Chat, Personality, Dashboard, and every
  authenticated module route feel simple, beautiful, coherent, and ready to
  inform the future mobile app.
- Why this mission now: the user explicitly asked the coordinator team to keep
  working until all web views are wonderful on mobile and desktop, using the
  strongest reference screens as the quality bar rather than stopping at smoke
  correctness.
- Release objective or product milestone advanced: v1.2 web visual readiness
  and mobile-transfer baseline.
- First/next checkpoint: v1.2 web beauty polish checkpoint is complete on the
  working branch. Next mission should either prepare a v1.2 release candidate
  or run a narrower taste pass only if new screenshots/user notes identify a
  specific remaining surface.
- Stop conditions: canonical images conflict with accepted user notes; a view
  needs product behavior instead of visual polish; responsive smoke reports
  overflow/clipping; a change would require route architecture or backend
  contract changes.
- Parent validation gate: `node --check scripts/route-smoke.mjs`,
  `npm run build`, route smoke, full screenshot gate for all 14 routes across
  desktop/tablet/mobile with zero UI failures, navigation proof, account
  proof, visual screenshot review, and cleanup checks.

## PRJ-1233 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status: UX spec, flagship frontend, module-surface, and QA visual gate
  lanes completed and integrated into
  `.codex/tasks/PRJ-1233-v12-web-beauty-polish-pass.md`.
- Implementation:
  - mobile Chat now reduces pre-thread cognitive cards so the transcript
    appears sooner
  - mobile Home hides duplicated hero micro-proof chips while preserving the
    scenic hero, CTAs, callouts, feature bridge, and trust closure
  - mobile Personality reduces figure-covering callouts
  - tablet/mobile Chat persona notes are quieter
  - module routes use compact mobile stat rows, bringing unique route content
    higher in the first scroll
  - Tools mobile summary/detail density is reduced
  - Automations/Integrations desktop scenic whitespace is tightened
  - all module routes are included in the route-manifest screenshot contract
- Validation:
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - route smoke -> `route_count=14`, `status=ok`
  - full responsive screenshot gate -> `viewport_count=3`,
    `screenshot_count=42`, `failed_count=0`
  - navigation proof -> `step_count=4`, `failed_count=0`
  - account proof -> `step_count=1`, `failed_count=0`
  - screenshot review covered mobile Home, Chat, Personality, Memory, Tools,
    and desktop Chat/Integrations.
- Artifacts:
  - `.codex/artifacts/prj1233-web-ui-polish-pass/route-smoke-report.json`
  - `.codex/artifacts/prj1233-web-ui-polish-pass/screenshot-gate-report.json`
  - `.codex/artifacts/prj1233-web-ui-polish-pass/navigation-proof-report.json`
  - `.codex/artifacts/prj1233-web-ui-polish-pass/account-proof-report.json`
  - `.codex/artifacts/prj1233-web-ui-polish-pass/screenshots/`

## PRJ-1233 Result

- Final verdict: DONE for the local v1.2 web beauty polish checkpoint.
- Release caveat: this is a verified local web branch checkpoint, not a
  production v1.2 release. Production release requires a separate candidate
  promotion mission with deploy parity and production smoke.

## Previous Mission

- Mission ID: PRJ-1232-v12-web-canonical-ui-system
- Status: COMPLETED
- Selected objective: build v1.2 web UI toward the canonical documentation
  references across mobile and desktop, using the web implementation as the
  foundation for the future mobile app. The work must be functional,
  polished, and free of unnecessary decorative or explanatory clutter.
- Why this mission now: v1.1.1 is released; the user explicitly requested v1.2
  frontend improvement with agent coordination, canonical images from docs,
  and all web views supervised across mobile and desktop.
- Release objective or product milestone advanced: v1.2 canonical web UI
  baseline for future native/mobile app transfer.
- First/next checkpoint: v1.2 web canonical UI checkpoints are complete on the
  working branch. Next mission should either prepare a v1.2 release candidate
  or perform a narrower visual taste pass from fresh screenshot review.
- Stop conditions: canonical references conflict; a route lacks enough spec to
  claim parity; validation cannot capture desktop/mobile screenshots; broad
  refactor risk exceeds the first batch; production v1.1.1 marker would be
  disturbed.
- Parent validation gate: per batch `npm run build`,
  `npm run audit:ui-responsive`, `npm run audit:ui-navigation`,
  route/account smoke where relevant, visual screenshot comparison against
  canonical assets, and cleanup checks for browser/dev-server leftovers.

## PRJ-1232 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status: UX spec, frontend architecture, and QA visual-gate explorer
  lanes completed and integrated into
  `.codex/tasks/PRJ-1232-v12-web-canonical-ui-system.md`.
- Foundation implementation:
  - added `web/src/route-manifest.json` as the shared route/marker source for
    web route contracts and smoke proof
  - derived `ROUTES` and route markers from the manifest in `web/src/routes.ts`
  - updated `web/scripts/route-smoke.mjs` to consume the same manifest and to
    use manifest markers for navigation/account proof
  - improved mobile Chat by replacing the narrow-screen clipped context belt
    with stacked, readable context cards
  - refined route-smoke overflow detection so contained intentional scrollers
    do not mask or misreport document-level overflow checks
  - removed transform scaling from the public landing scenic background so
    `/` and `/login` no longer report decorative out-of-viewport elements
- Validation:
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - route smoke -> `route_count=14`, `status=ok`
  - responsive screenshots -> `screenshot_count=18`, `failed_count=0`
  - mobile foundation screenshots for `/chat`, `/settings`, `/dashboard` ->
    `failed_count=0`, `overflowingElementCount=0`
  - navigation proof -> `step_count=4`, `failed_count=0`
  - account proof -> `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - public Home/Login gate -> `screenshot_count=4`, `failed_count=0`,
    `overflowingElementCount=0` across desktop/mobile `/` and `/login`
  - Shell/Dashboard batch disambiguated mobile/tablet Dashboard labels from
    public Home and tightened desktop Dashboard density; focused gate
    `screenshot_count=3`, `failed_count=0`.
  - Chat batch lightened the desktop cognitive belt; focused gate
    `screenshot_count=3`, `failed_count=0`.
  - Personality batch improved desktop/mobile hero rhythm and compact mobile
    overview status; focused gate `screenshot_count=3`, `failed_count=0`.
  - Final responsive gate covered public, flagship, and module routes:
    `screenshot_count=39`, `failed_count=0`.
- Artifacts:
  - `.codex/artifacts/prj1232-route-smoke/report.json`
  - `.codex/artifacts/prj1232-web-responsive-visual-gate/report.json`
  - `.codex/artifacts/prj1232-mobile-foundation-gate/report.json`
  - `.codex/artifacts/prj1232-navigation-proof/report.json`
  - `.codex/artifacts/prj1232-account-proof/report.json`
  - `.codex/artifacts/prj1232-public-home-gate/report.json`
  - `.codex/artifacts/prj1232-dashboard-shell-gate/report.json`
  - `.codex/artifacts/prj1232-chat-belt-gate/report.json`
  - `.codex/artifacts/prj1232-personality-hero-gate/report.json`
  - `.codex/artifacts/prj1232-final-route-smoke/report.json`
  - `.codex/artifacts/prj1232-final-responsive-gate/report.json`

## PRJ-1232 Result

- Final verdict: DONE for the v1.2 web/mobile foundation checkpoints.
- Release caveat: this is a verified web branch checkpoint, not a production
  v1.2 release. Production release requires a separate candidate promotion
  mission with deploy parity and release smoke.
- Residual non-blocking note: exact pixel-perfect parity is not claimed for
  every canonical reference; future refinements should be taste/precision
  passes, not blockers for the functional responsive web foundation.

## Previous Mission

- Mission ID: PRJ-1231-v1-production-candidate-promotion
- Status: COMPLETED
- Selected objective: turn locally verified selected-scope v1 into a real
  production-backed release fact by committing the refreshed candidate,
  publishing it to the deploy source, proving deployed revision parity, running
  production release smoke, and recording the final marker posture.
- Why this mission now: the user asked the coordinator to keep working until
  v1 is fact, and PRJ-1230 proved only local selected-scope readiness. The
  release boundary requires deploy parity and production smoke before any new
  release claim.
- Release objective or product milestone advanced: production-backed v1
  selected-scope marker for the current web-supported candidate.
- First/next checkpoint: v1 selected-scope is released as `v1.1.1`; next work
  should either monitor production or explicitly expand deferred extension
  scope.
- Stop conditions: git push is unavailable; deploy target/source branch cannot
  be confirmed; Coolify webhook/auto-deploy access is unavailable and
  production remains on an older SHA; release smoke fails; backend/web revision
  parity drifts; tag creation would point at an unproven SHA.
- Parent validation gate: completed. Local PRJ-1230 gate remained green;
  pre-push `git diff --check` passed; production release smoke with deploy
  parity passed; release reality audit returned `GO_FOR_SELECTED_SHA`;
  selected-tag go/no-go for `v1.1.1` returned `GO`.

## PRJ-1231 Release Result

- Selected SHA: `df677370f63d2688eb792f9a3a846d2cd40a564b`
- Release tag: `v1.1.1`
- Deploy source: `origin/main`
- Production URL: `https://aviary.luckysparrow.ch`
- Production proof: backend runtime revision and web shell build revision both
  match selected SHA; `release_ready=true`; no release violations; v1 final
  acceptance state `core_v1_bundle_ready`.
- Final verdict: `released`

## Previous Mission

- Mission ID: PRJ-1230-v1-selected-scope-final-readiness-refresh
- Status: COMPLETED
- Selected objective: refresh the selected-scope v1 readiness claim against the
  current workspace, coordinate lane findings, run the parent validation gate,
  and record whether v1 remains `verified`, `partially verified`, or `blocked`.
- Why this mission now: the user asked the coordinator to finish v1 using
  agents; the existing dashboard says selected-scope readiness is `11/11`, but
  the dated evidence is from 2026-05-14 and must not be silently reused for the
  current branch.
- Release objective or product milestone advanced: selected-scope v1 closure
  / web-supported release confidence.
- First/next checkpoint: selected-scope v1 local readiness is refreshed; next
  checkpoint is production candidate promotion only if a deploy target is
  selected.
- Stop conditions: a P0/P1 selected-scope blocker appears; architecture and
  implementation conflict; parent validation fails in a way that requires a
  product or deployment decision; production release parity is requested but
  target credentials/environment are unavailable.
- Parent validation gate: `git diff --check`; full backend pytest; web
  typecheck/build/responsive audit/navigation audit/route smoke; architecture
  dashboard refresh. Production release smoke is required only if this mission
  selects a new deployable release candidate.

## Source Rows

- Task board: latest completed UI slice `PRJ-1229`; next residual Dashboard
  lower-card proportions / first-viewport density.
- Planning: `docs/planning/current-v1-release-boundary.md`;
  `docs/planning/next-iteration-plan.md`.
- Delivery map: selected-scope v1 web-supported closure; native and provider
  extensions remain deferred unless scope is reactivated.
- Requirements: `REQ-UX-001`, `REQ-MOB-001`, `REQ-AI-001..003`.
- Quality scenarios: web route rendering and release readiness gates.
- Risks: deferred provider activation, proactive target sample, deploy
  automation convergence, and native mobile proof are nonblocking selected
  scope rows.
- Module confidence: `AVIARY-WEB-RESP-001`, `AVIARY-STATUS-001`,
  `AVIARY-COGNITIVE-RUNTIME-001`, `AVIARY-MEMORY-001`.
- System health: latest dated evidence from 2026-05-14 needs refresh if this
  branch becomes the active v1 closure basis.
- Architecture / UX / security / ops sources:
  `docs/operations/project-status-dashboard.md`,
  `docs/operations/v1-selected-scope-handoff-2026-05-11.md`,
  `docs/ux/screen-quality-checklist.md`, `docs/ux/design-memory.md`,
  `docs/operations/runtime-ops-runbook.md`.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Output | Validation/proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, mission control, project memory, state files | Integration, task closure, source-of-truth updates | Mission packet, task contract, final readiness decision | Parent validation gate | COMPLETED |
| Product/Requirements | Coordinator | Current v1 boundary, requirements matrix | Scope, accepted assumptions, exclusions | Selected-scope definition and deferred extension list | Requirements trace review | COMPLETED |
| Architecture | Coordinator | Project status dashboard, architecture audit | Architecture readiness posture | Alignment or mismatch note | Dashboard refresh | COMPLETED |
| Frontend/UX | UX explorer, then coordinator | UX refs, screenshots, web route files | Dashboard lower-row density refresh and route-smoke harness hardening | Web audit/screenshot proof | COMPLETED |
| Backend/API | Coordinator | Runtime confidence rows, backend tests | No backend code planned | Runtime gate status | Full backend pytest | COMPLETED |
| QA/Test | QA explorer, then coordinator | Known issues, system health, module confidence | Read-only gate report | Parent validation command set and blocker posture | Integrated into task evidence | COMPLETED |
| Security/Ops/Docs | Coordinator | Release boundary, ops runbook, security protocol | Release/ops evidence notes and state updates | Candidate versus non-candidate release posture | Smoke/deploy risk note | COMPLETED |
| Documentation/Memory | Coordinator | Task board, project state, ledgers | Active mission, PRJ-1230 task, state summaries | Durable handoff and next checkpoint | Source-of-truth diff review | COMPLETED |

## Delegation Plan

- Lanes kept local: coordination, final integration, shared state updates,
  parent validation, final `DONE`/blocked decision.
- Lanes delegated: QA/Release read-only blocker/gate report; Frontend/UX
  read-only next-slice report.
- Lanes intentionally omitted and why: Data/Migrations, Security deep review,
  and provider Ops smoke are omitted unless validation discovers a selected
  scope change; no schema, secrets, auth, permissions, or provider execution
  change is planned.
- Known overlap risks: avoid editing `.codex/context/PROJECT_STATE.md` over
  existing user governance additions; keep subagents read-only unless a later
  lane is explicitly given a disjoint write set.
- Forbidden files or surfaces: no provider credential activation, no native
  mobile proof work, no new web shell, no architecture rewrite, no temporary
  bypasses.

## Acceptance

- [x] Every important responsibility from source docs has an owner or explicit omission.
- [x] No two write lanes own the same file or shared registry.
- [x] Each lane has expected output and validation/proof.
- [x] Parent validation will run after accepted lane integration.
- [x] Missing or unclear ownership will be recorded in `.agents/state/responsibility-learning.md`.
- [x] Process quality will be evaluated in `.agents/state/agent-evals.md` when
      this mission is broad, repeated, partial, or subagent-heavy.

## Checkpoint Log

| Date | Checkpoint | Result | Evidence | Next action |
| --- | --- | --- | --- | --- |
| 2026-05-22 | Mission opened | Multi-lane coordinator mission created after user asked to finish v1 with agents. | Active mission packet; QA/Release and UX read-only lanes delegated. | Create task contract and run/record parent gate. |
| 2026-05-22 | Lane integration | QA confirmed no selected-scope blockers and UX identified Dashboard lower-row density as the smallest polish slice. | Subagent lane reports; PRJ-1230 task contract. | Patch the focused web slice and harden route-smoke fallback. |
| 2026-05-22 | Parent validation | COMPLETED: selected-scope v1 remains locally verified for this branch. | `git diff --check` PASS with LF/CRLF warnings only; backend `1105 passed`; web build/responsive/navigation/account/route smoke PASS; architecture dashboard `11/11`; screenshot review; cleanup no leftovers. | Promote only after explicit production deploy target/parity smoke. |
