import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(750,550)
image = r'udemy\day-25-us-states-game\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Reading Data
data_path = r'udemy\day-25-us-states-game\50_states.csv' 
data = pandas.read_csv(data_path)

correct_ans = 0
while correct_ans < 50:
    answer_state = screen.textinput(title=f'{correct_ans}/50 Guess the State', prompt="What's another state's name?")
    
    if len(data[data['state'] == answer_state]):
        correct_ans += 1
    print(correct_ans)

turtle.mainloop()
