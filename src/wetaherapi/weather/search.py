from .models import Country, Forecast
from .fetch import retrieve_weather

def get_forecast(dt, country_code):
    """
    Used to give a clear conclusion on the selected date and Country
    :param dt: date is the date of the weather forecast
    :param country_code: country_code is code of the country for which we want to get the forecast. See 3) for more info.
    :return:
    """

    try:
        country = Country.objects.get(iso_code=country_code)
    except Country.DoesNotExist:
        return 'not found weather data'

    queryset = Forecast.objects.filter(country_id=country.id, forecast_day=dt)
    if not queryset.exists():
        data = retrieve_weather(country, dt)
        if data:
            model = Forecast(country_id=country.id, forecast_day=dt)
            model.content = data
            model.save()
    else:
        model = queryset.get()
        data = model.content

    if 'avgtemp_c' not in data:
        return 'not found weather data'

    if data['avgtemp_c'] > 20:
        return 'good'
    elif data['avgtemp_c'] > 10 and data['avgtemp_c'] < 20:
        return 'soso'
    else:
        return 'bad'
