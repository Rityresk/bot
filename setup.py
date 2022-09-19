from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from random import choice
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
import os
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import pygame as pg
import eyed3
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.config import Config
from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
pg.init()


class MainApp(App):
    def build(self):
        Window.size = (340, 700)
        save = open('C:\\Users\\дом\\PycharmProjects\\pythonProject1\\rimu.txt', 'a')
        self.sm = ScreenManager()
        s = Screen(name='main')
        self.files = self.get_all_files()
        self.reverse = self.get_reverse()
        r = BoxLayout(orientation='vertical')
        label = Button(text="999", on_press=lambda x: x)
        label.size_hint_y = 90
        label.size_hint_x = 50
        r.add_widget(label)
        main_layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        main_layout.bind(minimum_height=main_layout.setter('height'))
        k = list(self.files.keys())
        self.list = k
        self.rev_list = list(self.files.values())
        p = 160 * (len(k) - 1) + 15
        sx = [30, p]
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        for i in range(len(k)):
            y = k[i]
            self.path = y
            x = self.files[y]
            btn = Button(text=x, on_press=self.btn_pressed, size_hint=(None, None))
            p = Window.width
            btn.size = (p, 150)
            main_layout.add_widget(btn)
            with btn.canvas:
                im = Image(source='C:\\Users\\дом\\Downloads\\react.png', size=(120, 120), pos=sx,
                           keep_ratio=False)
                sx[1] = sx[1] - 160
                sx = [sx[0], sx[1]]
        root.add_widget(main_layout)
        r.add_widget(root)
        self.loop_mode = True
        self.play_smth_now = False
        self.previous = None
        self.sound = False
        s.add_widget(r)
        self.sm.add_widget(s)
        self.sm.current = 'main'
        return self.sm

    def btn_pressed(self, instance):
        text = instance.text
        if self.play_smth_now is False or self.play_smth_now != text:
            self.play_smth_now = text
            path = self.reverse[text]
            self.sound = SoundLoader.load(path)
            self.sound.play()
            self.sound.seek(40)
            self.change_screen()
            y = pg.mixer.Sound(path).get_length() - 40
            self.event = Clock.schedule_once(self.queue, y)
        else:
            self.sound.pause()
            self.event.cancel()
            self.change_screen()
            self.previous = self.play_smth_now
            self.play_smth_now = False
        return True

    def get_all_files(self):
        c = []
        a = {}
        for m, r, x in os.walk("C:\\Users"):
            for i in x[::1]:
                t = m
                if i.endswith("mp3"):
                    t += "\\"
                    t += i
                    track = eyed3.load(t)
                    if track:
                        tg = track.tag
                        if tg:
                            title = tg.title
                        p = i[:-3]
                        if t not in list(a.values()) and title:
                            a[t] = title
                        else:
                            a[t] = p
        with open("C:\\Users\\дом\\PycharmProjects\\pythonProject1\\rimu.txt", "r") as f:
            text = f.read()
            c.append(text)
        if c != [""]:
            t = c[0].split("\n")
            for i in t[::1]:
                if len(i) >= 2:
                    i = i.split("+!")
                    a[i[1]] = i[0]
        return a

    def get_reverse(self):
        c = []
        a = {}
        for m, r, x in os.walk("C:\\Users"):
            for i in x[::1]:
                t = m
                if i.endswith("mp3"):
                    t += "\\"
                    t += i
                    if i:
                        track = eyed3.load(t)
                        if track:
                            tg = track.tag
                            if tg:
                                title = tg.title
                        p = i[:-3]
                        if t not in list(a.values()) and title:
                            a[title] = t
                        else:
                            a[p] = t
        with open("C:\\Users\\дом\\PycharmProjects\\pythonProject1\\rimu.txt", "r") as f:
            text = f.read()
            c.append(text)
        if c != [""]:
            t = c[0].split("\n")
            for i in t[::1]:
                if len(i) >= 2:
                    i = i.split("+!")
                    a[i[0]] = i[1]
        return a

    def change_name(self, title, path):
        with open("C:\\Users\\дом\\PycharmProjects\\pythonProject1\\rimu.txt", "a") as f:
            f.write(f"{title}+!{path}\n")
        self.files[path] = title
        self.reverse[title] = path

    def change_screen(self):
        print(Window.size)
        screen = Screen(name=f"button{self.rev_list.index(self.play_smth_now)}")
        self.button_layout = FloatLayout(size=(Window.width, Window.height))
        print(self.play_smth_now)
        label = Label(text=self.play_smth_now, size_hint=(None, None))
        label.size = ((Window.width - 260) // 3.176, 100)
        label.pos = [220 // 3.176, Window.height - 100]
        self.button_layout.add_widget(label)
        p = ((Window.width - 800) // 2 // 3.176, 10)
        with self.button_layout.canvas:
            im = Image(source='C:\\Users\\дом\\Downloads\\react.png', size=(800 // 3.176, 800), pos=(5, 150),
                       keep_ratio=False)
            Rectangle(pos=(200, 800), size=(680, 20))
        btn = Button(text="return", on_press=self.return_main_screen, size_hint=(None, None))
        btn.size = (200 // 3.176, 200)
        btn.pos = [0, Window.height - 200]
        self.button_layout.add_widget(btn)
        self.button_layout.add_widget(im)
        btn1 = Button(text=" ", background_normal="C:\\Users\\дом\\Downloads\\Wrench__1_-removebg-preview (3).png",
                      on_press=self.a, size_hint=(None, None))
        btn1.size = (156 // 3.176, 117)
        btn1.pos = (271 // 3.176, 500)
        self.button_layout.add_widget(btn1)
        btn2 = Button(text=" ", background_normal="C:\\Users\\дом\\Downloads\\Wrench__1_-removebg-preview (2).png",
                      on_press=self.a, size_hint=(None, None))
        btn2.size = (125, 125)
        btn2.pos = (477, 500)
        self.button_layout.add_widget(btn2)
        btn3 = Button(text=" ", background_normal="C:\\Users\\дом\\Downloads\\Wrench__1_-removebg-preview (4).png",
                      on_press=self.a, size_hint=(None, None))
        btn3.size = (156, 117)
        btn3.pos = (652, 500)
        self.button_layout.add_widget(btn3)
        #self.button_layout.add_widget(im)
        screen.add_widget(self.button_layout)
        self.sm.add_widget(screen)
        self.sm.current = f"button{self.rev_list.index(self.play_smth_now)}"

    def return_main_screen(self, isintance):
        self.sm.current = "main"

    def queue(self, z):
        if not self.previous:
            x = self.rev_list.index(self.play_smth_now)
        else:
            x = self.rev_list.index(self.previous)
        r = self.list[x + 1]
        self.play_smth_now = self.files[r]
        self_previous = self.play_smth_now
        self.sound.load(r)
        self.change_screen()
        self.sound.play()
        self.sound.set_pos(30)
        y = pg.mixer.Sound(r).get_length() - 30
        self.event = Clock.schedule_once(self.queue, y)

    def a(self, instance):
        pass


if __name__ == '__main__':
    MainApp().run()

ffmpeg -y -i "C:\\Users\\дом\\Music\\005. Ruins.mp3" -strict -2 -acodec vorbis -ac 2 -aq 50 "C:\\Users\\дом\\Music\\005. Ruins.ogg"

ogmmerge -c "artist=Someone" -c "title=Title" -o "C:\\Users\\дом\\Music\\005. Ruins.ogg" "C:\\Users\\дом\\Music\\005. Ruins.mp3"