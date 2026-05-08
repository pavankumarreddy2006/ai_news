import { usePlatformStore } from "@/store/usePlatformStore";

export function NotificationDock() {
  const notifications = usePlatformStore((state) => state.notifications).slice(0, 3);
  return (
    <div className="fixed bottom-4 right-4 z-50 hidden w-80 space-y-3 xl:block">
      {notifications.map((item) => (
        <div key={item.id} className="glass rounded-2xl p-4">
          <p className="text-sm font-medium text-white">{item.title}</p>
          <p className="mt-1 text-sm text-slate-400">{item.description}</p>
        </div>
      ))}
    </div>
  );
}

