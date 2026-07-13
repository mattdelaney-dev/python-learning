import requests
from twilio.rest import Client
import os

MY_LAT = -27.087554
MY_LNG = 152.951190
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "AUTHKEY"
auth_tocken = os.environ.get("AUTH_TOKEN")

paramaters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=paramaters)
response.raise_for_status()

will_rain = False 

weather_data = response.json()
for day in weather_data["list"]:
    weather_today = day["weather"][0]["id"]
    if int(weather_today) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_tocken)
    message = client.messages \
        .create(
            body="It's going to rain today. Bring a umbrella!",
            from_="+",
            to="+"
        )

    print(message.status)

