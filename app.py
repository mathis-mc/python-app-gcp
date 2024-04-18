import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("API_KEY")

class MakeApiCall:

    def get_data(self, api):
        response = requests.get(api)
        if response.status_code == 200:
            print("Successfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(f"Error: {response.status_code}. Failed to fetch data.")
            print("Response content:", response.content)

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):
        self.get_data(api)


if __name__ == "__main__":
    api_call = MakeApiCall(f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={key}")