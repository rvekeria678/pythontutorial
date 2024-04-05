from turtle import Turtle, Screen
import random

colors = ['red','purple','blue','orange','pink','green','yellow','black', 'indigo', 'violet']

t = Turtle()
t.shape('turtle')

number_of_sides = 3

for number_of_sides in range(3,10):
    t.color(random.choice(colors))
    for i in range(number_of_sides):
        t.right(360/number_of_sides)
        t.forward(100)


screen = Screen()
screen.exitonclick()