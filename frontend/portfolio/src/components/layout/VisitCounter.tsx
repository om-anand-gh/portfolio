"use client";

import { useEffect, useState } from "react";

const apiBase = process.env.NEXT_PUBLIC_API_BASE_URL;

export default function VisitCounter() {
  const [count, setCount] = useState<number | null>(null);

  useEffect(() => {
    fetch(`${apiBase}/analytics/track-visit/`, {
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => setCount(data.count))
      .catch(() => setCount(null));
  }, []);

  if (count === null) return null;

  return <span className="ml-2 text-xs text-gray-400">• {count} visits</span>;
}
