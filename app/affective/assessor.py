from typing import Any, Protocol

from app.core.contracts import AffectiveAssessmentOutput


class AffectiveClassifierClient(Protocol):
    async def classify_affective_state(self, *, user_text: str, response_language: str) -> dict[str, Any] | None: ...


class AffectiveAssessor:
    ALLOWED_LABELS = {
        "neutral",
        "support_distress",
        "urgent_pressure",
        "positive_engagement",
    }

    def __init__(self, classifier_client: AffectiveClassifierClient | None = None):
        self.classifier_client = classifier_client

    async def assess(
        self,
        *,
        user_text: str,
        response_language: str,
        fallback: AffectiveAssessmentOutput,
    ) -> AffectiveAssessmentOutput:
        text = str(user_text or "").strip()
        if not text:
            return self._fallback_output(fallback)

        if self.classifier_client is None:
            return self._fallback_output(fallback)

        raw = await self.classifier_client.classify_affective_state(
            user_text=text,
            response_language=response_language,
        )
        if not isinstance(raw, dict):
            return self._fallback_output(fallback)

        normalized = self._normalize_output(raw)
        if normalized is None:
            return self._fallback_output(fallback)

        return normalized

    def _fallback_output(self, fallback: AffectiveAssessmentOutput) -> AffectiveAssessmentOutput:
        return fallback.model_copy(update={"source": "fallback"})

    def _normalize_output(self, raw: dict[str, Any]) -> AffectiveAssessmentOutput | None:
        label = str(raw.get("affect_label", "")).strip().lower()
        if label not in self.ALLOWED_LABELS:
            return None

        intensity = self._clamp_float(raw.get("intensity"))
        confidence = self._clamp_float(raw.get("confidence"))
        needs_support = bool(raw.get("needs_support", False))
        evidence = self._normalize_evidence(raw.get("evidence"))

        if label == "support_distress":
            needs_support = True

        return AffectiveAssessmentOutput(
            affect_label=label,
            intensity=intensity,
            needs_support=needs_support,
            confidence=confidence,
            source="ai_classifier",
            evidence=evidence,
        )

    def _clamp_float(self, value: object) -> float:
        try:
            numeric = float(value)  # type: ignore[arg-type]
        except (TypeError, ValueError):
            numeric = 0.0
        return max(0.0, min(1.0, round(numeric, 2)))

    def _normalize_evidence(self, value: object) -> list[str]:
        if not isinstance(value, list):
            return []
        evidence: list[str] = []
        for item in value:
            text = str(item or "").strip()
            if not text:
                continue
            evidence.append(text[:80])
            if len(evidence) >= 3:
                break
        return evidence
