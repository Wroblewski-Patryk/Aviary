import routeManifest from "./route-manifest.json";

export type RoutePath =
  | "/login"
  | "/dashboard"
  | "/chat"
  | "/memory"
  | "/reflections"
  | "/plans"
  | "/goals"
  | "/insights"
  | "/automations"
  | "/integrations"
  | "/settings"
  | "/personality"
  | "/tools";

export type RouteManifestEntry = {
  path: "/" | RoutePath;
  marker: string;
  authenticated: boolean;
  screenshot: boolean;
  canonicalSurface: string;
};

export const ROUTE_MANIFEST = routeManifest.routes as RouteManifestEntry[];

export const ROUTES = ROUTE_MANIFEST.filter(
  (route): route is RouteManifestEntry & { path: RoutePath } => route.authenticated && route.path !== "/",
).map((route) => route.path);

export const ROUTE_MARKERS = Object.fromEntries(
  ROUTE_MANIFEST.map((route) => [route.path, route.marker]),
) as Record<"/" | RoutePath, string>;

export function normalizeRoute(pathname: string): RoutePath {
  if (pathname === "/dashboard") {
    return "/dashboard";
  }
  if (pathname === "/") {
    return "/login";
  }
  if (ROUTES.includes(pathname as RoutePath)) {
    return pathname as RoutePath;
  }
  return "/login";
}

export function navigate(path: RoutePath) {
  if (window.location.pathname !== path) {
    window.history.pushState({}, "", path);
  }
}

export function navigatePublicEntry(path: "/" | "/login") {
  if (window.location.pathname !== path) {
    window.history.pushState({}, "", path);
  }
}
