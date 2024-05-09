import os
from dotenv import load_dotenv

load_dotenv()

ISS_URL = "http://api.open-notify.org/iss-now.json"
SS_URL = "https://api.sunrise-sunset.org/json"
MARGIN = 5

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
PORT = 587
TIMEOUT = 120