from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from config.authorization import PHONE_NUMBER

data_manager = DataManager()
flight_search = FlightSearch()

#-----Ticket Logic-----#
loc_sheet_data = data_manager.get_all_loc()
for data in loc_sheet_data:
    if data['iataCode'] == '':
        iata_code = flight_search.get_iata_code(city_name=data['city'])
        data['iataCode'] = iata_code        
        row_data = {'iataCode':iata_code}
        data_manager.update_loc(rownum=data['id'], row_data=row_data)
# Generate Direct Flight Tickets
ticket_info = {data['iataCode']:FlightData(arrival_code=data['iataCode'],
                      price_limit=data['lowestPrice']).ticket_info['data'] 
                      for data in loc_sheet_data}
#-----Email Logic-----#
user_sheet_data = data_manager.get_all_emails()
# Extract Email Info. from JSON data
recipient_list = [row['email'] for row in user_sheet_data]
for loc in ticket_info:
    if ticket_info[loc]:
        NotificationManager(ticket_details=ticket_info[loc][0]).send_emails(recipients=recipient_list)
    else:
        ticket_info[loc] = FlightData(arrival_code=data['iataCode'], price_limit=data['lowestPrice'], stop_overs=1).ticket_info['data']
        if ticket_info[loc]:
            NotificationManager(ticket_details=ticket_info[loc]['data'][0]).send_emails(recipients=recipient_list)