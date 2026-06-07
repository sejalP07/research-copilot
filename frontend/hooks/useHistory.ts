import { useEffect, useState } from "react";
import axios from "axios";

export interface HistoryItem {
  id: string;
  question: string;
  answer: string;
  created_at: string;
}

export function useHistory() {
  const [history, setHistory] = useState<
    HistoryItem[]
  >([]);

  const fetchHistory = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/history"
      );

      setHistory(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  return {
    history,
    fetchHistory,
  };
}