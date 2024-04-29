from config.endpoints import TEQUILA_HOST, TEQUILA_LOCATION_EP
from config.authorization import FLIGHTSEARCH_API_KEY
import requests

#This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        self.header = {"apikey":FLIGHTSEARCH_API_KEY}

    def get_iata_code(self, city_name: str):
        url = f'{TEQUILA_HOST}{TEQUILA_LOCATION_EP}'
        parameters = {'term':city_name}
        response = requests.get(url=url, params=parameters, headers=self.header)
        response.raise_for_status()
        loc_data = response.json()
        return loc_data['locations'][0]['code']