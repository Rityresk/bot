from youtubesearchpython import VideosSearch
from pytube import YouTube
import os

videosSearch = VideosSearch('stollen dance', limit = 2)

a = videosSearch.result()
t = a['result'][0]['link']
print(t)
video = YouTube(t)
audio = video.streams.filter(only_audio=True).first()
out_file = audio.download(output_path=".")

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)