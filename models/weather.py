from pydantic import BaseModel
from typing import List
from datetime import datetime


# Define the CurrentWeather model to represent the weather data
class CurrentWeather(BaseModel):
    city_name: str
    temperature: int
    feels_like: int
    humidity: int
    wind: int
    description: str
    icon_url: str


# Define the model for a single forecast entry
class ForecastEntry(BaseModel):
    date_time: datetime
    temperature: int
    description: str
    icon_url: str


# Define the ForecastWeather model to represent the forecast data
class ForecastWeather(BaseModel):
    city_name: str
    forecast: List[ForecastEntry]
