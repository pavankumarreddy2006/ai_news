import React from "react";
import { Button } from "@/components/ui/Button";

export class AppErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Application error boundary captured an error.", error, errorInfo);
  }

  render() {
    if (!this.state.hasError) {
      return this.props.children;
    }

    return (
      <div className="mx-auto flex min-h-screen max-w-3xl items-center px-4 py-12">
        <section className="glass w-full rounded-[32px] p-8 text-center">
          <p className="text-xs uppercase tracking-[0.28em] text-[#ffd28a]">Recovery Mode</p>
          <h1 className="mt-4 text-3xl font-semibold text-white">The dashboard hit an unexpected UI error.</h1>
          <p className="mt-4 text-sm text-slate-300">
            The page stayed online, but this view needs a refresh. If the issue keeps happening, check the deployed API URL and browser console.
          </p>
          {this.state.error?.message ? (
            <p className="mt-4 rounded-2xl border border-white/10 bg-white/5 p-4 text-left text-xs text-slate-300">
              {this.state.error.message}
            </p>
          ) : null}
          <div className="mt-6 flex justify-center gap-3">
            <Button onClick={() => window.location.reload()}>Reload Dashboard</Button>
            <Button variant="secondary" onClick={() => window.location.assign("/")}>Go Home</Button>
          </div>
        </section>
      </div>
    );
  }
}
