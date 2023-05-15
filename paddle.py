from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, XPOS, YPOS):
        super().__init__()
        self.shape("square")
        self.color("grey")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(XPOS, YPOS)

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 350:
            self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -350:
            self.goto(new_x, self.ycor())