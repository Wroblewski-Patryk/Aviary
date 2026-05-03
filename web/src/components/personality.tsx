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

export function PersonalityTimelineRowList({
  items,
  className = "grid gap-3",
}: {
  items: Array<{
    token: string;
    title: string;
    detail: string;
    value: string;
  }>;
  className?: string;
}) {
  return (
    <div className={className}>
      {items.map((row) => (
        <PersonalityTimelineRow
          key={row.title}
          token={row.token}
          title={row.title}
          detail={row.detail}
          value={row.value}
        />
      ))}
    </div>
  );
}

export function PersonalitySignalRowList({
  items,
  className = "grid gap-3",
}: {
  items: Array<{
    label: string;
    value: string;
  }>;
  className?: string;
}) {
  return (
    <div className={className}>
      {items.map((item) => (
        <div key={item.label} className="aion-personality-signal-row">
          <span className="aion-personality-signal-label">{item.label}</span>
          <span className="aion-personality-signal-value">{item.value}</span>
        </div>
      ))}
    </div>
  );
}

export function PersonalityPreviewCalloutList({
  items,
}: {
  items: Array<{
    key: string;
    className: string;
    eyebrow: string;
    title: string;
    body: string;
  }>;
}) {
  return (
    <>
      {items.map((callout) => (
        <article key={callout.key} className={callout.className}>
          <p className="text-[10px] uppercase tracking-[0.18em] text-base-800">{callout.eyebrow}</p>
          <p className="mt-2 font-display text-xl text-base-900">{callout.title}</p>
          <p className="mt-2 text-sm leading-6 text-base-800">{callout.body}</p>
        </article>
      ))}
    </>
  );
}

export function PersonalityActivityRowList({
  items,
  viewLabel,
}: {
  items: Array<{
    key: string;
    title: string;
    when: string;
  }>;
  viewLabel: string;
}) {
  return (
    <div className="grid gap-3">
      {items.map((item) => (
        <div key={item.key} className="aion-personality-activity-row">
          <div>
            <p className="text-sm font-semibold text-base-900">{item.title}</p>
            <p className="mt-1 text-sm text-base-800">{item.when}</p>
          </div>
          <span className="aion-chip-ghost rounded-full px-3 py-1 text-xs font-medium">{viewLabel}</span>
        </div>
      ))}
    </div>
  );
}
