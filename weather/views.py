
from rest_framework import viewsets
from django.http import HttpResponse
import requests
from weather.models import Forecast
from .serializer import ForecastSerializer


class WeatherViewset(viewsets.ModelViewSet):
  serializer_class = ForecastSerializer

  def get_queryset(self):
    data = Forecast.objects.all()
    return data

  def _get_weather_data(self):
    url = "http://api.openweathermap.org/data/2.5/weather?q=bengaluru,IN&appid=840ebf6b453f7043e42ff0affffb2447"  # get the specific weather data in the city
    api_request = requests.get(url)  

    try:
      api_request.raise_for_status()         
      return api_request.json()              # return api request in the json format
    except:
      return None
     
  def save_weather_data(self):
    weather_data = self._get_weather_data()
    print(weather_data)                              # printing the weather data
    if weather_data is not None:
      try:
        weather_object = Forecast.objects.create(temperatuer=weather_data["main"]["temp"], description=weather_data["weather"][0]["description"], city=weather_data["name"])
        weather_data.save()                          # saving the weather data
      except:
        pass
