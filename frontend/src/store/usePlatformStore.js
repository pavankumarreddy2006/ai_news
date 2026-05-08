import { create } from "zustand";

const getSessionId = () => {
  if (typeof window === "undefined") return "server";
  const existing = window.localStorage.getItem("ai-news-session");
  if (existing) return existing;
  const generated = crypto.randomUUID();
  window.localStorage.setItem("ai-news-session", generated);
  return generated;
};

export const usePlatformStore = create((set) => ({
  sessionId: getSessionId(),
  activeCategory: "All",
  notifications: [],
  liveEvents: [],
  savedIds: [],
  setActiveCategory: (activeCategory) => set({ activeCategory }),
  addNotification: (notification) =>
    set((state) => ({
      notifications: [{ id: crypto.randomUUID(), ...notification }, ...state.notifications].slice(0, 10),
    })),
  addLiveEvent: (event) =>
    set((state) => ({
      liveEvents: [{ id: crypto.randomUUID(), ...event }, ...state.liveEvents].slice(0, 20),
    })),
  markSaved: (articleId) =>
    set((state) => ({
      savedIds: state.savedIds.includes(articleId) ? state.savedIds : [...state.savedIds, articleId],
    })),
}));

