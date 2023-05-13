from turtle import Turtle

pos = 'center'
font = ('Segoe UI Black', 70, 'normal')

class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.color('red')
        self.shape('circle')
        self.penup()
        self.hideturtle()
        self.show_lives()
        
    def show_lives(self):
        x_pos = -300
        y_pos = 320
        for i in range(self.lives):
            self.goto(x_pos, y_pos)
            self.stamp()
            x_pos += 40
            
    def lose_live(self):
        self.clear()
        self.lives -= 1
        self.show_lives()