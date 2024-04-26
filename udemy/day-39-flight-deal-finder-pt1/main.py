from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
from config import DEPARTURE_LOC

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_all()

for data in sheet_data:
    if data['iataCode'] == '':
        iata_code = flight_search.get_iata_code(city_name=data['city'])        
        row_data = {'iataCode':iata_code}
        data_manager.update(rownum=data['id'], row_data=row_data)


