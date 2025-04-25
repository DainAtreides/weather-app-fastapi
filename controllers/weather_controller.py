from core.api import build_url, get_json
from models.weather import CurrentWeather


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
        city_name=city_name.title(),
        temperature=data['main']['temp'],  # Temperature in Celsius
        # Weather description with title case
        description=data['weather'][0]['description'].title(),
        icon_url=icon_url  # Include the weather icon URL
    )
