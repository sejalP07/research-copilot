interface Document {
  id: string;
  filename: string;
  file_url: string;
}

interface Props {
  documents: Document[];
  deleteDocument: (
    id: string
  ) => void;
}

export default function DocumentList({
  documents,
  deleteDocument,
}: Props) {
  return (
    <div className="mt-8">
      <h2 className="text-xl font-bold mb-4">
        My Documents
      </h2>

      <div className="space-y-3">
        {documents.map(
          (doc) => (
            <div
              key={doc.id}
              className="border p-3 rounded flex justify-between items-center"
            >
              <span>
                {doc.filename}
              </span>

              <div className="space-x-2">
                <a
                  href={doc.file_url}
                  target="_blank"
                  className="px-3 py-1 bg-blue-500 text-white rounded"
                >
                  View
                </a>

                <button
                  onClick={() =>
                    deleteDocument(
                      doc.id
                    )
                  }
                  className="px-3 py-1 bg-red-500 text-white rounded"
                >
                  Delete
                </button>
              </div>
            </div>
          )
        )}
      </div>
    </div>
  );
}
