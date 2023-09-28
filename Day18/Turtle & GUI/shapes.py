from turtle import *
import random
my_turtle = Turtle()
my_screen = Screen()

colors = ["red", "blue", "orange", "pink", "brown", "yellow", "green", "aquamarine"]


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.right(angle)


for shape in range(3, 11):
    my_turtle.color(random.choice(colors))
    draw_shape(shape)

my_screen.exitonclick()
