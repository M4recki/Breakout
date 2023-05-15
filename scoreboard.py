from turtle import Turtle

font = ("Segoe UI Black", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("purple")
        self.penup()
        self.goto(-100, 0)
        self.hideturtle()
        self.position = "center"
        self.write("Breakout game \nPlease hit 'Enter' to start.",
                   font=font, align=self.position)

    def game_over(self, result):
        self.color("purple")
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write(
            f"Game over. \n You {result}! \n Press 'Enter' to restart.", font=font)

    def start_game(self):
        self.hideturtle()
        self.clear()
