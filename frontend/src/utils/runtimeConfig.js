const normalizeUrl = (value) => value?.replace(/\/+$/, "") || "";

const inferRenderBackendOrigin = () => {
  if (typeof window === "undefined") {
    return "http://localhost:10000";
  }
  const { origin, hostname } = window.location;
  if (hostname.includes("localhost") || hostname === "127.0.0.1") {
    return "http://localhost:10000";
  }
  if (hostname.includes("frontend")) {
    return origin.replace("frontend", "backend");
  }
  return origin;
};

export const getApiBaseUrl = () =>
  normalizeUrl(import.meta.env.VITE_API_URL) ||
  normalizeUrl(import.meta.env.VITE_API_BASE_URL) ||
  inferRenderBackendOrigin();

export const getWsBaseUrl = () => {
  const configured = normalizeUrl(import.meta.env.VITE_WS_URL);
  if (configured) {
    return configured;
  }
  const apiBase = getApiBaseUrl();
  if (apiBase.startsWith("https://")) {
    return apiBase.replace("https://", "wss://");
  }
  if (apiBase.startsWith("http://")) {
    return apiBase.replace("http://", "ws://");
  }
  return apiBase;
};
