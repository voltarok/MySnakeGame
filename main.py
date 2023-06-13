from turtle import Screen
import turtle as t
import time

import score_board
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Master")
screen.setup(width=600, height=600)
screen.tracer(0)

t.colormode(255)

snake = Snake()
food = Food()
board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on  = True

while game_is_on :
    screen.update()
    time.sleep(0.1)


    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15 :
        board.update_score()
        snake.extend_snake()
        food.refresh()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        board.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            board.game_over()


#todo 1 THERE IS A BUG WHEN USER PUSH KEYS CONSEQUENTLY
# SNAKE DOESN'T SEEM EAT ITSELF IT EATS ANYWAY, AND THIS LOOKs NOT NICE




game()
screen.exitonclick()