from tkinter import Tk, Canvas, Frame, BOTH, W, Button
from tkinter.ttk import Frame, Button, Style


class Example(Frame):

    def __init__(self):
        self.n = 1
        super().__init__()
        self.initUI()

    def initUI(self):
        x = '20'
        l1 = 50
        l2 = 210
        #8px = 1cm
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.dr(self.canvas, l1, l2, x)
        btn = Button(self, text="Следущая линейка", command=self.a)
        btn.place(x=20, y=300)
        self.canvas.pack(fill=BOTH, expand=1)

    def a(self):
        z = {1: ["20", 50, 210],
             2: ["15", 50, 170],
             3: ["10", 50, 130],
             4: ["5", 60, 100]
             }
        self.n += 1
        if self.n > 4:
            self.n = 1
        r = z[self.n]
        self.canvas.delete('all')
        self.dr(self.canvas, r[1], r[2], r[0])


    def dr(self, canvas, l1, l2, x):
        canvas.create_rectangle(
            270, 80, 360, 230,
            outline="#05f", fill="#05f"
        )

        canvas.create_rectangle(
            300, l1, 330, l2,
            outline="#E0C95C", fill="#E0C95C"
        )

        canvas.create_rectangle(
            270, 30, 360, 230
        )

        canvas.create_text(
            20, 60, anchor=W, font="TimesNewRoman",
            text=f"Длина линейки: {x} см"
        )





def main():
    root = Tk()
    ex = Example()
    root.geometry("400x400+200+200")
    root.mainloop()


if __name__ == '__main__':
    main()