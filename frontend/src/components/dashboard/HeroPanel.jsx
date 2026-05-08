import { motion } from "framer-motion";
import { ArrowRight, Sparkles } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { useNavigate } from "react-router-dom";

export function HeroPanel({ categories }) {
  const navigate = useNavigate();
  return (
    <section className="glass aurora-border section-grid relative overflow-hidden rounded-[34px] px-6 py-10 sm:px-8 lg:px-12">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(255,210,138,0.18),transparent_24%),linear-gradient(135deg,rgba(143,220,255,0.12),transparent_55%)]" />
      <motion.div initial={{ opacity: 0, y: 22 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="relative grid gap-10 lg:grid-cols-[1.45fr_0.8fr] lg:items-end">
        <div className="max-w-3xl">
          <div className="mb-5 inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-xs uppercase tracking-[0.28em] text-[#8fdcff]">
            <Sparkles className="h-3.5 w-3.5" />
            Realtime AI Intelligence
          </div>
          <h1 className="text-balance text-[clamp(2.6rem,6vw,5.4rem)] font-semibold leading-[0.96] text-white">
            Modern AI news that still makes sense at 8 in the morning.
          </h1>
          <p className="mt-5 max-w-2xl text-base text-slate-300 sm:text-lg">
            Track launches, tools, research, and market shifts in one editorial dashboard with beginner-friendly explanations and live updates.
          </p>
          <div className="mt-7 flex flex-wrap gap-3">
            <Button onClick={() => navigate("/news")}>Explore AI News</Button>
            <Button variant="secondary" onClick={() => navigate("/learn-ai")}>Teach Me AI</Button>
          </div>
          <div className="mt-8 flex flex-wrap gap-3">
            {categories.map((category) => (
              <button key={category} onClick={() => navigate(`/news?category=${encodeURIComponent(category)}`)} className="rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-slate-200 transition hover:border-[#8fdcff]/40 hover:bg-white/10 hover:text-white">
                {category}
              </button>
            ))}
          </div>
        </div>
        <div className="glass panel-strong rounded-[28px] p-5">
          <p className="text-xs uppercase tracking-[0.3em] text-[#ffd28a]">Today’s read</p>
          <div className="mt-4 space-y-4">
            <div className="rounded-[24px] border border-white/10 bg-white/5 p-4">
              <p className="text-sm text-slate-300">What you get</p>
              <p className="mt-2 text-xl font-semibold text-white">Fast summaries, stronger signals, fewer dead feeds.</p>
            </div>
            <button onClick={() => navigate("/trending")} className="flex w-full items-center justify-between rounded-[24px] border border-white/10 bg-[#8fdcff]/8 px-4 py-4 text-left transition hover:bg-[#8fdcff]/12">
              <div>
                <p className="text-sm text-slate-300">Live pulse</p>
                <p className="mt-1 text-base font-semibold text-white">See what is actually trending right now</p>
              </div>
              <ArrowRight className="h-5 w-5 text-[#8fdcff]" />
            </button>
          </div>
        </div>
      </motion.div>
    </section>
  );
}
