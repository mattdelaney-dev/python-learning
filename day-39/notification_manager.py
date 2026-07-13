import requests
from twilio.rest import Client
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.acc_sid = os.environ["TWILLIO_SID"]
        self.acc_auth = os.environ["TWILLIO_AUTH"]
        self.virtual_number = os.environ["TWILIO_VIRTUAL_NUMBER"]
        self.verified_number = os.environ["TWILIO_VERIFIED_NUMBER"]
        self.client = Client(self.acc_sid, self.acc_auth)

    def send_sms(self, flight):
        message_body = (
            f"Low price alert! Only GBP {flight.price} to fly from "
            f"{flight.origin_airport} to {flight.destination_airport}, "
            f"from {flight.out_date} to {flight.return_date}."
        )
        message = self.client.messages.create(
            body=message_body,
            from_=self.virtual_number,
            to=self.verified_number
        )
        print(message.sid)