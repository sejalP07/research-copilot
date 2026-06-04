"use client";

import { useState } from "react";

interface Props {
  onSubmit: (question: string) => void;
}

export default function ChatInput({ onSubmit }: Props) {
  const [question, setQuestion] = useState("");

  return (
    <div className="space-y-4">
      <textarea
        className="w-full border rounded p-3"
        rows={4}
        placeholder="Ask anything..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        className="border px-4 py-2 rounded"
        onClick={() => onSubmit(question)}
      >
        Research
      </button>
    </div>
  );
}