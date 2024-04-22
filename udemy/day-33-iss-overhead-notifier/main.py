import requests, time, smtplib
from datetime import datetime
from config import ISS_URL, SS_URL, MARGIN, PORT, TIMEOUT, EMAIL, PASSWORD
import geocoder

def current_loc():
    location = geocoder.ip('me')
    return (location.latlng[0], location.latlng[1])

def iss_loc():
    response = requests.get(ISS_URL)
    response.raise_for_status()
    data = response.json()
    return (float(data['iss_position']['latitude']), float(data['iss_position']['longitude']))

def dark(latitude, longitude):
    parameters = {'lat': latitude, 'lng':longitude, 'formatted':0}
    response = requests.get(SS_URL,params=parameters)
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = datetime.now().hour
    return True if time_now < sunrise or time_now > sunset else False

def visible(lat, lng, isslat, isslng):
    if abs(lat-isslat) <=MARGIN and abs(lng-isslng) <=MARGIN and dark(lat,lng):
        return True
    return False

# LOGIC

CUR_LAT, CUR_LNG = current_loc()
iss_lat, iss_lng = iss_loc()

while visible(CUR_LAT, CUR_LNG, iss_lat, iss_lng):
    print("Sending Notification...")
    with smtplib.SMTP('smtp.gmail.com', port=PORT, timeout=TIMEOUT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg='Subject:ISS NOTIFIER\n\nLook Up, there is a good chance you will see the ISS in the sky.')
    time.sleep(60)
    iss_lat, iss_lng = iss_loc()



