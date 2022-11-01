from turtle import *

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.level = 1
        self.goto(-220, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f'Level:{self.level}', move=False, align='left', font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', move=False, align='center', font=FONT)



