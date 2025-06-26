interface EntryContentProps {
  children: React.ReactNode;
}

export function EntryContent({ children }: EntryContentProps) {
  return <div className="mt-2 space-y-1">{children}</div>;
}
