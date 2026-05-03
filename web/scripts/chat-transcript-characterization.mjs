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

let sentMessageText = "";
let sendRequestCount = 0;

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

function caseFromRequest(request) {
  const referer = request.headers.referer ?? "";
  try {
    return new URL(referer).searchParams.get("case") ?? "full";
  } catch {
    return "full";
  }
}

function durableFullHistory() {
  return [
    {
      message_id: "chat-characterization:user",
      event_id: "chat-characterization",
      role: "user",
      text: "Please summarize the plan.",
      channel: "app",
      timestamp: "2026-05-03T12:00:00.000Z",
      metadata: { delivery_state: "delivered" },
    },
    {
      message_id: "chat-characterization:assistant",
      event_id: "chat-characterization",
      role: "assistant",
      text: "Here is the **plan**:\n\n- focus\n- ship",
      channel: "app",
      timestamp: "2026-05-03T12:00:02.000Z",
      metadata: { language: "en" },
    },
  ];
}

function durableSentHistory() {
  if (!sentMessageText) {
    return [];
  }
  return [
    {
      message_id: "chat-send:user",
      event_id: "chat-send",
      role: "user",
      text: sentMessageText,
      channel: "app",
      timestamp: "2026-05-03T12:05:00.000Z",
      metadata: { delivery_state: "delivered" },
    },
    {
      message_id: "chat-send:assistant",
      event_id: "chat-send",
      role: "assistant",
      text: "Assistant response ready with **bold** detail.",
      channel: "app",
      timestamp: "2026-05-03T12:05:02.000Z",
      metadata: { language: "en" },
    },
  ];
}

async function mockApi(request, response) {
  const url = new URL(request.url ?? "/", "http://127.0.0.1");

  if (request.method === "GET" && url.pathname === "/app/me") {
    jsonResponse(response, 200, {
      user: {
        id: "chat-characterization-user",
        email: "chat-characterization@example.com",
        display_name: "Chat Characterization",
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
    const activeCase = caseFromRequest(request);
    if (activeCase === "preview") {
      jsonResponse(response, 200, { items: [] });
      return true;
    }
    if (activeCase === "send") {
      jsonResponse(response, 200, { items: durableSentHistory() });
      return true;
    }
    jsonResponse(response, 200, { items: durableFullHistory() });
    return true;
  }

  if (request.method === "POST" && url.pathname === "/app/chat/message") {
    const rawBody = await readRequestBody(request);
    const parsedBody = rawBody ? JSON.parse(rawBody) : {};
    sendRequestCount += 1;
    sentMessageText = String(parsedBody.text ?? "");
    await new Promise((resolveDelay) => setTimeout(resolveDelay, 900));
    jsonResponse(response, 200, {
      event_id: "chat-send",
      trace_id: "chat-send-trace",
      reply: {
        message: "Assistant response ready with **bold** detail.",
        language: "en",
        tone: "calm",
        channel: "app",
      },
      runtime: {
        role: "assistant",
        motivation_mode: "support",
        action_status: "completed",
        reflection_triggered: false,
      },
    });
    return true;
  }

  if (request.method === "GET" && url.pathname === "/app/personality/overview") {
    jsonResponse(response, 200, {
      user_id: "chat-characterization-user",
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
      user_id: "chat-characterization-user",
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
      const response = await fetch(endpoint);
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

  socket.addEventListener("message", (event) => {
    const message = JSON.parse(event.data);
    if (message.method) {
      events.push(message);
    }
    if (!message.id || !pending.has(message.id)) {
      return;
    }
    const { resolveMessage, rejectMessage } = pending.get(message.id);
    pending.delete(message.id);
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
            pending.set(id, { resolveMessage, rejectMessage });
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

async function characterizeChat(cdp, baseUrl) {
  const results = [];

  await navigate(cdp, `${baseUrl}/chat?case=preview`);
  const previewState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      if (!text.includes("Good morning.") || !text.includes("Shall we refine the details together?")) {
        return null;
      }
      return {
        rowCount: document.querySelectorAll(".aion-chat-message-row").length,
        previewMetaCount: document.querySelectorAll(".aion-chat-message-meta-preview").length,
        previewCopyCount: document.querySelectorAll(".aion-chat-message-copy-preview").length,
      };
    })()`,
    "chat preview fallback",
  );
  assert(previewState.rowCount === 3, "Expected three preview transcript rows.");
  assert(previewState.previewMetaCount === 3, "Expected preview metadata class on every preview row.");
  assert(previewState.previewCopyCount === 3, "Expected preview copy class on every preview row.");
  results.push({ case: "preview", status: "ok", ...previewState });

  await navigate(cdp, "about:blank");
  await navigate(cdp, `${baseUrl}/chat?case=full&cacheBust=${Date.now()}`);
  const fullState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      if (!text.includes("Please summarize the plan.") || !text.includes("Here is the")) {
        return null;
      }
      return {
        rowCount: document.querySelectorAll(".aion-chat-message-row").length,
        deliveredCount: document.querySelectorAll(".aion-chat-delivery-status-delivered").length,
        strongCount: document.querySelectorAll(".aion-chat-message-copy strong").length,
        listItemCount: document.querySelectorAll(".aion-chat-message-copy li").length,
      };
    })()`,
    "durable chat transcript",
  );
  assert(fullState.rowCount === 2, "Expected two durable transcript rows.");
  assert(fullState.deliveredCount === 1, "Expected one delivered user indicator.");
  assert(fullState.strongCount >= 1, "Expected markdown strong element in assistant row.");
  assert(fullState.listItemCount === 2, "Expected markdown list items in assistant row.");
  results.push({ case: "full", status: "ok", ...fullState });

  sentMessageText = "";
  sendRequestCount = 0;
  await navigate(cdp, "about:blank");
  await navigate(cdp, `${baseUrl}/chat?case=send&cacheBust=${Date.now()}`);
  await waitFor(cdp, `document.body.innerText.includes("Good morning.")`, "send preview baseline");
  await evaluate(
    cdp,
    `(() => {
      const textarea = document.querySelector(".aion-chat-input");
      const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
      nativeSetter.call(textarea, "Local send smoke");
      textarea.dispatchEvent(new Event("input", { bubbles: true }));
      document.querySelector(".aion-chat-composer").dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
      return true;
    })()`,
  );
  const sendingState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      return text.includes("Local send smoke")
        ? {
            rowCount: document.querySelectorAll(".aion-chat-message-row").length,
            sendingCount: document.querySelectorAll(".aion-chat-delivery-status-sending").length,
          }
        : null;
    })()`,
    "optimistic local send row",
  );
  assert(sendingState.rowCount === 1, "Expected preview rows to collapse to one optimistic local row.");
  assert(sendingState.sendingCount === 1, "Expected sending delivery indicator for optimistic user row.");

  const deliveredState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      return text.includes("Assistant response ready")
        ? {
            rowCount: document.querySelectorAll(".aion-chat-message-row").length,
            deliveredCount: document.querySelectorAll(".aion-chat-delivery-status-delivered").length,
            strongCount: document.querySelectorAll(".aion-chat-message-copy strong").length,
          }
        : null;
    })()`,
    "delivered send response",
    7000,
  );
  assert(sendRequestCount === 1, "Expected one chat send request.");
  assert(deliveredState.rowCount === 2, "Expected durable sent user and assistant rows.");
  assert(deliveredState.deliveredCount === 1, "Expected delivered indicator after send response.");
  assert(deliveredState.strongCount >= 1, "Expected markdown strong element in sent assistant response.");
  results.push({ case: "send", status: "ok", sendingState, deliveredState });

  return results;
}

if (!existsSync(INDEX)) {
  console.error("web/dist/index.html is missing. Run `npm run build` before `npm run test:chat-transcript`.");
  process.exit(1);
}

const appServer = await startAppServer();
const profileDir = mkdtempSync(join(tmpdir(), "aion-chat-transcript-"));
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

  const results = await characterizeChat(cdp, baseUrl);
  console.log(
    JSON.stringify(
      {
        kind: "chat_transcript_characterization_report",
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
