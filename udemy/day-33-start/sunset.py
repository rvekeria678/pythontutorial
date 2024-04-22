import requests, geocoder
from datetime import datetime

location = geocoder.ip('me')

CUR_LAT = location.latlng[0]
CUR_LONG = location.latlng[1]

API_PATH = 'https://api.sunrise-sunset.org/json'

PARAMETERS = {'lat': CUR_LAT, 
              'lng': CUR_LONG,
              'formatted':0}

response = requests.get(API_PATH, params=PARAMETERS)
response.raise_for_status()

data = response.json()

sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

print(sunrise, sunset)

time_now = datetime.now().hour

print(time_now)