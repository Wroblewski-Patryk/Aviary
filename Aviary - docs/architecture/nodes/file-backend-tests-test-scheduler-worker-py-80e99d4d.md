---
id: "FILE-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-80E99D4D"
name: "test_scheduler_worker.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_scheduler_worker.py"
related_files: []
tags: ["auto", "test"]
---

# test_scheduler_worker.py

ID: `FILE-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-80E99D4D`

## Summary

Repository file `backend/tests/test_scheduler_worker.py` auto-discovered for architecture graph inventory.

## Links

- parent: none
- children: none
- depends_on: none
- used_by: none
- ui_related: none
- api_related: none
- database_related: none
- tests_related: none
- docs_related: none
- agent_related: none

## Relations

Outgoing:
- `parent_of` -> [[pyclass-backend-tests-test-scheduler-worker-py-fakereflectionworker-fcfaa8d0|PYCLASS-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-FAKEREFLECTIONWORKER-FCFAA8D0]]: `backend/tests/test_scheduler_worker.py` contains class `FakeReflectionWorker`.
- `parent_of` -> [[pyclass-backend-tests-test-scheduler-worker-py-fakememoryrepository-22442dfc|PYCLASS-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-FAKEMEMORYREPOSITORY-22442DFC]]: `backend/tests/test_scheduler_worker.py` contains class `FakeMemoryRepository`.
- `parent_of` -> [[pyclass-backend-tests-test-scheduler-worker-py-fakeruntime-ddd2998c|PYCLASS-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-FAKERUNTIME-DDD2998C]]: `backend/tests/test_scheduler_worker.py` contains class `FakeRuntime`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-re-d8798933|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-RE-D8798933]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_reflection_tick_runs_in_deferred_mode`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-re-fd065387|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-RE-FD065387]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_reflection_tick_skips_when_in_process_worker_is_running`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-re-eaedf3cb|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-RE-EAEDF3CB]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_reflection_tick_dispatches_when_in_process_worker_is_stopped`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-ma-db54543a|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-MA-DB54543A]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_maintenance_tick_uses_reflection_worker_guardrail_settings`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-ma-151c1b21|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-MA-151C1B21]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_maintenance_tick_hands_due_planned_work_to_proposal_boundary`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-ma-36255f3a|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-MA-36255F3A]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_maintenance_tick_dispatches_due_planned_work_via_runtime_foreground`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-de-74f97baf|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-DE-74F97BAF]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_delays_due_planned_work_during_quiet_hours`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-ad-35f195b4|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-AD-35F195B4]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_advances_recurring_due_planned_work_after_successful_delivery`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-st-cade4cc6|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-ST-CADE4CC6]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_start_is_noop_when_scheduler_disabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-ex-fe6a249d|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-EX-FE6A249D]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_externalized_execution_mode_disables_in_process_start`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-ma-09e56b2a|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-MA-09E56B2A]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_maintenance_tick_skips_when_execution_mode_is_externalized`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-ex-dfb070f4|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-EX-DFB070F4]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_external_maintenance_tick_runs_when_execution_mode_is_externalized`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-ex-756f5a48|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-EX-756F5A48]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_external_proactive_tick_noops_without_observer_admitted_work`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-sn-87c90e6e|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-SN-87C90E6E]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_snapshot_exposes_owner_aware_execution_posture`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-pr-d5032d11|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-PR-D5032D11]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_proactive_tick_noops_for_generic_candidates_without_due_work`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-pr-64ba28d1|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-PR-64BA28D1]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_proactive_tick_admits_due_planned_work_to_foreground`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-pr-80c66660|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-PR-80C66660]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_proactive_tick_persists_blocked_passive_active_evidence`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-sn-cc6bb736|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-SN-CC6BB736]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_snapshot_exposes_live_proactive_policy`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-re-49869e34|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-RE-49869E34]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_reflection_tick_logs_worker_mode_handoff_posture`.
- `parent_of` -> [[pyfunc-backend-tests-test-scheduler-worker-py-test-scheduler-worker-re-4fdba0a2|PYFUNC-BACKEND-TESTS-TEST-SCHEDULER-WORKER-PY-TEST-SCHEDULER-WORKER-RE-4FDBA0A2]]: `backend/tests/test_scheduler_worker.py` contains function `test_scheduler_worker_reflection_tick_logs_in_process_handoff_posture_when_worker_stopped`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
