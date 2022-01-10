import requests
import datetime
from django.conf import settings

API_KEY = getattr(settings, "WEATHER_API_KEY")
WEATHER_API_BASE_URL = 'http://api.weatherapi.com/v1'

def retrieve_weather(country:str, dt:str) -> dict:
    """
    This method used to get data from weatherapi.com
    :param country: country for which we want to get the forecast
    :param dt: date is the date of the weather forecast
    :return: dictionary data weather
    """

    url = f"{WEATHER_API_BASE_URL}/forecast.json?key={API_KEY}&q={country}&dt={dt}&aqi=no&alerts=no"
    # accessing the API json data
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        forecastday = data.get("forecast").get("forecastday")
        if len(forecastday) > 0:
            forecast_day = data.get("forecast").get("forecastday")[0]
            return forecast_day.get('day')
        else:
            return dict()
    else:
        return dict()


def validate_date(date_text:str):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
