from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
#sheet_data = data_manager.get_all()

print(data_manager.get(1))

#for data in sheet_data:
#    if data['iataCode'] == '':
#        pass
