from core.api import build_url, get_json
from models.weather import CurrentWeather


# Function to get the current weather for a given city
def show_current_weather(city_name: str) -> CurrentWeather:
    # Get the raw weather data from the API using the helper functions
    data = get_json(build_url('weather', city_name))

    # Return the weather data encapsulated in the CurrentWeather model
    return CurrentWeather(
        city_name=city_name,
        temperature=data['main']['temp'],  # Temperature in Celsius
        # Weather description with title case
        description=data['weather'][0]['description'].title()
    )
