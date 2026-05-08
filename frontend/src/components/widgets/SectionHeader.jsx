export function SectionHeader({ eyebrow, title, description }) {
  return (
    <div className="mb-6">
      {eyebrow ? <p className="text-sm uppercase tracking-[0.25em] text-glow">{eyebrow}</p> : null}
      <h2 className="mt-2 text-2xl font-semibold text-white">{title}</h2>
      {description ? <p className="mt-2 max-w-2xl text-sm text-slate-400">{description}</p> : null}
    </div>
  );
}

