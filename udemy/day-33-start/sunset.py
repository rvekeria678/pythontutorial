import requests, geocoder

location = geocoder.ip('me')

CUR_LAT = location.latlng[0]
CUR_LONG = location.latlng[1]

API_PATH = 'https://api.sunrise-sunset.org/json'

PARAMETERS = {'lat': CUR_LAT, 
              'lng': CUR_LONG}

response = requests.get(API_PATH, params=PARAMETERS)
response.raise_for_status()

data = response.json()

print(data)

