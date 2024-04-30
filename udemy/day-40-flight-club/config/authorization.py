import os
from dotenv import load_dotenv

load_dotenv()

FLIGHTSEARCH_API_KEY = os.environ.get("FLIGHTSEARCH_API_KEY")
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")

PHONE_NUMBER = os.environ.get('PHONE_NUMBER')