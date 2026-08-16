# 🛒 ShopWhisper AI

**ShopWhisper AI** is a voice-enabled conversational e-commerce assistant. Built using Python, OpenAI's Chat Completions API, local speech transcription via OpenAI Whisper, and Text-to-Speech (gTTS) integrated with Gradio, it allows users to interact with product catalogs using natural speech or text.

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


[ User Speech Input ] ──> [ Audio Recorder ] ──> [ OpenAI Whisper (Local STT) ]
                                                              │
                                                              ▼
[ Audio Output ] <─────── [ gTTS Engine ] <─────── [ OpenAI Chat API ]


shopwhisper-ai/
├── app.py                # Main application code (Gradio UI & API backend)
├── requirements.txt      # Python package dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Excludes secrets and temporary audio files
└── README.md             # Project documentation
