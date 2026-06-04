import SourceCard from "./SourceCard";

interface Source {
  title: string;
  url: string;
}

interface Props {
  answer: string;
  sources: Source[];
}

export default function ResearchResult({
  answer,
  sources,
}: Props) {
  if (!answer) return null;

  return (
    <div className="mt-6 border rounded-lg p-6 bg-white shadow-sm">
      <h2 className="text-xl font-semibold mb-4">
        Answer
      </h2>

      <div className="whitespace-pre-wrap text-gray-800">
        {answer}
      </div>

      {sources && sources.length > 0 && (
        <div className="mt-8">
          <h3 className="text-lg font-semibold mb-3">
            Sources
          </h3>

          <div className="space-y-2">
            {sources.map((source, index) => (
              <SourceCard
                key={index}
                title={source.title}
                url={source.url}
              />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}