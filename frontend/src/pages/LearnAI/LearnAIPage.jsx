import { TeachMePanel } from "@/components/ai/TeachMePanel";

export function LearnAIPage() {
  return (
    <div className="space-y-6">
      <section className="glass rounded-[28px] p-6">
        <h1 className="text-3xl font-semibold text-white">Learn AI</h1>
        <p className="mt-2 text-sm text-slate-400">A beginner-friendly AI learning center with simple explanations and practical examples.</p>
      </section>
      <TeachMePanel />
    </div>
  );
}

