import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, resolve } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const WEB_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const dependencyRoot = process.env.ROOST_TEST_DEPENDENCY_ROOT;
assert.ok(dependencyRoot, "ROOST_TEST_DEPENDENCY_ROOT must identify the sealed test toolkit");

const toolkitRequire = createRequire(resolve(dependencyRoot, "package.json"));
const React = toolkitRequire("react");
const { renderToStaticMarkup } = toolkitRequire("react-dom/server");
const ts = toolkitRequire("typescript");

function loadTrackedModule(relativePath) {
  const filename = resolve(WEB_ROOT, relativePath);
  const source = readFileSync(filename, "utf8");
  const transpiled = ts.transpileModule(source, {
    compilerOptions: {
      esModuleInterop: true,
      jsx: ts.JsxEmit.ReactJSX,
      module: ts.ModuleKind.CommonJS,
      target: ts.ScriptTarget.ES2020,
    },
    fileName: filename,
  });
  const module = { exports: {} };
  const execute = new Function("exports", "require", "module", "__filename", "__dirname", transpiled.outputText);
  execute(module.exports, toolkitRequire, module, filename, dirname(filename));
  return module.exports;
}

const formatting = loadTrackedModule("src/lib/learned-state-formatting.ts");
const dashboard = loadTrackedModule("src/components/dashboard.tsx");
const shared = loadTrackedModule("src/components/shared.tsx");

test("recentActivityRows returns no rows for absent or unusable activity", () => {
  const cases = [
    null,
    {},
    { recent_activity: null },
    { recent_activity: "not-an-array" },
    { recent_activity: [] },
    { recent_activity: [null, 42, "event", {}, { title: "  " }, { summary: "" }] },
  ];

  for (const overview of cases) {
    assert.deepEqual(formatting.recentActivityRows(overview, "en-US", "Unknown time"), []);
  }
});

test("recentActivityRows preserves valid identity, text, time, and input order in mixed activity", () => {
  const timestamp = "2026-10-04T01:02:03.000Z";
  const rows = formatting.recentActivityRows(
    {
      recent_activity: [
        null,
        { event_id: "event-17", title: "First actual event", timestamp },
        { title: "" },
        { summary: "Second actual event" },
        { title: "Third actual event", event_timestamp: "unparsed-time" },
      ],
    },
    "en-US",
    "Unknown time",
  );

  assert.deepEqual(rows, [
    {
      key: "event-17",
      title: "First actual event",
      when: formatting.formatTimestamp(timestamp, "en-US"),
    },
    {
      key: "activity-3-Second actual event",
      title: "Second actual event",
      when: "Unknown time",
    },
    {
      key: "activity-4-Third actual event",
      title: "Third actual event",
      when: "unparsed-time",
    },
  ]);
});

test("DashboardRecentActivityList renders neutral empty copy or actual rows, never both", () => {
  const emptyLabel = "No data available";
  const emptyHtml = renderToStaticMarkup(
    React.createElement(dashboard.DashboardRecentActivityList, { items: [], emptyLabel }),
  );
  assert.match(emptyHtml, /No data available/);
  assert.doesNotMatch(emptyHtml, /<article/);

  const populatedHtml = renderToStaticMarkup(
    React.createElement(dashboard.DashboardRecentActivityList, {
      emptyLabel,
      items: [{ key: "real-event", title: "Actual dashboard event", when: "Just now" }],
    }),
  );
  assert.match(populatedHtml, /Actual dashboard event/);
  assert.match(populatedHtml, /Just now/);
  assert.match(populatedHtml, /<article/);
  assert.doesNotMatch(populatedHtml, /No data available/);
});

test("ModuleActivityList renders neutral empty copy or actual rows, never both", () => {
  const emptyLabel = "No data available";
  const emptyHtml = renderToStaticMarkup(
    React.createElement(shared.ModuleActivityList, { routeKey: "memory", items: [], emptyLabel }),
  );
  assert.match(emptyHtml, /No data available/);
  assert.doesNotMatch(emptyHtml, /<article/);

  const populatedHtml = renderToStaticMarkup(
    React.createElement(shared.ModuleActivityList, {
      routeKey: "memory",
      emptyLabel,
      items: [{ key: "real-event", title: "Actual module event", when: "Earlier" }],
    }),
  );
  assert.match(populatedHtml, /Actual module event/);
  assert.match(populatedHtml, /Earlier/);
  assert.match(populatedHtml, /<article/);
  assert.doesNotMatch(populatedHtml, /No data available/);
});

test("App wires the localized neutral empty label to all recent activity consumers", () => {
  const appSource = readFileSync(resolve(WEB_ROOT, "src/App.tsx"), "utf8");
  assert.match(
    appSource,
    /recentActivityRows\(\s*overview,\s*resolvedUiLanguage,\s*copy\.common\.unknownTime,\s*\)/,
  );
  assert.doesNotMatch(
    appSource,
    /recentActivityRows\(\s*overview,\s*resolvedUiLanguage,\s*copy\.common\.recentActivity/,
  );
  assert.match(
    appSource,
    /<DashboardRecentActivityList\s+items=\{personalityRecentActivity\.slice\(0, 4\)\}\s+emptyLabel=\{copy\.common\.noData\}\s+\/>/,
  );
  for (const routeKey of ["memory", "reflections"]) {
    assert.match(
      appSource,
      new RegExp(`<ModuleActivityList\\s+routeKey="${routeKey}"\\s+items=\\{personalityRecentActivity\\.slice\\(0, 4\\)\\}\\s+emptyLabel=\\{copy\\.common\\.noData\\}\\s+\\/>`),
    );
  }
});

test("installed frontend project has no TypeScript diagnostics", () => {
  const configPath = resolve(WEB_ROOT, "tsconfig.app.json");
  const configFile = ts.readConfigFile(configPath, ts.sys.readFile);
  assert.equal(configFile.error, undefined);
  const parsed = ts.parseJsonConfigFileContent(configFile.config, ts.sys, WEB_ROOT, {
    incremental: false,
    noEmit: true,
  }, configPath);
  assert.deepEqual(parsed.errors, []);

  const program = ts.createProgram({
    rootNames: parsed.fileNames,
    options: parsed.options,
    projectReferences: parsed.projectReferences,
  });
  const diagnostics = ts.getPreEmitDiagnostics(program);
  assert.equal(
    diagnostics.length,
    0,
    ts.formatDiagnosticsWithColorAndContext(diagnostics, {
      getCanonicalFileName: (fileName) => fileName,
      getCurrentDirectory: () => WEB_ROOT,
      getNewLine: () => "\n",
    }),
  );
});
