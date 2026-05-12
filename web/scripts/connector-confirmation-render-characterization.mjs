import { createRequire } from "node:module";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const React = require("react");
const { renderToStaticMarkup } = require("react-dom/server");
const ts = require("typescript");

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const chatSource = readFileSync(resolve(ROOT, "src/components/chat.tsx"), "utf8");

const transpiled = ts.transpileModule(chatSource, {
  compilerOptions: {
    esModuleInterop: true,
    jsx: ts.JsxEmit.ReactJSX,
    module: ts.ModuleKind.CommonJS,
    target: ts.ScriptTarget.ES2020,
  },
  fileName: "chat.tsx",
}).outputText;

const moduleShim = { exports: {} };
new Function("require", "exports", "module", transpiled)(require, moduleShim.exports, moduleShim);

const { ChatComposerShell } = moduleShim.exports;
if (typeof ChatComposerShell !== "function") {
  throw new Error("ChatComposerShell was not exported from the transpiled component module.");
}

const pendingConfirmation = {
  status: "pending_confirmation",
  source_event_id: "connector-confirmation-event",
  trace_id: "connector-confirmation-trace",
  connector_kind: "task_system",
  provider_hint: "clickup",
  operation: "update_task",
  mode: "mutate_with_confirmation",
  candidate_summary: "Update ClickUp task #123 to Done",
  source_reference: "action_result.observations[0]",
  reason: "Explicit user confirmation is required before updating ClickUp.",
};

function icon(label) {
  return React.createElement("span", { "aria-hidden": "true" }, label);
}

function baseProps(overrides) {
  return {
    quickActions: [],
    text: "",
    placeholder: "Send a message...",
    sending: false,
    sendLabel: "Send message",
    note: "AION may make mistakes.",
    pendingConfirmation: null,
    pendingConfirmationLabel: "Confirmation required",
    pendingConfirmationBlockedLabel: "Blocked",
    pendingConfirmationConfirmLabel: "Confirm",
    pendingConfirmationSubmittingLabel: "Confirming...",
    pendingConfirmationCompleteLabel: "Confirmation complete",
    pendingConfirmationState: "idle",
    pendingConfirmationFeedback: null,
    addIcon: icon("+"),
    voiceIcon: icon("voice"),
    sendIcon: icon("send"),
    onQuickAction: () => {},
    onConfirmPendingConfirmation: () => {},
    onTextChange: () => {},
    onSubmit: () => {},
    ...overrides,
  };
}

function renderCase(name, overrides) {
  return {
    name,
    html: renderToStaticMarkup(React.createElement(ChatComposerShell, baseProps(overrides))),
  };
}

function assertIncludes(source, needle, label) {
  if (!source.includes(needle)) {
    throw new Error(`Missing ${label}: ${needle}`);
  }
}

function assertExcludes(source, needle, label) {
  if (source.includes(needle)) {
    throw new Error(`Unexpected ${label}: ${needle}`);
  }
}

function assertMatches(source, pattern, label) {
  if (!pattern.test(source)) {
    throw new Error(`Missing ${label}: ${pattern}`);
  }
}

const cases = [
  renderCase("pending", {
    pendingConfirmation,
    pendingConfirmationState: "idle",
  }),
  renderCase("submitting", {
    pendingConfirmation,
    pendingConfirmationState: "submitting",
    pendingConfirmationFeedback: "Confirming...",
  }),
  renderCase("success", {
    pendingConfirmation: null,
    pendingConfirmationState: "success",
    pendingConfirmationFeedback: "ClickUp task updated.",
  }),
  renderCase("error", {
    pendingConfirmation,
    pendingConfirmationState: "error",
    pendingConfirmationFeedback: "confirmation_stale",
  }),
];

const pendingHtml = cases.find((entry) => entry.name === "pending").html;
assertIncludes(pendingHtml, "Confirmation required", "pending eyebrow");
assertIncludes(pendingHtml, "clickup", "provider hint");
assertIncludes(pendingHtml, "update_task", "operation");
assertIncludes(pendingHtml, "Update ClickUp task #123 to Done", "candidate summary");
assertIncludes(pendingHtml, "Blocked", "blocked chip");
assertMatches(pendingHtml, />Confirm<\/button>/, "enabled confirm button");
assertExcludes(pendingHtml, "disabled", "pending disabled button state");

const submittingHtml = cases.find((entry) => entry.name === "submitting").html;
assertIncludes(submittingHtml, "Confirming...", "submitting copy");
assertIncludes(submittingHtml, "aion-chat-pending-confirmation-feedback-submitting", "submitting feedback class");
assertMatches(submittingHtml, /<button[^>]*disabled=""[^>]*>Confirming\.\.\.<\/button>/, "disabled submitting button");

const successHtml = cases.find((entry) => entry.name === "success").html;
assertIncludes(successHtml, "Confirmation complete", "success eyebrow");
assertIncludes(successHtml, "ClickUp task updated.", "success feedback");
assertIncludes(successHtml, "aion-chat-pending-confirmation-feedback-success", "success feedback class");
assertExcludes(successHtml, "Confirmation required", "stale pending eyebrow");
assertExcludes(successHtml, ">Confirm</button>", "success confirm button");

const errorHtml = cases.find((entry) => entry.name === "error").html;
assertIncludes(errorHtml, "Confirmation required", "error pending eyebrow");
assertIncludes(errorHtml, "Update ClickUp task #123 to Done", "error candidate summary");
assertIncludes(errorHtml, "confirmation_stale", "error feedback");
assertIncludes(errorHtml, "aion-chat-pending-confirmation-feedback-error", "error feedback class");
assertMatches(errorHtml, />Confirm<\/button>/, "retry confirm button");
assertExcludes(errorHtml, "disabled", "error disabled button state");

console.log(
  JSON.stringify(
    {
      kind: "connector_confirmation_render_characterization_report",
      schema_version: 1,
      status: "ok",
      cases: cases.map((entry) => ({
        name: entry.name,
        markup_length: entry.html.length,
      })),
    },
    null,
    2,
  ),
);
