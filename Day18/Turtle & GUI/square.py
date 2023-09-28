from turtle import *

my_turtle = Turtle()
my_screen = Screen()

#my_turtle.forward(200)
#my_turtle.right(90)
#my_turtle.forward(200)
#my_turtle.right(90)
#my_turtle.forward(200)
#my_turtle.right(90)
#my_turtle.forward(200)
# or
for _ in range(4):
    my_turtle.forward(200)
    my_turtle.right(90)


my_screen.exitonclick()
