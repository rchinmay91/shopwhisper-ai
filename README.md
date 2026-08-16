# 🛒 ShopWhisper AI — Multimodal Voice & Text Conversational E-Commerce Engine

<p align="center">
  <a href="https://github.com/rchinmay91/shopwhisper-ai">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python">
    <img src="https://img.shields.io/badge/OpenAI-GPT--4o%20%7C%20GPT--3.5-green?style=for-the-badge&logo=openai" alt="OpenAI">
    <img src="https://img.shields.io/badge/Whisper-Local%20STT-orange?style=for-the-badge&logo=openai" alt="Whisper">
    <img src="https://img.shields.io/badge/Gradio-4.0%2B-red?style=for-the-badge&logo=gradio" alt="Gradio">
    <img src="https://img.shields.io/badge/gTTS-Audio%20Synthesis-yellow?style=for-the-badge" alt="gTTS">
    <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="MIT License">
  </a>
</p>

An enterprise-ready, multimodal **Voice & Text E-Commerce Intelligence Assistant** designed to transform traditional product searching into an interactive, voice-driven shopping experience. Built with an optimized hybrid architecture, this system processes voice input locally using **OpenAI Whisper STT**, decouples intent reasoning via **OpenAI Chat Completions API**, synthesizes voice responses through **gTTS**, and serves a real-time responsive interface built on **Gradio Blocks**.

---

## 🗺️ System Engineering Topology

The dynamic flowchart below illustrates the end-to-end transactional data pipeline—from raw user speech capture down to local audio synthesis and multi-turn state persistence.

```mermaid
flowchart TD
    %% Global Styling Configurations
    classDef input fill:#f5f6fa,stroke:#7f8c8d,stroke-width:2px;
    classDef processing fill:#dff9fb,stroke:#0984e3,stroke-width:1px;
    classDef engine fill:#fff3e0,stroke:#f39c12,stroke-width:2px;
    classDef storage fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px;
    classDef output fill:#f1f2f6,stroke:#2f3542,stroke-width:2px;

    %% Multimodal Input Phase
    subgraph INPUT LAYER
        A1[Microphone Audio Recording]:::input --> B1[Temporal File Handler]:::processing
        A2[Raw Text User Input]:::input --> B2[State Session Buffer]:::processing
    end

    %% Pipeline Processing Phase
    subgraph SPEECH & REASONING PIPELINE
        B1 --> C[OpenAI Whisper Local STT]:::processing
        C --> D[Transcribed Intent String]:::processing
        B2 --> D
        D --> E[System Prompt & History Condenser]:::engine
        E --> F[OpenAI GPT-4o / GPT-3.5 API Endpoint]:::engine
    end

    %% Output Synthesis Phase
    subgraph RESPONSE & AUDIO SYNTHESIS
        F --> G[Text Response Payload]:::processing
        G --> H[Google Text-to-Speech Engine]:::engine
        H --> I[Temporary MP3 Audio Generator]:::processing
        G --> J[Gradio 4.0 Chatbot Presentation UI]:::output
        I --> K[Autoplay Audio Stream Component]:::output
    end




MIT License

Copyright (c) 2026 rchinmay91

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
