from turtle import Turtle, Screen
import random


t = Turtle()
colors = ['red','purple','blue','orange','pink','green','yellow','black', 'indigo', 'violet']
t.width(10)

directions = [0,1,2,3]

for _ in range(100):
    d = random.choice(directions)    
    t.color(random.choice(colors))
    if d == 0:
        t.forward(30)
    elif d == 1:
        t.right(90)
        t.forward(30)
    elif d == 2:
        t.left(90)
        t.forward(30)
    else:
        t.back(30)

screen = Screen()
screen.exitonclick()
