import { useQuery } from "@tanstack/react-query";
import { platformApi } from "@/services/platformApi";

export function useToolsQuery(category) {
  return useQuery({
    queryKey: ["tools", category],
    queryFn: () => platformApi.getTools(category ? { category } : undefined),
    staleTime: 300_000,
  });
}
