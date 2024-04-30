from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from config.authorization import PHONE_NUMBER

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_all()

tickets = []

for data in sheet_data:
    if data['iataCode'] == '':
        iata_code = flight_search.get_iata_code(city_name=data['city'])
        data['iataCode'] = iata_code        
        row_data = {'iataCode':iata_code}
        data_manager.update(rownum=data['id'], row_data=row_data)
    

tickets = {data['iataCode']:FlightData(arrival_code=data['iataCode'],
                      price_limit=data['lowestPrice']).ticket_info['data'] for data in sheet_data}
'''
for ticket in tickets:
    if tickets[ticket]:
        NotificationManager(ticket_details=tickets[ticket]['data'][0]).send_emails('')
    else:
        tickets[ticket] = FlightData(arrival_code=data['iataCode'], price_limit=data['lowestPrice'], stop_overs=1)
        if tickets[ticket]:
            NotificationManager(ticket_details=tickets[ticket]['data'][0]).send_emails('')'''