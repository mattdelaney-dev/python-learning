#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
import requests_cache
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

notification_manager = NotificationManager()

flight_search = FlightSearch()

today = datetime.now()

tomorrow = today + timedelta(days=1)

six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

for destination in sheet_data:
    flights = flight_search.check_flights("LHR", destination["iataCode"], tomorrow, six_month_from_today)

    cheapest_flight = find_cheapest_flight(flights, six_month_from_today.strftime("%Y-%m-%d"))
    new_price = cheapest_flight.price

    if new_price != "N/A" and new_price < destination["lowestPrice"]:
        print(f'{destination["city"]}: GBP {new_price}')
        print("Lower price flight found!")
        data_manager.update_lowest_price(destination["id"], new_price)
        notification_manager.send_sms(cheapest_flight)
