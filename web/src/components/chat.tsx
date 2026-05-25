import { forwardRef, type FormEvent, type ReactNode } from "react";
import type { AppChatHistoryEntry, AppPendingConnectorConfirmation } from "../lib/api";
import type { ChatDeliveryState } from "../lib/chat-transcript";

export type ChatCognitiveBeltItem = {
  key: string;
  eyebrow: string;
  title: string;
  body: string;
  bodyLines?: string[];
  meta: string;
  tone: "lead" | "soft" | "progress";
};

export type PendingConnectorConfirmationState = "idle" | "submitting" | "success" | "error";

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

export function ChatTopbar({
  title,
  activeSummary,
  linkedChannelsLabel,
  preferredLanguageLabel,
}: {
  title: string;
  activeSummary: string;
  linkedChannelsLabel: string;
  preferredLanguageLabel: string;
}) {
  return (
    <div className="aion-chat-topbar">
      <div className="aion-chat-headline">
        <div className="flex flex-wrap items-center gap-2.5">
          <h2 className="aion-chat-title">{title}</h2>
          <span className="aion-chat-live-status">
            <span className="aion-chat-live-status-dot" />
            {activeSummary}
          </span>
        </div>
      </div>
      <div className="aion-chat-route-posture">
        <span>{linkedChannelsLabel}</span>
        <span>{preferredLanguageLabel}</span>
      </div>
    </div>
  );
}

export const ChatTranscriptMessageRow = forwardRef<
  HTMLDivElement,
  {
    isUser: boolean;
    preview: boolean;
    speakerLabel: string;
    timestampLabel: string;
    sourceLabel: string;
    deliveryState: ChatDeliveryState | null;
    deliveryLabel: string | null;
    children: ReactNode;
  }
>(function ChatTranscriptMessageRow(
  {
    isUser,
    preview,
    speakerLabel,
    timestampLabel,
    sourceLabel,
    deliveryState,
    deliveryLabel,
    children,
  },
  ref,
) {
  return (
    <div
      ref={ref}
      className={`aion-chat-message-row ${isUser ? "justify-end" : "justify-start"}`}
    >
      {!isUser ? <span className="aion-chat-avatar">A</span> : null}
      <article className={`aion-chat-message ${isUser ? "aion-chat-message-user" : "aion-chat-message-assistant"}`}>
        <div className={`aion-chat-message-meta ${preview ? "aion-chat-message-meta-preview" : ""}`}>
          <span className="aion-chat-message-speaker">{speakerLabel}</span>
          <span className="aion-chat-meta-separator" aria-hidden="true" />
          <span>{timestampLabel}</span>
          <span className="aion-chat-source-marker">{sourceLabel}</span>
          {deliveryState && deliveryLabel ? (
            <span
              aria-label={deliveryLabel}
              className={`aion-chat-delivery-status aion-chat-delivery-status-${deliveryState}`}
              title={deliveryLabel}
            />
          ) : null}
        </div>
        <div className={`aion-chat-message-copy ${preview ? "aion-chat-message-copy-preview" : ""}`}>
          {children}
        </div>
      </article>
    </div>
  );
});

export const ChatTranscriptShell = forwardRef<
  HTMLDivElement,
  {
    loadingFallback?: ReactNode;
    transcript: ReactNode;
    composer: ReactNode;
  }
>(function ChatTranscriptShell(
  {
    loadingFallback,
    transcript,
    composer,
  },
  ref,
) {
  return (
    <div className="aion-chat-thread-column">
      <div
        ref={ref}
        className="aion-chat-transcript"
      >
        {loadingFallback}
        {transcript}
      </div>
      {composer}
    </div>
  );
});

export function ChatTranscriptMessageList({
  messages,
  preview,
  userSpeakerLabel,
  assistantSpeakerLabel,
  getDeliveryState,
  getDeliveryLabel,
  getSourceLabel,
  getTimestampLabel,
  renderMessage,
  registerMessageRef,
}: {
  messages: AppChatHistoryEntry[];
  preview: boolean;
  userSpeakerLabel: string;
  assistantSpeakerLabel: string;
  getDeliveryState: (message: AppChatHistoryEntry) => ChatDeliveryState | null;
  getDeliveryLabel: (deliveryState: ChatDeliveryState | null) => string | null;
  getSourceLabel: (message: AppChatHistoryEntry) => string;
  getTimestampLabel: (message: AppChatHistoryEntry) => string;
  renderMessage: (message: AppChatHistoryEntry) => ReactNode;
  registerMessageRef: (messageId: string, node: HTMLDivElement | null) => void;
}) {
  return (
    <>
      {messages.map((message) => {
        const isUser = message.role === "user";
        const deliveryState = getDeliveryState(message);
        const deliveryLabel = getDeliveryLabel(deliveryState);

        return (
          <ChatTranscriptMessageRow
            key={message.message_id}
            ref={(node) => {
              registerMessageRef(message.message_id, node);
            }}
            isUser={isUser}
            preview={preview}
            speakerLabel={isUser ? userSpeakerLabel : assistantSpeakerLabel}
            timestampLabel={getTimestampLabel(message)}
            sourceLabel={getSourceLabel(message)}
            deliveryState={deliveryState}
            deliveryLabel={deliveryLabel}
          >
            {renderMessage(message)}
          </ChatTranscriptMessageRow>
        );
      })}
    </>
  );
}

export function ChatCognitiveBelt({
  items,
  goalProgress,
}: {
  items: ChatCognitiveBeltItem[];
  goalProgress: string;
}) {
  return (
    <div className="aion-chat-cognitive-belt" aria-label="Conversation context">
      {items.map((item) => (
        <section
          key={item.key}
          className={`aion-chat-belt-item aion-chat-belt-item-${item.tone}`}
        >
          <div className="aion-chat-belt-item-head">
            <p className="aion-chat-belt-item-label">{item.eyebrow}</p>
            <span className="aion-chat-belt-item-meta">{item.meta}</span>
          </div>
          <p className="aion-chat-belt-item-title">{item.title}</p>
          <p
            className={`aion-chat-belt-item-body ${
              item.bodyLines?.length ? "aion-chat-belt-item-body-lines" : ""
            }`}
          >
            {item.bodyLines?.length
              ? item.bodyLines.map((line) => (
                  <span key={line} className="aion-chat-belt-item-body-line">
                    {line}
                  </span>
                ))
              : item.body}
          </p>
          {item.key === "goal" ? (
            <div className="aion-chat-belt-item-progress" aria-hidden="true">
              <span style={{ width: goalProgress }} />
            </div>
          ) : null}
        </section>
      ))}
    </div>
  );
}

export function ChatPortraitPanel({
  currentFocus,
  emphasis,
  learnedCueCount,
}: {
  currentFocus: string;
  emphasis: string;
  learnedCueCount: string;
}) {
  return (
    <aside className="aion-chat-portrait-panel aion-chat-portrait-panel-elevated">
      <article className="aion-chat-portrait-note aion-chat-portrait-note-memory">
        <p className="aion-chat-portrait-note-eyebrow">Memory continuity</p>
        <p className="aion-chat-portrait-note-title">Strong coherence</p>
        <p className="aion-chat-portrait-note-body">
          Preferences stable across touchpoints.
        </p>
      </article>
      <article className="aion-chat-portrait-note aion-chat-portrait-note-expression">
        <p className="aion-chat-portrait-note-eyebrow">Expression</p>
        <p className="aion-chat-portrait-note-title">Attentive</p>
        <p className="aion-chat-portrait-note-body">
          Listening and synthesizing context.
        </p>
      </article>
      <article className="aion-chat-portrait-note aion-chat-portrait-note-channels">
        <p className="aion-chat-portrait-note-eyebrow">Channel</p>
        <p className="aion-chat-portrait-note-title">App</p>
        <p className="aion-chat-portrait-note-body">
          Private focused environment.
        </p>
      </article>
      <div className="aion-chat-portrait-overlay">
        <p className="text-[11px] uppercase tracking-[0.22em] text-[#5f8f93]">Planning</p>
        <p className="mt-2 font-display text-[1.62rem] leading-[1.08] text-base-900">{currentFocus}</p>
        <div className="aion-chat-portrait-overlay-facts mt-3 text-[0.8rem] text-base-800">
          <div className="aion-chat-portrait-overlay-fact flex items-center justify-between gap-3">
            <span>Current focus</span>
            <span className="font-semibold text-base-900">{emphasis}</span>
          </div>
          <div className="aion-chat-portrait-overlay-fact aion-chat-portrait-overlay-fact-secondary flex items-center justify-between gap-3">
            <span>Learned cues</span>
            <span className="font-semibold text-[#5f8f93]">
              {learnedCueCount}
            </span>
          </div>
        </div>
      </div>
      <div className="aion-chat-portrait-copy">
        <span className="aion-chat-portrait-chip">Embodied cognition</span>
        <p className="mt-3.5 max-w-[12rem] text-[0.84rem] leading-6 text-base-800">
          Clarity forms before action takes shape.
        </p>
      </div>
    </aside>
  );
}

export function ChatComposerShell({
  quickActions,
  text,
  placeholder,
  sending,
  sendLabel,
  note,
  pendingConfirmation,
  pendingConfirmationLabel,
  pendingConfirmationBlockedLabel,
  pendingConfirmationConfirmLabel,
  pendingConfirmationSubmittingLabel,
  pendingConfirmationCompleteLabel,
  pendingConfirmationState,
  pendingConfirmationFeedback,
  attachments,
  attachIcon,
  sendIcon,
  onQuickAction,
  onConfirmPendingConfirmation,
  onAttachFiles,
  onRemoveAttachment,
  onTextChange,
  onSubmit,
}: {
  quickActions: string[];
  text: string;
  placeholder: string;
  sending: boolean;
  sendLabel: string;
  note: string;
  pendingConfirmation: AppPendingConnectorConfirmation | null;
  pendingConfirmationLabel: string;
  pendingConfirmationBlockedLabel: string;
  pendingConfirmationConfirmLabel: string;
  pendingConfirmationSubmittingLabel: string;
  pendingConfirmationCompleteLabel: string;
  pendingConfirmationState: PendingConnectorConfirmationState;
  pendingConfirmationFeedback: string | null;
  attachments: Array<{ id: string; name: string; sizeLabel: string }>;
  attachIcon: ReactNode;
  sendIcon: ReactNode;
  onQuickAction: (value: string) => void;
  onConfirmPendingConfirmation: () => void;
  onAttachFiles: (files: FileList | null) => void;
  onRemoveAttachment: (attachmentId: string) => void;
  onTextChange: (value: string) => void;
  onSubmit: (event: FormEvent<HTMLFormElement>) => void;
}) {
  const pendingConfirmationBusy = pendingConfirmationState === "submitting";
  const pendingConfirmationEyebrow =
    !pendingConfirmation && pendingConfirmationState === "success"
      ? pendingConfirmationCompleteLabel
      : pendingConfirmationLabel;

  return (
    <div className="aion-chat-composer-zone">
      <div className="aion-chat-action-tray">
        {quickActions.map((action) => (
          <button
            key={action}
            className={`aion-chat-action-chip ${
              quickActions.length === 1 ? "aion-chat-action-chip-solo" : ""
            }`}
            type="button"
            onClick={() => onQuickAction(action)}
          >
            {action}
          </button>
        ))}
      </div>
      {pendingConfirmation || pendingConfirmationFeedback ? (
        <section className="aion-chat-pending-confirmation" aria-live="polite">
          <div className="aion-chat-pending-confirmation-copy">
            <p className="aion-chat-pending-confirmation-eyebrow">
              {pendingConfirmationEyebrow}
            </p>
            {pendingConfirmation ? (
              <>
                <p className="aion-chat-pending-confirmation-title">
                  {pendingConfirmation.provider_hint ?? pendingConfirmation.connector_kind}
                  {" / "}
                  {pendingConfirmation.operation}
                </p>
                <p className="aion-chat-pending-confirmation-body">
                  {pendingConfirmation.candidate_summary}
                </p>
              </>
            ) : null}
            {pendingConfirmationFeedback ? (
              <p
                className={`aion-chat-pending-confirmation-feedback aion-chat-pending-confirmation-feedback-${pendingConfirmationState}`}
              >
                {pendingConfirmationFeedback}
              </p>
            ) : null}
          </div>
          {pendingConfirmation ? (
            <div className="aion-chat-pending-confirmation-actions">
              <span className="aion-chat-pending-confirmation-chip">
                {pendingConfirmationBlockedLabel}
              </span>
              <button
                className="aion-chat-pending-confirmation-button"
                disabled={pendingConfirmationBusy}
                type="button"
                onClick={onConfirmPendingConfirmation}
              >
                {pendingConfirmationBusy ? pendingConfirmationSubmittingLabel : pendingConfirmationConfirmLabel}
              </button>
            </div>
          ) : null}
        </section>
      ) : null}
      <form className="aion-chat-composer" onSubmit={onSubmit}>
        {attachments.length > 0 ? (
          <div className="aion-chat-attachment-row" aria-label="Attached files">
            {attachments.map((attachment) => (
              <span key={attachment.id} className="aion-chat-attachment-chip">
                <span className="aion-chat-attachment-chip-name">{attachment.name}</span>
                <span className="aion-chat-attachment-chip-size">{attachment.sizeLabel}</span>
                <button
                  aria-label={`Remove ${attachment.name}`}
                  className="aion-chat-attachment-chip-remove"
                  type="button"
                  onClick={() => onRemoveAttachment(attachment.id)}
                >
                  ×
                </button>
              </span>
            ))}
          </div>
        ) : null}
        <div className="aion-chat-composer-primary">
          <label className="aion-chat-icon-button aion-chat-attach-button" aria-label="Add files">
            {attachIcon}
            <input
              className="aion-chat-file-input"
              type="file"
              multiple
              onChange={(event) => {
                onAttachFiles(event.target.files);
                event.currentTarget.value = "";
              }}
            />
          </label>
          <div className="aion-chat-input-stack">
            <textarea
              aria-label={placeholder}
              className="aion-chat-input"
              placeholder={placeholder}
              value={text}
              onChange={(event) => onTextChange(event.target.value)}
            />
          </div>
          <button
            aria-label={sendLabel}
            className="aion-chat-send"
            disabled={sending}
            type="submit"
          >
            {sending ? "..." : sendIcon}
          </button>
        </div>
      </form>
      <p className="aion-chat-composer-note">{note}</p>
    </div>
  );
}
