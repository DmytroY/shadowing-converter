import whisper
import time
#import ffmpeg
from pydub import AudioSegment

start = time.time()
INPUT_FILE = "original_audio.mp3"
OUTPUT_FILE = "audio_with_pauses.mp3"


model = whisper.load_model("tiny")  # or "tiny", "base", "small", "medium", "large", "turbo"
# result = model.transcribe(AUDIO_FILE, verbose=False, language="cs")
result = model.transcribe(INPUT_FILE, verbose=False)

# Create 3000ms silence
silence = AudioSegment.silent(duration=3000)

# Load full audio with pydub
audio = AudioSegment.from_mp3(INPUT_FILE)
output = AudioSegment.empty()

for i, segment in enumerate(result['segments']):
    start_ms = int(segment['start'] * 1000)
    end_ms = int(segment['end'] * 1000)
    sentence_audio = audio[start_ms:end_ms]
    output += sentence_audio + silence
    print(f"Processed segment {i+1}/{len(result['segments'])}")

output.export(OUTPUT_FILE, format="mp3")
print(f"Done! Output file: {OUTPUT_FILE}")

# -------------------
end = time.time()
print(f"elapsed time: {(end - start):.2f} sec.")