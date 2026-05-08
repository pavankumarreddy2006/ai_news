import { motion } from "framer-motion";
import { Button } from "@/components/ui/Button";
import { useNavigate } from "react-router-dom";

export function HeroPanel({ categories }) {
  const navigate = useNavigate();
  return (
    <section className="glass section-grid relative overflow-hidden rounded-[34px] px-6 py-10 sm:px-8 lg:px-12">
      <div className="absolute inset-0 bg-gradient-to-r from-glow/10 via-transparent to-violetGlow/10" />
      <motion.div initial={{ opacity: 0, y: 22 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="relative max-w-3xl">
        <p className="mb-4 text-sm uppercase tracking-[0.32em] text-glow">Realtime AI Intelligence</p>
        <h1 className="text-[clamp(2.3rem,5vw,4.8rem)] font-semibold leading-tight text-white">Stay Updated with AI-Powered News</h1>
        <p className="mt-4 max-w-2xl text-base text-slate-300 sm:text-lg">
          Discover AI news, AI tools, and AI trends explained in simple English.
        </p>
        <div className="mt-6 flex flex-wrap gap-3">
          <Button onClick={() => navigate("/news")}>Explore AI News</Button>
          <Button variant="secondary" onClick={() => navigate("/learn-ai")}>Teach Me AI</Button>
        </div>
        <div className="mt-8 flex flex-wrap gap-3">
          {categories.map((category) => (
            <button key={category} onClick={() => navigate(`/news?category=${encodeURIComponent(category)}`)} className="rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-slate-200 transition hover:border-glow/40 hover:text-white">
              {category}
            </button>
          ))}
        </div>
      </motion.div>
    </section>
  );
}

