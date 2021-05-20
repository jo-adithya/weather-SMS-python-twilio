from dotenv import load_dotenv
import requests
import os
from twilio.rest import Client

load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=os.environ.get('VIRTUAL_PHONE'),
        to=os.environ.get('PHONE_NUMBER')
    )

    break
