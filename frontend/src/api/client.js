import axios from "axios";
import { getApiBaseUrl } from "@/utils/runtimeConfig";

export const apiClient = axios.create({
  baseURL: getApiBaseUrl(),
  timeout: 12000,
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      return Promise.reject(error);
    }
    return Promise.reject(
      new Error(`Unable to reach the AI News API at ${getApiBaseUrl()}. Check VITE_API_URL for this deployment.`),
    );
  },
);
