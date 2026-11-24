from turtle import Turtle
import random

class Food(Turtle):

    shapes = ["turtle", "arrow", "circle", "square", "triangle", "classic"]
    colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.speed("fastest")
        self.remaining_shapes = []
        self.remaining_colors = []
        self.refresh()

    def reset(self):
        self.refresh()

    def refresh(self):
        if not self.remaining_shapes:
            self.remaining_shapes = self.shapes.copy()
            random.shuffle(self.remaining_shapes)

        if not self.remaining_colors:
            self.remaining_colors = self.colors.copy()
            random.shuffle(self.remaining_colors)

        self.shape(self.remaining_shapes.pop())
        self.color(self.remaining_colors.pop())

        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
