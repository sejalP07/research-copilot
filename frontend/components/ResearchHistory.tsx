import { HistoryItem } from "@/hooks/useHistory";

interface Props {
  history: HistoryItem[];
}

export default function ResearchHistory({
  history,
}: Props) {
  return (
    <div className="w-72 border-r min-h-screen p-4 bg-gray-50">
      <h2 className="text-xl font-bold mb-4">
        Research History
      </h2>

      <div className="space-y-2">
        {history.map((item) => (
          <div
            key={item.id}
            className="p-3 bg-white border rounded cursor-pointer hover:bg-gray-100"
          >
            <p className="text-sm">
              {item.question}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}