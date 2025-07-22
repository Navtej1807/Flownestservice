from TTS.api import TTS

# Load the model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False, gpu=False)

# Your text
text = "Hello, how can I help you today?"

# Language
language = "en"

# Test top 5 speakers
for speaker in tts.speakers[:5]:
    print(f"🎤 Trying speaker: {speaker}")
    tts.tts_to_file(
        text=text,
        speaker=speaker,
        language=language,
        file_path=f"output_{speaker}.wav"
    )
