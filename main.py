# This is a sample Python script.
#import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from turtle import Screen, Turtle
from foodd import Food
from SCOREBOARD import scoreboard

from snake import Snake
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake=Snake()


food=Food()
scorecard=scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")






game_is_on=True
while(game_is_on):
    screen.update()
    time.sleep(0.5)
    Snake.move(snake)
#detect collision of food
    if snake.head.distance(food) <15:
        food.refresh()
        scorecard.scoreincrease()
    #detect collision of wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scorecard.game_over()



screen.exitonclick()




















