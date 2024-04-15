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

def camel(text):
    return ' '.join(word.lower().capitalize() for word in text.split())

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
guessed_states = []
all_states = data.state.to_list()
while len(guessed_states) < 50:
    answer_state = camel(screen.textinput(title=f'{len(guessed_states)}/50 Guess the State', prompt="What's another state's name?"))

    if answer_state == "Exit":
        break
    
    answer_state = data[data['state'] == answer_state]
    if len(answer_state):
        guessed_states.append(answer_state.state.iloc[0])
        x = int(answer_state['x'])
        y = int(answer_state['y'])
        writer.goto(x,y)
        writer.write(answer_state.state.iloc[0])

missing_states = [state for state in all_states if state not in missing_states]

new_data = pandas.DataFrame(missing_states)
new_data.to_csv('states_to_learn.csv')

turtle.mainloop()
