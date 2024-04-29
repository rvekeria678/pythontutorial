from config.endpoints import SHEETY_HOST, SHEETY_PROJECT_EP
from config.authorization import SHEETY_BEARER_TOKEN
import requests

#responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.headers = {"Authorization":f"Bearer {SHEETY_BEARER_TOKEN}"}
        

    def add(self, city_name, iata_code="", lowest_price=0):
        row_data = {"city:": city_name,"iataCode": iata_code,"lowestPrice": lowest_price}
        new_data = {"price": row_data}
        url = f"{SHEETY_HOST}/{SHEETY_PROJECT_EP}"
        response = requests.post(url=url, json=new_data, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (add) : Response Status: {response.status_code}")

    def get(self, rownum: int):
        url = f"{SHEETY_HOST}/{SHEETY_PROJECT_EP}/{rownum}"
        response = requests.get(url=url, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (get) : Response Status: {response.status_code} | id:{rownum}")
        return response.json()
        
    def get_all(self):
        url = f"{SHEETY_HOST}/{SHEETY_PROJECT_EP}"
        response = requests.get(url=url, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (get_all) : Response Status: {response.status_code}")
        return response.json()['prices']
    
    def update(self, rownum: int, row_data: dict):
        url = f"{SHEETY_HOST}/{SHEETY_PROJECT_EP}/{rownum}"
        new_data = {"price": row_data}
        response = requests.put(url=url, json=new_data, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (update) | Response Status: {response.status_code} | id:{rownum} -> {row_data}")

    def remove(self, rownum: int):
        url = f"{SHEETY_HOST}/{SHEETY_PROJECT_EP}/{rownum}"
        response = requests.delete(url=url, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (delete) | Response Status: {response.status_code}")
