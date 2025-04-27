from core.api import build_url, get_json
from models.weather import CurrentWeather, ForecastEntry, ForecastWeather
from datetime import datetime


# Function to get the current weather for a given city
def get_current(city_name: str) -> CurrentWeather:
    # Get the raw weather data from the API using the helper functions
    data = get_json(build_url('weather', city_name))
    temperature = data['main']['temp']  # Current Temperature
    feels_like = data['main']['feels_like']  # Temperature feels like
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    description = data['weather'][0]['description'].title()
    # Get the icon code from the weather data
    icon_code = data['weather'][0]['icon']
    # Build the URL for the weather icon
    icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'
    # Return the weather data encapsulated in the CurrentWeather model
    return CurrentWeather(
        city_name=city_name.title(),
        temperature=temperature,
        feels_like=feels_like,
        humidity=humidity,
        wind=wind,
        description=description,
        icon_url=icon_url
    )


# Function to get the forecast weather for a given city
def get_forecast(city_name: str) -> ForecastWeather:
    try:
        # Get the raw forecast data from the API using the helper functions
        data = get_json(build_url('forecast', city_name))
        # Extract the forecast list from the API response
        forecast_entries = []
        for entry in data['list']:
            # Parse the datetime from the response string
            date_time = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
            temperature = entry['main']['temp']
            description = entry['weather'][0]['description'].title()
            icon_code = entry['weather'][0]['icon']
            # Build the URL for the weather icon
            icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'
            # Append the forecast entry with its details
            forecast_entries.append(ForecastEntry(
                date_time=date_time,  # Datetime of the forecast entry
                temperature=temperature,  # Forecasted temperature
                description=description,  # Weather description
                icon_url=icon_url  # Icon URL for the forecast weather
            ))
        # Return the encapsulated forecast data
        return ForecastWeather(city_name=city_name.title(), forecast=forecast_entries)
    except Exception as e:
        print(f'Error: {e}')
        raise e
