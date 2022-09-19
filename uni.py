import os
from tkinter import S, CENTER, Canvas, PhotoImage


class Weight:
    def __init__(self, context=Canvas, value=5):
        self.ctx = context
        self.x = 50
        self.y = 150

        __dir = os.path.dirname(os.path.realpath(__file__))
        __imagePath = os.path.join(__dir, "static/weight.png")

        self.__image = PhotoImage(file=__imagePath).subsample(10, 10)

        self.width = self.__image.width()
        self.height = self.__image.height()

    def draw(self):
        self.ctx.create_image(
            self.x, self.y,
            anchor=S, image=self.__image,
            tags=("is_move", "weight")
        )