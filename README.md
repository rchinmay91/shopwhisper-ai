# 🛒 ShopWhisper AI

**ShopWhisper AI** is an enterprise-grade, voice-enabled conversational shopping assistant built with Python, Gradio, OpenAI's Chat Completions API (`gpt-3.5-turbo` / `gpt-4o`), local speech recognition via OpenAI Whisper, and Text-to-Speech synthesis using `gTTS`.

---

## 🎨 Interface Preview

```text
+---------------------------------------------------------------------------------------------------------+
|                                           🛒 ShopWhisper AI                                              |
|                                 Voice-Enabled E-Commerce Assistant                                      |
+--------------------------------------------------------------------+------------------------------------+
|  💬 Conversation                                                   |  🎙️ Voice Interaction               |
| +----------------------------------------------------------------+ | +--------------------------------+ |
| | User: What are the specs and price for the Redmi A1?           | | | [ 🎙️ Record Microphone ]         | |
| |                                                                | | +--------------------------------+ |
| | Bot: The Redmi A1 features 2GB RAM, 32GB storage, a 5000mAh    | | | Transcribed Input:             | |
| |      battery, and dual AI cameras. It is priced at ₹6,499.     | | | "Compare Redmi A1 & 9A Sport"  | |
| +----------------------------------------------------------------+ | +--------------------------------+ |
| | [ Ask about specs, pricing, or recommendations... ]  [ Send ]  | | | [ 🔊 Audio Player: Output.mp3] | |
+--------------------------------------------------------------------+------------------------------------+
