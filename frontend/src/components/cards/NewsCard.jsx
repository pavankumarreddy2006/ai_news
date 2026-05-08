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
    <article className="glass group flex h-full flex-col overflow-hidden rounded-[28px]">
      <a href={item.source_url} target="_blank" rel="noreferrer" className="block h-44 bg-gradient-to-br from-glow/25 via-slate-950 to-violetGlow/20 p-5">
        <div className="flex items-start justify-between">
          <span className="rounded-full border border-glow/30 bg-white/5 px-3 py-1 text-xs text-glow">{item.category}</span>
          {item.is_trending ? (
            <span className="rounded-full bg-white/10 px-3 py-1 text-xs text-white">
              <Sparkles className="mr-1 inline h-3 w-3 text-glow" /> Trending
            </span>
          ) : null}
        </div>
      </a>
      <div className="flex flex-1 flex-col gap-3 p-5">
        <a href={item.source_url} target="_blank" rel="noreferrer" className="space-y-3">
          <h3 className="text-lg font-semibold text-white transition group-hover:text-glow">{item.title}</h3>
          <p className="text-sm text-slate-300">{item.easy_summary}</p>
          <p className="text-sm text-slate-400">Why it matters: {item.why_it_matters}</p>
          <div className="flex flex-wrap gap-3 text-xs text-slate-500">
            <span>{item.source}</span>
            <span>{item.reading_time}</span>
            <span>Difficulty {item.difficulty_level}</span>
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
            <a href={`https://twitter.com/intent/tweet?text=${encodeURIComponent(item.title)}&url=${encodeURIComponent(item.source_url)}`} target="_blank" rel="noreferrer">
              <Button variant="secondary">
                <Share2 className="mr-2 inline h-4 w-4" />
                Share
              </Button>
            </a>
            <a href={item.source_url} target="_blank" rel="noreferrer">
              <Button variant="secondary">
                <ExternalLink className="mr-2 inline h-4 w-4" />
                Open
              </Button>
            </a>
          </div>
          <div className="flex flex-wrap items-center gap-3 text-xs text-slate-400">
            <button onClick={speech.pause}>Pause</button>
            <button onClick={speech.resume}>Replay</button>
            <button onClick={speech.stop}>Stop</button>
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

