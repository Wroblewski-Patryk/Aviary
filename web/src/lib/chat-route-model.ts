import { stringValue } from "./learned-state-formatting";

export type ChatIntentCard = {
  title: string;
  body: string;
  status: string;
  emphasis: string;
};

export type ChatMetric = {
  label: string;
  value: string;
};

export type ChatGoalCard = {
  title: string;
  body: string;
  progress: string;
};

export type ChatRelatedMemoryCard = {
  title: string;
  body: string;
  when: string;
};

export type ChatRouteModel = {
  quickActions: string[];
  currentFocus: string;
  linkedChannelsStatus: string;
  intentCard: ChatIntentCard;
  motivationMetrics: ChatMetric[];
  goalCard: ChatGoalCard;
  relatedMemory: ChatRelatedMemoryCard[];
};

function hasCount(summary: Record<string, unknown> | undefined, key: string) {
  return stringValue(summary?.[key], "0") !== "0";
}

export function buildChatRouteModel({
  planningSummary,
  preferenceSummary,
  knowledgeSummary,
  recentChannelsLabel,
  noDataLabel,
}: {
  planningSummary: Record<string, unknown> | undefined;
  preferenceSummary: Record<string, unknown> | undefined;
  knowledgeSummary: Record<string, unknown> | undefined;
  recentChannelsLabel: string;
  noDataLabel: string;
}): ChatRouteModel {
  const hasActiveGoals = hasCount(planningSummary, "active_goal_count");
  const hasActiveTasks = hasCount(planningSummary, "active_task_count");
  const intentCard = {
    title: "Plan my day",
    body: "Choose the next calm step.",
    status: hasActiveGoals ? "Live" : "Ready",
    emphasis: hasActiveGoals ? "High" : "Steady",
  };

  return {
    quickActions: ["Plan my day"],
    currentFocus: hasActiveGoals ? "Daily planning" : "Conversation continuity",
    linkedChannelsStatus: recentChannelsLabel === noDataLabel ? "App only" : recentChannelsLabel,
    intentCard,
    motivationMetrics: [
      { label: "Importance", value: hasActiveGoals ? "0.80" : "0.62" },
      { label: "Urgency", value: hasActiveTasks ? "0.50" : "0.32" },
      { label: "Valence", value: "+0.20" },
      { label: "Arousal", value: "0.60" },
    ],
    goalCard: {
      title: "Project: Next meaningful step",
      body: hasActiveGoals ? "Protect the current plan." : "Shape the next focus point.",
      progress: hasActiveGoals ? "72%" : "36%",
    },
    relatedMemory: [
      {
        title: `${stringValue(preferenceSummary?.learned_preference_count, "0")} learned cues`,
        body: "Preferences stay near.",
        when: "Recent",
      },
      {
        title: `${stringValue(knowledgeSummary?.semantic_conclusion_count, "0")} reusable patterns`,
        body: "Summaries stay near.",
        when: "Today",
      },
    ],
  };
}
