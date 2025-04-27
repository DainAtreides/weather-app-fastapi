from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from controllers.weather_controller import get_current, get_forecast
from models.weather import CurrentWeather, ForecastWeather


templates = Jinja2Templates(directory='static/templates')


def render_weather(request: Request, city_name: str, view_type: str) -> HTMLResponse:
    if view_type == 'current':
        current: CurrentWeather = get_current(city_name)
        return templates.TemplateResponse('current.html', {
            'request': request,
            'current': current
        })
    if view_type == 'forecast':
        forecast: ForecastWeather = get_forecast(city_name)
        return templates.TemplateResponse('forecast.html', {
            'request': request,
            'forecast': forecast
        })
