import os, requests
from dotenv import load_dotenv

load_dotenv()

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": os.environ['TOKEN'],
    "username": os.environ['USERNAME'],
    "agreeTermsOfService": "yes",
    "notMinor": "no"
}

requests.post()