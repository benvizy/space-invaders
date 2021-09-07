from turtle import Screen
from enemy import EnemyGenerator
from player import Player
from scoreboard import ScoreBoard
import time


# Constants & Lists

OFF_SCREEN_TOP = 360
OFF_SCREEN_BOTTOM = -360
ammunition_count = 1


# Set Up Screen
screen = Screen()

screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Invedas")
screen.tracer(0)

# TODO:
enemy_generator = EnemyGenerator()
scoreboard = ScoreBoard()
player = Player()


# # Key Commands # #
screen.listen()

screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
screen.onkey(player.blam, "Up")


# Initialize Variables
game_is_on = True
enemy_generator.create_enemies()
for i in range(49):
    enemy_generator.setup_enemies(i)


# NECESSARY FUNCTIONS
def endgame():
    if scoreboard.score == 490:
        scoreboard.winner()
    else:
        scoreboard.loser()

while game_is_on:

    screen.update()
    time.sleep(0.1)

    if scoreboard.score == 490:
        endgame()
        game_is_on = False

    for i in range(len(enemy_generator.enemies)-1):
        enemy_generator.setup_enemies(i)

    enemy_generator.move_enemies()

    for shot in player.shots:

        for enemy in enemy_generator.enemies:
            if abs(enemy.ycor() - player.ycor()) < 10:
                endgame()
                game_is_on = False

            if abs(shot.ycor() - enemy.ycor()) < 20 and abs(shot.xcor() - enemy.xcor()) < 20:
                scoreboard.increase_score()
                enemy.goto(400,400)
                try:
                    enemy_generator.enemies.remove(enemy)
                except:
                    print("can't remove enemigo")
                try:
                    shot.goto(400,400)
                except:
                    shot.clear()
                    print("can't remove blicky")

        if shot.ycor() < OFF_SCREEN_TOP:
            shot.go_up()
        else:
            player.shots.remove(shot)

    for shot in enemy_generator.shots:
        if abs(shot.ycor() - player.ycor()) < 15 and abs(shot.xcor() - player.xcor()) < 15:
            print('u died')
            enemy_generator.shots.remove(shot)
            endgame()
            game_is_on = False
        if shot.ycor() > OFF_SCREEN_BOTTOM:
            shot.go_down()
        else:
            enemy_generator.shots.remove(shot)

screen.exitonclick()

