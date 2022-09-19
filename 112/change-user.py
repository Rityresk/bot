import pygame
from pygame import Color
import math
import csv
from apscheduler.schedulers.background import BackgroundScheduler
from pygame import mixer
import pygame_widgets as pw
from pygame_widgets.button import Button
import pygame_widgets

def music():
    mixer.Channel(0).play(pygame.mixer.Sound('mansion.mp3'))


def music_menu():
    mixer.Channel(0).play(pygame.mixer.Sound('menu.wav'))

def music_jump():
    mixer.Channel(1).play(pygame.mixer.Sound('jump.wav'))


def new():
    global ng
    ng = True

def optin():
    global ops
    ops = True

def levd():
    global ce
    ce = True

def finish(left, top, screen, color1, color2, color3):
    pygame.draw.rect(screen, color1, (left, top, 92, 108))
    pygame.draw.polygon(screen, color1, ((left, top), (left + 46, top - 30), (left + 92, top)))
    pygame.draw.line(screen, color3, (left, top + 2), (left + 92, top + 2), 3)
    pygame.draw.line(screen, color3, (left + 5, top + 1), (left + 5, top + 107), 3)
    pygame.draw.line(screen, color3, (left + 86, top + 1), (left + 86, top + 107), 3)
    pygame.draw.line(screen, color3, (left + 46, top), (left + 46, top - 30), 4)
    pygame.draw.line(screen, color3, (left + 20, top - 12), (left + 72, top - 12), 3)
    pygame.draw.circle(screen, color2, (left + 46, top + 31), 29)
    pygame.draw.rect(screen, color2, (left + 16, top + 28, 60, 80))

def pol(cx, cy, r, rb, n, m):
    q = 360 / n
    spots = []
    for i in range(n):
        w = r * math.cos(math.radians(360 - i * q + m)) + cx
        w2 = r * math.sin(math.radians(360 - i * q + m)) + cy
        w3 = rb * math.cos(math.radians(360 - i * q - q / 2 + m)) + cx
        w4 = rb * math.sin(math.radians(360 - i * q - q / 2 + m)) + cy
        spots.append((w, w2))
        spots.append((w3, w4))
    return spots


class Portal(pygame.sprite.Sprite):
    def __init__(self, left, top):
        super().__init__(all_sprites, port)
        pygame.draw.polygon(screen, color, t)
        self.t = t
        self.rect = pygame.Rect(left, top, left + 92, top + 108)
        self.image = pygame.Surface((90, 90),
                                    pygame.SRCALPHA, 32)
        self.x, self.y = left, top
        self.add(port)


class Main(pygame.sprite.Sprite):
    def __init__(self, screen, color):
        super().__init__(all_sprites, main)
        t = pol(130, 60, 25, 45, 10, 0)
        pygame.draw.polygon(screen, color, t)
        self.t = t
        self.rect = pygame.Rect(130, 60, 55, 55)
        self.image = pygame.Surface((90, 90),
                                    pygame.SRCALPHA, 32)
        self.x, self.y = 130, 60
        self.add(main)

    def update(self, screen, color):
        for i in main:
            if i.x:
                pygame.draw.polygon(screen, color, i.t)

    def down(self, r):
        self.y += r
        self.rect.x = self.x
        self.rect.y = self.y
        self.t = pol(self.x, self.y, 25, 45, 10, 0)

    def jump(self, screen, color, r):
        self.y -= r
        self.rect.x = self.x
        self.rect.y = self.y
        self.t = pol(self.x, self.y, 25, 45, 10, 0)

    def move(self, screen, color, m):
        self.x += m
        self.t = pol(self.x, self.y, 25, 45, 10, 0)
        self.rect.x = self.x
        self.rect.y = self.y

    def move_circle(self, screen, color, x, r, cx, cy, ch):
        self.x = x
        p = (r ** 2 - (x - cx) ** 2) ** 0.5 + cy
        if ch == 4 or ch == 1:
            p = -(r ** 2 - (x - cx) ** 2) ** 0.5 + cy
        self.y = int(p)
        self.t = pol(self.x, self.y, 25, 45, 10, 0)
        self.rect.x = self.x
        self.rect.y = self.y


class Smth (pygame.sprite.Sprite):
    def __init__(self, i, screen, color):
        super().__init__(all_sprites, objects)
        if i["object"] == 'rectangle':
            self.image = pygame.Surface((int(i['width']), int(i['height'])),
                                        pygame.SRCALPHA, 32)
            k = line(int(i['left']), int(i['top']), int(i['width']), int(i["n"]), 0)
            self.k = k
            pygame.draw.polygon(screen, color, k)
            self.rect = pygame.Rect(int(i['left']) + 22, int(i['top']), int(i['width']) + 6, int(i["height"]))
            self.left, self.top = int(i['left']), int(i['top'])
            self.width, self.n, self.height = int(i['width']), int(i["n"]), int(i['height'])
            self.x, self.y = int(i['left']), int(i['top'])
            self.type = 'rectangle'
            self.add(objects)
        else:
            self.image = pygame.Surface((int(i['rb']), int(i['rb'])),
                                        pygame.SRCALPHA, 32)
            k = pol(int(i['cx']), int(i['cy']), int(i['r']), int(i['rb']), int(i['n']), 0)
            self.k = k
            self.type = 'circle'
            self.m = 0
            pygame.draw.polygon(screen, color, k)
            self.r, self.rb, self.n = int(i['r']), int(i['rb']), int(i['n'])
            self.rect = pygame.Rect(int(i['cx']) - int(i['rb']) + 45, int(i['cy']) - 20, int(i['rb']) + 40, int(i['rb']) + 75)
            self.x, self.y = int(i['cx']), int(i['cy'])
            self.add(objects)


    def update(self, screen, color):
        for i in objects:
            if i.x:
                pygame.draw.polygon(screen, color, i.k)

    def move(self, screen, color, m):
        if self.x and self.type == 'rectangle':
            k = line(self.left, self.top, self.width, self.n, m)
            self.k = k
            self.update(screen, color)
        else:
            self.m += m
            k = pol(self.x, self.y, self.r, self.rb, self.n, self.m)
            self.k = k


def line(left, top, width, n, m):
    spots = []
    p = width / n
    x = 0
    if m:
        m = m % width
    for i in range(n):
        w = (left + (i) * p + m)
        w2 = top
        w3 = (left + (i) * p + p / 2 + m)
        w4 = top - 40
        spots.append((w, w2))
        spots.append((w3, w4))
    w = left + (i + 1) * p + m
    w2 = top
    spots.append((w, w2))
    w = len(spots)
    s = 0
    t = []
    uu = []
    for h in spots:
        e, r = h[0], h[1]
        if e > width + left:
            uu.append(s)
            x += 1
            if x % 2 == 0:
                r = top
            else:
                r = top - 40
            cv = (spots[0][0] - p / 2 * x, r)
            t.append(cv)
        s += 1
    if uu:
        spots = spots[:uu[0]]
    if m:
        t.reverse()
        spots = t + spots
    w = left + width
    w2 = top
    spots.append((w, w2))
    y1 = spots[0][1]
    x1 = spots[0][0]
    y2 = spots[1][1]
    x2 = spots[1][0]
    k = (y1 - y2) / (x1 - x2)
    spots[0] = (left, top)
    y = left * k + (y1 - k * x1)
    spots.insert(1, (left, y))
    return spots


def arc(rect, start_angle, stop_angle, n, m):
    q = 360 / n
    start_angle = math.degrees(start_angle)
    stop_angle = math.degrees(stop_angle)
    spots = []
    r = rect.width / 2
    cx = rect.width / 2 + rect.left
    cy = rect.height / 2 + rect.top
    i = 0
    y = start_angle // q
    e = start_angle
    for i in range(int(y) + 1):
        w = r * math.cos(math.radians(-start_angle + 360 - i * q + m)) + cx
        w2 = r * math.sin(math.radians(-start_angle + 360 - i * q + m)) + cy
        w3 = (r + 20) * math.cos(math.radians(-start_angle + 360 - i * q - q / 2 + m)) + cx
        w4 = (r + 20) * math.sin(math.radians(-start_angle + 360 - i * q - q / 2 + m)) + cy
        spots.append((w, w2))
        spots.append((w3, w4))
    spots = spots[:-1]
    return spots


if __name__ == '__main__':
    mixer.init()
    sched = BackgroundScheduler()
    music_menu()
    sched.add_job(music_menu, 'interval', seconds=201)
    sched.start()
    intro = True
    all_sprites = pygame.sprite.Group()
    objects = pygame.sprite.Group()
    port = pygame.sprite.Group()
    main = pygame.sprite.Group()
    pygame.init()
    obj = []
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    running = False
    clock = pygame.time.Clock()
    x = 10
    t = pol(150, 150, 40, 60, 16, 0)
    r = False
    color = Color('#b59700')
    y = Color('yellow')
    f = Color('#504a24')
    tre = Color("#b8b497")
    qwer = Color("#960916")
    clock = pygame.time.Clock()
    ng = False
    ce = False
    ops = False
    b = Color('black')
    with open('Книга3.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):
            obj.append(row)
    pos = []
    for i in obj:
        if i["object"] == "portal":
            pr = Portal(int(i["left"]), int(i['top']))
            pr_cord = int(i["left"]), int(i['top'])
        else:
            smth = Smth(i, screen, color)
            pos.append(smth)
    mn = Main(screen, color)
    start = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
    jump = 0
    double_jump = False
    float = False
    u = 0
    under = 0
    mob = 0
    cir = 0
    ch = 1
    now = ""
    screen.fill("#afffb0")
    contin = Button(
        screen, 150, 160, 500, 65, text='Continue',
        fontSize=45, margin=20,
        inactiveColour=('#77bf9b'),
        hoverColour=('#77bf9b'),
        pressedColour=('#53f0a0'),
        textColour=("#005e45"),
        radius=5,
        onClick=new
    )
    options = Button(
        screen, 150, 385, 500, 65, text='Options',
        fontSize=50, margin=20,
        inactiveColour=('#77bf9b'),
        hoverColour=('#77bf9b'),
        pressedColour=('#53f0a0'),
        textColour=("#005e45"),
        radius=5,
        onClick=optin
    )
    new_game = Button(
        screen, 150, 270, 500, 65, text='New game',
        fontSize=50, margin=20,
        inactiveColour=('#77bf9b'),
        hoverColour=('#77bf9b'),
        pressedColour=('#53f0a0'),
        textColour=("#005e45"),
        radius=5,
        onClick=levd
    )
    while intro:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                intro = False
        pygame_widgets.update(events)
        pygame.display.update()
        if ce or ops or ng:
            intro = False
            running = True
    music()
    sched.remove_all_jobs()
    sched.add_job(music, 'interval', seconds=48)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if not jump and pygame.sprite.spritecollideany(mn, objects):
                        jump = 15
                        music_jump()
                        double_jump = True
                    else:
                        if jump or double_jump:
                            jump = 15
                            under = 0
                            music_jump()
                            double_jump = False
        pygame.event.pump()
        keyinput = pygame.key.get_pressed()
        if keyinput[pygame.K_SPACE]:
            start = True
        if keyinput[pygame.K_RIGHT] and (pygame.sprite.spritecollideany(mn, objects) or jump or under):
            u += 2
            if jump or under:
                mn.move(screen, color, 2)
            else:
                s = pygame.sprite.spritecollide(mn, objects, dokill=False)
                if s != []:
                    smth = s[0]
                    if smth.type == "rectangle":
                        mn.move(screen, color, 2)
                        smth.move(screen, color, u)
                    else:
                        if not mob:
                            mob = 1
                        if now == "l":
                            if mob == 1:
                                mob = -1
                            else:
                                mob = 1
                        now = "r"
                        if cir >= smth.x + smth.rb:
                            mob = -1
                        if cir <= smth.x - smth.rb:
                            mob = 1
                        cir += mob
                        if mn.y == smth.y or cir == smth.x:
                            ch += 1
                            if ch > 4:
                                ch = 1
                        mn.move_circle(screen, color, cir, smth.rb, smth.x, smth.y, ch)
                        smth.move(screen, color, 1)
        if keyinput[pygame.K_LEFT] and (pygame.sprite.spritecollideany(mn, objects) or jump or under):
            u -= 2
            if jump or under:
                mn.move(screen, color, -2)
            else:
                s = pygame.sprite.spritecollide(mn, objects, dokill=False)
                if s != []:
                    smth = s[0]
                    if smth.type == "rectangle":
                        mn.move(screen, color, -2)
                        smth.move(screen, color, u)
                    else:
                        if not mob:
                            mob = -1
                        if now == "r":
                            if mob == 1:
                                mob = -1
                            else:
                                mob = 1
                        now = "l"
                        if cir >= smth.x + smth.rb:
                            mob = -1
                        if cir <= smth.x - smth.rb:
                            mob = 1
                        cir += mob
                        if mn.y == smth.y or cir == smth.x:
                            ch -= 1
                            if ch < 1:
                                ch = 4
                        mn.move_circle(screen, color, cir, smth.rb, smth.x, smth.y, ch)
                        smth.move(screen, color, -1)
        smth.update(screen, color)
        if not jump and start and not pygame.sprite.spritecollideany(mn, objects):
            mn.down(2)
        if jump:
            mn.jump(screen, color, jump)
            jump -= 1
            if jump == 0:
                under = 80
        if under:
            under -= 1
        if not pygame.sprite.spritecollideany(mn, objects):
            cir = mn.x
            mob = 0
        finish(pr_cord[0], pr_cord[1], screen, tre, f, qwer)
        mn.update(screen, color)
        clock.tick(30)
        pygame.display.flip()
        screen.fill(Color("#f0f88f"))