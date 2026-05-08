import { useQuery } from "@tanstack/react-query";
import { platformApi } from "@/services/platformApi";

export function useTrendingQuery() {
  return useQuery({
    queryKey: ["trending"],
    queryFn: platformApi.getTrending,
    staleTime: 120_000,
  });
}
