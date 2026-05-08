import { usePlatformStore } from "@/store/usePlatformStore";

export function LiveUpdatesPanel() {
  const liveEvents = usePlatformStore((state) => state.liveEvents);
  return (
    <section className="glass aurora-border panel-strong rounded-[28px] p-5">
      <div className="mb-4 flex items-center justify-between">
        <h3 className="text-lg font-semibold text-white">Live AI Updates</h3>
        <span className="rounded-full bg-emerald-400/10 px-3 py-1 text-xs text-emerald-300">Realtime</span>
      </div>
      <div className="space-y-3">
        {liveEvents.length ? liveEvents.map((event) => (
          <div key={event.id} className="rounded-2xl border border-white/8 bg-white/5 p-3 text-sm">
            <p className="text-white">{event.message}</p>
            <p className="mt-1 text-xs text-slate-400">{event.time}</p>
          </div>
        )) : <p className="text-sm text-slate-400">Waiting for AI launches, trending shifts, and morning digest events.</p>}
      </div>
    </section>
  );
}
