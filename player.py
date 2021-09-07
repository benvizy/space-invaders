from turtle import Turtle
from bullet import Bullet

STARTING_POSITION = (0,-300)
MOVE_DISTANCE = 5
LEFT_BORDER = -350
RIGHT_BORDER = 350
OFF_SCREEN = 360


class Player(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("triangle")
        self.color("white")
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shots = [Bullet()]
        self.shots[-1].goto(360,360)



    def go_left(self):
        self.new_x = self.xcor() - MOVE_DISTANCE
        self.goto(self.new_x, self.ycor())

    def go_right(self):
        self.new_x = self.xcor() + MOVE_DISTANCE
        self.goto(self.new_x, self.ycor())

    def blam(self):

        # Shoot your shot if there are less than 7 on screen
        if len(self.shots) < 7:
            self.shots.append(Bullet())
            self.shots[-1].goto(self.xcor(),self.ycor())
            self.shots[-1].shoot(start_x=self.xcor(), start_y=self.ycor())