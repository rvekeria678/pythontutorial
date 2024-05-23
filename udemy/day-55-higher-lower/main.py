from flask import Flask
import random

app = Flask(__name__)

secret = random.randint(1,8)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9<h1><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNW14eG9sc2x2MjUybTBuNDZ1ZHU3MXUwMHdpdmJhbGhnMGxlbTVndSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rs2QPsshsFI9zeT4Kn/giphy.gif' style='width:480px;'>"

@app.route('/<guess>')
def user_guess(guess):
    guess=int(guess)
    if guess > 0 and guess < 9:
        if guess < secret:
            return "<h1>Your guess was too low</h1><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXpleHp1YnB3OXMxbGVicXFhNml5NjM2ZDA0cW94Y2VrYXlrNXh1NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ul1KLURPJJ7zy/giphy.gif' style='width:480px;'>"
        elif guess > secret:
            return "<h1>Your guess was too high</h1><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExODd3bDd1OGI4MnR3cGIyNmU3c3dldm5vbnF0enVuOHlmd2t2ajhvcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Xg3ySobhfo9uvYm2YA/giphy.gif' style='width:480px'>"
        else:
            return "<h1>Your guess was correct!</h1><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd21jdHY5MzF0Z2kyYW45Z28wZWduM2VhdWNuNzRvbWNlMjBnaWQ3NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2afdli2NFvmq1KsIeS/giphy.gif' style='width:480px'>"
    else:
        return "<h1>The number you guess does not fall in the range! Try again.</h1>"

if __name__ == "__main__":
    app.run(debug=True)

# Higher Lower Game