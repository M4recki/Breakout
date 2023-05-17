from turtle import Turtle



font = ("Segoe UI Black", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-15, -50)
        self.hideturtle()
        self.position = "center"
        self.color("#FC4F00")
        self.write("                       Breakout game \nPlease hit 'Enter' to start, or 'q' to exit",
                   font=font, align=self.position)
        

    def game_over(self, result):
        self.color("#FC4F00")
        self.penup()
        self.goto(-130, -115)
        self.hideturtle()
        self.text = self.write(
            f"Game over. You {result}!\nPress 'Enter' to restart\nor 'q' to exit.", font=font)
