#import colorgram
#colors = colorgram.extract('image1.jpeg',10)
#list_colors = []
#for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   list_colors.append((r, g, b))
#print(list_colors)

import turtle
from turtle import *
import random

colors_list = [(215, 68, 117), (229, 144, 77), (101, 190, 115), (230, 219, 93), (160, 73, 134), (76, 110, 164), (63, 174, 142), (231, 94, 82), (108, 103, 164), (233, 110, 160)]

timy = Turtle()
my_screen = Screen()
timy.speed("fastest")
timy.penup()
timy.hideturtle()

turtle.colormode(255)
timy.setheading(225)
timy.forward(250)
timy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    timy.dot(15, random.choice(colors_list))
    timy.forward(50)

    if dot_count % 10 == 0:
        timy.setheading(90)
        timy.forward(50)
        timy.setheading(180)
        timy.forward(500)
        timy.setheading(0)



my_screen.exitonclick()
