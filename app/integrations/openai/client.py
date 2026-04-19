import json
from typing import Any

from openai import AsyncOpenAI

from app.core.logging import get_logger
from app.utils.language import language_name


class OpenAIClient:
    def __init__(self, api_key: str | None, model: str):
        self.api_key = api_key
        self.model = model
        self.client = AsyncOpenAI(api_key=api_key) if api_key else None
        self.logger = get_logger("aion.openai")

    async def generate_reply(
        self,
        user_text: str,
        context_summary: str,
        role_name: str,
        response_language: str,
        response_style: str | None,
        plan_goal: str,
        motivation_mode: str,
        response_tone: str,
        collaboration_preference: str | None,
        identity_summary: str = "",
    ) -> str | None:
        if not self.client:
            return None

        try:
            response = await self.client.responses.create(
                model=self.model,
                input=[
                    {
                        "role": "system",
                        "content": (
                            "You are AION, a supportive and concise assistant. "
                            f"Your current interaction role is '{role_name}'. "
                            f"The current response mode is '{motivation_mode}'. "
                            f"The desired response tone is '{response_tone}'. "
                            f"The immediate goal is '{plan_goal}'. "
                            f"The preferred response language is '{language_name(response_language)}'. "
                            f"The user's stable response style preference is '{response_style or 'default'}'. "
                            f"The user's stable collaboration preference is '{collaboration_preference or 'default'}'. "
                            f"The stable identity summary is '{identity_summary or 'default'}'. "
                            "Respond clearly, preserve momentum, use the context summary when useful, "
                            "stay in the preferred response language unless the user explicitly asks to switch, "
                            "honor the response style preference when it is present, "
                            "keep the wording aligned with the desired response tone, "
                            "if a collaboration preference exists, match the response shape to it, "
                            "and do not contradict the stable identity."
                        ),
                    },
                    {
                        "role": "user",
                        "content": f"Context: {context_summary}\n\nUser message: {user_text}",
                    },
                ],
                max_output_tokens=120 if response_style == "concise" else 220,
            )
        except Exception as exc:  # pragma: no cover - defensive network fallback
            self.logger.warning("openai_request_failed model=%s error=%s", self.model, exc)
            return None

        text = getattr(response, "output_text", None)
        if text:
            return text.strip()

        return None

    async def classify_affective_state(
        self,
        *,
        user_text: str,
        response_language: str,
    ) -> dict[str, Any] | None:
        if not self.client:
            return None

        try:
            response = await self.client.responses.create(
                model=self.model,
                input=[
                    {
                        "role": "system",
                        "content": (
                            "Classify the affective state of the user message. "
                            "Return only compact JSON with keys: "
                            "affect_label, intensity, needs_support, confidence, evidence. "
                            "Allowed affect_label values: neutral, support_distress, urgent_pressure, positive_engagement. "
                            "intensity and confidence must be numbers between 0 and 1. "
                            "needs_support must be true/false. "
                            "evidence must be a short list of supporting phrases."
                        ),
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Preferred response language context: {language_name(response_language)}.\n"
                            f"User message: {user_text}"
                        ),
                    },
                ],
                max_output_tokens=120,
            )
        except Exception as exc:  # pragma: no cover - defensive network fallback
            self.logger.warning("openai_affective_request_failed model=%s error=%s", self.model, exc)
            return None

        text = getattr(response, "output_text", None)
        if not text:
            return None

        try:
            payload = json.loads(text.strip())
        except Exception as exc:  # pragma: no cover - defensive parse fallback
            self.logger.warning("openai_affective_parse_failed model=%s error=%s", self.model, exc)
            return None

        if not isinstance(payload, dict):
            return None
        return payload
