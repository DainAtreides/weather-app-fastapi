from core.api import get_json, build_url
from models.weather import CurrentWeather, ForecastEntry, ForecastWeather
from datetime import datetime


# Fetch current weather data for a specific city
def get_current(city_name: str) -> CurrentWeather:
    # Fetch the raw weather data using the build_url function
    data = get_json(build_url('weather', city_name))
    # Extract weather details from the response data
    temperature = int(data['main']['temp'])
    feels_like = int(data['main']['feels_like'])
    humidity = int(data['main']['humidity'])
    wind = int(data['wind']['speed'])
    description = data['weather'][0]['description'].title()
    icon_code = data['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'

    # Return a CurrentWeather object with the extracted data
    return CurrentWeather(
        city_name=city_name.title(),
        temperature=temperature,
        feels_like=feels_like,
        humidity=humidity,
        wind=wind,
        description=description,
        icon_url=icon_url
    )


# Fetch weather forecast data for a specific city
def get_forecast(city_name: str) -> ForecastWeather:
    # Fetch the raw forecast data using the build_url function
    data = get_json(build_url('forecast', city_name))
    forecast_entries = []

    # Loop through forecast data to create forecast entries
    for entry in data['list']:
        date_time = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
        temperature = int(entry['main']['temp'])
        description = entry['weather'][0]['description'].title()
        icon_code = entry['weather'][0]['icon']
        icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'

        # Add the forecast entry to the list
        forecast_entries.append(ForecastEntry(
            date_time=date_time,
            temperature=temperature,
            description=description,
            icon_url=icon_url
        ))

    # Return a ForecastWeather object with the list of forecast entries
    return ForecastWeather(city_name=city_name.title(), forecast=forecast_entries)
