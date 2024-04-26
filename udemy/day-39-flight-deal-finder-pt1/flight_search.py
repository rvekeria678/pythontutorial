from config import TEQUILA_HOST, LOCATION_EP, FLIGHTSEARCH_API_KEY
import requests

#This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        pass

    def get_iata_code(self, city_name: str):
        url = f'{TEQUILA_HOST}{LOCATION_EP}'
        parameters = {'term':city_name}
        header =  {"apikey":FLIGHTSEARCH_API_KEY}
        response = requests.get(url=url, params=parameters, headers=header)
        response.raise_for_status()
        loc_data = response.json()
        return loc_data['locations'][0]['code']