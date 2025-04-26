from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from views.weather_view import render_weather


# Create an APIRouter instance to define API routes
router = APIRouter()


# Route to display the form page where the user can enter the city name
@router.get('/', response_class=HTMLResponse)
def base_page(request: Request):
    # Initialize Jinja2Templates to load templates from the static/templates directory
    templates = Jinja2Templates(directory='static/templates')
    # Render the base.html template and pass the request object for rendering
    return templates.TemplateResponse('base.html', {'request': request})


@router.get('/weather', response_class=HTMLResponse)
def weather_html(request: Request, city_name: str, view_type: str):
    return render_weather(request, city_name, view_type)
