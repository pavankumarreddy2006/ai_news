import { useEffect } from "react";
import { usePlatformStore } from "@/store/usePlatformStore";
import { getWsBaseUrl } from "@/utils/runtimeConfig";

export function useLiveUpdates() {
  const addLiveEvent = usePlatformStore((state) => state.addLiveEvent);
  const addNotification = usePlatformStore((state) => state.addNotification);

  useEffect(() => {
    let disposed = false;
    let socket;
    let reconnectTimer;
    let attempts = 0;

    const connect = () => {
      const base = getWsBaseUrl();
      socket = new WebSocket(`${base}/ws/live-updates`);
      socket.onopen = () => {
        attempts = 0;
      };
      socket.onmessage = (event) => {
        const payload = JSON.parse(event.data);
        const message = payload.payload?.message
          || payload.payload?.refreshed_at
          || payload.payload?.reason
          || `${payload.type} event received`;
        addLiveEvent({ type: payload.type, message, time: new Date().toLocaleTimeString() });
        addNotification({ title: "Live AI Update", description: message });
      };
      socket.onclose = () => {
        if (disposed) {
          return;
        }
        attempts += 1;
        reconnectTimer = window.setTimeout(connect, Math.min(15000, 1000 * attempts));
      };
    };

    connect();

    return () => {
      disposed = true;
      if (reconnectTimer) {
        window.clearTimeout(reconnectTimer);
      }
      socket?.close();
    };
  }, [addLiveEvent, addNotification]);
}
