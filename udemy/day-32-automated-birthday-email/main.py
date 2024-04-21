##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas, os, random, smtplib
import datetime as dt

# ------ CONSTANTS ------ #
CURRENT_DIR = os.path.dirname(__file__)
BIRTHDAY_DATA_PATH = os.path.join(CURRENT_DIR, './birthdays.csv')
LETTER_PATHS = {
    "letter_1.txt", "letter_2.txt", "letter_3.txt"
}
STMP_DATA = {
    "@gmail": 'smtp.gmail.com',
    "@yahoo": 'smtp.mail.yahoo.com'
}
EMAIL = "zeffarlo53@gmail.com"
PASSWORD = "kgck smtk dshj nbka"
PORT = 587
TIMEOUT = 120
# ------ GLOBALS -------- #

# ---- BIRTHDAY DATA ---- #
def get_bdays():
    try: birthday_data = pandas.read_csv(BIRTHDAY_DATA_PATH)
    except FileNotFoundError: print("Failed to retrieve resources.")
    else: return birthday_data
# -- LETTER TEMPLATES --- #
def generate_letter():
    path = os.path.join(CURRENT_DIR, f"./letter_templates/{random.choice(list(LETTER_PATHS))}")
    with open(path) as letter_data:
        return letter_data.read()

current_date = dt.datetime.now()

for _, row in get_bdays().iterrows():
    if row['month'] == current_date.month and row['day'] == current_date.day:
        letter = generate_letter().replace('[NAME]', row['name'])
        with smtplib.SMTP(STMP_DATA['@gmail'], port=PORT, timeout=TIMEOUT) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=row['email'], msg=f'Subject:Happy Birthday!\n\n{letter}')

