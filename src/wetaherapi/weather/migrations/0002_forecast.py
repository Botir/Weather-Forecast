# Generated by Django 4.0.1 on 2022-01-10 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.JSONField(default=dict)),
                ('forecast_day', models.DateField()),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_dt', models.DateTimeField(auto_now=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='weather.country')),
            ],
            options={
                'verbose_name': 'Forecast',
                'verbose_name_plural': 'Forecasts',
                'unique_together': {('country', 'forecast_day')},
            },
        ),
    ]
