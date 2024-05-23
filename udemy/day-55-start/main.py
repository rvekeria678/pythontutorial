from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}<b>"
    return wrapper

def make_emphasis():
    pass

def make_underlined():
    pass

@app.route('/')
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>"

@app.route('/bye')
def bye():
    return "Bye!"

@app.route('/username/<name>')
def greet(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)
