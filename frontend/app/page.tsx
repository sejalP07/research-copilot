"use client";

import ChatInput from "@/components/ChatInput";
import ResearchResult from "@/components/ResearchResult";
import { useResearch } from "@/hooks/useResearch";
import FileUpload from "@/components/FileUpload";

export default function Home() {
  const {
    loading,
    answer,
    sources,
    research,
} = useResearch();

  return (
    <main className="max-w-4xl mx-auto p-10">
      <h1 className="text-4xl font-bold mb-8">
        Research Copilot
      </h1>
      
      <FileUpload />
      <ChatInput onSubmit={research} />

      {loading && (
        <p className="mt-4">Researching...</p>
      )}

     <ResearchResult
  answer={answer}
  sources={sources}
    />
    </main>
  );
}