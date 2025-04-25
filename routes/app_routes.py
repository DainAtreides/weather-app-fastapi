from fastapi import APIRouter
from controllers.weather_controller import show_current_weather

router = APIRouter()


@router.get("/weather/current/{city_name}")
def current_weather(city_name: str):
    return show_current_weather(city_name)
