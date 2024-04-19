import datetime as dt
import os, smtplib, random

# ----- CONSTANTS ----- #
EMAIL = "zeffarlo53@gmail.com"
PASSWORD = "kgck smtk dshj nbka"
PORT = 587
TIMEOUT = 120
# ----- EMAIL LOGIC ----- #
with smtplib.SMTP('smtp.gmail.com', port=PORT, timeout=TIMEOUT) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    current_date = dt.datetime.now()
    if current_date.weekday() == 4:
        with open(os.path.join(os.path.dirname(__file__), './quotes.txt')) as data_file:
            data = data_file.readlines()
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f'Subject=Motivational Message\n\n{random.choice(data)}')