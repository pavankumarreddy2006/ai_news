import { Bookmark, ExternalLink, Headphones, Share2, Sparkles } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { useSpeechControls } from "@/hooks/useSpeechControls";
import { platformApi } from "@/services/platformApi";
import { usePlatformStore } from "@/store/usePlatformStore";

export function NewsCard({ item }) {
  const speech = useSpeechControls();
  const sessionId = usePlatformStore((state) => state.sessionId);
  const markSaved = usePlatformStore((state) => state.markSaved);

  return (
    <article className="glass aurora-border panel-strong group flex h-full flex-col overflow-hidden rounded-[28px]">
      <a href={item.source_url} target="_blank" rel="noreferrer" className="block h-48 bg-[radial-gradient(circle_at_top_right,rgba(255,210,138,0.22),transparent_20%),linear-gradient(135deg,rgba(143,220,255,0.22),rgba(7,16,30,0.98)_70%)] p-5">
        <div className="flex items-start justify-between gap-3">
          <span className="rounded-full border border-[#8fdcff]/30 bg-white/5 px-3 py-1 text-xs text-[#8fdcff]">{item.category}</span>
          {item.is_trending ? (
            <span className="rounded-full bg-white/10 px-3 py-1 text-xs text-white">
              <Sparkles className="mr-1 inline h-3 w-3 text-[#ffd28a]" /> Trending
            </span>
          ) : null}
        </div>
        <div className="mt-10 max-w-[14rem]">
          <p className="text-xs uppercase tracking-[0.28em] text-slate-300">{item.source}</p>
          <p className="mt-3 text-2xl font-semibold leading-tight text-white">{item.title}</p>
        </div>
      </a>
      <div className="flex flex-1 flex-col gap-3 p-5">
        <a href={item.source_url} target="_blank" rel="noreferrer" className="space-y-3">
          <h3 className="text-lg font-semibold text-white transition group-hover:text-[#8fdcff]">{item.title}</h3>
          <p className="text-sm text-slate-300">{item.easy_summary}</p>
          <p className="text-sm text-slate-400">Why it matters: {item.why_it_matters}</p>
          <div className="flex flex-wrap gap-3 text-xs text-slate-500">
            <span>{item.reading_time}</span>
            <span>Difficulty {item.difficulty_level}</span>
            <span>Score {Math.round(item.ranking_score || 0)}</span>
          </div>
        </a>
        <div className="mt-auto space-y-3">
          <div className="flex flex-wrap gap-2">
            <Button onClick={() => speech.speak(`${item.title}. ${item.easy_summary}. ${item.beginner_explanation}`)}>
              <Headphones className="mr-2 inline h-4 w-4" />
              Listen Summary
            </Button>
            <Button
              variant="secondary"
              onClick={async () => {
                await platformApi.saveArticle({ session_id: sessionId, article_id: item.id });
                markSaved(item.id);
              }}
            >
              <Bookmark className="mr-2 inline h-4 w-4" />
              Save
            </Button>
            <Button asChild variant="secondary">
              <a href={`https://twitter.com/intent/tweet?text=${encodeURIComponent(item.title)}&url=${encodeURIComponent(item.source_url)}`} target="_blank" rel="noreferrer">
                <Share2 className="mr-2 inline h-4 w-4" />
                Share
              </a>
            </Button>
            <Button asChild variant="secondary">
              <a href={item.source_url} target="_blank" rel="noreferrer">
                <ExternalLink className="mr-2 inline h-4 w-4" />
                Open
              </a>
            </Button>
          </div>
          <div className="flex flex-wrap items-center gap-3 text-xs text-slate-400">
            <button type="button" onClick={speech.pause}>Pause</button>
            <button type="button" onClick={speech.resume}>Resume</button>
            <button type="button" onClick={speech.stop}>Stop</button>
            <label className="flex items-center gap-2">
              Speed
              <input type="range" min="0.8" max="1.5" step="0.1" value={speech.speed} onChange={(e) => speech.setSpeed(Number(e.target.value))} />
            </label>
            <span>{speech.isSpeaking ? "Playing" : "Ready"}</span>
          </div>
        </div>
      </div>
    </article>
  );
}
