import pygame
from pygame import Color


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.list = []
        e = self.left
        t = self.top
        self.color = {}
        for i in range(self.height):
            k = []
            for j in range(self.width):
                k.append((e, t))
                self.color[(e, t)] = 0
                e += self.cell_size
            self.list.append(k)
            e = self.left
            t += self.cell_size

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        e = self.left
        t = self.top
        self.list = []
        self.color = {}
        for i in range(self.height):
            k = []
            for j in range(self.width):
                k.append((e, t))
                self.color[(e, t)] = 0
                e += self.cell_size
            self.list.append(k)
            e = self.left
            t += self.cell_size

    def render(self, screen):
        self.screen = screen
        e = self.left
        t = self.top
        x = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.color[self.list[i][j]] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), (e, t, self.cell_size, self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (e, t, self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (e, t, self.cell_size, self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (e, t, self.cell_size, self.cell_size), 1)
                x += 1
                e += self.cell_size
            e = self.left
            t += self.cell_size

    def get_cell(self, mouse_pos):
        r = mouse_pos[0]
        s = mouse_pos[1]
        for j in self.list:
            for i in j:
                if i[0] + self.cell_size > r >= i[0] and i[1] + self.cell_size > s >= i[1]:
                    return (self.list.index(j), j.index(i))

    def on_click(self, cell_coords):
        s = cell_coords[0]
        y = cell_coords[1]
        self.color[self.list[s][y]] = 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def next_move(self):
        x = 0
        y = 0
        new = []
        op = {}
        for i in list(self.color.keys()):
            op[i] = self.color[i]
        for g in self.list:
            k = []
            for i in g:
                p = 0
                if x == 0 and y == 0 or y == self.width - 1 and x == self.height - 1:
                    k.append(0)
                    op[self.list[x][y]] = 0
                elif y == 0 and x == self.height - 1 or y == self.width and x == 0:
                    k.append(0)
                    op[self.list[x][y]] = 0
                else:
                    p = 0
                    if x != 0:
                        if self.color[self.list[x - 1][y]] == 1:
                            p += 1
                        if y != 0:
                            if self.color[self.list[x - 1][y - 1]] == 1:
                                p += 1
                        else:
                            if self.color[self.list[x - 1][len(self.list[0]) - 1]] == 1:
                                p += 1
                        if y < self.width - 1:
                            if self.color[self.list[x - 1][y + 1]] == 1:
                                p += 1
                        else:
                            if self.color[self.list[x - 1][0]] == 1:
                                p += 1
                    else:
                        if self.color[self.list[len(self.list) - 1][y]] == 1:
                            p += 1
                        if y != 0:
                            if self.color[self.list[len(self.list) - 1][y - 1]] == 1:
                                p += 1
                        else:
                            if self.color[self.list[len(self.list) - 1][len(self.list[0])]] == 1:
                                p += 1
                        if y < self.width - 1:
                            if self.color[self.list[len(self.list) - 1][y + 1]] == 1:
                                p += 1
                        else:
                            if self.color[self.list[len(self.list) - 1][0]] == 1:
                                p += 1
                    if y != 0:
                        if x < self.height - 1:
                            if self.color[self.list[x + 1][y - 1]] == 1:
                                p += 1
                        else:
                            if self.color[self.list[0][y - 1]] == 1:
                                p += 1
                        if self.color[self.list[x][y - 1]] == 1:
                            p += 1
                    else:
                        if x < self.height - 1:
                            if self.color[self.list[x + 1][len(self.list[0]) - 1]] == 1:
                                p += 1
                        else:
                            if self.color[self.list[len(self.list) - 1][len(self.list[0]) - 1]] == 1:
                                p += 1
                        if self.color[self.list[x][len(self.list[0]) - 1]] == 1:
                            p += 1
                    if x < self.height - 1:
                        if self.color[self.list[x + 1][y]] == 1:
                            p += 1
                    else:
                        if self.color[self.list[0][y]] == 1:
                            p += 1
                    if y < self.width - 1:
                        if x != 0:
                            if self.color[self.list[x][y + 1]] == 1:
                                p += 1
                        else:
                            if self.color[self.list[len(self.list) - 1][y + 1]] == 1:
                                p += 1
                        if x < self.height - 1:
                            if self.color[self.list[x + 1][y + 1]] == 1:
                                p += 1
                        else:
                            if self.color[self.list[0][y + 1]] == 1:
                                p += 1
                    else:
                        if x != 0:
                            if self.color[self.list[x][0]] == 1:
                                p += 1
                        else:
                            if self.color[self.list[len(self.list) - 1][0]] == 1:
                                p += 1
                        if x < self.height - 1:
                            if self.color[self.list[x + 1][0]] == 1:
                                p += 1
                        else:
                            if self.color[self.list[0][0]] == 1:
                                p += 1
                    if p < 2 or p > 3:
                        op[self.list[x][y]] = 0
                    else:
                        if self.color[self.list[x][y]] == 0 and p == 3:
                            op[self.list[x][y]] = 1
                        elif self.color[self.list[x][y]] == 1:
                            op[self.list[x][y]] = 1
                        else:
                            op[self.list[x][y]] = 0
                y += 1
            y = 0
            x += 1
        self.color = op


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    board = Board(30, 20)
    board.set_view(50, 50, 20)
    running = True
    x = 1
    next = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.next_move()
                    if next:
                        next = False
                    else:
                        next = True
        screen.fill((0, 0, 0))
        board.render(screen)
        if next:
            board.next_move()
            clock.tick(10)
        pygame.display.flip()