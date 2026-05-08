export function CategoryFilterBar({ categories, activeCategory, onSelect }) {
  return (
    <div className="flex flex-wrap gap-3">
      {["All", ...categories].map((category) => (
        <button
          key={category}
          onClick={() => onSelect(category)}
          className={activeCategory === category ? "rounded-full bg-glow px-4 py-2 text-sm text-night" : "rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-slate-300"}
        >
          {category}
        </button>
      ))}
    </div>
  );
}

