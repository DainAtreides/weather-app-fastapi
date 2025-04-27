from pydantic import BaseModel
from typing import List
from datetime import datetime


# Define the CurrentWeather model to represent the weather data
class CurrentWeather(BaseModel):
    city_name: str
    temperature: float
    feels_like: float  # Temperature feels like
    humidity: float
    wind: float
    description: str
    icon_url: str


# Define the model for a single forecast entry
class ForecastEntry(BaseModel):
    date_time: datetime
    temperature: float
    description: str
    icon_url: str


# Define the ForecastWeather model to represent the forecast data
class ForecastWeather(BaseModel):
    city_name: str
    forecast: List[ForecastEntry]
