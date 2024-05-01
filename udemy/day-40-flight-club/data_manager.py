from config.endpoints import SHEETY_HOST, SHEETY_PRICES_SHEET_EP, SHEETY_USERS_SHEET_EP
from config.authorization import SHEETY_BEARER_TOKEN
import requests

#responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.headers = {"Authorization":f"Bearer {SHEETY_BEARER_TOKEN}"}
        

    def add_loc(self, city_name, iata_code="", lowest_price=0):
        row_data = {"city:": city_name,"iataCode": iata_code,"lowestPrice": lowest_price}
        new_data = {"price": row_data}
        url = f"{SHEETY_HOST}/{SHEETY_PRICES_SHEET_EP}"
        response = requests.post(url=url, json=new_data, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (add loc) : Response Status: {response.status_code}")

    def get_loc(self, rownum: int):
        url = f"{SHEETY_HOST}/{SHEETY_PRICES_SHEET_EP}/{rownum}"
        response = requests.get(url=url, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (get loc) : Response Status: {response.status_code} | id:{rownum}")
        return response.json()
        
    def get_all_loc(self):
        url = f"{SHEETY_HOST}/{SHEETY_PRICES_SHEET_EP}"
        response = requests.get(url=url, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (get_all loc) : Response Status: {response.status_code}")
        return response.json()['prices']
    
    def update_loc(self, rownum: int, row_data: dict):
        url = f"{SHEETY_HOST}/{SHEETY_PRICES_SHEET_EP}/{rownum}"
        new_data = {"price": row_data}
        response = requests.put(url=url, json=new_data, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (update loc) | Response Status: {response.status_code} | id:{rownum} -> {row_data}")

    def remove_loc(self, rownum: int):
        url = f"{SHEETY_HOST}/{SHEETY_PRICES_SHEET_EP}/{rownum}"
        response = requests.delete(url=url, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (delete loc) | Response Status: {response.status_code}")

    def get_all_emails(self):
        url = f"{SHEETY_HOST}/{SHEETY_USERS_SHEET_EP}"
        response = requests.get(url=url, headers=self.headers)
        response.raise_for_status()
        print(f"DataManager (get_all emails) : Response Status: {response.status_code}")
        return response.json()['users']