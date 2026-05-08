import { Bell, Bot, Moon, Search, Sun } from "lucide-react";
import { NavLink, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { usePlatformStore } from "@/store/usePlatformStore";

const navItems = [
  { to: "/", label: "Home" },
  { to: "/trending", label: "Trending" },
  { to: "/news", label: "News" },
  { to: "/tools", label: "AI Tools" },
  { to: "/learn-ai", label: "Learn AI" },
  { to: "/saved", label: "Telegram" },
];

export function Navbar() {
  const [search, setSearch] = useState("");
  const [theme, setTheme] = useState(() => {
    if (typeof window === "undefined") return "dark";
    return window.localStorage.getItem("ai-news-theme") || "dark";
  });
  const navigate = useNavigate();
  const notifications = usePlatformStore((state) => state.notifications);

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
    window.localStorage.setItem("ai-news-theme", theme);
  }, [theme]);

  return (
    <header className="sticky top-0 z-50 border-b border-white/10 bg-night/70 backdrop-blur-2xl">
      <div className="mx-auto flex max-w-7xl flex-wrap items-center gap-4 px-4 py-4 sm:px-6 lg:px-8">
        <NavLink to="/" className="flex items-center gap-3 text-lg font-semibold text-white">
          <span className="rounded-2xl border border-[#8fdcff]/30 bg-[#8fdcff]/10 p-2 shadow-glow">
            <Bot className="h-5 w-5 text-[#8fdcff]" />
          </span>
          <span>
            AI Updates
            <span className="ml-2 hidden text-xs font-medium uppercase tracking-[0.32em] text-[#ffd28a] sm:inline">Morning Brief</span>
          </span>
        </NavLink>
        <form
          className="glass panel-strong flex min-w-[220px] flex-1 items-center gap-3 rounded-full px-4 py-2 lg:min-w-[280px]"
          onSubmit={(event) => {
            event.preventDefault();
            navigate(`/search?q=${encodeURIComponent(search)}`);
          }}
        >
          <Search className="h-4 w-4 text-slate-400" />
          <input
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            className="min-w-0 w-full bg-transparent text-sm text-white outline-none placeholder:text-slate-500"
            placeholder="Search AI news, tools, trends..."
          />
        </form>
        <nav className="order-3 flex w-full items-center gap-3 overflow-x-auto pb-1 lg:order-none lg:w-auto lg:pb-0">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) => (
                isActive
                  ? "whitespace-nowrap rounded-full border border-white/10 bg-white/10 px-4 py-2 text-white"
                  : "whitespace-nowrap rounded-full px-4 py-2 text-slate-300 transition hover:bg-white/5 hover:text-white"
              )}
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
        <button
          type="button"
          onClick={() => setTheme((current) => current === "dark" ? "light" : "dark")}
          className="glass panel-strong rounded-full p-2 text-slate-200 transition hover:text-white"
          aria-label="Toggle theme"
        >
          {theme === "dark" ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
        </button>
        <NavLink to="/settings" className="glass panel-strong relative rounded-full p-2 text-slate-200 transition hover:text-white">
          <Bell className="h-4 w-4" />
          <span className="absolute -right-1 -top-1 rounded-full bg-[#ffd28a] px-1.5 text-[10px] font-semibold text-slate-950">{notifications.length}</span>
        </NavLink>
      </div>
    </header>
  );
}
