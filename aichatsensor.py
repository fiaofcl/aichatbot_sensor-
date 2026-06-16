from groq import Groq
from langchain_groq import ChatGroq
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
client = Groq(
    api_key="YOUR API KEY"
)
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key="YOUR API KEY"
)
fs = 16000
SILENCE_THRESHOLD = 500
SILENCE_LIMIT = 30
chunk_duration = 30
chunk_size = int(fs * chunk_duration / 1000)
def is_speech(audio_chunk):
    
    energy = np.abs(audio_chunk).mean()
    return energy > SILENCE_THRESHOLD

while True:
    input("Press Enter and start recording: ")
    print("Listening")
    frames = []
    silence = 0

    with sd.InputStream(
        samplerate=fs,
        channels=1,
        dtype="int16"
    ) as stream:
        while True:
            audio_chunk, overflowed = stream.read(chunk_size)
            frames.append(audio_chunk)

            if is_speech(audio_chunk):
                silence = 0
            else:
                silence += 1

            if silence > SILENCE_LIMIT:
                break

    audio = np.concatenate(frames, axis=0)
    write("recording.wav", fs, audio)

    with open("recording.wav", "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=audio_file
        )

    text = transcription.text
    print("You:", text)

    p = llm.invoke(text)
    print("Bot:", p.content)

    q = input("Press Y to exit and N to continue: ")
    if q.lower() in ["y", "yes"]:
        break