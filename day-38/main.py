import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 180
AGE = 18

APP_ID = os.environ["FITNESS_API_ID"]
API_KEY = os.environ["FITNESS_API_KEY"]
APP_URL = os.environ["FITNESS_API_URL"]

SHEETY_URL = os.environ["SHEETY_ENDPOINT_URL"]

basic = HTTPBasicAuth(os.environ["SHEETY_USERNAME"], os.environ["SHEETY_PASSWORD"])

exercise = input("What exercise did you do? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

app_params = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=APP_URL, json=app_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {os.environ["TOKEN"]}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]           
        }
    }

    sheet_response = requests.post(url=SHEETY_URL, json=sheet_inputs, headers=bearer_headers)
    
    print(sheet_response.text)