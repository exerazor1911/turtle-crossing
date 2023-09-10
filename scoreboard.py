from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(-200, 250)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", FONT)