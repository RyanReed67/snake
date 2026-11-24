from turtle import Terminator
from tkinter import TclError
from controls import Controls, snake, food, scoreboard
import time


def restart_game():
    global game_is_on
    if not game_is_on:
        controls.restart()
        game_is_on = True

controls = Controls()


controls.screen.listen()
# arrow keys
controls.set_keys("Up", "Down", "Left", "Right")
# wsad keys
controls.set_keys("w", "s", "a", "d")
controls.screen.onkey(restart_game, "space")

game_is_on = True
try:
    while True:
        controls.screen.update()
        time.sleep(0.1)
        if not game_is_on:
            continue
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #   Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

except Terminator, TclError:
    pass

