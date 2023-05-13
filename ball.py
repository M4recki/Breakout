from turtle import Turtle
from time import sleep


class Ball(Turtle):
    def __init__(self, x_pos, y_pos=-290):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_ball_y_pos(self):
        self.y_move *= -1
        
    def bounce_ball_x_pos(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        
        
    def reset_ball(self, x_pos):
        self.goto(x_pos, -290)
        self.move_speed = 0.1
        sleep(1)
        self.bounce_ball_x_pos()
        self.bounce_ball_y_pos()