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

const pendingConfirmation = {
  status: "pending_confirmation",
  source_event_id: "connector-browser-event",
  trace_id: "connector-browser-trace",
  connector_kind: "task_system",
  provider_hint: "clickup",
  operation: "update_task",
  mode: "mutate_with_confirmation",
  candidate_summary: "Update ClickUp task #123 to Done",
  source_reference: "action_result.observations[0]",
  reason: "Explicit user confirmation is required before updating ClickUp.",
};

const requests = {
  sentMessages: [],
  confirmations: [],
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

function confirmedHistory() {
  return [
    {
      message_id: "connector-browser-event:user",
      event_id: "connector-browser-event",
      role: "user",
      text: "Please update the ClickUp task.",
      channel: "app",
      timestamp: "2026-05-08T12:00:00.000Z",
      metadata: { delivery_state: "delivered" },
    },
    {
      message_id: "connector-browser-event:assistant",
      event_id: "connector-browser-event",
      role: "assistant",
      text: "I found the candidate task and need your confirmation before updating ClickUp.",
      channel: "app",
      timestamp: "2026-05-08T12:00:02.000Z",
      metadata: { language: "en", action_status: "confirmation_required" },
    },
  ];
}

async function mockApi(request, response) {
  const url = new URL(request.url ?? "/", "http://127.0.0.1");

  if (request.method === "GET" && url.pathname === "/app/me") {
    jsonResponse(response, 200, {
      user: {
        id: "connector-browser-user",
        email: "connector-browser@example.com",
        display_name: "Connector Browser",
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
      items: requests.sentMessages.length ? confirmedHistory() : [],
    });
    return true;
  }

  if (request.method === "POST" && url.pathname === "/app/chat/message") {
    const rawBody = await readRequestBody(request);
    const parsedBody = rawBody ? JSON.parse(rawBody) : {};
    requests.sentMessages.push(parsedBody);
    jsonResponse(response, 200, {
      event_id: "connector-browser-event",
      trace_id: "connector-browser-trace",
      reply: {
        message: "I found the candidate task and need your confirmation before updating ClickUp.",
        language: "en",
        tone: "calm",
        channel: "app",
      },
      runtime: {
        role: "assistant",
        motivation_mode: "execute",
        action_status: "confirmation_required",
        reflection_triggered: false,
      },
      pending_confirmation: pendingConfirmation,
    });
    return true;
  }

  if (request.method === "POST" && url.pathname === "/app/connectors/confirm") {
    const rawBody = await readRequestBody(request);
    const parsedBody = rawBody ? JSON.parse(rawBody) : {};
    requests.confirmations.push(parsedBody);
    if (requests.confirmations.length === 1) {
      jsonResponse(response, 409, { detail: "confirmation_stale" });
      return true;
    }
    jsonResponse(response, 200, {
      action_status: "completed",
      actions: ["clickup.update_task"],
      notes: "ClickUp task updated.",
      pending_confirmation: null,
    });
    return true;
  }

  if (request.method === "GET" && url.pathname === "/app/personality/overview") {
    jsonResponse(response, 200, {
      user_id: "connector-browser-user",
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
    jsonResponse(response, 200, {
      policy_owner: "app_tools_overview_contract",
      user_id: "connector-browser-user",
      group_order: [],
      groups: [],
      summary: {
        total_groups: 0,
        total_items: 0,
        integral_enabled_count: 0,
        provider_ready_count: 0,
        provider_blocked_count: 0,
        link_required_count: 0,
        planned_placeholder_count: 0,
      },
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
  const events = [];

  socket.addEventListener("message", async (event) => {
    const rawData =
      typeof event.data === "string"
        ? event.data
        : event.data instanceof Blob
          ? await event.data.text()
          : Buffer.from(event.data).toString("utf8");
    const message = JSON.parse(rawData);
    if (message.method) {
      events.push(message);
    }
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
        events,
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
  await waitFor(cdp, `document.readyState === "complete"`, `document load for ${url}`, 10000);
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
  const diagnostic = await evaluate(
    cdp,
    `(document.body?.innerText?.replace(/\\s+/g, " ").slice(0, 700) || document.documentElement?.outerHTML?.replace(/\\s+/g, " ").slice(0, 700) || "")`,
  );
  const recentEvents = JSON.stringify(cdp.events.slice(-5)).slice(0, 1200);
  throw new Error(`Timed out waiting for ${label}. DOM excerpt: ${diagnostic}. Recent events: ${recentEvents}`);
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function assertPendingPayloadMatches(actual) {
  for (const [key, expected] of Object.entries(pendingConfirmation)) {
    assert(
      actual?.[key] === expected,
      `Expected confirmation payload field ${key}=${expected}, got ${actual?.[key]}.`,
    );
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
  for (let attempt = 0; attempt < 80; attempt += 1) {
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

async function characterizeConfirmation(cdp, baseUrl) {
  await navigate(cdp, `${baseUrl}/chat?case=connector-confirmation`);
  await waitFor(cdp, `Boolean(document.querySelector(".aion-chat-input"))`, "chat composer");

  await evaluate(
    cdp,
    `(() => {
      const textarea = document.querySelector(".aion-chat-input");
      const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
      nativeSetter.call(textarea, "Please update the ClickUp task.");
      textarea.dispatchEvent(new Event("input", { bubbles: true }));
      document.querySelector(".aion-chat-composer").dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
      return true;
    })()`,
  );

  const pendingState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      const normalizedText = text.toLowerCase();
      if (!normalizedText.includes("confirmation required") || !text.includes("Update ClickUp task #123 to Done")) {
        return null;
      }
      return {
        rowCount: document.querySelectorAll(".aion-chat-message-row").length,
        pendingCount: document.querySelectorAll(".aion-chat-pending-confirmation").length,
        buttonText: Array.from(document.querySelectorAll(".aion-chat-pending-confirmation-button")).map((button) => button.innerText.trim()).join("|"),
        blockedChip: text.includes("Blocked"),
        ariaLive: document.querySelector(".aion-chat-pending-confirmation")?.getAttribute("aria-live"),
      };
    })()`,
    "pending connector confirmation",
    7000,
  );
  assert(requests.sentMessages.length === 1, "Expected one chat send request.");
  assert(pendingState.pendingCount === 1, "Expected one pending confirmation section.");
  assert(pendingState.buttonText.toLowerCase() === "confirm", "Expected an enabled Confirm button.");
  assert(pendingState.blockedChip === true, "Expected the blocked chip to stay visible.");
  assert(pendingState.ariaLive === "polite", "Expected pending confirmation feedback to be aria-live polite.");

  await evaluate(
    cdp,
    `(() => {
      const button = document.querySelector(".aion-chat-pending-confirmation-button");
      button.click();
      return true;
    })()`,
  );

  const errorState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      if (!text.includes("confirmation_stale") || !text.includes("Update ClickUp task #123 to Done")) {
        return null;
      }
      const button = document.querySelector(".aion-chat-pending-confirmation-button");
      return {
        pendingCount: document.querySelectorAll(".aion-chat-pending-confirmation").length,
        feedbackCount: document.querySelectorAll(".aion-chat-pending-confirmation-feedback-error").length,
        buttonText: button?.innerText.trim(),
        buttonDisabled: Boolean(button?.disabled),
      };
    })()`,
    "fail-closed confirmation error",
    7000,
  );
  assert(requests.confirmations.length === 1, "Expected one failed confirmation request.");
  assertPendingPayloadMatches(requests.confirmations[0]);
  assert(errorState.pendingCount === 1, "Expected pending confirmation to remain after failure.");
  assert(errorState.feedbackCount === 1, "Expected error feedback class after failure.");
  assert(errorState.buttonText.toLowerCase() === "confirm", "Expected retry Confirm button after failure.");
  assert(errorState.buttonDisabled === false, "Expected retry button to be enabled after failure.");

  await evaluate(
    cdp,
    `(() => {
      const button = document.querySelector(".aion-chat-pending-confirmation-button");
      button.click();
      return true;
    })()`,
  );

  const successState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      const normalizedText = text.toLowerCase();
      if (!normalizedText.includes("confirmation complete") || !text.includes("ClickUp task updated.")) {
        return null;
      }
      return {
        pendingCount: document.querySelectorAll(".aion-chat-pending-confirmation").length,
        feedbackCount: document.querySelectorAll(".aion-chat-pending-confirmation-feedback-success").length,
        confirmButtonCount: document.querySelectorAll(".aion-chat-pending-confirmation-button").length,
        stalePendingCopy: text.includes("Update ClickUp task #123 to Done"),
      };
    })()`,
    "successful connector confirmation",
    7000,
  );
  assert(requests.confirmations.length === 2, "Expected retry confirmation request.");
  assertPendingPayloadMatches(requests.confirmations[1]);
  assert(successState.pendingCount === 1, "Expected success feedback section to remain visible.");
  assert(successState.feedbackCount === 1, "Expected success feedback class.");
  assert(successState.confirmButtonCount === 0, "Expected no confirm button after successful execution.");
  assert(successState.stalePendingCopy === false, "Expected stale pending candidate copy to be removed after success.");

  return {
    pendingState,
    errorState,
    successState,
    requests: {
      sentMessageCount: requests.sentMessages.length,
      confirmationCount: requests.confirmations.length,
    },
  };
}

if (!existsSync(INDEX)) {
  console.error("web/dist/index.html is missing. Run `npm run build` before `npm run test:connector-confirmation-browser`.");
  process.exit(1);
}

const appServer = await startAppServer();
const profileDir = mkdtempSync(join(tmpdir(), "aion-connector-confirmation-"));
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
      "--disable-breakpad",
      "--disable-crash-reporter",
      "--disable-component-update",
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

  const result = await characterizeConfirmation(cdp, baseUrl);
  console.log(
    JSON.stringify(
      {
        kind: "connector_confirmation_browser_characterization_report",
        schema_version: 1,
        status: "ok",
        result,
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
