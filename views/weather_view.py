from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from controllers.weather_controller import get_current, get_forecast
from models.weather import CurrentWeather, ForecastWeather

# Initialize Jinja2Templates to load templates from the static/templates directory
templates = Jinja2Templates(directory='static/templates')


# Function to render weather information based on the view type (current or forecast)
def render_weather(request: Request, city_name: str, view_type: str) -> HTMLResponse:
    # If the view type is 'current', fetch current weather data and render the current.html template
    if view_type == 'current':
        current: CurrentWeather = get_current(city_name)
        return templates.TemplateResponse('current.html', {
            'request': request,
            'current': current
        })
    # If the view type is 'forecast', fetch forecast data and render the forecast.html template
    if view_type == 'forecast':
        forecast: ForecastWeather = get_forecast(city_name)
        return templates.TemplateResponse('forecast.html', {
            'request': request,
            'forecast': forecast
        })
