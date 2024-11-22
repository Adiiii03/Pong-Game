import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()


    #detect collision by upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce back
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()


    #when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()