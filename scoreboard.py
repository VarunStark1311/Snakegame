from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Arial", 18, "bold")

with open("../../Desktop/data.txt") as file:
    high_score = int(file.read())


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High_Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.data_update()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 10
        self.update_score()

    def data_update(self):
        with open("../../Desktop/data.txt", mode="w") as file_2:
            file_2.write(f"{self.high_score}")
