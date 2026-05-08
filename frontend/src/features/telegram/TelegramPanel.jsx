import { useState } from "react";
import { useMutation, useQuery } from "@tanstack/react-query";
import { Button } from "@/components/ui/Button";
import { platformApi } from "@/services/platformApi";

export function TelegramPanel({ sessionId }) {
  const [chatId, setChatId] = useState("");
  const [username, setUsername] = useState("");
  const subscribe = useMutation({ mutationFn: platformApi.subscribeTelegram });
  const digest = useMutation({ mutationFn: platformApi.sendTelegramDigest });
  const { data: workflow } = useQuery({ queryKey: ["workflow"], queryFn: platformApi.getWorkflowStatus, refetchInterval: 30000 });

  return (
    <section className="glass rounded-[28px] p-6">
      <h3 className="text-xl font-semibold text-white">Telegram AI Summaries</h3>
      <p className="mt-2 text-sm text-slate-400">Connect Telegram and receive morning AI digests automatically.</p>
      <div className="mt-4 rounded-2xl border border-white/10 bg-white/5 p-4 text-sm text-slate-300">
        <p className="text-white">Daily digest workflow</p>
        <p className="mt-2">Status: {workflow?.telegram_ready ? "Bot configured" : "Bot token missing, fallback logging only"}</p>
        <p className="mt-1">Last run: {workflow?.last_digest_at || "No digest sent yet"}</p>
      </div>
      <div className="mt-4 grid gap-3">
        <input value={chatId} onChange={(event) => setChatId(event.target.value)} placeholder="Telegram chat ID" className="rounded-full border border-white/10 bg-white/5 px-4 py-3 text-white outline-none" />
        <input value={username} onChange={(event) => setUsername(event.target.value)} placeholder="Telegram username" className="rounded-full border border-white/10 bg-white/5 px-4 py-3 text-white outline-none" />
        <div className="flex flex-wrap gap-3">
          <Button onClick={() => subscribe.mutate({ chat_id: chatId, username, first_name: sessionId })}>Connect Telegram</Button>
          <Button variant="secondary" onClick={() => digest.mutate()}>Send Test Digest</Button>
        </div>
      </div>
      {subscribe.data ? <p className="mt-3 text-sm text-emerald-300">{subscribe.data.message}</p> : null}
      {digest.data ? <p className="mt-2 text-sm text-emerald-300">Digest prepared. Sent: {digest.data.sent}</p> : null}
      {digest.data?.message ? <pre className="mt-4 overflow-x-auto rounded-2xl border border-white/10 bg-slate-950/60 p-4 text-xs text-slate-300 whitespace-pre-wrap">{digest.data.message}</pre> : null}
    </section>
  );
}
