export function PersonalityTimelineRow({
  token,
  title,
  detail,
  value,
}: {
  token: string;
  title: string;
  detail: string;
  value: string;
}) {
  return (
    <article className="aion-personality-timeline-row">
      <span className="aion-personality-timeline-token">{token}</span>
      <div className="min-w-0">
        <p className="text-sm font-semibold text-base-900">{title}</p>
        <p className="mt-1 text-xs leading-6 text-base-800">{detail}</p>
      </div>
      <div className="aion-personality-timeline-track" aria-hidden="true">
        <span />
      </div>
      <span className="aion-personality-timeline-value">{value}</span>
    </article>
  );
}
