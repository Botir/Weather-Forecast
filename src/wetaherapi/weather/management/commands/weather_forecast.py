from django.core.management.base import BaseCommand
from django.conf import settings
from ...search import get_forecast

API_KEY = getattr(settings, "WEATHER_API_KEY")
WEATHER_API_BASE_URL = 'http://api.weatherapi.com/v1'

class Command(BaseCommand):
    help = 'Info about weather forecast'

    def add_arguments(self, parser):
        parser.add_argument('dt', nargs='+', type=str, help='Date is the date of the weather forecast',)
        parser.add_argument('code', nargs='+', type=str, help='Code of the country for which we want to get the forecast',)

    def handle(self, *args, **options):
        result = get_forecast(options['dt'][0], options['code'][0])
        self.stdout.write(result)
