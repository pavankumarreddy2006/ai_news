import { Helmet } from "react-helmet-async";
import { useQuery } from "@tanstack/react-query";
import { HeroPanel } from "@/components/dashboard/HeroPanel";
import { StatsGrid } from "@/components/dashboard/StatsGrid";
import { SectionHeader } from "@/components/widgets/SectionHeader";
import { LiveUpdatesPanel } from "@/components/widgets/LiveUpdatesPanel";
import { TeachMePanel } from "@/components/ai/TeachMePanel";
import { NewsCard } from "@/components/cards/NewsCard";
import { ToolCard } from "@/components/cards/ToolCard";
import { useNewsQuery } from "@/features/news/useNewsQuery";
import { useToolsQuery } from "@/features/tools/useToolsQuery";
import { platformApi } from "@/services/platformApi";

export function HomePage() {
  const { data: news = [], isLoading: newsLoading, isError: newsError } = useNewsQuery();
  const { data: tools = [], isLoading: toolsLoading } = useToolsQuery();
  const { data: categories = { categories: [] } } = useQuery({ queryKey: ["categories"], queryFn: platformApi.getCategories });

  return (
    <div className="space-y-8">
      <Helmet>
        <title>AI News Platform</title>
        <meta name="description" content="AI news, launches, tools, live updates, and beginner-friendly AI learning." />
      </Helmet>
      <HeroPanel categories={categories.categories.slice(0, 8)} />
      <StatsGrid
        stats={[
          { label: "Ranked AI stories", value: newsLoading ? "..." : news.length, note: "Fresh AI updates cleaned and simplified." },
          { label: "Tracked AI tools", value: toolsLoading ? "..." : tools.length, note: "Searchable directory with AI rankings." },
          { label: "Realtime feed", value: "24/7", note: "Live WebSocket updates across the dashboard." },
          { label: "Beginner mode", value: "On", note: "Every article includes easy English context." },
        ]}
      />
      <div className="grid gap-8 xl:grid-cols-[1.7fr_1fr]">
        <section>
          <SectionHeader eyebrow="Top Stories" title="Ranked AI News" description="The strongest AI launches, tutorials, tools, and startup shifts happening right now." />
          {newsError ? <div className="glass rounded-[24px] p-6 text-sm text-amber-200">News could not load from the API right now. The backend fallback content should appear again after the next refresh.</div> : null}
          {!newsError && !news.length && !newsLoading ? <div className="glass rounded-[24px] p-6 text-sm text-slate-300">No stories are available yet. The backend is preparing the next AI digest.</div> : null}
          <div className="grid gap-5 md:grid-cols-2">
            {news.slice(0, 6).map((item) => <NewsCard key={item.id} item={item} />)}
          </div>
        </section>
        <div className="space-y-6">
          <LiveUpdatesPanel />
          <TeachMePanel />
        </div>
      </div>
      <section>
        <SectionHeader eyebrow="AI Directory" title="Recommended AI Tools" description="High-signal AI products across coding, automation, chat, and media." />
        <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">
          {tools.map((tool) => <ToolCard key={tool.id} tool={tool} />)}
        </div>
      </section>
    </div>
  );
}
