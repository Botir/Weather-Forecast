from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models import JSONField

# List of all countries
class Country(models.Model):
    id = models.AutoField(primary_key=True)

    iso_code = models.CharField(max_length=2, unique=True, blank=False, null=True, db_index=True, default=None,
                                help_text='ISO 3166-1 alpha 2', validators=[MinLengthValidator(2)])

    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Forecast(models.Model):

    # WEATHER DATA FROM API
    content = JSONField(blank=False, null=False, default=dict)

    # City Model
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="countries")

    # weather date
    forecast_day = models.DateField(blank=False, null=False)

    # system created or updated time
    created_dt = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, editable=False)
    updated_dt = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, editable=False)

    class Meta:
        unique_together = (('country', 'forecast_day'))
        verbose_name = "Forecast"
        verbose_name_plural = "Forecasts"
