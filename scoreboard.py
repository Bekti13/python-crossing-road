from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 0
        self.goto(-220, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", False, 'center', FONT)

    def add_score(self):
        self.level += 1
        self.clear()
        self.update_score()
