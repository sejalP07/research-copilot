"use client";

import { useState } from "react";
import axios from "axios";

export default function FileUpload() {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");

  const uploadFile = async () => {
    if (!file) {
      setMessage("Please select a PDF file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setUploading(true);
      setMessage("");

      const response = await axios.post(
        "http://localhost:8000/documents",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setMessage("✅ PDF uploaded successfully!");
      console.log(response.data);
    } catch (error) {
      console.error(error);
      setMessage("❌ Upload failed.");
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="mb-6 p-4 border rounded-lg bg-white shadow-sm">
      <label
        htmlFor="pdf-upload"
        className="block text-sm font-medium mb-2"
      >
        Upload PDF Document
      </label>

      <input
        id="pdf-upload"
        type="file"
        accept=".pdf"
        onChange={(e) =>
          setFile(e.target.files?.[0] || null)
        }
        className="block w-full border rounded p-2 mb-3"
      />

      <button
        onClick={uploadFile}
        disabled={uploading}
        className="px-4 py-2 bg-black text-white rounded hover:bg-gray-800 disabled:opacity-50"
      >
        {uploading ? "Uploading..." : "Upload PDF"}
      </button>

      {message && (
        <p className="mt-3 text-sm">
          {message}
        </p>
      )}
    </div>
  );
}