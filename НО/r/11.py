import pygame
import sys, os
from pygame import Color

pygame.init()


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mario.png')

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        wall[self] = tile_type


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


player = None


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), (550, 550))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50


wall = {}
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y

if __name__ == '__main__':
    size = width, height = 550,550
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    player, level_x, level_y = generate_level(load_level(input()))
    z = True
    while running:
        pygame.event.pump()
        if not z:
            keyinput = pygame.key.get_pressed()
            if keyinput[pygame.K_LEFT]:
                player.rect.x -= 50
                qw = pygame.sprite.spritecollideany(player, tiles_group)
                if qw:
                    if wall[qw] == 'wall':
                        player.rect.x += 50
            elif keyinput[pygame.K_RIGHT]:
                player.rect.x += 50
                qw = pygame.sprite.spritecollideany(player, tiles_group)
                if qw:
                    if wall[qw] == 'wall':
                        player.rect.x -= 50
            elif keyinput[pygame.K_UP]:
                player.rect.y -= 50
                qw = pygame.sprite.spritecollideany(player, tiles_group)
                if qw:
                    if wall[qw] == 'wall':
                        player.rect.y += 50
            elif keyinput[pygame.K_DOWN]:
                player.rect.y += 50
                qw = pygame.sprite.spritecollideany(player, tiles_group)
                if qw:
                    if wall[qw] == 'wall':
                        player.rect.y -= 50
            all_sprites.draw(screen)
            clock.tick(10)
            screen.blit(player.image, player.rect)
        else:
            start_screen()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    z = False
        pygame.display.flip()