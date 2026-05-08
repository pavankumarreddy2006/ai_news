import { TeachMePanel } from "@/components/ai/TeachMePanel";

export function LearnAIPage() {
  return (
    <div className="space-y-6">
      <section className="glass rounded-[28px] p-6">
        <h1 className="text-3xl font-semibold text-white">Learn AI</h1>
        <p className="mt-2 text-sm text-slate-400">A beginner-friendly AI learning center with simple explanations and practical examples.</p>
      </section>
      <section className="grid gap-4 md:grid-cols-3">
        {[
          { title: "Start Here", text: "Learn what AI tools, agents, workflows, and copilots actually do in plain English." },
          { title: "Use Cases", text: "See how AI helps with coding, research, content, productivity, automation, and video work." },
          { title: "Stay Practical", text: "Each explanation is written for real people who want useful outcomes, not theory overload." },
        ].map((item) => (
          <div key={item.title} className="glass rounded-[24px] p-5">
            <h2 className="text-lg font-semibold text-white">{item.title}</h2>
            <p className="mt-2 text-sm text-slate-400">{item.text}</p>
          </div>
        ))}
      </section>
      <TeachMePanel />
    </div>
  );
}
