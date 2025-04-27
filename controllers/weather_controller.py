from core.api import get_json, build_url
from models.weather import CurrentWeather, ForecastEntry, ForecastWeather
from datetime import datetime


def get_current(city_name: str) -> CurrentWeather:
    data = get_json(build_url('weather', city_name))
    temperature = int(data['main']['temp'])
    feels_like = int(data['main']['feels_like'])
    humidity = int(data['main']['humidity'])
    wind = int(data['wind']['speed'])
    description = data['weather'][0]['description'].title()
    icon_code = data['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'
    return CurrentWeather(
        city_name=city_name.title(),
        temperature=temperature,
        feels_like=feels_like,
        humidity=humidity,
        wind=wind,
        description=description,
        icon_url=icon_url
    )


def get_forecast(city_name: str) -> ForecastWeather:
    data = get_json(build_url('forecast', city_name))
    forecast_entries = []
    for entry in data['list']:
        date_time = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
        temperature = int(entry['main']['temp'])
        description = entry['weather'][0]['description'].title()
        icon_code = entry['weather'][0]['icon']
        icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'
        forecast_entries.append(ForecastEntry(
            date_time=date_time,
            temperature=temperature,
            description=description,
            icon_url=icon_url
        ))
    return ForecastWeather(city_name=city_name.title(), forecast=forecast_entries)
