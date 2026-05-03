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
