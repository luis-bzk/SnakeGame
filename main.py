from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time

# set screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# snake delcaration
snake = Snake()
# food declaration
food = Food()
# scoreboard
scoreboard = ScoreBoard()

# listen screen
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# variable
game_is_on = True

# move snake
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # detect coliction with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # detect colition with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # detect collition with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
