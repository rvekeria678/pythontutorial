from flask import Flask
from flask import render_template

app = Flask(__name__)

# root path
@app.route('/')
def root():
    return render_template('./index.html')

# server start
if __name__ == "__main__":
    app.run(debug=True)