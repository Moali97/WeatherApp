import requests
from django.shortcuts import render, redirect
from .forms import CityForm
from .models import City


def index(request, objects=None):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5b96a99b221f2256b435467d7f5371f3'

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid()  :
            new_city = form.cleaned_data['name']
            city_count = City.objects.filter(name=new_city).count()

            if city_count == 0:
                form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city': city.name,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
            }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weatherApp/index.html', context)


def delete(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('index')