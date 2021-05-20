from dotenv import load_dotenv
import requests
import os

load_dotenv()
url = 'https://api.openweathermap.org/data/2.5/onecall'
parameter = {
    'lat': -6.238960,
    'lon': 106.658409,
    'exclude': 'current,minutely,daily',
    'appid': os.environ.get('OWM_API_KEY')
}

response = requests.get(url, params=parameter)
response.raise_for_status()
print(response.json())
