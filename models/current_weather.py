from models.weather import Weather
from core.api import build_url, get_json


class CurrentWeather(Weather):
    def fetch(self):
        url = build_url('weather', self.city.name)
        data = get_json(url)
        self.temp = data['main']['temp']
        self.description = data['weather'][0]['description']
