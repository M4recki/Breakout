from turtle import Screen
from paddle import Paddle
from rectangles import Rectangles
from ball import Ball
from lives import Lives
from scoreboard import Scoreboard
from time import sleep
import sys

s = Screen()
s.setup(width=700, height=700)
s.bgcolor('black')
s.title('Breakout game by Marek Baranski')
s.tracer(0)


paddle = Paddle(XPOS=0, YPOS=-300)

s.listen()
s.onkey(paddle.go_right, 'd')
s.onkey(paddle.go_left, 'a')

ball = Ball(x_pos=paddle.xcor())

rectangles = Rectangles()

scoreboard = Scoreboard()

lives = Lives()

continue_game = True


def game():
    global continue_game
    while continue_game:
        sleep(ball.move_speed)
        s.update()
        ball.move_ball()
        scoreboard.clear()
        scoreboard.hideturtle()

        # Check for collision with rectangles
        for rectangle in rectangles.rectangles_list:
            if ball.distance(rectangle) < 41:
                rectangle.clear()
                rectangle.hideturtle()
                rectangles.rectangles_list.remove(rectangle)
                if abs(ball.xcor() - rectangle.xcor()) > 30:
                    ball.bounce_ball_x_pos()
                else:
                    ball.bounce_ball_y_pos()

        # Check collision with walls
        if ball.xcor() > 320 or ball.xcor() < -320:
            ball.bounce_ball_x_pos()

        if ball.ycor() > 320:
            ball.bounce_ball_y_pos()

        if ball.distance(paddle) < 90 and abs(ball.ycor() - paddle.ycor()) < 50 - paddle.shapesize()[1]*10/2:
            ball.bounce_ball_y_pos()

        if ball.ycor() < -380:
            ball.reset_ball(x_pos=paddle.xcor())
            lives.lose_live()

        if len(rectangles.rectangles_list) == 0:
            scoreboard.game_over(result="won")
            continue_game = False

            if s.onkeypress(game, "Return"):
                game()
            elif s.onkeypress(sys.exit, "q"):
                sys.exit()

        if lives.lives == 0:
            scoreboard.game_over(result="lost")
            continue_game = False

            if s.onkeypress(game, "Return"):
                game()
            elif s.onkeypress(sys.exit, "q"):
                sys.exit()


if s.onkeypress(game, "Return"):
    game()
elif s.onkeypress(sys.exit, "q"):
    sys.exit()


s.mainloop()