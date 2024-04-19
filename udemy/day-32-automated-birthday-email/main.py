'''
import smtplib

my_email = "zeffarlo53@gmail.com"
password = "kgck smtk dshj nbka"
sender_email = "farlotaylor@yahoo.com"

with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs=sender_email, msg="Subject:hello\n\nThis is the body of my email.")
'''

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month


print(year, month)


date_of_birth = dt.datetime(year=1995, month=12, day=15)

print(date_of_birth)