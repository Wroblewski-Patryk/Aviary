import assert from "node:assert/strict";
import { createRequire } from "node:module";
import { dirname, resolve } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

import "./recent-activity.test.ts";

const WEB_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const dependencyRoot = process.env.ROOST_TEST_DEPENDENCY_ROOT;
assert.ok(dependencyRoot, "ROOST_TEST_DEPENDENCY_ROOT must identify the sealed test toolkit");

const toolkitRequire = createRequire(resolve(dependencyRoot, "package.json"));
const ts = toolkitRequire("typescript");

function formatDiagnostics(diagnostics) {
  return ts.formatDiagnosticsWithColorAndContext(diagnostics, {
    getCanonicalFileName: (fileName) => fileName,
    getCurrentDirectory: () => WEB_ROOT,
    getNewLine: () => "\n",
  });
}

function parseNodeProject(configPath, optionsToExtend) {
  const unrecoverableDiagnostics = [];
  const parsed = ts.getParsedCommandLineOfConfigFile(configPath, optionsToExtend, {
    ...ts.sys,
    onUnRecoverableConfigFileDiagnostic: (diagnostic) => {
      unrecoverableDiagnostics.push(diagnostic);
    },
  });
  assert.ok(parsed, formatDiagnostics(unrecoverableDiagnostics));
  assert.deepEqual(unrecoverableDiagnostics, []);
  return parsed;
}

function withoutEmissionOverrides(options) {
  const preserved = { ...options };
  delete preserved.composite;
  delete preserved.incremental;
  delete preserved.noEmit;
  delete preserved.tsBuildInfoFile;
  return preserved;
}

test("installed node project has no TypeScript diagnostics", () => {
  const configPath = resolve(WEB_ROOT, "tsconfig.node.json");
  const original = parseNodeProject(configPath, {});
  const parsed = parseNodeProject(configPath, {
    composite: false,
    incremental: false,
    noEmit: true,
  });

  assert.deepEqual(parsed.fileNames, original.fileNames);
  assert.deepEqual(withoutEmissionOverrides(parsed.options), withoutEmissionOverrides(original.options));
  assert.equal(parsed.options.composite, false);
  assert.equal(parsed.options.incremental, false);
  assert.equal(parsed.options.noEmit, true);
  assert.deepEqual(parsed.errors, []);

  const program = ts.createProgram({
    rootNames: parsed.fileNames,
    options: parsed.options,
    projectReferences: parsed.projectReferences,
  });
  const diagnostics = ts.getPreEmitDiagnostics(program);
  assert.equal(diagnostics.length, 0, formatDiagnostics(diagnostics));
});
