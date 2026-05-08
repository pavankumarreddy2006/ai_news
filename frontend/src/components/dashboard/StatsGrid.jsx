export function StatsGrid({ stats }) {
  return (
    <section className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      {stats.map((item) => (
        <div key={item.label} className="glass rounded-[24px] p-5">
          <p className="text-sm text-slate-400">{item.label}</p>
          <p className="mt-3 text-3xl font-semibold text-white">{item.value}</p>
          <p className="mt-2 text-sm text-slate-300">{item.note}</p>
        </div>
      ))}
    </section>
  );
}

