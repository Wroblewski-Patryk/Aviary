from dataclasses import dataclass

from app.utils.language import normalize_for_matching


@dataclass(frozen=True)
class GoalSignal:
    name: str
    description: str
    priority: str
    goal_type: str


@dataclass(frozen=True)
class TaskSignal:
    name: str
    description: str
    priority: str
    status: str


@dataclass(frozen=True)
class TaskStatusSignal:
    status: str
    task_hint: str


def detect_goal_signal(text: str) -> GoalSignal | None:
    normalized = normalize_for_matching(text)
    if not normalized:
        return None

    patterns = (
        "my goal is to ",
        "the goal is to ",
        "goal: ",
        "i want to achieve ",
        "moim celem jest ",
        "celem jest ",
        "cel: ",
        "chce osiagnac ",
    )
    for pattern in patterns:
        if normalized.startswith(pattern):
            raw = text[len(pattern):].strip() if text.lower().startswith(pattern) else text.strip()
            cleaned = _clean_signal_text(raw, fallback=text)
            if not cleaned:
                return None
            return GoalSignal(
                name=cleaned[:160],
                description=f"User-declared goal: {cleaned[:220]}",
                priority=_goal_priority(normalized),
                goal_type=_goal_type(normalized),
            )
    return None


def detect_task_signal(text: str) -> TaskSignal | None:
    normalized = normalize_for_matching(text)
    if not normalized:
        return None

    patterns = (
        "i need to ",
        "next task is ",
        "task: ",
        "we need to ",
        "musze ",
        "mam zrobic ",
        "zadanie: ",
    )
    for pattern in patterns:
        if normalized.startswith(pattern):
            raw = text[len(pattern):].strip() if text.lower().startswith(pattern) else text.strip()
            cleaned = _clean_signal_text(raw, fallback=text)
            if not cleaned:
                return None
            return TaskSignal(
                name=cleaned[:160],
                description=f"User-declared task: {cleaned[:220]}",
                priority=_task_priority(normalized),
                status="blocked" if _looks_blocked(normalized) else "todo",
            )
    return None


def detect_task_status_signal(text: str) -> TaskStatusSignal | None:
    normalized = normalize_for_matching(text)
    if not normalized:
        return None

    done_prefixes = (
        "i fixed ",
        "fixed ",
        "i finished ",
        "i completed ",
        "i resolved ",
        "done with ",
        "naprawilem ",
        "naprawilam ",
        "skonczylem ",
        "skonczylam ",
        "ukonczylem ",
        "ukonczylam ",
        "rozwiazalem ",
        "rozwiazalam ",
    )
    done_suffixes = (
        " is fixed",
        " was fixed",
        " is done",
        " is completed",
        " is resolved",
        " naprawione",
        " zrobione",
        " skonczone",
        " ukonczone",
        " rozwiazane",
    )
    blocked_prefixes = (
        "i am blocked on ",
        "blocked on ",
        "this is blocked by ",
        "jestem zablokowany na ",
        "jestem zablokowana na ",
        "blokuje mnie ",
    )
    in_progress_prefixes = (
        "i am working on ",
        "working on ",
        "i started ",
        "zaczalem ",
        "zaczelam ",
        "pracuje nad ",
    )
    cancelled_prefixes = (
        "i cancelled ",
        "cancelled ",
        "anulowalem ",
        "anulowalam ",
    )

    for pattern in done_prefixes:
        if normalized.startswith(pattern):
            return TaskStatusSignal(status="done", task_hint=_clean_signal_text(text[len(pattern):], fallback=text))
    for pattern in done_suffixes:
        if normalized.endswith(pattern):
            return TaskStatusSignal(status="done", task_hint=_clean_signal_text(text[: -len(pattern)], fallback=text))
    for pattern in blocked_prefixes:
        if normalized.startswith(pattern):
            return TaskStatusSignal(status="blocked", task_hint=_clean_signal_text(text[len(pattern):], fallback=text))
    for pattern in in_progress_prefixes:
        if normalized.startswith(pattern):
            return TaskStatusSignal(status="in_progress", task_hint=_clean_signal_text(text[len(pattern):], fallback=text))
    for pattern in cancelled_prefixes:
        if normalized.startswith(pattern):
            return TaskStatusSignal(status="cancelled", task_hint=_clean_signal_text(text[len(pattern):], fallback=text))
    return None


def _goal_priority(normalized: str) -> str:
    if any(keyword in normalized for keyword in ("critical", "urgent", "production", "pilne", "produkcja")):
        return "critical"
    if any(keyword in normalized for keyword in ("this week", "mvp", "launch", "wydac", "w tym tygodniu")):
        return "high"
    return "medium"


def _goal_type(normalized: str) -> str:
    if any(keyword in normalized for keyword in ("this week", "today", "tomorrow", "w tym tygodniu", "dzis", "jutro")):
        return "operational"
    if any(keyword in normalized for keyword in ("mvp", "system", "architecture", "projekt", "project")):
        return "tactical"
    return "strategic"


def _task_priority(normalized: str) -> str:
    if any(
        keyword in normalized
        for keyword in ("urgent", "now", "production", "pilne", "teraz", "produkcja", "blocker", "blocked", "blokuje")
    ):
        return "high"
    return "medium"


def _looks_blocked(normalized: str) -> bool:
    return any(
        keyword in normalized
        for keyword in ("blocked", "blocker", "failing", "broken", "zablokowane", "blokuje", "awaria")
    )


def _clean_signal_text(value: str, fallback: str) -> str:
    text = " ".join(value.split()).strip(" .,:;!-")
    if not text:
        text = " ".join(fallback.split()).strip(" .,:;!-")
    return text
