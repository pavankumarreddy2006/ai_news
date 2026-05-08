import { Bell, Bot, Search } from "lucide-react";
import { NavLink, useNavigate } from "react-router-dom";
import { useState } from "react";
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
  const navigate = useNavigate();
  const notifications = usePlatformStore((state) => state.notifications);

  return (
    <header className="sticky top-0 z-50 border-b border-white/10 bg-night/80 backdrop-blur-2xl">
      <div className="mx-auto flex max-w-7xl flex-wrap items-center gap-4 px-4 py-4 sm:px-6 lg:px-8">
        <NavLink to="/" className="flex items-center gap-3 text-lg font-semibold text-white">
          <span className="rounded-2xl border border-glow/30 bg-glow/10 p-2 shadow-glow">
            <Bot className="h-5 w-5 text-glow" />
          </span>
          AI News Platform
        </NavLink>
        <form
          className="glass flex min-w-[220px] flex-1 items-center gap-3 rounded-full px-4 py-2"
          onSubmit={(event) => {
            event.preventDefault();
            navigate(`/search?q=${encodeURIComponent(search)}`);
          }}
        >
          <Search className="h-4 w-4 text-slate-400" />
          <input
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            className="w-full bg-transparent text-sm text-white outline-none placeholder:text-slate-500"
            placeholder="Search AI news, tools, trends..."
          />
        </form>
        <nav className="hidden items-center gap-4 lg:flex">
          {navItems.map((item) => (
            <NavLink key={item.to} to={item.to} className={({ isActive }) => (isActive ? "text-white" : "text-slate-300 hover:text-white")}>
              {item.label}
            </NavLink>
          ))}
        </nav>
        <NavLink to="/settings" className="glass relative rounded-full p-2 text-slate-200 transition hover:text-white">
          <Bell className="h-4 w-4" />
          <span className="absolute -right-1 -top-1 rounded-full bg-glow px-1.5 text-[10px] text-night">{notifications.length}</span>
        </NavLink>
      </div>
    </header>
  );
}

