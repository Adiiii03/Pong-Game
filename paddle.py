from turtle import Turtle
WIDTH = 20
HEIGHT = 100
MOVE_BY = 20


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.position = pos
        self.penup()
        self.goto(pos)
        self.turtlesize(5, 1)
        self.shape("square")
        self.color("white")

    def move_up(self):
        new_y = (self.ycor() + MOVE_BY)
        self.goto(self.position[0], new_y)

    def move_down(self):
        new_y = (self.ycor() - MOVE_BY)
        self.goto(self.position[0], new_y)
