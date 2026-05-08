import { useSearchParams } from "react-router-dom";
import { NewsCard } from "@/components/cards/NewsCard";
import { ToolCard } from "@/components/cards/ToolCard";
import { useSearchQuery } from "@/features/search/useSearchQuery";

export function SearchPage() {
  const [params] = useSearchParams();
  const query = params.get("q") || "AI";
  const { data } = useSearchQuery(query);

  return (
    <div className="space-y-8">
      <section className="glass rounded-[28px] p-6">
        <h1 className="text-3xl font-semibold text-white">Search AI</h1>
        <p className="mt-2 text-sm text-slate-400">Results for “{query}”.</p>
      </section>
      <section>
        <h2 className="mb-4 text-xl font-semibold text-white">News</h2>
        <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
          {(data?.news || []).map((item) => <NewsCard key={item.id} item={item} />)}
        </div>
      </section>
      <section>
        <h2 className="mb-4 text-xl font-semibold text-white">Tools</h2>
        <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
          {(data?.tools || []).map((tool) => <ToolCard key={tool.id} tool={tool} />)}
        </div>
      </section>
    </div>
  );
}

