from config import SHEETY_BEARER_TOKEN, SHEETY_EP
import requests

#responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.headers = {"Authorization":f"Bearer {SHEETY_BEARER_TOKEN}"}

    def add(self, city_name, iata_code="", lowest_price=0):
        json_data = {
            "price": {
                "city": city_name,
                "iataCode": iata_code,
                "lowestPrice": lowest_price
            }
        }
        response = requests.post(url=SHEETY_EP, json=json_data, headers=self.headers)
        response.raise_for_status()

    def get(self, rownum: int):
        query_ep = f"{SHEETY_EP}/{rownum}"
        response = requests.get(url=query_ep, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_all(self):
        response = requests.get(url=SHEETY_EP, headers=self.headers)
        response.raise_for_status()
        return response.json()['prices']
    
    def update(self, rownum: int, new_data: dict):
        query_ep = f"{SHEETY_EP}/{rownum}"
        response = requests.put(url=query_ep, json=new_data, headers=self.headers)
        response.raise_for_status()

    def remove(self, city_name: str):
        pass


