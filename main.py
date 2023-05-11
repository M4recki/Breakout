from turtle import Screen
from paddle import Paddle
from rectangles import Rectangles
from ball import Ball
from lives import Lives
from time import sleep

s = Screen()
s.setup(width=700., height=700)
s.bgcolor('black')
s.title('Breakout game by Marek Baranski')
s.tracer(0)

paddle = Paddle(XPOS=0, YPOS=-300)

s.listen()
s.onkey(paddle.go_right, 'd')
s.onkey(paddle.go_left, 'a')

rectangles = Rectangles()
rectangles.create_rectangles(5, 10, 6)

ball = Ball(x_pos=paddle.xcor())

lives = Lives()

continue_game = True

while continue_game:
    sleep(ball.move_speed)
    s.update()
    ball.move_ball()

    if ball.xcor() > 320 or ball.xcor() < -320:
        ball.bounce_ball_x_pos()

    if ball.ycor() > 320:
        ball.bounce_ball_y_pos()

    if ball.distance(paddle) < 40 and abs(ball.ycor() - paddle.ycor()) < 20:
        ball.bounce_ball_y_pos()

    if ball.ycor() < -380:
        ball.reset_ball(x_pos=paddle.xcor())
        lives.lose_live()

s.exitonclick()
