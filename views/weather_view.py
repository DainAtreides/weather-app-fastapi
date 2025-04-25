from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from controllers.weather_controller import get_current_weather
from models.weather import CurrentWeather


# Function to render the weather data for a given city
def render_weather(request: Request, city_name: str) -> HTMLResponse:
    # Get the weather data using the show_current_weather function
    weather: CurrentWeather = get_current_weather(city_name)
    # Initialize Jinja2Templates to load templates from the static/templates directory
    templates = Jinja2Templates(directory='static/templates')
    # Render the weather.html template and pass the weather data along with the request object
    return templates.TemplateResponse('weather.html', {
        'request': request,
        'weather': weather  # Pass the weather data to be displayed in the template
    })
