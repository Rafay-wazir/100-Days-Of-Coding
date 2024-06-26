from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < - 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    for segments in snake.segments[1:]:  ####################
        if snake.head.distance(segments) < 10:              ########  (Using Slicing
            game_is_on = False                              ########      Method)
            score.game_over()            ####################

        # if segments == snake.head:     ####################
        #     pass                                         ##
        # elif snake.head.distance(segments) < 10:         #########  Ordinary Method (Without Using Slicing)
        #     game_is_on = False                           ##
        #     score.game_over()         #####################


screen.exitonclick()
