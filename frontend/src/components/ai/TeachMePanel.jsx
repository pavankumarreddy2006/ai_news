import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { Button } from "@/components/ui/Button";
import { platformApi } from "@/services/platformApi";

export function TeachMePanel() {
  const [topic, setTopic] = useState("AI agents");
  const mutation = useMutation({ mutationFn: platformApi.learn });

  return (
    <section className="glass rounded-[28px] p-6">
      <h3 className="text-2xl font-semibold text-white">Teach Me AI</h3>
      <p className="mt-2 text-sm text-slate-400">Explain AI step-by-step with simple examples and real-world usage.</p>
      <div className="mt-4 flex flex-col gap-3 sm:flex-row">
        <input value={topic} onChange={(event) => setTopic(event.target.value)} className="flex-1 rounded-full border border-white/10 bg-white/5 px-4 py-3 text-white outline-none" />
        <Button onClick={() => mutation.mutate(topic)}>Explain Simply</Button>
      </div>
      {mutation.data ? (
        <div className="mt-5 space-y-3 text-sm text-slate-300">
          <p>{mutation.data.explanation}</p>
          <p><span className="text-white">Why it matters:</span> {mutation.data.why_it_matters}</p>
          <p><span className="text-white">Difficulty:</span> {mutation.data.difficulty}</p>
          <div className="space-y-1">
            {mutation.data.steps.map((step) => <p key={step}>{step}</p>)}
          </div>
        </div>
      ) : null}
    </section>
  );
}

