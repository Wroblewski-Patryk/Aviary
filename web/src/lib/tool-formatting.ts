export type ToolFormattingCopy = {
  statusAlwaysOn: string;
  statusReadyToUse: string;
  statusLinkRequired: string;
  statusNeedsReview: string;
  linkStateLinkedValue: string;
  linkStateNotLinkedValue: string;
  linkStateRequiredValue: string;
  linkStatePendingValue: string;
  linkStateUnknownValue: string;
};

export function toolStatusClass(status: string) {
  if (status === "integral_active" || status === "provider_ready") {
    return "badge-success";
  }
  if (status === "provider_ready_link_required") {
    return "badge-warning";
  }
  return "badge-outline";
}

export function formatToolState(status: string, toolsCopy: ToolFormattingCopy) {
  if (status === "integral_active") {
    return toolsCopy.statusAlwaysOn;
  }
  if (status === "provider_ready") {
    return toolsCopy.statusReadyToUse;
  }
  if (status === "provider_ready_link_required") {
    return toolsCopy.statusLinkRequired;
  }
  return toolsCopy.statusNeedsReview;
}

export function formatToolLinkState(status: string, toolsCopy: ToolFormattingCopy) {
  if (status === "linked") {
    return toolsCopy.linkStateLinkedValue;
  }
  if (status === "not_linked") {
    return toolsCopy.linkStateNotLinkedValue;
  }
  if (status === "link_required") {
    return toolsCopy.linkStateRequiredValue;
  }
  if (status === "pending_confirmation") {
    return toolsCopy.linkStatePendingValue;
  }
  return toolsCopy.linkStateUnknownValue;
}

export function summarizeToolAction(nextActions: string[], fallback: string) {
  const action = nextActions[0];
  if (!action) {
    return fallback;
  }
  return formatToolAction(action);
}

export function formatToolAction(action: string) {
  const actionCopy: Record<string, string> = {
    configure_clickup_api_token_and_clickup_list_id: "Add ClickUp token and list ID",
    configure_google_calendar_access_token_and_calendar_id: "Connect Google Calendar access",
    configure_google_calendar_access_token_calendar_id_and_timezone: "Connect Google Calendar access",
    configure_google_drive_access_token_and_folder_id: "Connect Google Drive folder access",
    generate_link_code_and_confirm_from_telegram_chat: "Start Telegram link confirmation",
    ready_for_clickup_operator_acceptance: "Ready for ClickUp operator acceptance",
    ready_for_google_calendar_operator_acceptance: "Ready for Google Calendar operator acceptance",
    ready_for_google_drive_operator_acceptance: "Ready for Google Drive operator acceptance",
    send_link_code_to_configured_telegram_bot: "Send link code to Telegram bot",
    telegram_link_confirmed: "Telegram link confirmed",
  };

  return actionCopy[action] ?? action.replaceAll("_", " ");
}
