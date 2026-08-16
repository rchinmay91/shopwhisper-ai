import os
import tempfile
import gradio as gr
from gtts import gTTS
import openai
import whisper

# Fetch environment variables safely
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Load Whisper model locally for Speech-to-Text
stt_model = whisper.load_model("base")

SYSTEM_PROMPT = """You are EchoCommerce, an expert product assistant for online shopping. 
Provide concise, helpful product comparisons, pricing insights, and recommendations."""


def generate_voice_response(text: str) -> str:
    """Converts text into audio output using gTTS and returns the temp file path."""
    tts = gTTS(text=text, lang="en", slow=False)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name


def process_voice_input(audio_path: str, chat_history: list):
    """Transcribes audio using Whisper, queries OpenAI GPT, and generates speech output."""
    if not audio_path:
        return chat_history, None, ""

    # Transcribe speech to text using Whisper
    transcription = stt_model.transcribe(audio_path)["text"]

    # Format history for OpenAI Chat Completions API
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for user_msg, assistant_msg in chat_history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": transcription})

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=300
    )
    bot_reply = response.choices[0].message.content

    # Generate synthesized speech output
    audio_response_path = generate_voice_response(bot_reply)

    # Update chat state
    chat_history.append((transcription, bot_reply))
    return chat_history, audio_response_path, transcription


def process_text_input(user_message: str, chat_history: list):
    """Processes plain text user chat interactions."""
    if not user_message.strip():
        return chat_history, ""

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for user_msg, assistant_msg in chat_history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    bot_reply = response.choices[0].message.content

    chat_history.append((user_message, bot_reply))
    return chat_history, ""


# Gradio Block UI
with gr.Blocks(theme=gr.themes.Soft(), title="EchoCommerce AI") as demo:
    gr.Markdown(
        """
        # 🛒 EchoCommerce AI
        ### Your Voice-Enabled E-Commerce & Product Assistant
        """
    )
    
    with gr.Row():
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(label="Conversation", height=450)
            
            with gr.Row():
                text_input = gr.Textbox(
                    placeholder="Ask about product specs, pricing, or recommendations...", 
                    show_label=False,
                    scale=4
                )
                send_btn = gr.Button("Send", variant="primary", scale=1)
                
        with gr.Column(scale=1):
            gr.Markdown("### 🎙️ Voice Interaction")
            audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Record Audio")
            transcribed_text = gr.Textbox(label="Transcribed Voice Input", interactive=False)
            audio_output = gr.Audio(label="Voice Response", autoplay=True)

    # Event Handlers
    send_btn.click(
        fn=process_text_input,
        inputs=[text_input, chatbot],
        outputs=[chatbot, text_input]
    )
    text_input.submit(
        fn=process_text_input,
        inputs=[text_input, chatbot],
        outputs=[chatbot, text_input]
    )
    audio_input.stop_recording(
        fn=process_voice_input,
        inputs=[audio_input, chatbot],
        outputs=[chatbot, audio_output, transcribed_text]
    )

if __name__ == "__main__":
    demo.launch()