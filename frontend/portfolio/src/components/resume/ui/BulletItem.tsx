interface BulletItemProps {
  children: React.ReactNode;
  keywords?: string[]; // for future filtering
  faded?: boolean; // for highlighting logic (e.g. opacity)
}

export function BulletItem({ children, faded = false }: BulletItemProps) {
  return (
    <li
      className={`ml-5 list-disc ${
        faded ? "opacity-30" : "opacity-100"
      } transition-opacity duration-300`}
    >
      {children}
    </li>
  );
}
