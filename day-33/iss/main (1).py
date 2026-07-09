import requests
from datetime import datetime
import time
import smtplib

my_email = "moo232519@gmail.com"
password = "PASSWORD"

MY_LAT = -27.087554 # Your latitude
MY_LONG = 152.951190 # Your longitude


#Your position is within +5 or -5 degrees of the ISS position.
def is_it_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    lat_diff = abs(MY_LAT - iss_latitude)
    lng_diff = abs(MY_LONG - iss_longitude)

    if (lat_diff <= 5) and (lng_diff <= 5):
        return True
    else:
        return False
    
def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour
    
    if sunrise > current_hour or sunset < current_hour:
        return True
    else:
        return False




#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

email_sent = False

while True:
    time.sleep(60)
    if is_it_close() and is_night():
        if not email_sent:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs="moomoothemoo22@gmail.com", 
                    msg=f"Subject:ISS IS OVERHEAD!!\n\nTHE ISS IS OVERHEAD LOOK UP!"
                )
            email_sent = True  # Locks the email so it doesn't spam
    else:
        email_sent = False  # Resets the lock once the ISS leaves the area
    



