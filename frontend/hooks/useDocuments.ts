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

  const fetchDocuments = async () => {
    try {
      const response =
        await axios.get<Document[]>(
          "http://localhost:8000/documents/list"
        );

      setDocuments(response.data);
    } catch (error) {
      console.error(
        "Error fetching documents:",
        error
      );
    }
  };

  const deleteDocument = async (
    id: string
  ) => {
    try {
      await axios.delete(
        `http://localhost:8000/documents/${id}`
      );

      await fetchDocuments();
    } catch (error) {
      console.error(
        "Error deleting document:",
        error
      );
    }
  };

  const refreshDocuments = () => {
    fetchDocuments();
  };

  useEffect(() => {
    fetchDocuments();
  }, []);

  return {
    documents,
    deleteDocument,
    fetchDocuments,
    refreshDocuments,
  };
}