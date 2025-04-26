from core.api import build_url, get_json
from models.weather import CurrentWeather, ForecastEntry, ForecastWeather


# Function to get the current weather for a given city
def get_current_weather(city_name: str) -> CurrentWeather:
    # Get the raw weather data from the API using the helper functions
    data = get_json(build_url('weather', city_name))
    # Get the icon code from the weather data
    icon_code = data['weather'][0]['icon']
    # Build the URL for the weather icon
    icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'
    # Return the weather data encapsulated in the CurrentWeather model
    return CurrentWeather(
        city_name=city_name,  # City name
        temperature=data['main']['temp'],  # Current Temperature
        # Weather description
        description=data['weather'][0]['description'],
        icon_url=icon_url  # Include the weather icon URL
    )


# Function to get the forecast weather for a given city
def get_forecast_weather(city_name: str) -> ForecastWeather:
    # Get the raw forecast data from the API using the helper functions
    data = get_json(build_url('forecast', city_name))
    # Extract the forecast list from the API response
    forecast_entries = []
    for entry in data['list']:
        # Parse the datetime from the response string
        datetime = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
        temperature = entry['main']['temp']
        description = entry['weather'][0]['description']
        icon_code = entry['weather'][0]['icon']
        # Build the URL for the weather icon
        icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'
        # Append the forecast entry with its details
        forecast_entries.append(ForecastEntry(
            datetime=datetime,  # Datetime of the forecast entry
            temperature=temperature,  # Forecasted temperature
            description=description,  # Weather description
            icon_url=icon_url  # Icon URL for the forecast weather
        ))
    # Return the encapsulated forecast data
    return ForecastWeather(city_name=city_name, forecast=forecast_entries)
