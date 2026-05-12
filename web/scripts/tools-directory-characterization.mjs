import { createServer } from "node:http";
import { spawn } from "node:child_process";
import { existsSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { platform, tmpdir } from "node:os";
import { extname, join, normalize, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const DIST = join(ROOT, "dist");
const INDEX = join(DIST, "index.html");
const MIME_TYPES = {
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".webp": "image/webp",
};

const requests = {
  preferenceBodies: [],
  telegramLinkStarts: 0,
};

function jsonResponse(response, status, payload) {
  const body = JSON.stringify(payload);
  response.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Content-Length": Buffer.byteLength(body),
  });
  response.end(body);
}

function readRequestBody(request) {
  return new Promise((resolveBody) => {
    let body = "";
    request.on("data", (chunk) => {
      body += chunk.toString();
    });
    request.on("end", () => resolveBody(body));
  });
}

function toolsOverview({
  clickupEnabled = false,
  telegramLinked = false,
  empty = false,
} = {}) {
  const groups = empty
    ? []
    : [
        {
          id: "communication",
          title: "Communication",
          description: "Tools that carry conversations across product channels.",
          item_count: 2,
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
              user_control: {
                toggle_allowed: false,
                preference_supported: false,
                requested_enabled: null,
              },
              link_required: false,
              link_state: "not_required",
              capabilities: ["chat"],
              next_actions: [],
              source_of_truth: ["app_tools_overview_contract"],
            },
            {
              id: "telegram",
              label: "Telegram",
              category: "communication",
              kind: "channel",
              description: "External Telegram channel linking.",
              status: telegramLinked ? "provider_ready" : "link_required",
              status_reason: telegramLinked
                ? "Telegram is linked for this identity."
                : "Telegram is ready but still needs a link code.",
              enabled: true,
              integral: false,
              provider: { name: "telegram", ready: true, configured: true },
              user_control: {
                toggle_allowed: true,
                preference_supported: true,
                requested_enabled: true,
              },
              link_required: !telegramLinked,
              link_state: telegramLinked ? "linked" : "not_linked",
              capabilities: ["send_message", "receive_message"],
              next_actions: telegramLinked ? [] : ["link_telegram_chat"],
              source_of_truth: ["telegram_link_contract"],
            },
          ],
        },
        {
          id: "task_management",
          title: "Task management",
          description: "Provider-backed task tools.",
          item_count: 1,
          items: [
            {
              id: "clickup",
              label: "ClickUp",
              category: "task_management",
              kind: "provider",
              description: "Task provider readiness row.",
              status: clickupEnabled ? "provider_ready" : "provider_blocked",
              status_reason: clickupEnabled
                ? "ClickUp preference is enabled in this characterization."
                : "Provider credentials are not configured in this characterization.",
              enabled: clickupEnabled,
              integral: false,
              provider: { name: "clickup", ready: clickupEnabled, configured: clickupEnabled },
              user_control: {
                toggle_allowed: true,
                preference_supported: true,
                requested_enabled: clickupEnabled,
              },
              link_required: false,
              link_state: "not_required",
              capabilities: ["create_task", "list_tasks"],
              next_actions: clickupEnabled ? [] : ["configure_provider_credentials"],
              source_of_truth: ["connector_execution_baseline"],
            },
          ],
        },
      ];

  return {
    policy_owner: "app_tools_overview_contract",
    user_id: "tools-characterization-user",
    group_order: groups.map((group) => group.id),
    summary: {
      total_groups: groups.length,
      total_items: groups.reduce((sum, group) => sum + group.items.length, 0),
      integral_enabled_count: empty ? 0 : 1,
      provider_ready_count: empty ? 0 : clickupEnabled ? 2 : 1,
      provider_blocked_count: empty ? 0 : clickupEnabled ? 0 : 1,
      link_required_count: empty || telegramLinked ? 0 : 1,
      planned_placeholder_count: 0,
    },
    groups,
  };
}

function caseFromRequest(request) {
  const referer = request.headers.referer ?? "";
  try {
    return new URL(referer).searchParams.get("case") ?? "full";
  } catch {
    return "full";
  }
}

async function mockApi(request, response) {
  const url = new URL(request.url ?? "/", "http://127.0.0.1");

  if (request.method === "GET" && url.pathname === "/app/me") {
    jsonResponse(response, 200, {
      user: {
        id: "tools-characterization-user",
        email: "tools-characterization@example.com",
        display_name: "Tools Characterization",
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

  if (request.method === "GET" && url.pathname === "/app/personality/overview") {
    jsonResponse(response, 200, {
      user_id: "tools-characterization-user",
      recent_activity: [],
      identity_state: { profile: { preferred_language: "en" } },
      learned_knowledge: {},
      planning_state: {
        active_goals: [],
        active_tasks: [],
        pending_proposals: [],
        continuity_summary: {},
      },
      role_skill_state: {},
      capability_catalog: {},
      api_readiness: {},
    });
    return true;
  }

  if (request.method === "GET" && url.pathname === "/app/tools/overview") {
    const activeCase = caseFromRequest(request);
    if (activeCase === "error") {
      jsonResponse(response, 503, { detail: "Tools overview unavailable." });
      return true;
    }
    if (activeCase === "slow") {
      await new Promise((resolveDelay) => setTimeout(resolveDelay, 1500));
    }
    jsonResponse(response, 200, toolsOverview({ empty: activeCase === "empty" }));
    return true;
  }

  if (request.method === "PATCH" && url.pathname === "/app/tools/preferences") {
    const rawBody = await readRequestBody(request);
    const parsedBody = rawBody ? JSON.parse(rawBody) : {};
    requests.preferenceBodies.push(parsedBody);
    jsonResponse(response, 200, toolsOverview({ clickupEnabled: Boolean(parsedBody.clickup_enabled) }));
    return true;
  }

  if (request.method === "POST" && url.pathname === "/app/tools/telegram/link/start") {
    requests.telegramLinkStarts += 1;
    jsonResponse(response, 200, {
      link_code: "TG-123456",
      instruction_text: "Send TG-123456 to the configured Aviary Telegram bot.",
      expires_in_seconds: 600,
    });
    return true;
  }

  if (request.method === "GET" && url.pathname === "/health") {
    jsonResponse(response, 200, { status: "ok" });
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
  }
  const body = readFileSync(filePath);
  const contentType = MIME_TYPES[extname(filePath)] ?? "application/octet-stream";
  response.writeHead(200, {
    "Content-Type": contentType,
    "Content-Length": body.length,
  });
  response.end(body);
}

function startAppServer() {
  const server = createServer(async (request, response) => {
    if (await mockApi(request, response)) {
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
  const candidates = [
    configured,
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
  throw new Error("Chrome/Edge executable was not found. Set CHROME_PATH to run this characterization.");
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

async function evaluate(cdp, expression) {
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

async function navigate(cdp, url) {
  await cdp.send("Page.navigate", { url });
}

async function waitFor(cdp, expression, label, timeoutMs = 5000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    const value = await evaluate(cdp, expression);
    if (value) {
      return value;
    }
    await new Promise((resolveDelay) => setTimeout(resolveDelay, 100));
  }
  throw new Error(`Timed out waiting for ${label}.`);
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function waitForProcessExit(child, timeoutMs = 2000) {
  if (child.exitCode !== null || child.signalCode !== null) {
    return Promise.resolve();
  }
  return new Promise((resolveExit) => {
    const timeout = setTimeout(resolveExit, timeoutMs);
    child.once("exit", () => {
      clearTimeout(timeout);
      resolveExit();
    });
  });
}

function killProcessTree(child) {
  if (platform() !== "win32" || !child?.pid) {
    child?.kill();
    return waitForProcessExit(child);
  }
  return new Promise((resolveKill) => {
    const taskkill = spawn("taskkill.exe", ["/PID", String(child.pid), "/T", "/F"], {
      windowsHide: true,
    });
    taskkill.on("close", () => resolveKill());
    taskkill.on("error", () => resolveKill());
  });
}

function stopProfileProcesses(profileDir) {
  if (platform() !== "win32") {
    return Promise.resolve();
  }
  return new Promise((resolveStop) => {
    const child = spawn(
      "powershell.exe",
      [
        "-NoProfile",
        "-Command",
        "$profilePath = $env:AION_CHROME_PROFILE; " +
          "Get-CimInstance Win32_Process | " +
          "Where-Object { $_.CommandLine -like \"*$profilePath*\" } | " +
          "ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }",
      ],
      {
        env: { ...process.env, AION_CHROME_PROFILE: profileDir },
        windowsHide: true,
      },
    );
    child.on("close", () => resolveStop());
    child.on("error", () => resolveStop());
  });
}

async function removeProfileDir(profileDir) {
  for (let attempt = 0; attempt < 40; attempt += 1) {
    try {
      rmSync(profileDir, { recursive: true, force: true });
      return;
    } catch (error) {
      if (attempt === 39) {
        console.warn(`Warning: Chrome profile cleanup is still locked: ${error.message}`);
        return;
      }
      await new Promise((resolveDelay) => setTimeout(resolveDelay, 250));
    }
  }
}

async function characterizeTools(cdp, baseUrl) {
  const results = [];

  await navigate(cdp, `${baseUrl}/tools?case=full`);
  const fullState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      if (!text.includes("Tool directory") || !text.includes("Telegram") || !text.includes("ClickUp")) {
        return null;
      }
      return {
        groupCount: document.querySelectorAll(".aion-tools-group").length,
        itemCount: document.querySelectorAll(".aion-tools-item-card").length,
        toggleCount: document.querySelectorAll(".aion-tools-item-card input[type='checkbox']").length,
        hasTelegramLinkPanel: text.toLowerCase().includes("telegram linking") && text.includes("Generate code"),
        hasTechnicalDetails: text.includes("Technical details"),
        textExcerpt: text.replace(/\\s+/g, " ").slice(0, 1000),
      };
    })()`,
    "full tools directory",
  );
  assert(fullState.groupCount === 2, "Expected two tools groups in the full state.");
  assert(fullState.itemCount === 3, "Expected three tools item cards in the full state.");
  assert(fullState.toggleCount === 2, "Expected two user-control toggles in the full state.");
  assert(
    fullState.hasTelegramLinkPanel,
    `Expected Telegram link panel in the full state. Text excerpt: ${fullState.textExcerpt}`,
  );
  assert(fullState.hasTechnicalDetails, "Expected technical details in the full state.");
  results.push({ case: "full", status: "ok", ...fullState });

  await evaluate(
    cdp,
    `(() => {
      const card = Array.from(document.querySelectorAll(".aion-tools-item-card"))
        .find((candidate) => candidate.innerText.includes("ClickUp"));
      const toggle = card?.querySelector("input[type='checkbox']");
      toggle?.click();
      return Boolean(toggle);
    })()`,
  );
  await waitFor(
    cdp,
    `document.body.innerText.includes("Your tool choices have been saved.")`,
    "tool preference saved toast",
  );
  assert(
    requests.preferenceBodies.some((body) => body.clickup_enabled === true),
    "Expected ClickUp toggle to call PATCH /app/tools/preferences with clickup_enabled=true.",
  );
  results.push({ case: "toggle", status: "ok", request: requests.preferenceBodies.at(-1) });

  await evaluate(
    cdp,
    `(() => {
      const button = Array.from(document.querySelectorAll("button"))
        .find((candidate) => candidate.innerText.includes("Generate code"));
      button?.click();
      return Boolean(button);
    })()`,
  );
  const linkState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      return text.includes("TG-123456") && text.includes("Your Telegram link code is ready.")
        ? { hasCode: true, linkStarts: ${requests.telegramLinkStarts} }
        : null;
    })()`,
    "Telegram link code",
  );
  assert(requests.telegramLinkStarts === 1, "Expected one Telegram link-start request.");
  results.push({ case: "telegram_link_start", status: "ok", ...linkState });

  await navigate(cdp, `${baseUrl}/tools?case=slow&cacheBust=${Date.now()}`);
  const loadingState = await waitFor(
    cdp,
    `document.body.innerText.includes("Loading your tools overview.")`,
    "tools loading state",
    1000,
  );
  assert(loadingState === true, "Expected tools loading state to render during a delayed overview request.");
  results.push({ case: "loading", status: "ok" });
  await waitFor(cdp, `document.body.innerText.includes("Tool directory")`, "slow tools completion");

  await navigate(cdp, `${baseUrl}/tools?case=empty&cacheBust=${Date.now()}`);
  const emptyState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      if (!text.includes("Tool directory")) {
        return null;
      }
      return {
        groupCount: document.querySelectorAll(".aion-tools-group").length,
        itemCount: document.querySelectorAll(".aion-tools-item-card").length,
      };
    })()`,
    "empty tools overview",
  );
  assert(emptyState.groupCount === 0, "Expected no group cards for an empty tools overview.");
  assert(emptyState.itemCount === 0, "Expected no item cards for an empty tools overview.");
  results.push({ case: "empty", status: "ok", ...emptyState });

  await navigate(cdp, `${baseUrl}/tools?case=error&cacheBust=${Date.now()}`);
  const errorState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      return text.includes("Tools overview unavailable.")
        ? { hasError: true, groupCount: document.querySelectorAll(".aion-tools-group").length }
        : null;
    })()`,
    "tools error state",
  );
  assert(errorState.groupCount === 0, "Expected no tools groups after an overview error.");
  results.push({ case: "error", status: "ok", ...errorState });

  return results;
}

if (!existsSync(INDEX)) {
  console.error("web/dist/index.html is missing. Run `npm run build` before `npm run test:tools-directory`.");
  process.exit(1);
}

const appServer = await startAppServer();
const profileDir = mkdtempSync(join(tmpdir(), "aion-tools-directory-"));
const devtoolsPort = await availablePort();
let chrome;
let cdp;

try {
  const address = appServer.address();
  const baseUrl = `http://${address.address}:${address.port}`;
  chrome = spawn(
    chromePath(),
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

  const results = await characterizeTools(cdp, baseUrl);
  console.log(
    JSON.stringify(
      {
        kind: "tools_directory_characterization_report",
        schema_version: 1,
        status: "ok",
        results,
      },
      null,
      2,
    ),
  );
} finally {
  if (cdp) {
    cdp.close();
  }
  if (chrome) {
    await killProcessTree(chrome);
    await waitForProcessExit(chrome);
  }
  await stopProfileProcesses(profileDir);
  await new Promise((resolveClose) => appServer.close(resolveClose));
  await removeProfileDir(profileDir);
}
