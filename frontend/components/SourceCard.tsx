interface Props {
  title: string;
  url: string;
}

export default function SourceCard({
  title,
  url,
}: Props) {
  return (
    <a
      href={url}
      target="_blank"
      rel="noopener noreferrer"
      className="block border rounded-lg p-3 hover:bg-gray-50 transition"
    >
      <div className="font-medium">
        {title}
      </div>

      <div className="text-sm text-gray-500 truncate">
        {url}
      </div>
    </a>
  );
}