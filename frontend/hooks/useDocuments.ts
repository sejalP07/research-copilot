import { useEffect, useState } from "react";
import axios from "axios";

export interface Document {
  id: string;
  filename: string;
  file_url: string;
}

export function useDocuments() {
  const [documents, setDocuments] =
    useState<Document[]>([]);

  const fetchDocuments =
    async () => {
      try {
        const response =
          await axios.get(
            "http://localhost:8000/documents/list"
          );

        setDocuments(
          response.data
        );
      } catch (error) {
        console.error(error);
      }
    };

  const deleteDocument =
    async (id: string) => {
      try {
        await axios.delete(
          `http://localhost:8000/documents/${id}`
        );

        fetchDocuments();
      } catch (error) {
        console.error(error);
      }
    };

  useEffect(() => {
    fetchDocuments();
  }, []);

  return {
    documents,
    deleteDocument,
    fetchDocuments,
  };
}