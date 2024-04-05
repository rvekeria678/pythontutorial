from turtle import Turtle as t, Screen as s

my_turtle = t()

my_turtle.shape('turtle')
my_turtle.color('indigo')

for _ in range(4):
    my_turtle.right(90)
    my_turtle.forward(100)

screen = s()
screen.exitonclick()
