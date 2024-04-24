import os, requests
from dotenv import load_dotenv
from datetime import datetime
from config import TOKEN, USERNAME, GRAPH_ID, GRAPH_NAME, ATOS, NM, PIXELA_EP, GRAPH_EP, PIXEL_POST_EP, HEADERS

load_dotenv()

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": ATOS,
    "notMinor": NM
}

#response = requests.post(url=PIXELA_EP, json=user_params)
#print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

#response = requests.post(url=GRAPH_EP,json=graph_config, headers=HEADERS)
#print(response.text)
today = datetime.now()
today_YYYYMMDD = today.strftime('%Y%m%d')

pixel_config = {
    "date":today_YYYYMMDD,
    "quantity":'93.1',
}

#response = requests.post(url=PIXEL_POST_EP, json=pixel_config, headers=HEADERS)
#response.raise_for_status()

new_pixel_data = {
    "quantity": "4.5"
}

update_endpoint = f"{PIXELA_EP}/{USERNAME}/graphs/{GRAPH_ID}/{today_YYYYMMDD}"

#response = requests.put(url=update_endpoint,json=new_pixel_data, headers=HEADERS)
#print(response.text)

response = requests.delete(url=update_endpoint, headers=HEADERS)
print(response.text)