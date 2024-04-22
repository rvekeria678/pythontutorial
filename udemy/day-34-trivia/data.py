import requests
from config import TRIVIA_URL

question_parameters = {
    "amount":10,
    "type":"boolean"
}

response = requests.get(TRIVIA_URL, params=question_parameters)
data = response.json()
question_data = data['results']
