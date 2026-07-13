import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT_URL1"]

class DataManager:
    
    def __init__(self):
        self.user = os.environ["SHEETY_USER1"]
        self.password = os.environ["SHEETY_PASS1"]
        self.auth = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self.auth)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data
    
    def update_lowest_price(self, row_id, new_price):
        update_endpoint = f"{SHEETY_ENDPOINT}/{row_id}"
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(url=update_endpoint, json=new_data, auth=self.auth)
        print(response.text)