from turtle import Turtle, Screen, colormode
import random


t = Turtle()
colormode(255)

t.width(10)
t.speed('fastest')
directions = [0,90,180,360]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for _ in range(300):
    d = random.choice(directions)    
    t.pencolor(random_color())
    t.right(random.choice(directions))
    t.forward(30)

screen = Screen()
screen.exitonclick()
