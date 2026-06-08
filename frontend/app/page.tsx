"use client";

import ChatInput from "@/components/ChatInput";
import ResearchResult from "@/components/ResearchResult";
import ResearchHistory from "@/components/ResearchHistory";
import DocumentList from "@/components/DocumentList";
import FileUpload from "@/components/FileUpload";

import { useResearch } from "@/hooks/useResearch";
import { useHistory } from "@/hooks/useHistory";
import { useDocuments } from "@/hooks/useDocuments";

export default function Home() {
  const {
    loading,
    answer,
    sources,
    research,
  } = useResearch();

  const {
    history,
  } = useHistory();

  const {
    documents,
    deleteDocument,
    refreshDocuments,
  } = useDocuments();

  return (
    <main className="flex min-h-screen bg-gray-50">
      <ResearchHistory
        history={history}
      />

      <div className="flex-1 p-10">
        <h1 className="text-4xl font-bold mb-8">
          Research Copilot
        </h1>

        {/* PDF Upload Section */}
        <FileUpload
          onUploadSuccess={
            refreshDocuments
          }
        />

        {/* Research Section */}
        <ChatInput
          onSubmit={research}
        />

        {loading && (
          <p className="mt-4">
            Researching...
          </p>
        )}

        <ResearchResult
          answer={answer}
          sources={sources}
        />

        {/* Documents Section */}
        <DocumentList
          documents={documents}
          deleteDocument={
            deleteDocument
          }
        />
      </div>
    </main>
  );
}