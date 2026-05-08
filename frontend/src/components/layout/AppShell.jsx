import { Navbar } from "@/components/layout/Navbar";
import { Footer } from "@/components/layout/Footer";
import { NotificationDock } from "@/components/widgets/NotificationDock";

export function AppShell({ children }) {
  return (
    <div className="app-shell min-h-screen">
      <Navbar />
      <main className="mx-auto max-w-7xl px-4 pb-16 pt-6 sm:px-6 lg:px-8">{children}</main>
      <Footer />
      <NotificationDock />
    </div>
  );
}
