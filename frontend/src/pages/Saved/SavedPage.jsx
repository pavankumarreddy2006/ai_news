import { useQuery } from "@tanstack/react-query";
import { NewsCard } from "@/components/cards/NewsCard";
import { TelegramPanel } from "@/features/telegram/TelegramPanel";
import { platformApi } from "@/services/platformApi";
import { usePlatformStore } from "@/store/usePlatformStore";

export function SavedPage() {
  const sessionId = usePlatformStore((state) => state.sessionId);
  const { data: saved = [] } = useQuery({ queryKey: ["saved", sessionId], queryFn: () => platformApi.getSavedArticles(sessionId) });

  return (
    <div className="space-y-6">
      <section className="glass rounded-[28px] p-6">
        <h1 className="text-3xl font-semibold text-white">Saved + Telegram</h1>
        <p className="mt-2 text-sm text-slate-400">Manage saved AI stories and Telegram delivery in one place.</p>
      </section>
      <TelegramPanel sessionId={sessionId} />
      <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
        {saved.map((item) => <NewsCard key={item.id} item={item} />)}
      </div>
    </div>
  );
}

