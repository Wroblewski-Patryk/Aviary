import { createServer } from "node:http";
import { spawn } from "node:child_process";
import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, extname, join, normalize, resolve } from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const REPO_ROOT = resolve(ROOT, "..");
const DIST = join(ROOT, "dist");
const INDEX = join(DIST, "index.html");
const require = createRequire(import.meta.url);

const args = process.argv.slice(2);
const routeManifest = JSON.parse(readFileSync(join(ROOT, "src", "route-manifest.json"), "utf8"));

const ROUTES = routeManifest.routes.map((route) => ({
  path: route.path,
  marker: route.marker,
  authenticated: Boolean(route.authenticated),
  screenshot: Boolean(route.screenshot),
  canonicalSurface: route.canonicalSurface ?? "",
}));
const ROUTES_BY_PATH = new Map(ROUTES.map((route) => [route.path, route]));

function routeByPath(path) {
  const route = ROUTES_BY_PATH.get(path);
  if (!route) {
    throw new Error(`Route manifest is missing '${path}'.`);
  }
  return route;
}

const MIME_TYPES = {
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".webp": "image/webp",
};

const RESPONSIVE_VIEWPORTS = {
  desktop: { width: 1440, height: 960 },
  tablet: { width: 1024, height: 900 },
  mobile: { width: 390, height: 844 },
};

function optionValue(name) {
  const index = args.indexOf(name);
  if (index === -1) {
    return "";
  }
  return args[index + 1] ?? "";
}

function listOption(name) {
  const raw = optionValue(name);
  if (!raw) {
    return [];
  }
  return raw
    .split(",")
    .map((value) => value.trim())
    .filter(Boolean);
}

function routeSlug(routePath) {
  if (routePath === "/") {
    return "home";
  }
  return routePath.replace(/^\//, "").replace(/[^a-z0-9-]+/gi, "-");
}

function resolveArtifactPath(value) {
  if (!value) {
    return "";
  }
  return resolve(REPO_ROOT, value);
}

const screenshotDir = resolveArtifactPath(optionValue("--screenshots"));
const reportPath = resolveArtifactPath(optionValue("--report"));
const requestedScreenshotRoutes = new Set(listOption("--screenshot-routes"));
const requestedViewportNames = listOption("--viewports");
const screenshotViewportNames =
  requestedViewportNames.length > 0 ? requestedViewportNames : Object.keys(RESPONSIVE_VIEWPORTS);
const failOnUiFindings = args.includes("--fail-on-ui-findings");
const navigationProofEnabled = args.includes("--navigation-proof");
const accountProofEnabled = args.includes("--account-proof");
let lastDocumentRoutePath = "/";
let activeFallbackAuthenticatedRoute = false;

function jsonResponse(response, status, payload) {
  const body = JSON.stringify(payload);
  response.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Content-Length": Buffer.byteLength(body),
  });
  response.end(body);
}

function mockApi(request, response) {
  const url = new URL(request.url ?? "/", "http://127.0.0.1");
  const referer = request.headers.referer ?? "";
  const refererPath = (() => {
    try {
      return referer ? new URL(referer).pathname : "";
    } catch {
      return "";
    }
  })();
  const routeSmokeAuthenticated = (() => {
    try {
      return referer ? new URL(referer).searchParams.get("route_smoke_auth") === "1" : false;
    } catch {
      return false;
    }
  })();
  const documentRoutePath = refererPath && refererPath !== "/" ? refererPath : lastDocumentRoutePath;
  const isLoginRoute =
    !activeFallbackAuthenticatedRoute &&
    !routeSmokeAuthenticated &&
    (documentRoutePath === "/" || documentRoutePath === "/login");

  if (request.method === "GET" && url.pathname === "/app/me") {
    if (isLoginRoute) {
      jsonResponse(response, 401, { detail: "Unauthenticated route smoke." });
      return true;
    }
    jsonResponse(response, 200, {
      user: {
        id: "route-smoke-user",
        email: "route-smoke@example.com",
        display_name: "Route Smoke",
      },
      settings: {
        preferred_language: "en",
        ui_language: "en",
        utc_offset: "UTC+00:00",
        proactive_opt_in: true,
      },
    });
    return true;
  }

  if (request.method === "GET" && url.pathname === "/app/chat/history") {
    jsonResponse(response, 200, {
      items: [
        {
          message_id: "route-smoke:user",
          event_id: "route-smoke",
          role: "user",
          text: "Route smoke user turn",
          channel: "api",
          timestamp: "2026-05-03T12:00:00.000Z",
          metadata: null,
        },
        {
          message_id: "route-smoke:assistant",
          event_id: "route-smoke",
          role: "assistant",
          text: [
            "Here is a complete plan that should stay readable in the chat surface:",
            "",
            "1. Define the outcome: Clarify what the user wants to achieve before choosing the next action.",
            "   Keep the continuation inside the first numbered card instead of dropping it into a loose paragraph.",
            "2. Connect the context: Use memory, active goals, and recent chat turns as input for the response.",
            "3. Finish the answer: Close the list with a concrete next step so the transcript does not feel cut off.",
          ].join("\n"),
          channel: "api",
          timestamp: "2026-05-03T12:00:02.000Z",
          metadata: { language: "en" },
        },
      ],
    });
    return true;
  }

  if (request.method === "GET" && url.pathname === "/app/personality/overview") {
    jsonResponse(response, 200, {
      user_id: "route-smoke-user",
      recent_activity: [
        {
          event_id: "route-smoke-activity",
          title: "Route smoke activity",
          timestamp: "2026-05-03T12:00:00Z",
          source: "api",
          importance: 0.72,
        },
      ],
      identity_state: {
        profile: { preferred_language: "en" },
        preference_summary: { learned_preference_count: 1 },
      },
      learned_knowledge: {
        knowledge_summary: {
          semantic_conclusion_count: 1,
          affective_conclusion_count: 1,
        },
      },
      planning_state: {
        active_goals: [],
        active_tasks: [],
        pending_proposals: [],
        continuity_summary: {
          active_goal_count: 0,
          active_task_count: 0,
          blocked_task_count: 0,
          active_milestone_count: 0,
          pending_proposal_count: 0,
          primary_goal_names: [],
          primary_task_names: [],
        },
      },
      role_skill_state: {
        selection_visibility_summary: {
          catalog_skill_count: 5,
          runtime_selection_surface: "available",
        },
      },
      capability_catalog: {
        tool_and_connector_posture: {
          organizer_stack_state: "provider_credentials_missing",
          selectable_tool_families: ["calendar", "task_system", "cloud_drive"],
        },
      },
      api_readiness: {
        product_stage: "route_smoke",
        internal_inspection_path: "available",
      },
    });
    return true;
  }

  if (request.method === "GET" && url.pathname === "/app/tools/overview") {
    jsonResponse(response, 200, {
      policy_owner: "app_tools_overview_contract",
      user_id: "route-smoke-user",
      group_order: ["communication", "task_management"],
      summary: {
        total_groups: 2,
        total_items: 2,
        integral_enabled_count: 1,
        provider_ready_count: 1,
        provider_blocked_count: 1,
        link_required_count: 1,
        planned_placeholder_count: 0,
      },
      groups: [
        {
          id: "communication",
          title: "Communication",
          description: "Route smoke communication tools.",
          item_count: 1,
          items: [
            {
              id: "internal_chat",
              label: "Internal chat",
              category: "communication",
              kind: "channel",
              description: "Built-in chat channel.",
              status: "integral_active",
              status_reason: "Available inside the product shell.",
              enabled: true,
              integral: true,
              provider: { name: "internal", ready: true, configured: true },
              user_control: { toggle_allowed: false, preference_supported: false, requested_enabled: null },
              link_required: false,
              link_state: "not_required",
              capabilities: ["chat"],
              skill_tool_bindings: [],
              next_actions: [],
              source_of_truth: ["app_tools_overview_contract"],
            },
          ],
        },
        {
          id: "task_management",
          title: "Task management",
          description: "Route smoke task tools.",
          item_count: 1,
          items: [
            {
              id: "clickup",
              label: "ClickUp",
              category: "task_management",
              kind: "provider",
              description: "Task provider readiness row.",
              status: "provider_blocked",
              status_reason: "Provider credentials are not configured in route smoke.",
              enabled: false,
              integral: false,
              provider: { name: "clickup", ready: false, configured: false },
              user_control: { toggle_allowed: true, preference_supported: true, requested_enabled: false },
              link_required: false,
              link_state: "not_required",
              capabilities: ["create_task", "list_tasks"],
              skill_tool_bindings: [
                {
                  skill_id: "clickup_task_management",
                  label: "ClickUp task management",
                  posture: "confirmation_required_for_mutation",
                  allowed_operations: ["list_tasks", "create_task", "update_task"],
                  execution_owner: "action",
                  authority: "metadata_only",
                },
              ],
              next_actions: ["configure_provider_credentials"],
              source_of_truth: ["connector_execution_baseline"],
            },
          ],
        },
      ],
    });
    return true;
  }

  if (request.method === "GET" && url.pathname === "/health") {
    jsonResponse(response, 200, {
      status: "ok",
      conversation_channels: {
        telegram: {
          round_trip_ready: false,
          round_trip_state: "route_smoke",
        },
      },
      attention: {
        pending: 0,
        claimed: 0,
        answered: 0,
      },
      proactive: {
        scheduler_tick_summary: {},
      },
    });
    return true;
  }

  return false;
}

function serveStatic(request, response) {
  const url = new URL(request.url ?? "/", "http://127.0.0.1");
  let filePath = normalize(join(DIST, decodeURIComponent(url.pathname)));
  if (!filePath.startsWith(DIST)) {
    response.writeHead(403);
    response.end("Forbidden");
    return;
  }
  if (url.pathname === "/" || !existsSync(filePath)) {
    filePath = INDEX;
    lastDocumentRoutePath = url.pathname;
  }
  const body = readFileSync(filePath);
  const contentType = MIME_TYPES[extname(filePath)] ?? "application/octet-stream";
  response.writeHead(200, {
    "Content-Type": contentType,
    "Content-Length": body.length,
  });
  response.end(body);
}

function startServer() {
  const server = createServer((request, response) => {
    if (mockApi(request, response)) {
      return;
    }
    serveStatic(request, response);
  });
  return new Promise((resolveServer) => {
    server.listen(0, "127.0.0.1", () => resolveServer(server));
  });
}

function chromePath() {
  const configured = process.env.CHROME_PATH;
  const localAppData = process.env.LOCALAPPDATA;
  const playwrightRoot = localAppData ? join(localAppData, "ms-playwright") : "";
  const playwrightShells = existsSync(playwrightRoot)
    ? readdirSync(playwrightRoot, { withFileTypes: true })
        .filter((entry) => entry.isDirectory() && entry.name.startsWith("chromium_headless_shell-"))
        .map((entry) => join(playwrightRoot, entry.name, "chrome-win", "headless_shell.exe"))
        .filter((candidate) => existsSync(candidate))
        .sort()
        .reverse()
    : [];
  const candidates = [
    configured,
    ...playwrightShells,
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
    "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
    "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "google-chrome",
    "chromium",
    "chromium-browser",
  ].filter(Boolean);
  for (const candidate of candidates) {
    if (candidate.includes("\\") || candidate.includes("/")) {
      if (existsSync(candidate)) {
        return candidate;
      }
      continue;
    }
    return candidate;
  }
  throw new Error("Chrome/Edge executable was not found. Set CHROME_PATH to run the route smoke.");
}

function loadPlaywright() {
  const candidateRoots = [
    join(ROOT, "node_modules"),
    process.env.USERPROFILE
      ? join(
          process.env.USERPROFILE,
          ".cache",
          "codex-runtimes",
          "codex-primary-runtime",
          "dependencies",
          "node",
          "node_modules",
        )
      : "",
  ].filter(Boolean);
  for (const candidateRoot of candidateRoots) {
    try {
      const resolved = require.resolve("playwright", { paths: [candidateRoot] });
      return require(resolved);
    } catch {
      // Try the next local runtime.
    }
  }
  return null;
}

function dumpDom(executable, url, marker) {
  return new Promise((resolveDump, rejectDump) => {
    const profileDir = mkdtempSync(join(tmpdir(), "aion-route-smoke-"));
    let settled = false;
    function cleanup() {
      try {
        rmSync(profileDir, { recursive: true, force: true });
      } catch (error) {
        console.warn(`Warning: Chrome profile cleanup is still locked: ${error.message}`);
      }
    }
    function finish(callback, value) {
      if (settled) {
        return;
      }
      settled = true;
      clearTimeout(timeout);
      cleanup();
      callback(value);
    }
    const child = spawn(
      executable,
      [
        "--headless=new",
        "--disable-gpu",
        "--disable-gpu-sandbox",
        "--disable-software-rasterizer",
        "--disable-gpu-compositing",
        "--disable-accelerated-2d-canvas",
        "--disable-accelerated-video-decode",
        "--disable-webgl",
        "--disable-features=VizDisplayCompositor",
        "--disable-extensions",
        "--disable-background-networking",
        "--disable-breakpad",
        "--disable-crash-reporter",
        "--disable-component-update",
        "--disable-metrics",
        "--disable-metrics-reporting",
        "--noerrdialogs",
        "--no-first-run",
        "--no-default-browser-check",
        `--user-data-dir=${profileDir}`,
        "--dump-dom",
        url,
      ],
      { windowsHide: true },
    );
    let stdout = "";
    let stderr = "";
    const timeout = setTimeout(() => {
      child.kill("SIGKILL");
      if (stdout.includes(marker)) {
        finish(resolveDump, stdout);
        return;
      }
      finish(rejectDump, new Error(`Chrome timed out while dumping DOM for ${url}.`));
    }, 45000);
    child.stdout.on("data", (chunk) => {
      stdout += chunk.toString();
    });
    child.stderr.on("data", (chunk) => {
      stderr += chunk.toString();
    });
    child.on("error", (error) => {
      finish(rejectDump, error);
    });
    child.on("close", (code) => {
      if (code !== 0) {
        finish(rejectDump, new Error(`Chrome exited with ${code}: ${stderr}`));
        return;
      }
      finish(resolveDump, stdout);
    });
  });
}

function availablePort() {
  const server = createServer();
  return new Promise((resolvePort) => {
    server.listen(0, "127.0.0.1", () => {
      const address = server.address();
      const port = address.port;
      server.close(() => resolvePort(port));
    });
  });
}

async function waitForDevtools(port) {
  const endpoint = `http://127.0.0.1:${port}/json/list`;
  for (let attempt = 0; attempt < 80; attempt += 1) {
    try {
      const response = await fetch(endpoint, { signal: AbortSignal.timeout(1000) });
      if (response.ok) {
        const targets = await response.json();
        const page = targets.find((target) => target.type === "page");
        if (page?.webSocketDebuggerUrl) {
          return page.webSocketDebuggerUrl;
        }
      }
    } catch {
      // Chrome may still be starting.
    }
    await new Promise((resolveDelay) => setTimeout(resolveDelay, 100));
  }
  throw new Error("Timed out waiting for Chrome DevTools endpoint.");
}

function connectCdp(webSocketUrl) {
  const socket = new WebSocket(webSocketUrl);
  let nextId = 1;
  const pending = new Map();

  socket.addEventListener("message", async (event) => {
    const rawData =
      typeof event.data === "string"
        ? event.data
        : event.data instanceof Blob
          ? await event.data.text()
          : Buffer.from(event.data).toString("utf8");
    const message = JSON.parse(rawData);
    if (!message.id || !pending.has(message.id)) {
      return;
    }
    const { resolveMessage, rejectMessage, timeout } = pending.get(message.id);
    pending.delete(message.id);
    clearTimeout(timeout);
    if (message.error) {
      rejectMessage(new Error(message.error.message));
      return;
    }
    resolveMessage(message.result);
  });

  return new Promise((resolveSocket, rejectSocket) => {
    socket.addEventListener("open", () => {
      resolveSocket({
        send(method, params = {}) {
          const id = nextId;
          nextId += 1;
          socket.send(JSON.stringify({ id, method, params }));
          return new Promise((resolveMessage, rejectMessage) => {
            const timeout = setTimeout(() => {
              pending.delete(id);
              rejectMessage(new Error(`Timed out waiting for CDP response to ${method}.`));
            }, 10000);
            pending.set(id, { resolveMessage, rejectMessage, timeout });
          });
        },
        close() {
          socket.close();
        },
      });
    });
    socket.addEventListener("error", rejectSocket);
  });
}

async function evaluateCdp(cdp, expression) {
  const result = await cdp.send("Runtime.evaluate", {
    expression,
    awaitPromise: true,
    returnByValue: true,
  });
  if (result.exceptionDetails) {
    throw new Error(result.exceptionDetails.text ?? "Runtime.evaluate failed.");
  }
  return result.result.value;
}

async function waitForCdp(cdp, expression, label, timeoutMs = 10000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    const value = await evaluateCdp(cdp, expression);
    if (value) {
      return value;
    }
    await new Promise((resolveDelay) => setTimeout(resolveDelay, 100));
  }
  throw new Error(`Timed out waiting for ${label}.`);
}

async function setViewportCdp(cdp, viewport) {
  await cdp.send("Emulation.setDeviceMetricsOverride", {
    width: viewport.width,
    height: viewport.height,
    deviceScaleFactor: 1,
    mobile: viewport.width < 700,
  });
}

function cdpRouteUrl(baseUrl, route) {
  const routeUrl = new URL(`${baseUrl}${route.path}`);
  if (route.authenticated) {
    routeUrl.searchParams.set("route_smoke_auth", "1");
  }
  return routeUrl.href;
}

async function gotoRouteCdp(cdp, baseUrl, route, viewport) {
  activeFallbackAuthenticatedRoute = route.authenticated;
  if (viewport) {
    await setViewportCdp(cdp, viewport);
  }
  await cdp.send("Page.navigate", { url: cdpRouteUrl(baseUrl, route) });
  await waitForCdp(cdp, "document.querySelector('#root') !== null", "#root");
  await waitForCdp(
    cdp,
    `document.documentElement.outerHTML.includes(${JSON.stringify(route.marker)})`,
    route.marker,
  );
  activeFallbackAuthenticatedRoute = false;
}

async function collectRenderedStateCdp(cdp, marker) {
  return evaluateCdp(
    cdp,
    `(() => {
      const expectedMarker = ${JSON.stringify(marker)};
      const bodyText = document.body?.innerText?.replace(/\\s+/g, " ").trim() ?? "";
      const viewportWidth = document.documentElement.clientWidth;
      const frameworkOverlay = Boolean(
        document.querySelector("[data-vite-error-overlay], nextjs-portal, vite-error-overlay"),
      );
      const isVisible = (element) => {
        const style = window.getComputedStyle(element);
        return (
          style.display !== "none" &&
          style.visibility !== "hidden" &&
          Number(style.opacity) !== 0 &&
          element.getClientRects().length > 0
        );
      };
      const isInsideContainedHorizontalScroller = (element) => {
        const scroller = element.closest(
          ".aion-mobile-tabbar-scroll, .aion-route-switcher-scroll, .aion-chat-cognitive-belt",
        );
        if (!scroller) {
          return false;
        }
        const scrollerRect = scroller.getBoundingClientRect();
        return scrollerRect.left >= -1 && scrollerRect.right <= viewportWidth + 1;
      };
      const unnamedInteractive = Array.from(
        document.querySelectorAll("button, a[href], input, select, textarea, [role='button'], [role='link']"),
      ).filter((element) => {
        if (!isVisible(element)) {
          return false;
        }
        const ariaLabel = element.getAttribute("aria-label")?.trim();
        const ariaLabelledBy = element.getAttribute("aria-labelledby")?.trim();
        const htmlLabels =
          "labels" in element && element.labels instanceof NodeList
            ? element.labels.length
            : 0;
        const title = element.getAttribute("title")?.trim();
        const text = element.textContent?.replace(/\\s+/g, " ").trim();
        return !ariaLabel && !ariaLabelledBy && htmlLabels === 0 && !title && !text;
      });
      const overflowingElements = Array.from(document.body?.querySelectorAll("*") ?? [])
        .filter((element) => {
          if (!isVisible(element)) {
            return false;
          }
          if (isInsideContainedHorizontalScroller(element)) {
            return false;
          }
          const rect = element.getBoundingClientRect();
          return rect.right > viewportWidth + 1 || rect.left < -1;
        })
        .slice(0, 8)
        .map((element) => {
          const className = typeof element.className === "string" ? element.className : "";
          const rect = element.getBoundingClientRect();
          return {
            tag: element.tagName.toLowerCase(),
            className: className.split(/\\s+/).slice(0, 4).join(" "),
            left: Math.round(rect.left),
            right: Math.round(rect.right),
            width: Math.round(rect.width),
          };
        });
      return {
        markerFound: document.documentElement.outerHTML.includes(expectedMarker),
        bodyTextLength: bodyText.length,
        frameworkOverlay,
        horizontalOverflow:
          document.documentElement.scrollWidth > document.documentElement.clientWidth + 1 ||
          document.body.scrollWidth > document.documentElement.clientWidth + 1,
        viewportWidth,
        documentWidth: document.documentElement.scrollWidth,
        bodyWidth: document.body.scrollWidth,
        unnamedInteractiveCount: unnamedInteractive.length,
        unnamedInteractivePreview: unnamedInteractive.slice(0, 5).map((element) => {
          const className = typeof element.className === "string" ? element.className : "";
          return \`\${element.tagName.toLowerCase()}\${className ? \`.\${className.split(/\\s+/).slice(0, 3).join(".")}\` : ""}\`;
        }),
        overflowingElementCount: overflowingElements.length,
        overflowingElementPreview: overflowingElements,
      };
    })()`,
  );
}

async function screenshotCdp(cdp, screenshotPath) {
  const capture = await cdp.send("Page.captureScreenshot", {
    format: "png",
    fromSurface: true,
    captureBeyondViewport: true,
  });
  writeFileSync(screenshotPath, Buffer.from(capture.data, "base64"));
}

async function runNavigationProofCdp(cdp, baseUrl) {
  const proofSteps = [
    { label: "Chat", ...routeByPath("/chat") },
    { label: "Settings", ...routeByPath("/settings") },
    { label: "Personality", ...routeByPath("/personality") },
    { label: "Dashboard", ...routeByPath("/dashboard") },
  ];
  const steps = [];
  await gotoRouteCdp(cdp, baseUrl, routeByPath("/dashboard"), RESPONSIVE_VIEWPORTS.mobile);
  for (const step of proofSteps) {
    const clickResult = await evaluateCdp(
      cdp,
      `(() => {
        const button = document.querySelector(${JSON.stringify(`.aion-mobile-tabbar button[aria-label="${step.label}"]`)});
        if (!button) return { clicked: false, count: 0 };
        button.scrollIntoView({ block: "nearest", inline: "center" });
        button.click();
        return { clicked: true, count: 1 };
      })()`,
    );
    if (!clickResult.clicked) {
      steps.push({
        label: step.label,
        expected_path: step.path,
        passed: false,
        reason: `expected one mobile nav button, found ${clickResult.count}`,
      });
      continue;
    }
    await waitForCdp(cdp, `window.location.pathname === ${JSON.stringify(step.path)}`, step.path);
    await waitForCdp(
      cdp,
      `document.documentElement.outerHTML.includes(${JSON.stringify(step.marker)})`,
      step.marker,
    );
    const state = await collectRenderedStateCdp(cdp, step.marker);
    const renderedPath = await evaluateCdp(cdp, "window.location.pathname");
    steps.push({
      label: step.label,
      expected_path: step.path,
      rendered_path: renderedPath,
      marker: step.marker,
      passed: renderedPath === step.path && state.markerFound && !state.frameworkOverlay && !state.horizontalOverflow,
      state,
    });
  }
  const failedSteps = steps.filter((step) => !step.passed);
  return {
    viewport: "mobile",
    status: failedSteps.length === 0 ? "ok" : "failed",
    step_count: steps.length,
    failed_count: failedSteps.length,
    steps,
  };
}

async function runAccountProofCdp(cdp, baseUrl) {
  const dashboardRoute = routeByPath("/dashboard");
  await gotoRouteCdp(cdp, baseUrl, dashboardRoute, RESPONSIVE_VIEWPORTS.mobile);
  const clickResult = await evaluateCdp(
    cdp,
    `(() => {
      const trigger = document.querySelector(".aion-mobile-account-button");
      if (!trigger) return { clicked: false, count: 0 };
      trigger.click();
      return { clicked: true, count: 1 };
    })()`,
  );
  if (!clickResult.clicked) {
    return {
      viewport: "mobile",
      status: "failed",
      step_count: 1,
      failed_count: 1,
      steps: [
        {
          label: "Account trigger",
          passed: false,
          reason: `expected one mobile account trigger, found ${clickResult.count}`,
        },
      ],
    };
  }
  await waitForCdp(
    cdp,
    'document.querySelector(".aion-mobile-account-button")?.getAttribute("aria-expanded") === "true"',
    "account panel expanded",
  );
  const panelVisible = await evaluateCdp(
    cdp,
    `(() => {
      const panel = document.querySelector(".aion-mobile-account-panel");
      if (!panel) return false;
      const style = window.getComputedStyle(panel);
      return style.display !== "none" && style.visibility !== "hidden" && panel.getClientRects().length > 0;
    })()`,
  );
  const state = await collectRenderedStateCdp(cdp, dashboardRoute.marker);
  const passed = panelVisible && state.markerFound && !state.frameworkOverlay && !state.horizontalOverflow;
  return {
    viewport: "mobile",
    status: passed ? "ok" : "failed",
    step_count: 1,
    failed_count: passed ? 0 : 1,
    steps: [
      {
        label: "Account trigger opens account panel",
        rendered_path: await evaluateCdp(cdp, "window.location.pathname"),
        passed,
        panel_visible: panelVisible,
        state,
      },
    ],
  };
}

async function closeChrome(child, profileDir) {
  if (child) {
    child.kill("SIGKILL");
  }
  try {
    rmSync(profileDir, { recursive: true, force: true });
  } catch {
    // Best-effort cleanup; final process checks catch validation leftovers.
  }
}

if (!existsSync(INDEX)) {
  console.error("web/dist/index.html is missing. Run `npm run build` before `npm run smoke:routes`.");
  process.exit(1);
}

async function collectRenderedState(page, marker) {
  return page.evaluate((expectedMarker) => {
    const bodyText = document.body?.innerText?.replace(/\s+/g, " ").trim() ?? "";
    const viewportWidth = document.documentElement.clientWidth;
    const frameworkOverlay = Boolean(
      document.querySelector("[data-vite-error-overlay], nextjs-portal, vite-error-overlay"),
    );
    const isVisible = (element) => {
      const style = window.getComputedStyle(element);
      return (
        style.display !== "none" &&
        style.visibility !== "hidden" &&
        Number(style.opacity) !== 0 &&
        element.getClientRects().length > 0
      );
    };
    const isInsideContainedHorizontalScroller = (element) => {
      const scroller = element.closest(
        ".aion-mobile-tabbar-scroll, .aion-route-switcher-scroll, .aion-chat-cognitive-belt",
      );
      if (!scroller) {
        return false;
      }
      const scrollerRect = scroller.getBoundingClientRect();
      return scrollerRect.left >= -1 && scrollerRect.right <= viewportWidth + 1;
    };
    const unnamedInteractive = Array.from(
      document.querySelectorAll("button, a[href], input, select, textarea, [role='button'], [role='link']"),
    ).filter((element) => {
      if (!isVisible(element)) {
        return false;
      }
      const ariaLabel = element.getAttribute("aria-label")?.trim();
      const ariaLabelledBy = element.getAttribute("aria-labelledby")?.trim();
      const htmlLabels =
        "labels" in element && element.labels instanceof NodeList
          ? element.labels.length
          : 0;
      const title = element.getAttribute("title")?.trim();
      const text = element.textContent?.replace(/\s+/g, " ").trim();
      return !ariaLabel && !ariaLabelledBy && htmlLabels === 0 && !title && !text;
    });
    const overflowingElements = Array.from(document.body?.querySelectorAll("*") ?? [])
      .filter((element) => {
        if (!isVisible(element)) {
          return false;
        }
        if (isInsideContainedHorizontalScroller(element)) {
          return false;
        }
        const rect = element.getBoundingClientRect();
        return rect.right > viewportWidth + 1 || rect.left < -1;
      })
      .slice(0, 8)
      .map((element) => {
        const className = typeof element.className === "string" ? element.className : "";
        const rect = element.getBoundingClientRect();
        return {
          tag: element.tagName.toLowerCase(),
          className: className.split(/\s+/).slice(0, 4).join(" "),
          left: Math.round(rect.left),
          right: Math.round(rect.right),
          width: Math.round(rect.width),
        };
      });
    return {
      markerFound: document.documentElement.outerHTML.includes(expectedMarker),
      bodyTextLength: bodyText.length,
      frameworkOverlay,
      horizontalOverflow:
        document.documentElement.scrollWidth > document.documentElement.clientWidth + 1 ||
        document.body.scrollWidth > document.documentElement.clientWidth + 1,
      viewportWidth,
      documentWidth: document.documentElement.scrollWidth,
      bodyWidth: document.body.scrollWidth,
      unnamedInteractiveCount: unnamedInteractive.length,
      unnamedInteractivePreview: unnamedInteractive.slice(0, 5).map((element) => {
        const className = typeof element.className === "string" ? element.className : "";
        return `${element.tagName.toLowerCase()}${className ? `.${className.split(/\s+/).slice(0, 3).join(".")}` : ""}`;
      }),
      overflowingElementCount: overflowingElements.length,
      overflowingElementPreview: overflowingElements,
    };
  }, marker);
}

async function gotoRoute(page, baseUrl, routePath, marker = "") {
  await page.goto(`${baseUrl}${routePath}`, { waitUntil: "domcontentloaded", timeout: 30000 });
  await page.locator("#root").waitFor({ state: "attached", timeout: 10000 });
  if (marker) {
    await page.waitForFunction(
      (expectedMarker) => document.documentElement.outerHTML.includes(expectedMarker),
      marker,
      { timeout: 10000 },
    );
  }
}

async function runNavigationProof(page, baseUrl) {
  const proofSteps = [
    { label: "Chat", ...routeByPath("/chat") },
    { label: "Settings", ...routeByPath("/settings") },
    { label: "Personality", ...routeByPath("/personality") },
    { label: "Dashboard", ...routeByPath("/dashboard") },
  ];
  const steps = [];

  await page.setViewportSize(RESPONSIVE_VIEWPORTS.mobile);
  await gotoRoute(page, baseUrl, "/dashboard", routeByPath("/dashboard").marker);

  for (const step of proofSteps) {
    const locator = page.locator(`.aion-mobile-tabbar button[aria-label="${step.label}"]`);
    const count = await locator.count();
    if (count !== 1) {
      steps.push({
        label: step.label,
        expected_path: step.path,
        passed: false,
        reason: `expected one mobile nav button, found ${count}`,
      });
      continue;
    }

    await locator.scrollIntoViewIfNeeded({ timeout: 10000 });
    await locator.click({ timeout: 10000 });
    await page.waitForURL(`**${step.path}`, { timeout: 10000 });
    await page.waitForFunction(
      (expectedMarker) => document.documentElement.outerHTML.includes(expectedMarker),
      step.marker,
      { timeout: 10000 },
    );
    const state = await collectRenderedState(page, step.marker);
    const renderedPath = new URL(page.url()).pathname;
    steps.push({
      label: step.label,
      expected_path: step.path,
      rendered_path: renderedPath,
      marker: step.marker,
      passed: renderedPath === step.path && state.markerFound && !state.frameworkOverlay && !state.horizontalOverflow,
      state,
    });
  }

  const failedSteps = steps.filter((step) => !step.passed);
  return {
    viewport: "mobile",
    status: failedSteps.length === 0 ? "ok" : "failed",
    step_count: steps.length,
    failed_count: failedSteps.length,
    steps,
  };
}

async function runAccountProof(page, baseUrl) {
  const dashboardRoute = routeByPath("/dashboard");
  await page.setViewportSize(RESPONSIVE_VIEWPORTS.mobile);
  await gotoRoute(page, baseUrl, dashboardRoute.path, dashboardRoute.marker);

  const trigger = page.locator(".aion-mobile-account-button");
  const triggerCount = await trigger.count();
  if (triggerCount !== 1) {
    return {
      viewport: "mobile",
      status: "failed",
      step_count: 1,
      failed_count: 1,
      steps: [
        {
          label: "Account trigger",
          passed: false,
          reason: `expected one mobile account trigger, found ${triggerCount}`,
        },
      ],
    };
  }

  await trigger.click({ timeout: 10000 });
  await page.waitForFunction(
    () => document.querySelector(".aion-mobile-account-button")?.getAttribute("aria-expanded") === "true",
    { timeout: 10000 },
  );

  const panelVisible = await page.locator(".aion-mobile-account-panel").isVisible({ timeout: 10000 });
  const state = await collectRenderedState(page, dashboardRoute.marker);
  const passed = panelVisible && state.markerFound && !state.frameworkOverlay && !state.horizontalOverflow;
  return {
    viewport: "mobile",
    status: passed ? "ok" : "failed",
    step_count: 1,
    failed_count: passed ? 0 : 1,
    steps: [
      {
        label: "Account trigger opens account panel",
        rendered_path: new URL(page.url()).pathname,
        passed,
        panel_visible: panelVisible,
        state,
      },
    ],
  };
}

const server = await startServer();
try {
  const address = server.address();
  const baseUrl = `http://${address.address}:${address.port}`;
  const playwright = loadPlaywright();
  const results = [];
  const uiAuditResults = [];
  let navigationProof = null;
  let accountProof = null;
  if (playwright?.chromium) {
    const browser = await playwright.chromium.launch({ headless: true });
    try {
      const page = await browser.newPage({ viewport: { width: 1366, height: 900 } });
      for (const route of ROUTES) {
        await gotoRoute(page, baseUrl, route.path, route.marker);
        const dom = await page.content();
        const state = await collectRenderedState(page, route.marker);
        const passed =
          state.markerFound &&
          state.bodyTextLength > 0 &&
          !state.frameworkOverlay &&
          state.unnamedInteractiveCount === 0;
        results.push({
          route: route.path,
          marker: route.marker,
          authenticated: route.authenticated,
          passed,
          rendered_path: new URL(page.url()).pathname,
          title: await page.title(),
          state,
          diagnostic_excerpt: passed ? "" : dom.replace(/\s+/g, " ").slice(0, 320),
        });
      }
      if (screenshotDir) {
        mkdirSync(screenshotDir, { recursive: true });
        const screenshotRoutes = ROUTES.filter((route) => {
          if (requestedScreenshotRoutes.size === 0) {
            return true;
          }
          return requestedScreenshotRoutes.has(route.path);
        });
        for (const viewportName of screenshotViewportNames) {
          const viewport = RESPONSIVE_VIEWPORTS[viewportName];
          if (!viewport) {
            throw new Error(`Unknown responsive viewport "${viewportName}".`);
          }
          await page.setViewportSize(viewport);
          for (const route of screenshotRoutes) {
            await gotoRoute(page, baseUrl, route.path, route.marker);
            const fileName = `${viewportName}-${routeSlug(route.path)}.png`;
            const screenshotPath = join(screenshotDir, fileName);
            const state = await collectRenderedState(page, route.marker);
            await page.screenshot({ path: screenshotPath, fullPage: true });
            const passed =
              state.markerFound &&
              state.bodyTextLength > 0 &&
              !state.frameworkOverlay &&
              !state.horizontalOverflow &&
              state.unnamedInteractiveCount === 0;
            uiAuditResults.push({
              route: route.path,
              viewport: viewportName,
              viewport_size: viewport,
              passed,
              screenshot: normalize(screenshotPath),
              state,
            });
          }
        }
      }
      if (navigationProofEnabled) {
        navigationProof = await runNavigationProof(page, baseUrl);
      }
      if (accountProofEnabled) {
        accountProof = await runAccountProof(page, baseUrl);
      }
    } finally {
      await browser.close();
    }
  } else {
    const executable = chromePath();
    const profileDir = mkdtempSync(join(tmpdir(), "aion-route-smoke-cdp-"));
    const devtoolsPort = await availablePort();
    let chrome = null;
    let cdp = null;
    try {
      chrome = spawn(
        executable,
        [
          "--headless=new",
          "--disable-gpu",
          "--disable-gpu-sandbox",
          "--disable-software-rasterizer",
          "--disable-gpu-compositing",
          "--disable-accelerated-2d-canvas",
          "--disable-accelerated-video-decode",
          "--disable-webgl",
          "--disable-features=VizDisplayCompositor",
          "--disable-extensions",
          "--disable-background-networking",
          "--disable-breakpad",
          "--disable-crash-reporter",
          "--disable-component-update",
          "--disable-metrics",
          "--disable-metrics-reporting",
          "--noerrdialogs",
          "--no-first-run",
          "--no-default-browser-check",
          `--remote-debugging-port=${devtoolsPort}`,
          `--user-data-dir=${profileDir}`,
          "about:blank",
        ],
        { windowsHide: true },
      );
      const webSocketUrl = await waitForDevtools(devtoolsPort);
      cdp = await connectCdp(webSocketUrl);
      await cdp.send("Page.enable");
      await cdp.send("Runtime.enable");
      await setViewportCdp(cdp, { width: 1366, height: 900 });

      for (const route of ROUTES) {
        await gotoRouteCdp(cdp, baseUrl, route);
        const dom = await evaluateCdp(cdp, "document.documentElement.outerHTML");
        const state = await collectRenderedStateCdp(cdp, route.marker);
        const passed =
          state.markerFound &&
          state.bodyTextLength > 0 &&
          !state.frameworkOverlay &&
          state.unnamedInteractiveCount === 0;
        results.push({
          route: route.path,
          marker: route.marker,
          authenticated: route.authenticated,
          passed,
          rendered_path: await evaluateCdp(cdp, "window.location.pathname"),
          title: await evaluateCdp(cdp, "document.title"),
          state,
          diagnostic_excerpt: passed ? "" : dom.replace(/\s+/g, " ").slice(0, 320),
        });
      }

      if (screenshotDir) {
        mkdirSync(screenshotDir, { recursive: true });
        const screenshotRoutes = ROUTES.filter((route) => {
          if (requestedScreenshotRoutes.size === 0) {
            return true;
          }
          return requestedScreenshotRoutes.has(route.path);
        });
        for (const viewportName of screenshotViewportNames) {
          const viewport = RESPONSIVE_VIEWPORTS[viewportName];
          if (!viewport) {
            throw new Error(`Unknown responsive viewport "${viewportName}".`);
          }
          for (const route of screenshotRoutes) {
            await gotoRouteCdp(cdp, baseUrl, route, viewport);
            const fileName = `${viewportName}-${routeSlug(route.path)}.png`;
            const screenshotPath = join(screenshotDir, fileName);
            const state = await collectRenderedStateCdp(cdp, route.marker);
            await screenshotCdp(cdp, screenshotPath);
            const passed =
              state.markerFound &&
              state.bodyTextLength > 0 &&
              !state.frameworkOverlay &&
              !state.horizontalOverflow &&
              state.unnamedInteractiveCount === 0;
            uiAuditResults.push({
              route: route.path,
              viewport: viewportName,
              viewport_size: viewport,
              passed,
              screenshot: normalize(screenshotPath),
              state,
            });
          }
        }
      }
      if (navigationProofEnabled) {
        navigationProof = await runNavigationProofCdp(cdp, baseUrl);
      }
      if (accountProofEnabled) {
        accountProof = await runAccountProofCdp(cdp, baseUrl);
      }
    } finally {
      if (cdp) {
        cdp.close();
      }
      await closeChrome(chrome, profileDir);
    }
  }
  const failed = results.filter((result) => !result.passed);
  const failedUiAudit = uiAuditResults.filter((result) => !result.passed);
  const navigationProofFailed = Boolean(navigationProof && navigationProof.status !== "ok");
  const accountProofFailed = Boolean(accountProof && accountProof.status !== "ok");
  const report = {
    kind: "frontend_route_smoke_report",
    schema_version: 2,
    route_count: results.length,
    status:
      failed.length === 0 &&
      (!failOnUiFindings || failedUiAudit.length === 0) &&
      !navigationProofFailed &&
      !accountProofFailed
        ? "ok"
        : "failed",
    results,
    ui_audit:
      uiAuditResults.length > 0
        ? {
            artifact_dir: normalize(screenshotDir),
            viewport_count: screenshotViewportNames.length,
            screenshot_count: uiAuditResults.length,
            status: failedUiAudit.length === 0 ? "ok" : "findings",
            failed_count: failedUiAudit.length,
            results: uiAuditResults,
        }
        : null,
    navigation_proof: navigationProof,
    account_proof: accountProof,
  };
  if (reportPath) {
    mkdirSync(dirname(reportPath), { recursive: true });
    writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`);
  }
  console.log(JSON.stringify(report, null, 2));
  process.exitCode =
    failed.length === 0 &&
    (!failOnUiFindings || failedUiAudit.length === 0) &&
    !navigationProofFailed &&
    !accountProofFailed
      ? 0
      : 1;
} finally {
  await new Promise((resolveClose) => server.close(resolveClose));
  process.exit(process.exitCode ?? 0);
}
