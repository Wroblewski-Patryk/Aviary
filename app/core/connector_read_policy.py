from __future__ import annotations


def connector_read_baseline_snapshot() -> dict[str, object]:
    return {
        "policy_owner": "connector_read_execution_baseline",
        "selected_live_read_path": {
            "connector_kind": "calendar",
            "provider": "google_calendar",
            "operation": "read_availability",
            "execution_mode": "provider_backed_next",
            "why_selected": "extends_connector_execution_into_a_bounded_read_only_calendar_slice_without_widening_mutation_scope",
        },
        "deferred_families": {
            "task_system": "current_live_read_path_already_implemented_through_clickup_list_tasks",
            "cloud_drive": "policy_only_until_document_scope_and_safe-read summarization boundary are explicit",
        },
        "current_live_mutation_path": {
            "connector_kind": "task_system",
            "provider": "clickup",
            "operation": "create_task",
        },
    }
