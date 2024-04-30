from config.authorization import TWILIO_PHONE_NUMBER, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from twilio.rest import Client

#This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self, reciever_phone_number: str, ticket_details: dict):
        price = ticket_details['price']
        flyFrom = ticket_details['flyFrom']
        cityFrom = ticket_details['cityFrom']
        flyTo = ticket_details['flyTo']
        cityTo = ticket_details['cityTo']
        depart_date = ticket_details['route'][0]['local_departure'].split('T')[0]
        arrive_date = ticket_details['route'][1]['local_departure'].split('T')[0]

        msg=f"Low price alert! Only ${price} to fly from {cityFrom}-{flyFrom} to {cityTo}-{flyTo}, from {depart_date} to {arrive_date}"

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
                body=msg,
                from_=TWILIO_PHONE_NUMBER,
                to=reciever_phone_number
            )
    
    def send_text(phone_number):
        pass