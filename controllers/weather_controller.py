from models.city import City
from models.current_weather import CurrentWeather
from views.weather_view import display_weather


def show_current_weather(city_name: str):
    city = City(city_name)
    weather = CurrentWeather(city)
    weather.fetch()
    display_weather(weather)
