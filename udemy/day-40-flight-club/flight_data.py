
    
from config.flight_data import DEPARTURE_CITY, DEPARTURE_CODE, MAX_STOPOVERS, MIN_TRAVEL_TIME, MAX_TRAVEL_TIME, CURRENCY
from config.authorization import FLIGHTSEARCH_API_KEY
from config.endpoints import TEQUILA_SEARCH_HOST, TEQUILA_SEARCH_EP
from datetime import datetime, timedelta
import requests

#This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self, arrival_code: str, price_limit: int, stop_overs=0, via_city="", limit=1):
        self.header = {"apikey":FLIGHTSEARCH_API_KEY}
        
        self.arrival_code = arrival_code
        tomorrow_date = datetime.now() + timedelta(1)
        six_month_date = datetime.now() + timedelta(180)
        
        parameters = {
            "fly_from":DEPARTURE_CODE,
            "fly_to":self.arrival_code,
            "nights_in_dst_from":MIN_TRAVEL_TIME,
            "nights_in_dst_to":MAX_TRAVEL_TIME,
            "date_from":tomorrow_date.strftime('%d/%m/%Y'),
            "date_to":six_month_date.strftime('%d/%m/%Y'),
            "max_stopovers": stop_overs,
            "ret_to_diff_city": False,
            "curr": CURRENCY,
            "price_to": price_limit,
            "sort":"price",
            "limit": limit
        }
        
        url=f"{TEQUILA_SEARCH_HOST}/{TEQUILA_SEARCH_EP}"
        response = requests.get(url=url, params=parameters, headers=self.header)
        response.raise_for_status()
        self.ticket_info = response.json()

    