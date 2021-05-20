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
weather_data = response.json()['hourly'][:13]
weather_data = filter(lambda x: x['weather'][0]['id'] < 700, weather_data)

for _ in weather_data:
    print('it is going to rain')
    break
