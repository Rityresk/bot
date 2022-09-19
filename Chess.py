import tkinter as tk
from tkinter import messagebox

WHITE = 1
BLACK = 2
label7 = 0
m = '1 0 2 5'

master = tk.Tk()
def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def print_board(board):
    global m
    def get(event):
        global m
        m = enter.get()
    if m != "exit":
        h = m.split()
        a = [int(i) for i in h[::1]]
        row, col, row1, col1 = a
        if board.move_piece(row, col, row1, col1):
            p = True
        else:
            p = False
        master = tk.Tk()
        label = tk.Label(master, text='     +----+----+----+----+----+----+----+----+')
        label.pack()
        for row in range(8):
            t = '  ' + str(row) + '  '
            for col in range(8):
                t += "|"
                if board.cell(row, col) != "  ":
                    t += " "
                    t += str(board.cell(row, col))
                    t += "  "
                else:
                    t += "        "
            t +='|'
            label1 = tk.Label(master, text=t)
            label1.pack()
            label2 = tk.Label(master, text='     +----+----+----+----+----+----+----+----+')
            label2.pack()
        t = '         '
        for col in range(8):
            t += str(col)
            t += '       '
        label3 = tk.Label(master, text=t)
        label3.pack()
        label4 = tk.Label(master, text='Команды:')
        label5 = tk.Label(master, text='     <row> <col> <row1> <row1>     -- ход из клетки (row, col)')
        label6 = tk.Label(master, text='                                          в клетку (row1, col1)')
        label9 = tk.Label(master, text="     exit                          -- выход из игры")
        global text
        if board.current_player_color() == WHITE:
            label7 = tk.Label(master, text='Ход белых:')
        else:
            label7 = tk.Label(master, text='Ход чёрных:')
        label8 = tk.Label(master, text="")
        if p:
            label8['text'] = "Успешный ход"
        else:
            label8['text'] = "Нельзя походить в эту клетку"
        label4.pack()
        label5.pack()
        label6.pack()
        label9.pack()
        label7.pack()
        label8.pack()
        enter = tk.Entry(master)
        enter.bind("<Return>", get)
        enter.pack()
        master.mainloop()




def main():
    board = Board()
    while True:
        global m
        print_board(board)
        if m == "exit":
            break

def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.m0 = 0
        self.m7 = 0
        self.color = WHITE
        self.field = []
        for roew in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        d = self.field[row][col]
        if isinstance(d, Pawn):
            if d.can_move(self, row, col, row1, col1) or d.can_attack(self, row, col, row1, col1):
                if char == "Q":
                    self.field[row1][col1] = Queen(self.field[row][col].color)
                elif char == "R":
                    self.field[row1][col1] = Rook(self.field[row][col].color)
                elif char == "B":
                    self.field[row1][col1] = Bishop(self.field[row][col].color)
                else:
                    self.field[row1][col1] = Knight(self.field[row][col].color)
                self.field[row][col] = None
                return True
        return False

    def cell(self, row, col):
        '''Возвращает строку из двух символов. Если в клетке (row, col)
          находится фигура, символы цвета и фигуры. Если клетка пуста,
          то два пробела.'''
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        if self.color != self.field[row][col].color:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_move(self, row, col, row1, col1):
                return False
        else:
            return False
        piece.move = True
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True

    def castling0(self):
        if self.color == WHITE:
            if self.field[0][4] is not None and isinstance(self.field[0][4], King):
                if self.field[0][2] is None and self.field[0][3] is None:
                    if self.field[0][1] is None and self.field[0][5] is None:
                        if not self.field[0][4].move:
                            if isinstance(self.field[0][0], Rook):
                                p = self.field[0][0].move
                                if not p and not self.field[0][4].move:
                                    self.field[0][2] = self.field[0][4]
                                    self.field[0][4] = None
                                    self.field[0][3] = self.field[0][0]
                                    self.field[0][0] = None
                                    self.m7 += 1
                                    self.color = opponent(self.color)
                                    return True
        else:
            if self.field[7][4] is not None and isinstance(self.field[7][4], King):
                if not self.field[7][4].move:
                    if self.field[7][2] is None and self.field[7][3] is None:
                        if self.field[7][1] is None and self.field[7][5] is None:
                            if isinstance(self.field[0][0], Rook):
                                p = self.field[7][0].move
                                if not p and not self.field[7][4].move:
                                    self.field[7][2] = self.field[7][4]
                                    self.field[7][4] = None
                                    self.field[7][3] = self.field[7][0]
                                    self.field[7][0] = None
                                    self.m7 += 1
                                    self.color = opponent(self.color)
                                    return True
        return False

    def castling7(self):
        if self.color == BLACK:
            if self.field[7][4] is not None and not self.field[7][4].move:
                if self.field[7][6] is None and self.field[7][5] is None:
                    if isinstance(self.field[7][7], Rook) and isinstance(self.field[7][4], King):
                        p = self.field[7][7].move
                        if not p and not self.field[7][4].move:
                            self.field[7][6] = self.field[7][4]
                            self.field[7][4] = None
                            self.field[7][5] = self.field[7][7]
                            self.field[7][7] = None
                            self.color = opponent(self.color)
                            return True
        else:
            if self.field[0][4] is not None and not self.field[0][4].move:
                if self.field[0][6] is None and self.field[0][5] is None:
                    if isinstance(self.field[0][7], Rook) and isinstance(self.field[0][4], King):
                        p = self.field[0][7].move
                        if not p and not self.field[0][4].move:
                            self.field[0][6] = self.field[0][4]
                            self.field[0][4] = None
                            self.field[0][5] = self.field[0][7]
                            self.field[0][7] = None
                            self.color = opponent(self.color)
                            return True
        return False


class Rook:

    def __init__(self, color):
        self.color = color
        self.move = False

    def get_color(self):
        return self.color

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(row, c) is None):
                return False

        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn:

    def __init__(self, color):
        self.color = color
        self.move = False

    def get_color(self):
        return self.color

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        if col != col1:
            return False
        if board.field[row1][col1] is not None:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if row + direction == row1:
            return True

        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        if board.field[row1][col1]:
            if self.color != board.field[row1][col1].color:
                return (row + direction == row1
                        and (col + 1 == col1 or col - 1 == col1))
            else:
                return False
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Knight:
    '''Класс коня. Пока что заглушка, которая может ходить в любую клетку.'''

    def __init__(self, color):
        self.color = color
        self.move = False

    def get_color(self):
        return self.color

    def char(self):
        return 'N'  # kNight, буква 'K' уже занята королём

    def can_move(self, board, row, col, row1, col1):
        p = []
        t = (row1, col1)
        f, z = row, col
        if f - 2 >= 0:
            a = f - 2
            if z - 1 >= 0 and (board.field[a][z - 1] is None or board.field[a][z - 1].color != self.color):
                x = (a, z - 1)
                p.append(x)
            if z + 1 <= 7and (board.field[a][z + 1] is None or board.field[a][z + 1].color != self.color):
                x = (a, z + 1)
                p.append(x)
        if z - 2 >= 0:
            a = z - 2
            if f - 1 >= 0 and (board.field[f - 1][a] is None or board.field[f - 1][a].color != self.color):
                p.append((f - 1, a))
            if f + 1 <= 7 and (board.field[f + 1][a] is None or board.field[f + 1][a].color != self.color):
                p.append((f + 1, a))
        if f + 2 <= 7:
            a = f + 2
            if z - 1 >= 0 and (board.field[a][z - 1] is None or board.field[a][z - 1].color != self.color):
                x = (a, z - 1)
                p.append(x)
            if z + 1 <= 7 and (board.field[a][z + 1] is None or board.field[a][z + 1].color != self.color):
                x = (a, z + 1)
                p.append(x)
        if z + 2 <= 7:
            a = z + 2
            if f - 1 >= 0 and (board.field[f - 1][a] is None or board.field[f - 1][a].color != self.color):
                x = (f - 1, a)
                p.append(x)
            if f + 1 <= 7 and (board.field[f + 1][a] is None or board.field[f + 1][a].color != self.color):
                x = (f + 1, a)
                p.append(x)
        if t in p:
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class King:

    def __init__(self, color):
        self.move = False
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        t = (row1, col1)
        f = board.field
        if f[row1][col1] is None or f[row1][col1].color == self.color:
            p = []
            if row > 0 and col < 7:
                p.append((row - 1, col + 1))
            if row > 0 and col > 0:
                p.append((row - 1, col - 1))
            if row < 7 and col < 7:
                p.append((row + 1, col + 1))
            if row < 7 and col > 0:
                p.append((row + 1, col - 1))
            if row > 0:
                p.append((row - 1, col))
            if row < 7:
                p.append((row + 1, col))
            if col < 7:
                p.append((row, col + 1))
            if col > 0:
                p.append((row, col - 1))
            if t in p:
                return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class Queen:

    def __init__(self, color):
        self.move = False
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'Q'

    def set_position(self, row, col):
        self.row, self.col = row, col

    def can_move(self, board, row, col, row1, col1):
        p = []
        t = (row1, col1)
        k = 1
        f = board.field
        if k:
            d, n = row, col
            while d < 7 and n < 7:
                d += 1
                n += 1
                if f[d][n] is None:
                    p.append((d, n))
                elif f[d][n].color != self.color:
                    p.append((d, n))
                    break
                else:
                    break
            d, n = row, col
            while d < 7:
                d += 1
                if f[d][n] is None:
                    p.append((d, n))
                elif f[d][n].color != self.color:
                    p.append((d, n))
                    break
                else:
                    break
            d, n = row, col
            while d > 0:
                d -= 1
                if f[d][n] is None:
                    p.append((d, n))
                elif f[d][n].color != self.color:
                    p.append((d, n))
                    break
                else:
                    break
            d, n = row, col
            while n < 7:
                n += 1
                if f[d][n] is None:
                    p.append((d, n))
                elif f[d][n].color != self.color:
                    p.append((d, n))
                    break
                else:
                    break
            d, n = row, col
            while n > 0:
                n -= 1
                if f[d][n] is None:
                    p.append((d, n))
                elif f[d][n].color != self.color:
                    p.append((d, n))
                    break
                else:
                    break
            d, n = row, col
            while d > 0 and n > 0:
                d -= 1
                n -= 1
                if f[d][n] is None:
                    p.append((d, n))
                elif f[d][n].color != self.color:
                    p.append((d, n))
                    break
                else:
                    break
            d, n = row, col
            while d < 7 and n > 0:
                d += 1
                n -= 1
                if f[d][n] is None:
                    p.append((d, n))
                elif f[d][n].color != self.color:
                    p.append((d, n))
                    break
                else:
                    break
            d, n = row, col
            while d > 0 and n < 7:
                d -= 1
                n += 1
                if f[d][n] is None:
                    p.append((d, n))
                elif f[d][n].color != self.color:
                    p.append((d, n))
                    break
                else:
                    break
            if t in p:
                return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class Bishop:
    def __init__(self, color):
        self.move = False
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        p = []
        t = (row1, col1)
        d, n = row, col
        f = board.field
        while d < 7 and n < 7:
            d += 1
            n += 1
            if f[d][n] is None:
                p.append((d, n))
            elif f[d][n].color != self.color:
                p.append((d, n))
                break
            else:
                break
        d, n = row, col
        while d > 0 and n > 0:
            d -= 1
            n -= 1
            if f[d][n] is None:
                p.append((d, n))
            elif f[d][n].color != self.color:
                p.append((d, n))
                break
            else:
                break
        d, n = row, col
        while d < 7 and n > 0:
            d += 1
            n -= 1
            if f[d][n] is None:
                p.append((d, n))
            elif f[d][n].color != self.color:
                p.append((d, n))
                break
            else:
                break
        d, n = row, col
        while d > 0 and n < 7:
            d -= 1
            n += 1
            if f[d][n] is None:
                p.append((d, n))
            elif f[d][n].color != self.color:
                p.append((d, n))
                break
            else:
                break
        if t in p:
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)

main()
master.mainloop()