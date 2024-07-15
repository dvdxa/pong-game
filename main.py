from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
screen.listen()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ycor()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_xcor()
        ball.move_speed *= 0.9
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.move_speed *= 0.9
        ball.bounce_xcor()

    # Detect R paddle misses:
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detect L paddle misses:
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()