from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

class Controls(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    @staticmethod
    def restart():
        snake.reset()
        food.reset()
        scoreboard.reset()

    @staticmethod
    def set_keys(up, down, left, right):
        screen.onkey(snake.up, up)
        screen.onkey(snake.down, down)
        screen.onkey(snake.left, left)
        screen.onkey(snake.right, right)


