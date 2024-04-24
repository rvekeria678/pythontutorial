import os, requests
from dotenv import load_dotenv

load_dotenv()

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": os.environ['TOKEN'],
    "username": os.environ['PIXELA_USERNAME'],
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{os.environ["PIXELA_USERNAME"]}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

response = requests.post(url=graph_endpoint,json=graph_config, headers=os.environ['TOKEN'])

print(response.text)