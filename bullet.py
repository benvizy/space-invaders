from turtle import Turtle, colormode
import random

SPEED = 20

colormode(255)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    ran_col = (r, g, b)
    return ran_col


class Bullet(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("circle")
        self.color(random_color())
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.pu()

    def go_up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - SPEED
        self.goto(self.xcor(), new_y)

    def shoot(self, start_x, start_y):
        self.goto(start_x, start_y)
