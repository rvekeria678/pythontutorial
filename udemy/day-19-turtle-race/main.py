from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make you bet',prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
continue_race = False

turtles = []
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    turtles.append(new_turtle)

start_x = -230
start_y = -150

for turtle in turtles:
    turtle.penup()
    turtle.goto(start_x, start_y)
    start_y += 60

if user_bet:
    continue_race = True

while continue_race:
    for turtle in turtles:
        turtle.forward(random.randint(0,10))

        if turtle.xcor() >= 220:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won! The {winning_color} turtle is the winner!')
            else:
                print(f"You lost! The {winning_color} turtle is the winner")
            continue_race = False
            break

screen.exitonclick()