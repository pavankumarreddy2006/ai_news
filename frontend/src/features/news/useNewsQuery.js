import { useQuery } from "@tanstack/react-query";
import { platformApi } from "@/services/platformApi";

export function useNewsQuery(category) {
  return useQuery({
    queryKey: ["news", category],
    queryFn: () => platformApi.getNews(category && category !== "All" ? { category } : undefined),
  });
}

