import { AppShell } from "@/components/layout/AppShell";
import { AppRoutes } from "@/routes/AppRoutes";
import { useLiveUpdates } from "@/hooks/useLiveUpdates";

export default function App() {
  useLiveUpdates();
  return (
    <AppShell>
      <AppRoutes />
    </AppShell>
  );
}

