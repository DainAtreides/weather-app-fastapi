from pydantic import BaseModel, field_validator
from typing import List
from datetime import datetime


# Generic mixin for title case
class TitleCaseMixin:
    # Ensure the value is in title case
    @field_validator('*')  # '*' applies to all fields in the model
    @classmethod
    def title_case(cls, value: str) -> str:
        if isinstance(value, str):
            return value.title()
        return value


# Define the CurrentWeather model to represent the weather data
class CurrentWeather(TitleCaseMixin, BaseModel):
    city_name: str
    temperature: float
    description: str
    icon_url: str


# Define the model for a single forecast entry
class ForecastEntry(TitleCaseMixin, BaseModel):
    datetime: datetime
    temperature: float
    description: str
    icon_url: str


# Define the ForecastWeather model to represent the forecast data
class ForecastWeather(TitleCaseMixin, BaseModel):
    city_name: str
    forecast: List[ForecastEntry]
