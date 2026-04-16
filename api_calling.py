from google import genai
from dotenv import load_dotenv
import os, io
from gtts import gTTS

# Loading the environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# initializing a client
client = genai.Client(api_key=api_key)


# Note generator
def note_generator(images):
    prompt = """Summarize the picture in note format at max 100 words in language modern Bangla with English used in it to sound more natural
    Make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images, prompt]
    )

    return response.text

# Audio Transcription
def audio_transcription(text):
    speech = gTTS(text, lang="bn", slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer