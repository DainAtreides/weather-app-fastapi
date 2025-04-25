from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from controllers.weather_controller import show_current_weather
from models.weather import CurrentWeather


def render_weather(request: Request, city_name: str) -> HTMLResponse:
    weather: CurrentWeather = show_current_weather(city_name)
    templates = Jinja2Templates(directory='static/templates')
    return templates.TemplateResponse('weather.html', {
        'request': request,
        'weather': weather
    })
