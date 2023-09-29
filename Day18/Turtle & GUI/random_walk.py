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


directions = [0, 90, 180, 270]
my_turtle.width(10)
my_turtle.speed(10)

for _ in range(200):
    my_turtle.color(random_color())
    my_turtle.forward(20)
    my_turtle.setheading(random.choice(directions))
