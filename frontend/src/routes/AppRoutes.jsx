import { Routes, Route } from "react-router-dom";
import { HomePage } from "@/pages/Home/HomePage";
import { TrendingPage } from "@/pages/Trending/TrendingPage";
import { NewsPage } from "@/pages/News/NewsPage";
import { ToolsPage } from "@/pages/Tools/ToolsPage";
import { LearnAIPage } from "@/pages/LearnAI/LearnAIPage";
import { SearchPage } from "@/pages/Search/SearchPage";
import { SavedPage } from "@/pages/Saved/SavedPage";
import { SettingsPage } from "@/pages/Settings/SettingsPage";
import { NotFoundPage } from "@/pages/NotFound/NotFoundPage";

export function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/trending" element={<TrendingPage />} />
      <Route path="/news" element={<NewsPage />} />
      <Route path="/tools" element={<ToolsPage />} />
      <Route path="/learn-ai" element={<LearnAIPage />} />
      <Route path="/search" element={<SearchPage />} />
      <Route path="/saved" element={<SavedPage />} />
      <Route path="/settings" element={<SettingsPage />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}

