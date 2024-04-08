from turtle import Turtle, Screen, colormode
import random

my_turtle = Turtle()
colormode(255)

my_turtle.shape("turtle")
my_turtle.speed("fastest")
my_turtle.pensize(3)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_spirograph(r,size_of_gap):
    for i in range(int(360 / size_of_gap)):
        my_turtle.pencolor(random_color())
        my_turtle.circle(r)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)

draw_spirograph(600,0.1)

screen = Screen()
screen.exitonclick()