from turtle import Screen
from paddle import Paddle
from rectangles import Rectangles
from ball import Ball
from lives import Lives
from time import sleep

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

lives = Lives()

continue_game = True

while continue_game:
    sleep(ball.move_speed)
    s.update()
    ball.move_ball()

    # Check for collision with rectangles
    for i, rectangle in enumerate(rectangles.rectangles_list):
        if ball.distance(rectangle) < 20:
            print(rectangle)
            rectangles.rectangles_list.pop(i)
            del rectangle
            if abs(ball.xcor() - rectangle.xcor()) > 30:
                ball.bounce_ball_x_pos()
            else:
                ball.bounce_ball_y_pos()
            rectangles.rectangles_list.remove(rectangle)
            rectangle.hideturtle()

    if ball.xcor() > 320 or ball.xcor() < -320:
        ball.bounce_ball_x_pos()

    if ball.ycor() > 320:
        ball.bounce_ball_y_pos()

    if ball.distance(paddle) < 90 and abs(ball.ycor() - paddle.ycor()) < 50 - paddle.shapesize()[1]*10/2:
        ball.bounce_ball_y_pos()

    if ball.ycor() < -380:
        ball.reset_ball(x_pos=paddle.xcor())
        lives.lose_live()

s.exitonclick()

#FIXME: Fix interaction with ball and rectangle
#TODO: Add scoreboard
