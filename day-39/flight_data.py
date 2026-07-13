import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os


load_dotenv()

class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(data, return_date):
    if data is None:
            return FlightData(
                price="N/A",
                origin_airport="N/A",
                destination_airport="N/A",
                out_date="N/A",
                return_date="N/A"
            )  

    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    cheapest_flight = FlightData(
        price=float("inf"),
        origin_airport="N/A",
        destination_airport="N/A",
        out_date="N/A",
        return_date="N/A"
    )

    for flight in all_flights:
        try:
            price = flight["price"]
        except KeyError:
            continue

        if price < cheapest_flight.price:
            origin = flight["flights"][0]["departure_airport"]["id"]
            destination = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

            cheapest_flight = FlightData(
                price=price,
                origin_airport=origin,
                destination_airport=destination,
                out_date=out_date,
                return_date=return_date
            )
   
    return cheapest_flight