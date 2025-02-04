from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1
        self.move()
        self.speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move()
        self.speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.speed = 0.1


   #my way to increase speed after every miss
    # def speed(self):
    #     self.x_move *= 1.1
    #     self.y_move *= 1.1



