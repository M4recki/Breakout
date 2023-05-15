from turtle import Turtle
from random import choice

class Rectangles(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.colors = ["purple", "orange", "yellow", "green", "blue"]
        self.rectangles_list = []
        self.position_x = -270
        self.position_y = 260
        self.create_rectangles()

    def create_rectangles(self):
        for i in range(5):
            for j in range(5):
                t = Turtle("square")
                t.penup()
                t.goto(self.position_x, self.position_y)
                t.shapesize(stretch_wid=1, stretch_len=6)
                t.color(self.colors[i])
                t.stamp()
                self.rectangles_list.append(t)
                self.position_x += 135
            self.position_x = -270
            self.position_y -= 35


