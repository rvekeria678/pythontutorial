import os
from dotenv import load_dotenv

load_dotenv()

FLIGHTSEARCH_API_KEY = os.environ.get("FLIGHTSEARCH_API_KEY")
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")