# Event Contract

## Purpose

This document defines the standard structure for all inputs in AION.

Every stimulus must be converted into a unified event format before processing.

This ensures:

- consistency  
- scalability  
- predictable behavior  

---

## Core Principle

Everything is an event.

Sources may vary:

- Telegram  
- system triggers  
- scheduler  
- API calls  

But all must be normalized.

---

## Text-First Baseline And Multimodal Direction

The current canonical event examples remain text-first.

This means the stable repo contract still treats normalized user text as the
primary conscious-turn input, even when the transport is Telegram.

Future multimodal support is allowed only through the same normalization
boundary, not by letting raw transport payloads leak directly into cognition.

If photo, voice, or later app-native media support is added, the transport
adapter should first reduce it into bounded normalized fields such as:

- user text
- caption text
- speech transcription
- attachment metadata needed for later action-owned retrieval or delivery

Raw binary provider payloads must remain outside the cognitive contract until
an explicit normalized media schema is approved.

---

## Event Structure

{
  "event_id": "uuid",
  "source": "telegram|system|scheduler|api",
  "subsource": "user_message|ritual|alert",
  "timestamp": "ISO-8601",
  "payload": {},
  "meta": {
    "user_id": "uuid",
    "trace_id": "uuid"
  }
}

---

## Field Definitions

event_id  
Unique identifier for event  

source  
High-level origin  

subsource  
Specific type  

timestamp  
Time of occurrence  

payload  
Event data  

meta  
Operational metadata  

---

## Example – Telegram Message

{
  "event_id": "evt_001",
  "source": "telegram",
  "subsource": "user_message",
  "timestamp": "2026-01-01T10:00:00Z",
  "payload": {
    "text": "Pomóż mi zaplanować dzień"
  },
  "meta": {
    "user_id": "user_1",
    "trace_id": "trace_1"
  }
}

---

## Example – Scheduled Event

{
  "event_id": "evt_002",
  "source": "scheduler",
  "subsource": "morning_check",
  "timestamp": "2026-01-01T07:00:00Z",
  "payload": {},
  "meta": {
    "user_id": "user_1",
    "trace_id": "trace_2"
  }
}

---

## Future Multimodal Example

Illustrative direction only; this is not yet the frozen production contract:

{
  "event_id": "evt_003",
  "source": "telegram",
  "subsource": "user_message",
  "timestamp": "2026-01-01T10:05:00Z",
  "payload": {
    "text": "Powiedz, co widzisz na zdjęciu",
    "caption_text": "to ja na spacerze",
    "speech_text": null,
    "attachments": [
      {
        "kind": "image",
        "provider_file_id": "telegram-file-id",
        "mime_type": "image/jpeg"
      }
    ]
  },
  "meta": {
    "user_id": "user_1",
    "trace_id": "trace_3"
  }
}

Any final multimodal payload shape must stay transport-neutral enough to work
for Telegram now and a later first-party app without creating parallel event
contracts per channel.

---

## Runtime State

After normalization, event becomes runtime state.

{
  "event": {},
  "context": {},
  "memory": {},
  "motivation": {},
  "role": null,
  "plan": null,
  "result": null
}

---

## Rules

- every input must follow event structure  
- no direct raw input processing  
- no exceptions  

## Linked-Channel Continuity Baseline

The first-party authenticated app remains the canonical conversation surface.

Linked channels such as Telegram are ingress and egress transports that attach
to the same backend-owned user continuity after explicit account linking.

Contract implications:

1. a linked-channel inbound user message must still normalize into one shared
   event and one shared `user_id` continuity owner
2. linked-channel ingress must enrich the canonical app transcript rather than
   create a parallel conversation history
3. channel-specific transport metadata may exist in payload or delivery layers,
   but it must not fork event semantics into separate cognitive contracts
4. future linked channels should reuse this same normalization posture instead
   of introducing per-channel reasoning pipelines

---

## Benefits

- unified pipeline  
- easier debugging  
- easier scaling  
- predictable system behavior  

---

## Final Principle

If something enters AION,
it must become an event first.

Without this rule,
architecture breaks.
