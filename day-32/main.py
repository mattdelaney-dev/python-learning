import smtplib
import datetime as dt
import os
import random
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

my_email = "moo232519@gmail.com"
password = "bijn qglr jawc hrot"

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












# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="moomoothemoo22@gmail.com", 
#         msg="Subject:Hello!\n\nThis is the content"
#     )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()

# data_of_birth = dt.datetime(year=2000, month=12, day=15, hour=4)
# print(data_of_birth)