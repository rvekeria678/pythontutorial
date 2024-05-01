from config.authorization import TWILIO_PHONE_NUMBER, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from config.email import ORIGIN_EMAIL, ORIGIN_PASSWORD, PORT, TIMEOUT
from config.endpoints import SHEETY_USERS_SHEET_EP
from twilio.rest import Client
import smtplib

#This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self, ticket_details: dict):
        self.ticket_details = ticket_details
        self.message = self.generate_message()

    def generate_message(self):
        price = self.ticket_details['price']
        flyFrom = self.ticket_details['flyFrom']
        cityFrom = self.ticket_details['cityFrom']
        flyTo = self.ticket_details['flyTo']
        cityTo = self.ticket_details['cityTo']
        routes = self.ticket_details['route']
        depart_date = self.ticket_details['local_departure'].split('T')[0]
        arrival_date = self.ticket_details['local_arrival'].split('T')[0]

        message = f"Low price alert! Only ${price} to fly from {cityFrom}-{flyFrom}, to {cityTo}-{flyTo}, from {depart_date} to {arrival_date}\n\n"
        
        if len(routes) > 2:
            message += f"Flight has 1 stop over, via {self.ticket_details['route'][0]['cityTo']}."
 
        return message

    def send_texts(self, recipient:str):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        msg = client.messages.create(
                body=self.message,
                from_=TWILIO_PHONE_NUMBER,
                to=recipient
        )

    def send_emails(self, recipients:list):
        with smtplib.SMTP('smtp.gmail.com', port=PORT, timeout=TIMEOUT) as conn:
            conn.starttls()
            conn.login(user=ORIGIN_EMAIL, password=ORIGIN_PASSWORD)
            conn.sendmail(from_addr=ORIGIN_EMAIL, to_addrs=recipients, msg=f"Subject:Flight Club [Low Price Alert]\n\n{self.message}")



