from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates Screen to reflect current Level."""
        self.goto(-200, 240)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        """Increases Level by 1"""
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Prints Game Over in the Screen."""
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)
