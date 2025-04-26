from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from views.weather_view import render_current, render_forecast


# Create an APIRouter instance to define API routes
router = APIRouter()


# Route to display the form page where the user can enter the city name
@router.get('/', response_class=HTMLResponse)
def base_page(request: Request):
    # Initialize Jinja2Templates to load templates from the static/templates directory
    templates = Jinja2Templates(directory='static/templates')
    # Render the base.html template and pass the request object for rendering
    return templates.TemplateResponse('base.html', {'request': request})


# Route to display the current weather for a specific city
@router.get('/weather/current', response_class=HTMLResponse)
def current_html(request: Request, city_name: str):
    # Call the render_current function to display the weather for the given city
    return render_current(request, city_name)


# Route to display the forecats weather for a specific city
@router.get('/weather/forecast', response_class=HTMLResponse)
def forecast_html(request: Request, city_name: str):
    # Call the render_forecast function to display the weather for the given city
    return render_forecast(request, city_name)
