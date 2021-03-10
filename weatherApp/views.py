from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}' \
          '&units=metric&lang=lang&appid=5b96a99b221f2256b435467d7f5371f3'
    cities = City.objects.all()
    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate

    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city.name)).json()
        # request the API data and convert the JSON to Python data types

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }
    weather_data.append(weather)  # add the data for the current city into our list
    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weatherApp/index.html', context)
