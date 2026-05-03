export function ChatFlowStage({
  label,
  title,
  detail,
  active = false,
}: {
  label: string;
  title: string;
  detail: string;
  active?: boolean;
}) {
  return (
    <article className={`aion-chat-flow-stage ${active ? "aion-chat-flow-stage-active" : ""}`}>
      <span className={`aion-chat-flow-icon ${active ? "aion-chat-flow-icon-active" : ""}`}>{label}</span>
      <div>
        <p className="text-base font-semibold text-base-900">{title}</p>
        <p className="mt-1 text-sm leading-6 text-base-800">{detail}</p>
      </div>
    </article>
  );
}
