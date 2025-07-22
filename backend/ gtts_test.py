from gtts import gTTS
import subprocess

text = "Welcome to Flownest AI voice bot. How can I help you today?"

# Use Indian accent
tts = gTTS(text=text, lang='en', tld='co.in')

# Save audio
tts.save("gtts_output.mp3")
print("✅ Audio generated as gtts_output.mp3")

# Use subprocess instead of os.system (more reliable)
try:
    subprocess.run(["afplay", "gtts_output.mp3"], check=True)
    print("🔊 Playing audio now...")
except Exception as e:
    print("❌ Failed to play audio:", e)
