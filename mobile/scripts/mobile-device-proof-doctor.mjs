import { spawn } from "node:child_process";
import { mkdirSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const MOBILE_ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const REPO_ROOT = resolve(MOBILE_ROOT, "..");
const DEFAULT_ARTIFACT_DIR = join(
  REPO_ROOT,
  ".codex",
  "artifacts",
  "prj1182-mobile-device-proof-doctor",
);

const CHECKS = [
  {
    name: "adb",
    command: "adb",
    args: ["version"],
    requiredFor: "Android device or emulator proof",
  },
  {
    name: "emulator",
    command: "emulator",
    args: ["-version"],
    requiredFor: "Android emulator launch proof",
  },
];

function optionValue(name, fallback = "") {
  const index = process.argv.indexOf(name);
  if (index === -1) {
    return fallback;
  }
  return process.argv[index + 1] ?? fallback;
}

function run(command, args, timeoutMs = 10000) {
  return new Promise((resolveRun) => {
    const child = spawn(command, args, { windowsHide: true });
    let stdout = "";
    let stderr = "";
    let settled = false;
    const finish = (result) => {
      if (settled) {
        return;
      }
      settled = true;
      clearTimeout(timeout);
      resolveRun(result);
    };
    const timeout = setTimeout(() => {
      child.kill("SIGKILL");
      finish({ code: 1, stdout, stderr: `${stderr}\nTimed out after ${timeoutMs}ms` });
    }, timeoutMs);

    child.stdout?.on("data", (chunk) => {
      stdout += chunk;
    });
    child.stderr?.on("data", (chunk) => {
      stderr += chunk;
    });
    child.on("close", (code) => finish({ code, stdout, stderr }));
    child.on("error", (error) => finish({ code: 1, stdout, stderr: String(error) }));
  });
}

async function main() {
  const artifactDir = resolve(REPO_ROOT, optionValue("--artifacts", DEFAULT_ARTIFACT_DIR));
  const reportPath = resolve(artifactDir, "report.json");
  mkdirSync(artifactDir, { recursive: true });

  const checks = [];
  for (const check of CHECKS) {
    const result = await run(check.command, check.args);
    checks.push({
      name: check.name,
      required_for: check.requiredFor,
      available: result.code === 0,
      command: [check.command, ...check.args].join(" "),
      stdout: result.stdout.trim(),
      stderr: result.stderr.trim(),
    });
  }

  const missing = checks.filter((check) => !check.available);
  const report = {
    status: missing.length === 0 ? "ready" : "blocked",
    blocked: missing.length > 0,
    missing_tools: missing.map((check) => check.name),
    next_action:
      missing.length === 0
        ? "Run Expo Go or simulator proof for Home, Chat, Personality, Settings, and Tools."
        : "Install Android platform tools or connect a supported device before native proof.",
    checks,
  };

  writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
  console.log(JSON.stringify(report, null, 2));
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exitCode = 1;
});
