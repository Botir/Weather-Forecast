from django.urls import path
from .views import ForecastView

urlpatterns = [
    path('weather-forecast/', ForecastView.as_view(), name='weather-forecast'),
]
