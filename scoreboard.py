from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.color('pink')
        self.pu()
        self.hideturtle()

        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 240)
        self.write(self.score, align='center', font=('Ariel', 40, 'normal'))

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def winner(self):
        self.clear()
        self.write('o boy u won!', align='center', font=('Times New Roman', 100, 'normal'))

    def loser(self):
        self.clear()
        self.write('o boy u LOST!', align='center', font=('Papyrus', 80, 'normal'))