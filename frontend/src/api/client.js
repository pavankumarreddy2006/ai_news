import axios from "axios";
import { getApiBaseUrl } from "@/utils/runtimeConfig";

export const apiClient = axios.create({
  baseURL: getApiBaseUrl(),
  timeout: 12000,
});
