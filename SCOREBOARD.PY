from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.Score=-1
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.scoreincrease()

    def update_scoreboard(self):
        self.write(f"Score:{self.Score}",align="center",font=("Arial",24,"normal"))
    def scoreincrease(self):
        self.Score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial",24,"normal"))
