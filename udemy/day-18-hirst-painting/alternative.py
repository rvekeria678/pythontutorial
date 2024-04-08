import turtle as turtle_module
import random

my_turtle = turtle_module.Turtle()
palette = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85)]
turtle_module.colormode(255)
my_turtle.speed('fastest')
my_turtle.hideturtle()
my_turtle.penup()

my_turtle.setheading(225)
my_turtle.forward(500)
my_turtle.setheading(0)

for _ in range(10):
    for _ in range(10):
        my_turtle.pendown()
        my_turtle.dot(30, random.choice(palette))
        my_turtle.penup()
        my_turtle.forward(70)
    my_turtle.left(90)
    my_turtle.forward(70)
    my_turtle.left(90)
    my_turtle.forward(700)
    my_turtle.left(180)


screen = turtle_module.Screen()
screen.exitonclick()