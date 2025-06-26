interface SectionBlockProps {
  title: string;
  children: React.ReactNode;
}

export function SectionBlock({ title, children }: SectionBlockProps) {
  return (
    <section className="mb-8">
      <h2 className="text-xl font-semibold">{title}</h2>
      <div className="bg-muted my-2 h-[1px] w-full" />
      <div className="space-y-4">{children}</div>
    </section>
  );
}
