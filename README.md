# shadowing-converter
It is coverter which add pauses after every sentence in audio file, so you can practice shadowing foreing language with comfort.

I recomend to use virtual evironment:

`python -m venv venv`

`venv\Scripts\Activate.ps1`

install ffmpeg:
* ror Windows: https://ffmpeg.org/download.html
* for macOS: brew install ffmpeg
* for Linux: sudo apt install ffmpeg

Install requirements: `pip install -r requirements.txt`

Script *transcribe.py* contains names for input and output file, change it accordingly.:
```
INPUT_FILE = "original_audio.mp3"
OUTPUT_FILE = "audio_with_pauses.mp3"
``` 

Also in next fragment of *transcribe.py* you can specify bigger but more presice variant of Whisper model:
```
model = whisper.load_model("tiny")  # or "tiny", "base", "small", "medium", "large", "turbo"
```

run converter `python transcribe.py` - 
it will download Whisper newronetwork model, split audio by segments and insert pauses between segments. Be avare - it is time consuming process. Try it with small audio first.