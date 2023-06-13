from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 260)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", False, align=ALIGNMENT,font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        return self.score
