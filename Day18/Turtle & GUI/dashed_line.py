from turtle import *

my_turtle = Turtle()
my_screen = Screen()

for _ in range(10):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(20)
    my_turtle.pendown()

my_screen.exitonclick()
