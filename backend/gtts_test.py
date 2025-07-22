from gtts import gTTS
import os

text = "Hello! Welcome to Flownest AI voice bot."
tts = gTTS(text=text, lang='en', tld='co.in')  # Female Indian accent
tts.save("gtts_output.mp3")

print("✅ Audio generated as gtts_output.mp3")
