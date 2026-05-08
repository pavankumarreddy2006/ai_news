export function WorkflowStatusPanel({ workflow }) {
  const checks = [
    { label: "Database", value: workflow?.database_ready },
    { label: "Telegram", value: workflow?.telegram_ready },
    { label: "Scheduler", value: workflow?.scheduler_ready },
    { label: "Live Updates", value: workflow?.live_updates_ready },
    { label: "AI Aggregation", value: workflow?.aggregation_ready },
  ];

  return (
    <section className="glass rounded-[28px] p-6">
      <div className="flex items-center justify-between gap-3">
        <div>
          <h3 className="text-xl font-semibold text-white">Automation Workflow</h3>
          <p className="mt-2 text-sm text-slate-400">Startup health, source coverage, cleanup, and digest status in one place.</p>
        </div>
        <span className="rounded-full bg-emerald-400/10 px-3 py-1 text-xs text-emerald-300">Always On</span>
      </div>
      <div className="mt-5 grid gap-3 sm:grid-cols-2 xl:grid-cols-5">
        {checks.map((item) => (
          <div key={item.label} className="rounded-2xl border border-white/8 bg-white/5 p-4">
            <p className="text-xs uppercase tracking-[0.24em] text-slate-400">{item.label}</p>
            <p className={`mt-2 text-base font-semibold ${item.value ? "text-emerald-300" : "text-amber-300"}`}>
              {item.value ? "Ready" : "Fallback"}
            </p>
          </div>
        ))}
      </div>
      <div className="mt-5 grid gap-3 md:grid-cols-3">
        <div className="rounded-2xl border border-white/8 bg-white/5 p-4">
          <p className="text-xs uppercase tracking-[0.24em] text-slate-400">Last Refresh</p>
          <p className="mt-2 text-sm text-white">{workflow?.last_refresh_at || "Waiting for first run"}</p>
        </div>
        <div className="rounded-2xl border border-white/8 bg-white/5 p-4">
          <p className="text-xs uppercase tracking-[0.24em] text-slate-400">Cleanup Window</p>
          <p className="mt-2 text-sm text-white">{workflow?.summary?.cleanup_window_hours || 48} hours</p>
        </div>
        <div className="rounded-2xl border border-white/8 bg-white/5 p-4">
          <p className="text-xs uppercase tracking-[0.24em] text-slate-400">Tracked Records</p>
          <p className="mt-2 text-sm text-white">{workflow?.counts?.articles || 0} news - {workflow?.counts?.tools || 0} tools</p>
        </div>
      </div>
    </section>
  );
}
