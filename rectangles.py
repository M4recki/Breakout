from turtle import Turtle


class Rectangles(Turtle):
    def __init__(self):
        super().__init__()
        self.x_start = -270
        self.y_start = 260
        self.speed(0)
        self.colors = ["purple", "orange", "yellow", "green", "blue"]
        self.rectangles_list = []
        self.create_rectangles()

    def create_rectangles(self):
        for i in range(5):
            for j in range(5):
                t = Turtle("square")
                t.penup()
                t.goto(self.x_start, self.y_start)
                t.shapesize(stretch_wid=1, stretch_len=6)
                t.color(self.colors[i])
                t.stamp()
                self.rectangles_list.append(t)
                self.x_start += 135
            self.x_start = -270
            self.y_start -= 35
