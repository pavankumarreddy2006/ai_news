import { ExternalLink } from "lucide-react";

export function ToolCard({ tool }) {
  return (
    <a href={tool.website_url} target="_blank" rel="noreferrer" className="glass flex h-full flex-col rounded-[26px] p-5 transition hover:-translate-y-1">
      <div className="mb-4 flex items-center justify-between">
        <span className="rounded-full border border-glow/30 px-3 py-1 text-xs text-glow">{tool.category}</span>
        <span className="text-xs text-slate-400">{tool.pricing}</span>
      </div>
      <h3 className="text-lg font-semibold text-white">{tool.name}</h3>
      <p className="mt-3 text-sm text-slate-300">{tool.simple_explanation}</p>
      <p className="mt-3 text-sm text-slate-400">{tool.features}</p>
      <div className="mt-auto pt-4 text-sm text-glow">
        Rank {tool.ai_ranking} - Popularity {tool.popularity_score}
        <ExternalLink className="ml-2 inline h-4 w-4" />
      </div>
    </a>
  );
}
