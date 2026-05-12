import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));

function readProjectFile(path) {
  return readFileSync(resolve(ROOT, path), "utf8");
}

function assertIncludes(source, needle, label) {
  if (!source.includes(needle)) {
    throw new Error(`Missing ${label}: ${needle}`);
  }
}

function assertMatches(source, pattern, label) {
  if (!pattern.test(source)) {
    throw new Error(`Missing ${label}: ${pattern}`);
  }
}

const apiSource = readProjectFile("src/lib/api.ts");
const appSource = readProjectFile("src/App.tsx");
const chatSource = readProjectFile("src/components/chat.tsx");
const cssSource = readProjectFile("src/index.css");
const packageSource = readProjectFile("package.json");

const checks = [];

function check(name, callback) {
  callback();
  checks.push({ name, status: "ok" });
}

check("api_contract", () => {
  assertIncludes(apiSource, "export type AppConnectorConfirmationResponse", "confirmation response type");
  assertIncludes(apiSource, "confirmConnectorAction(", "confirmation API client method");
  assertIncludes(apiSource, '"/app/connectors/confirm"', "confirmation endpoint path");
  assertIncludes(apiSource, "{ ...pendingConfirmation }", "bounded pending payload submission");
});

check("package_script", () => {
  assertIncludes(packageSource, '"test:connector-confirmation"', "package characterization script");
});

check("app_state_matrix", () => {
  assertIncludes(appSource, "connectorConfirmationBusy", "busy state");
  assertIncludes(appSource, "connectorConfirmationFeedback", "feedback state");
  assertIncludes(appSource, "connectorConfirmationFeedbackState", "feedback status state");
  assertIncludes(appSource, 'useState<"idle" | "submitting" | "success" | "error">', "explicit confirmation state union");
  assertIncludes(appSource, "setConnectorConfirmationFeedbackState(\"submitting\")", "submitting transition");
  assertIncludes(appSource, "setConnectorConfirmationFeedbackState(\"success\")", "success transition");
  assertIncludes(appSource, "setConnectorConfirmationFeedbackState(\"error\")", "error transition");
  assertIncludes(appSource, "setPendingConnectorConfirmation(response.pending_confirmation ?? null)", "success pending clear");
  assertMatches(
    appSource,
    /catch \(caught\) \{[\s\S]*setConnectorConfirmationFeedback\(caught instanceof Error/,
    "local fail-closed error feedback",
  );
});

check("localized_copy", () => {
  assertIncludes(appSource, "confirmationRequired", "pending label copy");
  assertIncludes(appSource, "confirmationBlocked", "blocked chip copy");
  assertIncludes(appSource, "confirmationConfirm", "confirm button copy");
  assertIncludes(appSource, "confirmationSubmitting", "submitting copy");
  assertIncludes(appSource, "confirmationComplete", "complete label copy");
  assertIncludes(appSource, "confirmationFailed", "fail-closed copy");
});

check("composer_controls", () => {
  assertIncludes(chatSource, "PendingConnectorConfirmationState", "composer confirmation state type");
  assertIncludes(chatSource, "pendingConfirmationCompleteLabel", "complete label prop");
  assertIncludes(chatSource, "pendingConfirmationBusy", "busy derived state");
  assertIncludes(chatSource, "pendingConfirmationEyebrow", "state-aware eyebrow");
  assertIncludes(chatSource, "disabled={pendingConfirmationBusy}", "duplicate submit guard");
  assertIncludes(chatSource, "onClick={onConfirmPendingConfirmation}", "confirm handler wiring");
  assertIncludes(chatSource, "aion-chat-pending-confirmation-feedback-${pendingConfirmationState}", "state feedback class");
  assertIncludes(chatSource, "aria-live=\"polite\"", "local live region");
});

check("composer_layout", () => {
  assertIncludes(cssSource, ".aion-chat-pending-confirmation-actions", "action stack styles");
  assertIncludes(cssSource, ".aion-chat-pending-confirmation-button", "confirm button styles");
  assertIncludes(cssSource, ".aion-chat-pending-confirmation-feedback-success", "success feedback styles");
  assertIncludes(cssSource, ".aion-chat-pending-confirmation-feedback-error", "error feedback styles");
  assertIncludes(cssSource, "@media (max-width: 640px)", "mobile confirmation layout");
});

console.log(
  JSON.stringify(
    {
      kind: "connector_confirmation_characterization_report",
      schema_version: 1,
      status: "ok",
      checks,
    },
    null,
    2,
  ),
);
