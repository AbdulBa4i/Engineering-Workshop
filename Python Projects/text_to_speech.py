from gtts import gTTS
import os

text = "hello hi  "
tts=gTTS(text=text,lang="en")
tts.save("speech.wav")