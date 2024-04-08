from turtle import Turtle, Screen, colormode
import colorgram
import random

colors = colorgram.extract(r'painting.jpg', 10)
palette = []

for color in colors:
        palette.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(palette)

number_of_rows = 10
number_of_cols = 10
gap = 90
radius = 20

my_turtle = Turtle()
colormode(255)
my_turtle.speed('fastest')

def hirst():
    my_turtle.penup()
    my_turtle.back(300)
    my_turtle.right(90)
    my_turtle.forward(500)
    my_turtle.left(90)
    for y in range(number_of_rows):
        for x in range(number_of_cols):
            my_turtle.fillcolor(random.choice(palette))
            my_turtle.pendown()
            my_turtle.begin_fill()
            my_turtle.circle(radius)
            my_turtle.end_fill()
            my_turtle.penup()
            my_turtle.forward(gap)
        my_turtle.left(90)
        my_turtle.forward(90)
        my_turtle.left(90)
        my_turtle.forward(number_of_cols * gap)
        my_turtle.left(180)


hirst()

screen = Screen()
screen.exitonclick()
