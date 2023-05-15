from turtle import Turtle

font = ("Segoe UI Black", 24, "normal")

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
        self.color("red")
        self.penup()
        self.goto(-320, 300)
        self.hideturtle()
        self.write("Lives: ", font=font)
        x_pos = -200
        y_pos = 320
        for i in range(self.lives):
            self.goto(x_pos, y_pos)
            self.stamp()
            x_pos += 40
            
    def lose_live(self):
        self.clear()
        self.lives -= 1
        self.show_lives()