
# AI Audio Chatbot with Voice Activity Detection

A simple Python-based AI voice chatbot that records audio from the microphone, detects speech using energy-based voice activity detection, converts speech to text using Groq's Whisper API, and generates responses using the GPT-OSS-120B language model.

## Features

- Records audio directly from the microphone
- Energy-based voice activity detection to automatically stop recording on silence
- Converts speech to text using Whisper Large V3
- Generates AI responses using GPT-OSS-120B
- Simple command-line interface
- No external VAD dependencies required

## Technologies Used

- Python
- Groq API
- Whisper Large V3
- GPT-OSS-120B
- LangChain Groq
- SoundDevice
- SciPy
- NumPy

## Installation

Install the required dependencies:

```bash
pip install groq langchain-groq sounddevice scipy numpy
```

Or, if you are using the included `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

1. Add your Groq API key in the `aichatbot.py` file.
2. Run the script:

   ```bash
   python3 aichatbot.py
   ```

3. Press **Enter** to start recording.
4. Speak your question into the microphone.
5. Recording stops automatically when silence is detected.
6. The chatbot transcribes your speech and generates an AI response.
7. Enter `Y` when prompted if you want to exit the application.

## How Voice Detection Works

The chatbot uses a simple energy-based voice activity detection method instead of external VAD libraries. It continuously measures the average volume of incoming audio chunks and compares the value against a predefined threshold. When the audio energy remains below the threshold for a sufficient amount of time, the recording automatically stops.

### Configuration

| Parameter | Description |
|-----------|-------------|
| `fs = 16000` | Audio sample rate (Hz) |
| `SILENCE_THRESHOLD = 500` | Minimum energy level considered as speech |
| `SILENCE_LIMIT = 30` | Number of consecutive silent chunks before stopping |
| `chunk_duration = 30` | Length of each recorded audio chunk (milliseconds) |

## Project Structure

```text
ai-chatbot/
├── aichatbot.py
├── requirements.txt
└── README.md
```

## Future Improvements

- Real-time microphone streaming
- Text-to-speech for spoken responses
- Conversation history and memory
- Graphical user interface using Streamlit or Flask
- API key management using environment variables

## License

This project is intended for learning and educational purposes.

## About

This project is a beginner-friendly AI-powered voice chatbot built with Python, Groq Whisper, and the GPT-OSS-120B language model. It uses energy-based voice activity detection to automatically determine when the user has finished speaking, eliminating the need for a fixed recording duration. The application records audio from the microphone, transcribes speech into text, and generates AI responses through a simple command-line interface. It serves as an introductory project for exploring speech recognition, audio processing, and large language model applications.