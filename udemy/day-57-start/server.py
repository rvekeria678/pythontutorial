from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)

    return render_template("index.html", num=random_number, curr_year=datetime.now().year, author="Zeph")

if __name__ == "__main__":
    app.run(debug=True)