import { Helmet } from "react-helmet-async";
import { useTrendingQuery } from "@/features/trending/useTrendingQuery";
import { NewsCard } from "@/components/cards/NewsCard";

export function TrendingPage() {
  const { data } = useTrendingQuery();
  const topics = data?.topics || [];
  const stories = data?.stories || [];

  return (
    <div className="space-y-8">
      <Helmet><title>Trending AI</title></Helmet>
      <section className="glass rounded-[28px] p-6">
        <h1 className="text-3xl font-semibold text-white">Trending AI</h1>
        <div className="mt-5 flex flex-wrap gap-3">
          {topics.map((topic) => (
            <span key={topic.id} className="rounded-full border border-glow/30 px-4 py-2 text-sm text-glow">{topic.topic} - {topic.score}</span>
          ))}
        </div>
      </section>
      <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
        {stories.map((item) => <NewsCard key={item.id} item={item} />)}
      </div>
    </div>
  );
}
