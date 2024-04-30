import os
from dotenv import load_dotenv

load_dotenv()

ORIGIN_EMAIL = os.environ.get('ORIGIN_EMAIL_USER')
ORIGIN_PASSWORD = os.environ.get('ORIGIN_EMAIL_PASS')
PORT = 587
TIMEOUT = 120