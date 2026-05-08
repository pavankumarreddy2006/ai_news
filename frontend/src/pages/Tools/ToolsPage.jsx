import { useState } from "react";
import { ToolCard } from "@/components/cards/ToolCard";
import { useToolsQuery } from "@/features/tools/useToolsQuery";

export function ToolsPage() {
  const [query, setQuery] = useState("");
  const { data: tools = [] } = useToolsQuery();
  const filtered = tools.filter((tool) => `${tool.name} ${tool.category} ${tool.features}`.toLowerCase().includes(query.toLowerCase()));

  return (
    <div className="space-y-6">
      <section className="glass rounded-[28px] p-6">
        <h1 className="text-3xl font-semibold text-white">AI Tools Directory</h1>
        <p className="mt-2 text-sm text-slate-400">Search coding AI, video AI, productivity AI, voice AI, automation AI, and chatbot AI.</p>
        <input value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Search AI tools" className="mt-4 w-full rounded-full border border-white/10 bg-white/5 px-4 py-3 text-white outline-none" />
      </section>
      <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
        {filtered.map((tool) => <ToolCard key={tool.id} tool={tool} />)}
      </div>
    </div>
  );
}

