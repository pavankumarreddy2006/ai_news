const normalizeUrl = (value) => value?.replace(/\/+$/, "") || "";
const DEFAULT_LOCAL_BACKEND = "http://localhost:10000";
const DEFAULT_RENDER_BACKEND = "https://ai-news-backend.onrender.com";

const getInjectedConfig = () => {
  if (typeof window === "undefined") {
    return {};
  }
  return window.__AI_NEWS_CONFIG__ || {};
};

const getMetaContent = (name) => {
  if (typeof document === "undefined") {
    return "";
  }
  return document.querySelector(`meta[name="${name}"]`)?.content || "";
};

const inferRenderBackendOrigin = () => {
  if (typeof window === "undefined") {
    return DEFAULT_LOCAL_BACKEND;
  }
  const { origin, hostname } = window.location;
  if (hostname.includes("localhost") || hostname === "127.0.0.1") {
    return DEFAULT_LOCAL_BACKEND;
  }
  if (hostname.includes("frontend")) {
    return origin.replace("frontend", "backend");
  }
  if (hostname.endsWith(".onrender.com")) {
    return DEFAULT_RENDER_BACKEND;
  }
  return DEFAULT_RENDER_BACKEND;
};

export const getApiBaseUrl = () =>
  normalizeUrl(import.meta.env.VITE_API_URL) ||
  normalizeUrl(import.meta.env.VITE_API_BASE_URL) ||
  normalizeUrl(getInjectedConfig().apiBaseUrl) ||
  normalizeUrl(getMetaContent("ai-news-api-url")) ||
  inferRenderBackendOrigin();

export const getWsBaseUrl = () => {
  const configured = normalizeUrl(import.meta.env.VITE_WS_URL) || normalizeUrl(getInjectedConfig().wsBaseUrl);
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
