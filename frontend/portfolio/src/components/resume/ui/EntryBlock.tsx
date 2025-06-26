interface EntryBlockProps {
  title: string; // e.g. "Software Engineer"
  subtitle: string; // e.g. "Company Name"
  startDate: Date; // e.g. "Jan 2022"
  endDate?: Date; // e.g. "Present"
  location: string; // e.g. "Remote"
  children?: React.ReactNode;
}

function formatMonthYear(date: Date) {
  return date.toLocaleDateString(undefined, {
    year: "numeric",
    month: "short",
  });
}

export function EntryBlock({
  title,
  subtitle,
  startDate,
  endDate,
  location,
  children,
}: EntryBlockProps) {
  const dateRange = endDate
    ? `${formatMonthYear(startDate)} - ${formatMonthYear(endDate)}`
    : `${formatMonthYear(startDate)} - Present`;

  return (
    <div className="space-y-1">
      <div className="flex flex-wrap items-baseline justify-between gap-4">
        <h3 className="font-semibold">{title}</h3>
        <span className="text-muted-foreground text-sm whitespace-nowrap">
          {dateRange}
        </span>
      </div>

      <div className="flex flex-wrap items-baseline justify-between gap-4">
        <p className="text-muted-foreground text-sm">{subtitle}</p>
        <span className="text-muted-foreground text-sm whitespace-nowrap">
          {location}
        </span>
      </div>

      <div className="mt-2">{children}</div>
    </div>
  );
}
