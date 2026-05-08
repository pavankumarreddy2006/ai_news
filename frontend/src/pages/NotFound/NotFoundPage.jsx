import { Link } from "react-router-dom";

export function NotFoundPage() {
  return (
    <div className="glass rounded-[28px] p-8 text-center">
      <h1 className="text-4xl font-semibold text-white">Page Not Found</h1>
      <p className="mt-3 text-slate-400">The AI page you were looking for is not available.</p>
      <Link to="/" className="mt-6 inline-block rounded-full bg-glow px-5 py-3 text-sm font-medium text-night">
        Back Home
      </Link>
    </div>
  );
}

