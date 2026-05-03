import type { ReactNode } from "react";

export function ToolsSummaryCard({
  title,
  value,
  note,
}: {
  title: string;
  value: string;
  note: string;
}) {
  return (
    <article className="aion-tools-summary-card">
      <p className="aion-tools-summary-label">{title}</p>
      <p className="aion-tools-summary-value">{value}</p>
      <p className="aion-tools-summary-note">{note}</p>
    </article>
  );
}

export function ToolsFactCard({
  label,
  children,
}: {
  label: string;
  children: ReactNode;
}) {
  return (
    <div className="aion-tools-fact-card">
      <p className="text-xs uppercase tracking-[0.18em] text-base-800">{label}</p>
      {children}
    </div>
  );
}
