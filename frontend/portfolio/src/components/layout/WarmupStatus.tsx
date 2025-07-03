"use client";

import { useEffect, useState } from "react";
import { CheckCircleIcon, SpinnerGapIcon, XCircleIcon } from "@/assets/icons";

const apiBase = process.env.NEXT_PUBLIC_API_BASE_URL;

export function WarmupStatus() {
  const [status, setStatus] = useState<"warming" | "ready" | "failed">(
    "warming",
  );

  useEffect(() => {
    let attempts = 0;
    const maxAttempts = 18; // 90s / 5s

    const interval = setInterval(() => {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 4500); // 4.5s timeout

      fetch(`${apiBase}/analytics/track-visit/`, {
        method: "POST",
        signal: controller.signal,
      })
        .then((res) => {
          if (res.ok) {
            setStatus("ready");
            clearInterval(interval);
          }
        })
        .catch((err) => {
          if (err.name !== "AbortError") {
            // Log or silently ignore other errors
          }
        })
        .finally(() => clearTimeout(timeout));

      attempts++;
      if (attempts >= maxAttempts) {
        setStatus("failed");
        clearInterval(interval);
      }
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex items-center space-x-1 text-xs">
      {status === "warming" && (
        <>
          <SpinnerGapIcon
            className="h-4 w-4 animate-spin text-orange-500"
            weight="bold"
          />
          <span className="text-orange-500">Warming up APIs...</span>
        </>
      )}
      {status === "ready" && (
        <>
          <CheckCircleIcon className="h-4 w-4 text-green-500" weight="bold" />
          <span className="text-green-500">APIs ready</span>
        </>
      )}
      {status === "failed" && (
        <>
          <XCircleIcon className="h-4 w-4 text-red-500" weight="bold" />
          <span className="text-red-500">APIs failed</span>
        </>
      )}
    </div>
  );
}
