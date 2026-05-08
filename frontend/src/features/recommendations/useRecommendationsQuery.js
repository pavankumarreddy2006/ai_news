import { useQuery } from "@tanstack/react-query";
import { platformApi } from "@/services/platformApi";

export function useRecommendationsQuery() {
  return useQuery({
    queryKey: ["recommendations"],
    queryFn: platformApi.getRecommendations,
  });
}

