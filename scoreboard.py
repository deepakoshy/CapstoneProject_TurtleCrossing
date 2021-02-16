from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_level(self):
        self.level += 1
        self.show_level()

    def over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Courier", 15, "normal"))
