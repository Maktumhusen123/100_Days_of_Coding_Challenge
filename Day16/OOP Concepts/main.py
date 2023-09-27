from turtle import Turtle, Screen

my_turtle = Turtle()  # object = Class() here my_turtle is an object of class Turtle()
print(my_turtle)
my_turtle.shape("square")
my_turtle.color("green")
my_turtle.forward(100)

screen = Screen()   # screen object is created
print(screen.canvheight)  # canvheight is an attribute of Screen() class, objectname.attribute
screen.exitonclick()    # exitonclick() is a method of Screen() class, objectname.method()

