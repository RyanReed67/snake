from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_board()

    def reset(self):
        self.score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(0, 265)
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -40)
        self.write("Press SPACE to restart", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_board()
