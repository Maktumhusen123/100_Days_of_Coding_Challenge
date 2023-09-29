import random
import turtle
from turtle import *

my_turtle = Turtle()
turtle.colormode(255)
my_screen = Screen()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour
# colors = ["red", "blue", "orange", "pink", "brown", "yellow", "green", "aquamarine"]


my_turtle.speed(20)


def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + gap)


draw_spirograph(5)
