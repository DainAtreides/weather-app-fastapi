from core.api import build_url, get_json
from models.weather import CurrentWeather


def show_current_weather(city_name: str) -> CurrentWeather:
    data = get_json(build_url('weather', city_name))
    return CurrentWeather(
        city_name=city_name,
        temperature=data['main']['temp'],
        description=data['weather'][0]['description']
    )
