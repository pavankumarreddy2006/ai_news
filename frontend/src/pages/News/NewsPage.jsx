import { useSearchParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { CategoryFilterBar } from "@/components/widgets/CategoryFilterBar";
import { NewsCard } from "@/components/cards/NewsCard";
import { usePlatformStore } from "@/store/usePlatformStore";
import { useNewsQuery } from "@/features/news/useNewsQuery";
import { platformApi } from "@/services/platformApi";

export function NewsPage() {
  const [params] = useSearchParams();
  const routeCategory = params.get("category") || "All";
  const activeCategory = usePlatformStore((state) => state.activeCategory);
  const setActiveCategory = usePlatformStore((state) => state.setActiveCategory);
  const selectedCategory = activeCategory === "All" ? routeCategory : activeCategory;
  const { data: categories = { categories: [] } } = useQuery({ queryKey: ["categories"], queryFn: platformApi.getCategories });
  const { data: news = [] } = useNewsQuery(selectedCategory);

  return (
    <div className="space-y-6">
      <section className="glass rounded-[28px] p-6">
        <h1 className="text-3xl font-semibold text-white">AI News Feed</h1>
        <p className="mt-2 text-sm text-slate-400">Fresh AI updates with ranking, beginner summaries, and importance signals.</p>
        <div className="mt-5">
          <CategoryFilterBar categories={categories.categories.slice(0, 8)} activeCategory={selectedCategory} onSelect={setActiveCategory} />
        </div>
      </section>
      <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
        {news.map((item) => <NewsCard key={item.id} item={item} />)}
      </div>
    </div>
  );
}

