from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_all()

for data in sheet_data:
    if data['iataCode'] == '':
        iata_code = flight_search.get_iata_code(city_name=data['city'])        
        row_data = {'iataCode':iata_code}
        data_manager.update(rownum=data['id'], row_data=row_data)
  
for ticket in [FlightData(data['iataCode'], data['lowestPrice']) for data in sheet_data]:
    if len(ticket.ticket_info['data']):
        NotificationManager(
            reciever_phone_number="+19787293654",
            ticket_details=ticket.ticket_info['data'][0]
        )
        print(f"{ticket.arrival_code}: ${ticket.ticket_info['data'][0]['price']}")