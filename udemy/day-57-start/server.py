from flask import Flask, render_template
from datetime import datetime
import random
import requests

#----Globals----#
app = Flask(__name__)
#----URL----#
AGEIFY_URL = 'https://api.agify.io'
GENDERIZE_URL = 'https://api.genderize.io'

@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, curr_year=datetime.now().year, author="Zeph")

@app.route('/guess/<name>')
def guess(name: str):
    agify_params = {"name":name}
    agify_data = requests.get(AGEIFY_URL, params=agify_params).json()

    genderize_params = {"name":name}
    genderize_data = requests.get(GENDERIZE_URL, params=genderize_params).json()

    return render_template("guess.html", name=name.title(), gender=genderize_data['gender'], age=agify_data['age'])

if __name__ == "__main__":
    app.run(debug=True)