export function StatePanel({
  tone,
  title,
  body,
  loading = false,
}: {
  tone: "neutral" | "success" | "error";
  title: string;
  body: string;
  loading?: boolean;
}) {
  const toneClasses =
    tone === "error"
      ? "border-error/30 bg-error/5 text-base-900"
      : tone === "success"
        ? "border-success/30 bg-success/10 text-base-900"
        : "border-base-300 bg-base-200 text-base-900";

  return (
    <div className={`rounded-2xl border px-4 py-5 ${toneClasses}`}>
      <div className="flex items-start gap-3">
        {loading ? <span className="loading loading-spinner loading-sm mt-0.5 text-primary" /> : null}
        <div>
          <p className="text-sm font-semibold">{title}</p>
          <p className="mt-1 text-sm leading-7 text-base-800">{body}</p>
        </div>
      </div>
    </div>
  );
}

export function FeedbackBanner({
  tone,
  title,
  body,
  detail,
  detailLabel,
}: {
  tone: "success" | "error";
  title: string;
  body: string;
  detail?: string | null;
  detailLabel: string;
}) {
  const toneClasses =
    tone === "error"
      ? "border-error/40 bg-error/8 text-base-900"
      : "border-success/40 bg-success/12 text-base-900";

  return (
    <div className={`mb-4 rounded-[1.5rem] border px-4 py-4 shadow-sm ${toneClasses}`}>
      <p className="text-sm font-semibold">{title}</p>
      <p className="mt-1 text-sm leading-7 text-base-800">{body}</p>
      {detail ? (
        <details className="mt-3">
          <summary className="cursor-pointer text-sm font-medium text-base-900">{detailLabel}</summary>
          <p className="mt-2 break-words rounded-xl bg-base-100/80 px-3 py-3 text-sm leading-7 text-base-800">
            {detail}
          </p>
        </details>
      ) : null}
    </div>
  );
}
