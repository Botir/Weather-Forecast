# Weather forecast
Weather forecast for the business inteligence system.
 
This microservice performs the required task for some business representatives. He predicts what the weather will be like in advance. Information is taken from weatherapi.com

The output of your interfaces can be
- good - in case average temperature on given day is > 20 celsius degrees
- soso - in case the average temperature on a given day is between 20 and 10-celsius degrees
- bad - in other cases

## Install via Docker
Run services in the background:

`docker-compose up -d`

Run services in the foreground:

`docker-compose up --build`

## API endpoint

`GET /weather-forecast/?date={YYYY-MM-DD}&country_code={ISO_CODE_2}`
- date is the date of the weather forecast
- country_code is code of the country for which we want to get the forecast
### example:
`/weather-forecast/?date=2022-01-12&country_code=CZ`

## Django command
`python manage.py weather_forecast 2022-01-12 CZ`

