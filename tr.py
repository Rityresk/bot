import math
import tkinter


class Scales:
    def __init__(self, context: tkinter.Canvas, scale: int = 1):
        self.ctx = context
        self.x = 0
        self.y = 0
        self.width = 400
        self.height = 400

        self.__angle = 0
        self.__value = 0.0
        self.__lWeight = 0
        self.__rWeight = 0

    def setLeft(self, value):
        self.__lWeight = max(self.__lWeight + value, 0)
        self.setScaleState()

    def setRight(self, value):
        self.__rWeight = max(self.__rWeight + value, 0)
        self.setScaleState()

    def setScaleState(self):
        if self.__lWeight != 0 and self.__rWeight == 0:
            self.__value = -1
        elif self.__lWeight == 0 and self.__rWeight != 0:
            self.__value = 1
        elif self.__lWeight == self.__rWeight == 0:
            self.__value = 0
        else:
            minW = min(self.__lWeight, self.__rWeight)
            maxW = max(self.__lWeight, self.__rWeight)

            self.__value = 1 - minW / maxW

            if self.__lWeight > self.__rWeight:
                self.__value *= -1

        self.__angle = self.__value * 15

    def pivot(self):
        # pivot: 200 15
        return self.__atSource([[200, 15]], addY=80)[0]

    def lCupPivot(self):
        # 75, 25
        point = self.__atSource([[75, 25]], addY=80)
        return self.__atPivot(point, self.pivot(), self.__angle)[0]

    def rCupPivot(self):
        # 325, 25
        point = self.__atSource([[325, 25]], addY=80)
        return self.__atPivot(point, self.pivot(), self.__angle)[0]

    def cupFramePivot(self, cupPivot):
        # 5, 260
        cupPivot[0] -= 70
        cupPivot[1] += 235
        return cupPivot

    def draw(self):
        self.__base()
        self.__arm()
        self.__cup(self.lCupPivot())
        self.__cup(self.rCupPivot())
        self.__display()

        self.__debug()

    def __base(self):
        points = self.__atSource([
            [198, 20],
            [190, 300],
            [150, 300],
            [150, 315],

            [250, 315],
            [250, 300],
            [210, 300],
            [202, 20]
        ], addY=80)

        self.ctx.create_polygon(
            points,
            fill="white",
            outline="grey"
        )

    def __arm(self):
        points = self.__atSource([
            [70, 25],
            [80, 25],
            [95, 15],
            [195, 15],
            [200, 40],
            [205, 15],
            [305, 15],
            [320, 25],
            [330, 25],

            [330, 20],
            [320, 15],
            [305, 5],
            [95, 5],
            [80, 15],
            [70, 20],
            [70, 25],
        ], addY=80)

        points = self.__atPivot(
            points,
            self.pivot(),
            self.__angle)

        self.ctx.create_polygon(
            points,
            fill="white",
            outline="grey"
        )

    def __cup(self, cupPivot=[0, 0]):
        # 75, 25
        x0, y0 = cupPivot

        # oval1 = self.__atSource([[5, 250], [145, 270]], addY=80)
        # line1 = self.__atSource([[5, 260], [5, 100]], addY=80)
        # arc = self.__atSource([[5, 30], [145, 170]], addY=80)
        # line2 = self.__atSource([[145, 100], [145, 260]], addY=80)
        # line3 = self.__atSource([[75, 20], [75, 35]], addY=80)

        oval1 = [[x0 - 70, y0 + 225], [x0 + 70, y0 + 245]]
        line1 = [[x0 - 70, y0 + 235], [x0 - 70, y0 + 75]]
        arc = [[x0 - 70, y0 + 5], [x0 + 70, y0 + 145]]
        line2 = [[x0 + 70, y0 + 75], [x0 + 70, y0 + 235]]
        line3 = [[x0, y0 - 1], [x0, y0 + 10]]

        self.ctx.create_oval(
            oval1,
            fill="white",
            outline="grey")
        self.ctx.create_line(line1, fill="grey")
        self.ctx.create_arc(
            arc,
            start=0, extent=180,
            style=tkinter.ARC,
            outline="grey",
            fill="grey"
        )
        self.ctx.create_line(line2, fill="grey")

        self.ctx.create_line(line3, fill="grey")

    def __display(self):
        frame = self.__atSource([[165, 200], [235, 240]])
        text = self.__atSource([[200, 220]])[0]

        self.ctx.create_rectangle(frame, outline="grey", fill="white")
        self.ctx.create_text(
            text,
            justify=tkinter.CENTER,
            font="Courier 22",
            text="%.1f" % self.__value,
            fill="grey"
        )

    def __debug(self):
        frame = self.__atSource([[3, 3], [self.width - 3, self.height - 3]])

        self.ctx.create_rectangle(frame, outline="red", fill=None)

        self.__redPoint(self.lCupPivot())
        self.__redPoint(self.rCupPivot())
        self.__redPoint(self.pivot())

        self.__redPoint(self.cupFramePivot(self.lCupPivot()))
        self.__redPoint(self.cupFramePivot(self.rCupPivot()))

        lcfp = self.cupFramePivot(self.lCupPivot())
        rcfp = self.cupFramePivot(self.rCupPivot())

        lCupFrame = [
            lcfp,
            [lcfp[0] + 140, lcfp[1] - 140]
        ]
        rCupFrame = [
            rcfp,
            [rcfp[0] + 140, rcfp[1] - 140]
        ]

        self.ctx.create_rectangle(lCupFrame, outline="lime", fill=None)
        self.ctx.create_rectangle(rCupFrame, outline="lime", fill=None)

    def __redPoint(self, point):
        self.ctx.create_oval(
            point[0] - 1, point[1] - 1, point[0] + 1, point[1] + 1,
            outline="red", fill="red")

    def __atSource(self, points, addX=0, addY=0):
        for i in range(len(points)):
            points[i][0] += self.x + addX
            points[i][1] += self.y + addY

        return points

    def __atPivot(self, points, pivot=[0, 0], angle=0):
        angle = angle * math.pi / 180

        for i in range(len(points)):
            dX = points[i][0] - pivot[0]
            dY = points[i][1] - pivot[1]
            shiftX = dX * math.cos(angle) - dY * math.sin(angle)
            shiftY = dX * math.sin(angle) + dY * math.cos(angle)

            points[i][0] = pivot[0] + shiftX
            points[i][1] = pivot[1] + shiftY

        return points