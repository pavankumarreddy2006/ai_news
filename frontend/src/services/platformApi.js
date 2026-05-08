import { apiClient } from "@/api/client";

export const platformApi = {
  getNews: async (params) => (await apiClient.get("/api/news", { params })).data,
  getTrending: async () => (await apiClient.get("/api/trending")).data,
  getTools: async (params) => (await apiClient.get("/api/tools", { params })).data,
  getCategories: async () => (await apiClient.get("/api/categories")).data,
  getRecommendations: async () => (await apiClient.get("/api/recommendations")).data,
  search: async (query) => (await apiClient.get("/api/search", { params: { query } })).data,
  getSummary: async (id) => (await apiClient.get(`/api/summary/${id}`)).data,
  learn: async (topic) => (await apiClient.post("/api/learn", { topic })).data,
  savePreferences: async (payload) => (await apiClient.post("/api/preferences", payload)).data,
  saveArticle: async (payload) => (await apiClient.post("/api/preferences/save-article", payload)).data,
  getSavedArticles: async (sessionId) => (await apiClient.get(`/api/preferences/saved/${sessionId}`)).data,
  subscribeTelegram: async (payload) => (await apiClient.post("/api/telegram/subscribe", payload)).data,
  sendTelegramDigest: async () => (await apiClient.post("/api/telegram/send-digest")).data,
  getLiveStatus: async () => (await apiClient.get("/api/live")).data,
};

