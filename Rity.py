import telebot
from youtubesearchpython import VideosSearch
from pytube import YouTube
import os
import requests

def search(r):
    videosSearch = VideosSearch(r, limit=2)

    a = videosSearch.result()
    t = a['result'][0]['link']
    video = YouTube(t)
    audio = video.streams.filter(only_audio=True).first()
    out_file = audio.download(output_path=".")
    os.remove("base.mp3")
    base, ext = os.path.splitext(out_file)
    new_file = "base" + '.mp3'
    os.rename(out_file, new_file)


rity = telebot.TeleBot("1694460219:AAEpMaPDnASHOc7ZOddtNmqSEopO0gHR5VE")
@rity.message_handler(commands=["greeting", 'bye'])
@rity.message_handler(content_types=['text'])
def greet(message):
    s = message.text
    a = message.from_user.id
    idf = message.chat.id
    if "/" in str(s):
        r = s[1:]
        search(r)
        rity.send_audio(chat_id=idf, audio=open("base.mp3", 'rb'))
rity.polling(none_stop=True)
