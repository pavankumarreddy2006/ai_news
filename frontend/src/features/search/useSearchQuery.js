import { useQuery } from "@tanstack/react-query";
import { platformApi } from "@/services/platformApi";

export function useSearchQuery(query) {
  return useQuery({
    queryKey: ["search", query],
    queryFn: () => platformApi.search(query),
    enabled: Boolean(query),
  });
}

