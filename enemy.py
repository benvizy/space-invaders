from turtle import Turtle
from bullet import Bullet
import random

MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
ENEMY_NUMBER = 50
LEFT_B = -300
RIGHT_B = 300

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    ran_col = (r, g, b)
    return ran_col


class EnemyGenerator():

    def __init__(self):
        self.enemies = []
        self.speed = MOVE_DISTANCE
        self.shots = [Bullet()]

    def create_enemies(self):
        for i in range(ENEMY_NUMBER):
            new_enemy = Turtle("square")
            new_enemy.pu()
            new_enemy.color(random_color())
            new_enemy.goto(300, 300)
            new_enemy.left(180)

            self.enemies.append(new_enemy)

    def shoot(self, index):
        if len(self.shots) < 7:
            self.shots.append(Bullet())
            self.shots[-1].goto(self.enemies[index].xcor(), self.enemies[index].ycor())
            self.shots[-1].shoot(start_x=self.enemies[index].xcor(), start_y=self.enemies[index].ycor())

    def setup_enemies(self, index):

        # TODO: Figure out where to put the for loop so the enemies go one by one!
        if abs(self.enemies[index].xcor() - self.enemies[index-1].xcor()) < 50:
           self.enemies[index].forward(MOVE_DISTANCE)

        if self.enemies[index].xcor() < LEFT_B:
            self.enemies[index].left(90)
            self.enemies[index].forward(MOVE_DISTANCE*2)

        if self.enemies[index].xcor() > RIGHT_B:
            self.enemies[index].right(90)
            self.enemies[index].forward(MOVE_DISTANCE * 2)

    def move_enemies(self):
        for enemy in self.enemies:
            rando = random.randint(1, 10)
            enemy.forward(MOVE_DISTANCE)
            if rando == 10:
                self.shoot(self.enemies.index(enemy))



    def faster(self):
        self.speed += MOVE_INCREMENT
