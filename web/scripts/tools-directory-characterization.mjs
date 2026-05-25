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
  seenPaths: [],
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
  googleCalendarEnabled = false,
  googleDriveEnabled = false,
  telegramLinked = false,
  telegramLinkPending = false,
  empty = false,
} = {}) {
  const skillBinding = ({ skillId, label, posture, allowedOperations }) => ({
    skill_id: skillId,
    label,
    posture,
    allowed_operations: allowedOperations,
    execution_owner: "action",
    authority: "metadata_only_not_execution_authority",
  });
  const clickupReady = clickupEnabled;
  const googleCalendarReady = googleCalendarEnabled;
  const googleDriveReady = googleDriveEnabled;
  const groups = empty
    ? []
    : [
        {
          id: "communication",
          title: "Communication",
          description: "Channels the personality can use to communicate with the user.",
          item_count: 2,
          items: [
            {
              id: "internal_chat",
              label: "Internal chat",
              category: "communication",
              kind: "channel",
              description: "Integral first-party communication through the web product shell.",
              status: "integral_active",
              status_reason: "backend_owned_first_party_ui_channel",
              enabled: true,
              integral: true,
              provider: { name: "first_party_web", ready: true, configured: true },
              user_control: {
                toggle_allowed: false,
                preference_supported: false,
                requested_enabled: null,
              },
              link_required: false,
              link_state: "not_applicable",
              capabilities: ["app.chat", "cookie_session", "first_party_auth"],
              skill_tool_bindings: [],
              next_actions: [],
              source_of_truth: ["/app/chat/message", "/app/me"],
            },
            {
              id: "telegram",
              label: "Telegram",
              category: "communication",
              kind: "channel",
              description: "External messaging channel backed by the existing Telegram bot.",
              status: telegramLinked ? "provider_ready" : "provider_ready_link_required",
              status_reason: telegramLinked
                ? "telegram_channel_linked_to_authenticated_user"
                : telegramLinkPending
                  ? "telegram_link_code_generated_waiting_for_chat_confirmation"
                  : "telegram_user_link_required_before_channel_can_be_used",
              enabled: telegramLinked,
              integral: false,
              provider: { name: "telegram", ready: true, configured: true },
              user_control: {
                toggle_allowed: true,
                preference_supported: true,
                requested_enabled: true,
              },
              link_required: !telegramLinked,
              link_state: telegramLinked ? "linked" : telegramLinkPending ? "pending_confirmation" : "not_linked",
              capabilities: ["telegram.delivery", "telegram.ingress"],
              skill_tool_bindings: [],
              next_actions: telegramLinked ? ["telegram_link_confirmed"] : ["generate_link_code_and_confirm_from_telegram_chat"],
              source_of_truth: ["/health.conversation_channels.telegram"],
            },
          ],
        },
        {
          id: "task_management",
          title: "Task Management",
          description: "Runtime-backed external task systems that can be inspected or enabled through existing provider contracts.",
          item_count: 1,
          items: [
            {
              id: "clickup",
              label: "ClickUp",
              category: "task_management",
              kind: "integration",
              description: "Current production task-system integration for listing and updating external tasks.",
              status: clickupReady ? "provider_ready" : "provider_configuration_required",
              status_reason: clickupReady
                ? "ClickUp preference is enabled in this characterization."
                : "Provider credentials are not configured in this characterization.",
              enabled: clickupReady && clickupEnabled,
              integral: false,
              provider: { name: "clickup", ready: clickupReady, configured: clickupReady },
              user_control: {
                toggle_allowed: true,
                preference_supported: true,
                requested_enabled: clickupEnabled,
              },
              link_required: false,
              link_state: "not_applicable",
              capabilities: [
                "task_system.clickup_create_task",
                "task_system.clickup_list_tasks",
                "task_system.clickup_update_task",
              ],
              skill_tool_bindings: [
                skillBinding({
                  skillId: "clickup_task_management",
                  label: "ClickUp task management",
                  posture: "read_only_and_confirmation_gated_mutation",
                  allowedOperations: [
                    "task_system.clickup_list_tasks",
                    "task_system.clickup_create_task",
                    "task_system.clickup_update_task",
                  ],
                }),
                skillBinding({
                  skillId: "work_partner_task_management",
                  label: "Work partner task management",
                  posture: "read_only_and_confirmation_gated_mutation",
                  allowedOperations: [
                    "task_system.clickup_list_tasks",
                    "task_system.clickup_create_task",
                    "task_system.clickup_update_task",
                  ],
                }),
              ],
              next_actions: clickupReady ? ["ready_for_clickup_operator_acceptance"] : ["configure_clickup_api_token_and_clickup_list_id"],
              source_of_truth: [
                "/health.connectors.execution_baseline.task_system.clickup_list_tasks",
                "/health.connectors.organizer_tool_stack",
              ],
            },
          ],
        },
        {
          id: "knowledge_and_web",
          title: "Knowledge and Web",
          description: "Integral public-web capabilities that remain bounded and backend-owned.",
          item_count: 2,
          items: [
            {
              id: "web_search",
              label: "Web search",
              category: "knowledge_and_web",
              kind: "tool",
              description: "Integral public web search capability available to the personality within bounded read-only policy.",
              status: "integral_active",
              status_reason: "web_search_ready",
              enabled: true,
              integral: true,
              provider: { name: "duckduckgo_html", ready: true, configured: true },
              user_control: {
                toggle_allowed: false,
                preference_supported: false,
                requested_enabled: null,
              },
              link_required: false,
              link_state: "not_applicable",
              capabilities: ["knowledge_search.search_web", "knowledge_search.suggest_search"],
              skill_tool_bindings: [
                skillBinding({
                  skillId: "web_research",
                  label: "Web research",
                  posture: "read_only",
                  allowedOperations: ["knowledge_search.search_web"],
                }),
                skillBinding({
                  skillId: "website_review",
                  label: "Website review",
                  posture: "read_only_search_support",
                  allowedOperations: ["knowledge_search.search_web"],
                }),
              ],
              next_actions: [],
              source_of_truth: [
                "/health.connectors.execution_baseline.knowledge_search.search_web",
                "/health.connectors.web_knowledge_tools",
              ],
            },
            {
              id: "web_browser",
              label: "Web browser",
              category: "knowledge_and_web",
              kind: "tool",
              description: "Integral single-page reading capability used for bounded website review.",
              status: "integral_active",
              status_reason: "web_browser_ready",
              enabled: true,
              integral: true,
              provider: { name: "generic_http", ready: true, configured: true },
              user_control: {
                toggle_allowed: false,
                preference_supported: false,
                requested_enabled: null,
              },
              link_required: false,
              link_state: "not_applicable",
              capabilities: ["web_browser.read_page", "web_browser.suggest_page_review"],
              skill_tool_bindings: [
                skillBinding({
                  skillId: "website_review",
                  label: "Website review",
                  posture: "read_only",
                  allowedOperations: ["web_browser.read_page", "web_browser.suggest_page_review"],
                }),
                skillBinding({
                  skillId: "web_research",
                  label: "Web research",
                  posture: "optional_read_only_page_review",
                  allowedOperations: ["web_browser.read_page"],
                }),
              ],
              next_actions: [],
              source_of_truth: [
                "/health.connectors.execution_baseline.web_browser.read_page",
                "/health.connectors.web_knowledge_tools",
              ],
            },
          ],
        },
        {
          id: "calendar_and_files",
          title: "Calendar and Files",
          description: "Organizer-style connectors for bounded availability and file-space inspection.",
          item_count: 2,
          items: [
            {
              id: "google_calendar",
              label: "Google Calendar",
              category: "calendar_and_files",
              kind: "integration",
              description: "Bounded calendar availability inspection provider.",
              status: googleCalendarReady ? "provider_ready" : "provider_configuration_required",
              status_reason: googleCalendarReady
                ? "Google Calendar preference is enabled in this characterization."
                : "Provider credentials are not configured in this characterization.",
              enabled: googleCalendarReady && googleCalendarEnabled,
              integral: false,
              provider: { name: "google_calendar", ready: googleCalendarReady, configured: googleCalendarReady },
              user_control: {
                toggle_allowed: true,
                preference_supported: true,
                requested_enabled: googleCalendarEnabled,
              },
              link_required: false,
              link_state: "not_applicable",
              capabilities: ["calendar.google_calendar_read_availability"],
              skill_tool_bindings: [],
              next_actions: googleCalendarReady
                ? ["ready_for_google_calendar_operator_acceptance"]
                : ["configure_google_calendar_access_token_calendar_id_and_timezone"],
              source_of_truth: [
                "/health.connectors.execution_baseline.calendar.google_calendar_read_availability",
                "/health.connectors.organizer_tool_stack",
              ],
            },
            {
              id: "google_drive",
              label: "Google Drive",
              category: "calendar_and_files",
              kind: "integration",
              description: "Bounded file-space inspection provider for metadata listing.",
              status: googleDriveReady ? "provider_ready" : "provider_configuration_required",
              status_reason: googleDriveReady
                ? "Google Drive preference is enabled in this characterization."
                : "Provider credentials are not configured in this characterization.",
              enabled: googleDriveReady && googleDriveEnabled,
              integral: false,
              provider: { name: "google_drive", ready: googleDriveReady, configured: googleDriveReady },
              user_control: {
                toggle_allowed: true,
                preference_supported: true,
                requested_enabled: googleDriveEnabled,
              },
              link_required: false,
              link_state: "not_applicable",
              capabilities: ["cloud_drive.google_drive_list_files"],
              skill_tool_bindings: [],
              next_actions: googleDriveReady
                ? ["ready_for_google_drive_operator_acceptance"]
                : ["configure_google_drive_access_token_and_folder_id"],
              source_of_truth: [
                "/health.connectors.execution_baseline.cloud_drive.google_drive_list_files",
                "/health.connectors.organizer_tool_stack",
              ],
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
      integral_enabled_count: groups
        .flatMap((group) => group.items)
        .filter((item) => item.integral && item.enabled).length,
      provider_ready_count: groups
        .flatMap((group) => group.items)
        .filter((item) => item.provider.ready).length,
      provider_blocked_count: groups
        .flatMap((group) => group.items)
        .filter((item) => !item.provider.ready).length,
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
  requests.seenPaths.push(`${request.method} ${url.pathname}`);

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
    jsonResponse(
      response,
      200,
      toolsOverview({
        empty: activeCase === "empty",
        telegramLinkPending: activeCase === "telegram-pending",
      }),
    );
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

async function waitForRequest(predicate, label, timeoutMs = 5000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    if (predicate()) {
      return;
    }
    await new Promise((resolveDelay) => setTimeout(resolveDelay, 100));
  }
  const diagnosticText = await evaluate(
    cdp,
    `document.body ? document.body.innerText.replace(/\\s+/g, " ").slice(0, 800) : ""`,
  ).catch(() => "");
  throw new Error(`Timed out waiting for ${label}. Body excerpt: ${diagnosticText}`);
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
  let fullState;
  try {
    fullState = await waitFor(
      cdp,
      `(() => {
      const text = document.body.textContent ?? "";
      if (!document.querySelector(".aion-tools-directory")) {
        return null;
      }
      const itemCards = document.querySelectorAll(".aion-tools-item-card");
      if (itemCards.length === 0) {
        return null;
      }
      const telegramCard = Array.from(itemCards)
        .find((candidate) => candidate.innerText.includes("Telegram"));
      return {
        groupCount: document.querySelectorAll(".aion-tools-group").length,
        itemCount: itemCards.length,
        toggleCount: document.querySelectorAll(".aion-tools-item-card input[type='checkbox']").length,
        hasTelegramLinkPanel: Boolean(telegramCard?.querySelector("button")),
        capabilityChipCount: document.querySelectorAll(".aion-tools-capability-chip").length,
        setupGuideCount: document.querySelectorAll(".aion-tools-setup-guide").length,
        integralSetupGuideCount: Array.from(itemCards)
          .filter((candidate) => candidate.innerText.includes("Internal chat") || candidate.innerText.includes("Web search") || candidate.innerText.includes("Web browser"))
          .filter((candidate) => candidate.querySelector(".aion-tools-setup-guide")).length,
        technicalDetailsCount: document.querySelectorAll(".aion-tools-details").length,
        hasBindingAuthority: text.includes("metadata_only_not_execution_authority"),
        hasBindingOperations: text.includes("task_system.clickup_update_task"),
        hasFullNextAction: text.includes("Start Telegram link confirmation"),
        hasSetupBoundary: text.includes("Overview only. Secrets and execution stay in the backend action layer."),
        hasClickUpSetup: text.includes("Add ClickUp token and list ID"),
        hasCalendarSetup: text.includes("Connect Google Calendar access"),
        hasDriveSetup: text.includes("Connect Google Drive folder access"),
        leaksEnvNames: /CLICKUP_API_TOKEN|GOOGLE_CALENDAR_ACCESS_TOKEN|GOOGLE_DRIVE_ACCESS_TOKEN/.test(text),
        textExcerpt: text.replace(/\\s+/g, " ").slice(0, 1000),
      };
    })()`,
      "full tools directory",
    );
  } catch (error) {
    throw new Error(`${error.message} Requests seen: ${requests.seenPaths.join(" | ")}`);
  }
  assert(
    fullState.groupCount === 4,
    `Expected four tools groups in the full state. State: ${JSON.stringify(fullState)}`,
  );
  assert(
    fullState.itemCount === 7,
    `Expected seven tools item cards in the full state. State: ${JSON.stringify(fullState)}`,
  );
  assert(
    fullState.toggleCount === 4,
    `Expected four user-control toggles in the full state. State: ${JSON.stringify(fullState)}`,
  );
  assert(
    fullState.hasTelegramLinkPanel,
    `Expected Telegram link panel button in the full state. Text excerpt: ${fullState.textExcerpt}`,
  );
  assert(
    fullState.capabilityChipCount === 21,
    `Expected three backend capability chips per tool card. State: ${JSON.stringify(fullState)}`,
  );
  assert(
    fullState.setupGuideCount === 4,
    `Expected setup guidance for four external provider/channel cards. State: ${JSON.stringify(fullState)}`,
  );
  assert(
    fullState.integralSetupGuideCount === 0,
    `Expected integral tools not to render setup guidance. State: ${JSON.stringify(fullState)}`,
  );
  assert(
    fullState.hasSetupBoundary,
    `Expected setup guidance to explain frontend/backend execution boundary. State: ${JSON.stringify(fullState)}`,
  );
  assert(
    fullState.hasClickUpSetup && fullState.hasCalendarSetup && fullState.hasDriveSetup,
    `Expected friendly setup copy for blocked providers. State: ${JSON.stringify(fullState)}`,
  );
  assert(
    fullState.leaksEnvNames === false,
    `Expected setup guidance not to expose environment variable names. State: ${JSON.stringify(fullState)}`,
  );
  assert(fullState.technicalDetailsCount === 7, "Expected technical details disclosures in the full state.");
  assert(
    fullState.hasBindingAuthority,
    `Expected skill binding authority details to be present in disclosures. State: ${JSON.stringify(fullState)}`,
  );
  assert(
    fullState.hasBindingOperations,
    `Expected skill binding allowed operations to be present in disclosures. State: ${JSON.stringify(fullState)}`,
  );
  assert(
    fullState.hasFullNextAction,
    `Expected full next actions to be present in disclosures. State: ${JSON.stringify(fullState)}`,
  );
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
    `(() => {
      const card = Array.from(document.querySelectorAll(".aion-tools-item-card"))
        .find((candidate) => candidate.innerText.includes("ClickUp"));
      return Boolean(card?.querySelector("input[type='checkbox']:checked"));
    })()`,
    "tool preference toggle checked state",
  );
  await waitForRequest(
    () => requests.preferenceBodies.some((body) => body.clickup_enabled === true),
    "tool preference request",
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
        .find((candidate) => candidate.closest(".aion-tools-item-card")?.innerText.includes("Telegram"));
      button?.click();
      return Boolean(button);
    })()`,
  );
  await waitForRequest(
    () => requests.telegramLinkStarts > 0,
    "telegram link start request",
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

  await navigate(cdp, `${baseUrl}/tools?case=telegram-pending&cacheBust=${Date.now()}`);
  const pendingTelegramState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      if (!text.includes("Code generated. Waiting for Telegram chat confirmation.")) {
        return null;
      }
      return {
        hasPendingCopy: true,
        hasPendingState: text.includes("Pending confirmation"),
        hasNoCodeFallback: text.includes("No active link code yet"),
      };
    })()`,
    "pending Telegram link state",
  );
  assert(
    pendingTelegramState.hasPendingCopy,
    `Expected Telegram pending confirmation copy. State: ${JSON.stringify(pendingTelegramState)}`,
  );
  assert(
    pendingTelegramState.hasNoCodeFallback === false,
    `Expected pending link state not to show no-code fallback. State: ${JSON.stringify(pendingTelegramState)}`,
  );
  assert(
    pendingTelegramState.hasPendingState,
    `Expected pending link state value to be formatted as pending confirmation. State: ${JSON.stringify(pendingTelegramState)}`,
  );
  results.push({ case: "telegram_link_pending", status: "ok", ...pendingTelegramState });

  await navigate(cdp, `${baseUrl}/tools?case=slow&cacheBust=${Date.now()}`);
  const loadingState = await waitFor(
    cdp,
    `Boolean(document.querySelector(".aion-tools-directory")) && document.querySelectorAll(".aion-tools-item-card").length === 0`,
    "tools loading state",
    1000,
  );
  assert(loadingState === true, "Expected tools loading state to render during a delayed overview request.");
  results.push({ case: "loading", status: "ok" });
  await waitFor(
    cdp,
    `document.querySelectorAll(".aion-tools-item-card").length === 7`,
    "slow tools completion",
  );

  await navigate(cdp, `${baseUrl}/tools?case=empty&cacheBust=${Date.now()}`);
  const emptyState = await waitFor(
    cdp,
    `(() => {
      const text = document.body.innerText;
      if (!document.querySelector(".aion-tools-directory")) {
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
