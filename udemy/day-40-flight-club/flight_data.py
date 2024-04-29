from config.flight_data import DEPARTURE_CITY, DEPARTURE_CODE, MAX_STOPOVERS, MIN_TRAVEL_TIME, MAX_TRAVEL_TIME, CURRENCY
from config.authorization import FLIGHTSEARCH_API_KEY
from config.endpoints import TEQUILA_SEARCH_HOST, TEQUILA_SEARCH_EP
from datetime import datetime, timedelta
import requests

#This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self, arrival_code: str, price_limit: int):
        self.header = {"apikey":FLIGHTSEARCH_API_KEY}

        self.departure_airport_code = DEPARTURE_CODE
        self.departure_city = DEPARTURE_CITY
        
        self.arrival_code = arrival_code

        self.price_limit = price_limit

        self.ticket_info = self.get_ticket_info()

    def get_ticket_info(self):
        tomorrow_date = datetime.now() + timedelta(1)
        six_month_date = datetime.now() + timedelta(180)
        parameters = {
            "fly_from":self.departure_airport_code,
            "fly_to":self.arrival_code,
            "nights_in_dst_from":MIN_TRAVEL_TIME,
            "nights_in_dst_to":MAX_TRAVEL_TIME,
            "date_from":tomorrow_date.strftime('%d/%m/%Y'),
            "date_to":six_month_date.strftime('%d/%m/%Y'),
            "max_stopovers": MAX_STOPOVERS,
            "ret_to_diff_city": False,
            "curr": CURRENCY,
            "price_to": self.price_limit,
            "sort":"price",
            "limit": 1
        }
        url=f"{TEQUILA_SEARCH_HOST}/{TEQUILA_SEARCH_EP}"
        response = requests.get(url=url, params=parameters, headers=self.header)
        response.raise_for_status()
        return response.json()