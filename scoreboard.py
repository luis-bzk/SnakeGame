from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, "bold")

with open("data.txt") as file:
    HIGH_SCORE_STORED = int(file.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE_STORED
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | HighScore: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over",
    #                align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        self.score = 0
        self.update_scoreboard()

    def save_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
