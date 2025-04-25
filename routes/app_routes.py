from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from views.weather_view import render_weather


router = APIRouter()


@router.get('/', response_class=HTMLResponse)
def form_page(request: Request):
    templates = Jinja2Templates(directory='static/templates')
    return templates.TemplateResponse('form.html', {'request': request})


@router.get('/weather/current', response_class=HTMLResponse)
def weather_html(request: Request, city_name: str):
    return render_weather(request, city_name)
