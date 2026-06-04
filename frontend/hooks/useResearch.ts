import { useState } from "react";
import { api } from "@/lib/api";
import { ResearchResponse, Source } from "@/types/research";

export function useResearch() {
  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState<Source[]>([]);

  const research = async (question: string) => {
    setLoading(true);

    try {
      const response = await api.post<ResearchResponse>(
        "/research",
        { question }
      );

      setAnswer(response.data.answer);
      setSources(response.data.sources || []);
    } catch (error) {
      console.error(error);
      setAnswer("");
      setSources([]);
    } finally {
      setLoading(false);
    }
  };

  return {
    loading,
    answer,
    sources,
    research,
  };
}