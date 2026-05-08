import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { Button } from "@/components/ui/Button";
import { platformApi } from "@/services/platformApi";
import { usePlatformStore } from "@/store/usePlatformStore";

const categories = ["AI Tools", "AI Agents", "OpenAI", "Coding AI", "Video AI", "Productivity", "Tutorials", "Startups"];

export function SettingsPage() {
  const sessionId = usePlatformStore((state) => state.sessionId);
  const [selected, setSelected] = useState(categories.slice(0, 3));
  const mutation = useMutation({ mutationFn: platformApi.savePreferences });

  return (
    <div className="space-y-6">
      <section className="glass rounded-[28px] p-6">
        <h1 className="text-3xl font-semibold text-white">Settings</h1>
        <p className="mt-2 text-sm text-slate-400">Save the AI categories you care about most.</p>
        <div className="mt-5 flex flex-wrap gap-3">
          {categories.map((category) => (
            <button
              key={category}
              type="button"
              onClick={() => setSelected((current) => current.includes(category) ? current.filter((item) => item !== category) : [...current, category])}
              className={selected.includes(category) ? "rounded-full bg-glow px-4 py-2 text-sm text-night" : "rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-white"}
            >
              {category}
            </button>
          ))}
        </div>
        <div className="mt-5">
          <Button onClick={() => mutation.mutate({ session_id: sessionId, favorite_categories: selected, difficulty_level: "Beginner", telegram_opt_in: true })}>
            Save Preferences
          </Button>
        </div>
        {mutation.data ? <p className="mt-3 text-sm text-emerald-300">{mutation.data.message}</p> : null}
      </section>
    </div>
  );
}
