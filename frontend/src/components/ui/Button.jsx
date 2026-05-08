import { Slot } from "@radix-ui/react-slot";
import { cn } from "../../utils/cn";

export function Button({ asChild = false, className, variant = "primary", type = "button", ...props }) {
  const Component = asChild ? Slot : "button";
  const variants = {
    primary: "bg-gradient-to-r from-[#8fdcff] via-[#6ee7c8] to-[#ffd28a] text-slate-950 shadow-glow",
    secondary: "border border-white/10 bg-white/5 text-white",
    ghost: "text-slate-300 hover:text-white",
  };
  return (
    <Component
      type={asChild ? undefined : type}
      className={cn("rounded-full px-4 py-2 text-sm font-medium transition hover:scale-[1.02]", variants[variant], className)}
      {...props}
    />
  );
}
