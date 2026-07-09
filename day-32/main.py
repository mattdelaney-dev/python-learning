import smtplib
import datetime as dt
import os
import random
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

my_email = "moo232519@gmail.com"
password = "PASSWORD"

now = dt.datetime.now()
weekday = now.weekday
file_path = os.path.join(BASE_DIR, "quotes.txt")

if weekday == 1:
    with open(file_path, "r") as data_file:
        file = data_file.readlines()
        quote = random.choice(file).strip()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="moomoothemoo22@gmail.com", 
            msg=f"Subject:Motivational Quote of the day!\n\n{quote}"
        )












