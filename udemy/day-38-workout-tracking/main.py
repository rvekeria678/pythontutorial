from config import APP_ID, API_KEY, HOST, NLE_EP
import requests

parameters = {
    "query":"I ran 4 miles and biked 15"
}

header = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY
}

nle_endpoint = f"{HOST}{NLE_EP}"
print(nle_endpoint)

response = requests.post(url=nle_endpoint,json=parameters,headers=header)
response.raise_for_status()

data = response.json()
print(data)