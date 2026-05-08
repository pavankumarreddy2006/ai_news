import { useEffect } from "react";
import { usePlatformStore } from "@/store/usePlatformStore";

export function useLiveUpdates() {
  const addLiveEvent = usePlatformStore((state) => state.addLiveEvent);
  const addNotification = usePlatformStore((state) => state.addNotification);

  useEffect(() => {
    const base = import.meta.env.VITE_WS_URL || "ws://localhost:10000";
    const socket = new WebSocket(`${base}/ws/live-updates`);
    socket.onmessage = (event) => {
      const payload = JSON.parse(event.data);
      const message = payload.payload?.message || `${payload.type} event received`;
      addLiveEvent({ type: payload.type, message, time: new Date().toLocaleTimeString() });
      addNotification({ title: "Live AI Update", description: message });
    };
    return () => socket.close();
  }, [addLiveEvent, addNotification]);
}

