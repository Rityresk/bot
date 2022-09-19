from os import path
from pydub import AudioSegment

# files
AudioSegment.converter = 'C:\\Users\\дом\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\ffmpeg'
src = "C:\\Users\\Public\\015. sans..mp3"
dst = "C:\\Users\\дом\\Music\\005. Ruins.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")