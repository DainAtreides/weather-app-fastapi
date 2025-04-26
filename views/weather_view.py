from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from controllers.weather_controller import get_current, get_forecast
from models.weather import CurrentWeather, ForecastWeather


# Function to render the weather page for a given city
def render_current(request: Request, city_name: str) -> HTMLResponse:
    # Get the weather data using the get_current function
    current: CurrentWeather = get_current(city_name)
    # Initialize Jinja2Templates to load templates from the static/templates directory
    templates = Jinja2Templates(directory='static/templates')
    # Render the weather.html template and pass the weather data along with the request object
    return templates.TemplateResponse('current.html', {
        'request': request,
        'current': current  # Pass the current weather data to be displayed in the template
    })


# Function to render the forecast page for a given city
def render_forecast(request: Request, city_name: str) -> HTMLResponse:
    # Get the forecast weather data using the get_forecast function
    forecast: ForecastWeather = get_forecast(city_name)
    # Initialize Jinja2Templates to load templates from the static/templates directory
    templates = Jinja2Templates(directory='static/templates')
    # Render the forecast.html template and pass the forecast data along with the request object
    return templates.TemplateResponse('forecast.html', {
        'request': request,
        'forecast': forecast  # Pass the forecast weather data to be displayed in the template
    })
